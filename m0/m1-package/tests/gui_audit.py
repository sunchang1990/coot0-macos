
# gui_audit.py -- run INSIDE the real Coot window (use tests/run-gui-audit.sh, which restarts Coot if an item crashes it):
#     ./tests/run-gui-audit.sh
# For every item of the main menu bar and every button of the main toolbar it:
#   activates it (a check item twice), lets the GUI run for a moment so windows are really drawn, clicks every button of
#   the dialogs that opened, closes them again, and records: a Python exception, a GTK CRITICAL/WARNING, a Traceback, an
#   item without any handler (= a dead menu entry), or a crash/hang (the driver script notes the item that was running).
# Result lines go to  <results>/gui-audit-<time>.txt .  Nothing here needs you to click anything.
import os, sys, re, time, ctypes, tempfile, threading, traceback
prefix = os.environ.get("COOT_PREFIX", "")
state_dir = os.environ.get("COOT_AUDIT_DIR", os.path.join(prefix, "work", "gui-audit"))
os.makedirs(state_dir, exist_ok=True)
OUT = os.path.join(state_dir, "audit_out.txt")
PROG = os.path.join(state_dir, "progress.txt")
START = int(os.environ.get("COOT_AUDIT_START", "0"))
BUTTONS = os.environ.get("COOT_AUDIT_BUTTONS", "1") != "0"
DWELL = float(os.environ.get("COOT_AUDIT_DWELL", "0.8"))          # seconds a new window stays up before its buttons are clicked
MODAL_CLOSE = float(os.environ.get("COOT_AUDIT_MODAL_CLOSE", "1.5"))   # a dialog that blocks (gtk_dialog_run, file chooser) is closed after this
HANG = float(os.environ.get("COOT_AUDIT_HANG", "300"))     # seconds without progress before the audit gives up on an item (some OK buttons start long jobs)
EXIT_AT_END = os.environ.get("COOT_AUDIT_EXIT", "0") == "1"
ONLY = os.environ.get("COOT_AUDIT_ONLY", "")                      # regex: audit only items whose menu path matches
SKIP_RE = re.compile(os.environ.get("COOT_AUDIT_SKIP", r"exit|quit|full ?screen|stereo|fetch|download|check for update|updates|\bebi\b|\bpdbe\b|\bemdb\b|pdb.?redo|get monomer|search monomer|online|internet|http"), re.I)
libc = ctypes.CDLL(None)
ORIG1 = os.dup(1)
def tell(s):
    try: os.write(ORIG1, (s + "\n").encode("utf-8", "replace"))
    except OSError: pass

import gtk, gobject, _gtk2core as _c, coot_python
import coot
HEADLESS = _c.HEADLESS
created = []                                            # headless self-test only: windows the scripts made (they are never "visible")
if HEADLESS:
    for cls in (gtk.Window, gtk.Dialog):
        def mk(c):
            orig = c.__init__
            def init(self, *a, **k): orig(self, *a, **k); created.append(self)
            c.__init__ = init
        mk(cls)

class Capture:
    """Redirect C/C++ and Python stdout+stderr (file descriptors 1 and 2) into a file while an item runs."""
    def __init__(self): self.path = tempfile.mktemp(prefix="coot-audit-"); self.depth = 0
    def start(self):
        if self.depth == 0:
            sys.stdout.flush(); sys.stderr.flush(); libc.fflush(None)
            self.f = os.open(self.path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
            self.s1 = os.dup(1); self.s2 = os.dup(2); os.dup2(self.f, 1); os.dup2(self.f, 2)
        self.depth += 1
    def stop(self):
        self.depth -= 1
        if self.depth == 0:
            sys.stdout.flush(); sys.stderr.flush(); libc.fflush(None)
            os.dup2(self.s1, 1); os.dup2(self.s2, 2); os.close(self.s1); os.close(self.s2); os.close(self.f)
    def text(self):
        try: return open(self.path, errors="replace").read()
        except OSError: return ""
cap = Capture()

def norm(s): return (s or "").replace("_", "").strip()
def label_of(w):
    try:
        for k in w.get_children():
            for m in ("get_text", "get_label"):
                if hasattr(k, m):
                    try:
                        r = getattr(k, m)()
                        if r: return r
                    except Exception: pass
    except Exception: pass
    try: return w.get_label() or ""
    except Exception: return ""

def collect_menu(shell, path, out):
    for it in shell.get_children():
        cls = type(it).__name__
        if cls == "SeparatorMenuItem": continue
        lab = norm(label_of(it)); p = path + [lab or "?"]
        sub = it.get_submenu() if hasattr(it, "get_submenu") else None
        if sub is not None: collect_menu(sub, p, out)
        else: out.append(("menu", " > ".join(p), it))
def collect_toolbar(w, path, out, depth=0):
    cls = type(w).__name__
    if cls in ("ToolButton", "ToggleToolButton", "MenuToolButton", "Button", "ToggleButton", "CheckButton", "RadioButton"):
        lab = norm(label_of(w)) or (w.get_tooltip_text() if hasattr(w, "get_tooltip_text") else "") or w.get_name()
        out.append(("tool", "Toolbar > %s" % (lab or "?"), w)); return
    try: kids = w.get_children()
    except Exception: kids = []
    for k in kids: collect_toolbar(k, path, out, depth + 1)

def shown(w):
    try:
        if w.get_visible(): return True
    except Exception: pass
    return HEADLESS and w in created
def toplevels(): return [w for w in gtk.window_list_toplevels() if w is not None]

def pump(seconds):
    t_end = time.time() + seconds
    while time.time() < t_end:
        n = 0
        while gtk.events_pending() and n < 200: gtk.main_iteration(False); n += 1
        time.sleep(0.02)

mb = coot_python.main_menubar(); tb = coot_python.main_toolbar()
main_win = mb.get_toplevel() if mb is not None else None
entries = []
if mb is not None: collect_menu(mb, [], entries)
if tb is not None: collect_toolbar(tb, [], entries)
if ONLY: entries = [e for e in entries if re.search(ONLY, e[1])]
def has_handler(kind, w):
    try:
        gt = _c.instance_gtype(w._ptr)
        for name in ("activate", "toggled", "clicked"):
            sid = _c.call("g_signal_lookup", name, gt)
            if sid and _c.call("g_signal_has_handler_pending", w._ptr, sid, 0, True): return True
        return False
    except Exception: return True

state = {"idx": START, "baseline_vis": set(), "inspect": set(), "t_item": 0.0, "active": False, "last_progress": time.time(), "age": {}}
results = []
def log(line):
    results.append(line); open(OUT, "a").write(line + "\n"); tell(line)

def watchdog():
    while True:
        time.sleep(5)
        if time.time() - state["last_progress"] > HANG:
            try: open(PROG, "a").write("HANG\n")
            except OSError: pass
            os._exit(9)
threading.Thread(target=watchdog, daemon=True).start()

def closer():
    """Closes dialogs that block inside activate() (modal dialogs, file choosers) so the audit can go on."""
    if state["active"]:
        now = time.time()
        for w in toplevels():
            p = w._ptr
            if p in state["baseline_vis"] or p in state["inspect"] or not shown(w): continue
            first = state["age"].setdefault(p, now)
            if now - first > MODAL_CLOSE:
                try: w.destroy()
                except Exception: pass
    return True

BTN_SKIP_RE = re.compile(SKIP_RE.pattern + r"|install|upgrade|\bget\b", re.I)
def click_buttons(win, items_log):
    n = 0
    if type(win).__name__ in ("FileChooserDialog", "FileSelection"): return 0
    btns = [x for x in walk(win) if type(x).__name__ == "Button"]
    # dialogs close themselves with Close / Cancel buttons: click those last
    btns.sort(key=lambda b: 1 if re.search(r"close|cancel|dismiss|\bno\b", norm(label_of(b)), re.I) else 0)
    for x in btns:
        if not HEADLESS:
            try:
                if not win.get_visible(): break            # an earlier button closed this window
            except Exception: break
        lab = norm(label_of(x))
        if BTN_SKIP_RE.search(lab): continue
        try:
            if not x.get_sensitive(): continue
        except Exception: pass
        if not HEADLESS:
            try:
                if not x.get_mapped(): continue            # hidden (e.g. Lidia's developer "test function" button): a user cannot press it
            except Exception: pass
        state["last_progress"] = time.time()
        open(PROG, "w").write("%d\t%s\tbutton [%s]\n" % (state["idx"], state["path"], lab))
        e0 = len(_c.CALLBACK_ERRORS)
        try: x.clicked()
        except BaseException as e: items_log.append("button [%s] raised %r" % (lab, e))
        pump(0.15)
        if len(_c.CALLBACK_ERRORS) > e0:
            items_log.append("button [%s]: %s" % (lab, _c.CALLBACK_ERRORS[-1][1].strip().splitlines()[-1][:160]))
        n += 1
    return n
def walk(w, out=None):
    out = out if out is not None else []
    out.append(w)
    try: kids = w.get_children()
    except Exception: kids = []
    for k in kids: walk(k, out)
    return out

BAD = re.compile(r"CRITICAL|Gtk-WARNING|Gdk-WARNING|GLib-WARNING|Pango-WARNING|Traceback|assertion|Segmentation")
def run_item(idx, kind, path, w):
    state["path"] = path; state["idx"] = idx; state["last_progress"] = time.time()
    open(PROG, "w").write("%d\t%s\n" % (idx, path))
    if SKIP_RE.search(path): return "SKIP", "not run (network / exit / display-mode item: try it by hand)"
    if not has_handler(kind, w): return "NO-HANDLER", "no signal handler attached - the entry does nothing"
    try:
        if not w.get_sensitive(): return "SKIP", "insensitive (greyed out) at this point"
    except Exception: pass
    load_data()                                   # same starting point for every entry
    before_all = {x._ptr for x in toplevels()}
    base = {x._ptr for x in toplevels() if shown(x)}
    state["baseline_vis"] = set(base); state["age"] = {}; state["inspect"] = set()
    e0 = len(_c.CALLBACK_ERRORS); notes = []; n_btn = 0
    cap.start(); state["active"] = True; t0 = time.time()
    try:
        times = 2 if type(w).__name__ == "CheckMenuItem" else 1
        for _ in range(times):
            if kind == "menu": w.activate()
            else:
                cn = type(w).__name__
                if cn in ("ToggleToolButton", "ToggleButton", "CheckButton"):
                    w.set_active(not w.get_active())
                elif cn in ("Button",): w.clicked()
                else: w.emit("clicked")
            pump(0.1)
        pump(DWELL)                                                   # let the windows appear and draw
        newwins = [x for x in toplevels() if shown(x) and x._ptr not in base]
        state["inspect"] = {x._ptr for x in newwins}
        if BUTTONS:
            for x in newwins: n_btn += click_buttons(x, notes)
        alive = {y._ptr for y in toplevels()}
        for x in newwins:
            if x._ptr not in alive: continue                          # the dialog closed itself (OK / Cancel)
            # windows that existed before (C dialogs that Coot re-uses) are only hidden; windows made by this item are destroyed
            try:
                if x._ptr in before_all: x.hide()
                else: x.destroy()
            except Exception: pass
        pump(0.2)
        for x in toplevels():                                          # anything else that opened as a side effect
            if shown(x) and x._ptr not in base:
                try: x.hide() if x._ptr in before_all else x.destroy()
                except Exception: pass
    except BaseException as e:
        notes.append("raised %r" % (e,))
    finally:
        state["active"] = False; cap.stop()
    txt = cap.text()
    cb = _c.CALLBACK_ERRORS[e0:]
    status = "ok"; detail = ""
    if cb or notes or re.search(r"Traceback", txt):
        status = "ERR"
        if cb: detail = cb[-1][1].strip().splitlines()[-1][:200]
        elif notes: detail = notes[0][:200]
        else:
            tl = txt.splitlines(); i = max(j for j, l in enumerate(tl) if "Traceback" in l)
            detail = " / ".join(l.strip() for l in tl[i:i + 6])[:240]
    else:
        bad = [l.strip() for l in txt.splitlines() if BAD.search(l)]
        if bad:
            status = "WARN"; detail = ("%d x " % len(bad)) + bad[0][:200]
    secs = time.time() - t0
    if status == "ok":
        info = [l.strip() for l in txt.splitlines() if re.search(r"^(WARNING|ERROR)::|BL WARNING|BL ERROR", l.strip())]
        detail = ("windows: %d, buttons clicked: %d, %.1f s" % (len(newwins), n_btn, secs)) + ((" | " + info[0][:120]) if info else "")
    else:
        detail += " (windows: %d, buttons clicked: %d, %.1f s)" % (len(newwins), n_btn, secs)
    if cb:
        open(OUT + ".tracebacks", "a").write("== %d %s\n%s\n" % (idx, path, cb[-1][1]))
    return status, detail

def finish():
    n = {}
    for l in results: 
        m = re.match(r"AUDIT +\d+ \| .* \| (\S+) \|", l)
        if m: n[m.group(1)] = n.get(m.group(1), 0) + 1
    tell("AUDIT done: " + ", ".join("%s=%d" % kv for kv in sorted(n.items())))
    open(PROG, "w").write("DONE\n")
    if EXIT_AT_END: coot.coot_real_exit(0)

def step(*args):
    i = state["idx"]
    if i >= len(entries):
        finish(); return False
    kind, path, w = entries[i]
    try: status, detail = run_item(i, kind, path, w)
    except BaseException as e: status, detail = "ERR", "audit itself raised %r" % (e,)
    log("AUDIT %3d | %s | %s | %s" % (i, path, status, detail))
    state["idx"] = i + 1
    return True

if START == 0:
    open(OUT, "w").write("")
    log("== Coot GUI audit %s | %d items (menu bar + toolbar) | %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), len(entries), "headless self-test" if HEADLESS else "real window"))
DATA = {"imol": None, "imap": None}
def load_data():
    """(Re)load the tutorial model and map when they are missing (an earlier entry may have closed or deleted them) and centre on residue A 40."""
    if os.environ.get("COOT_AUDIT_NODATA", "0") == "1": return
    here = prefix
    try:
        if DATA["imol"] is None or not coot.is_valid_model_molecule(DATA["imol"]):
            DATA["imol"] = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
        if DATA["imap"] is None or not coot.is_valid_map_molecule(DATA["imap"]):
            DATA["imap"] = coot.make_and_draw_map(os.path.join(here, "test-data", "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
        coot.set_imol_refinement_map(DATA["imap"])
        coot.set_go_to_atom_molecule(DATA["imol"]); coot.set_go_to_atom_chain_residue_atom_name("A", 40, " CA ")
        import __main__; __main__.imol = DATA["imol"]; __main__.imol_map = DATA["imap"]
    except BaseException: tell("could not load the test data: " + traceback.format_exc()[-200:])
gobject.timeout_add(250, closer)
if HEADLESS:
    # self-test: no main loop is running, so drive the steps here
    load_data()
    while step(): pass
    coot.coot_real_exit(0)
else:
    def begin(*a):
        load_data()                       # inside the main loop, when the OpenGL window exists
        pump(1.0)
        gobject.timeout_add(60, step)     # then one item after the other (each step runs the GUI for a while itself)
        return False
    gobject.timeout_add(2000, begin)      # begin once the main window is up and the main loop is running
