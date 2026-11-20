
# Headless sweep of every menu item the Python GUI layer added to the main menubar.
# For each item: does it have an "activate" handler, and does activating it raise?
# (C++-built items are covered by the real-GUI audit; here headless GTK cannot show C dialogs.)
# Env: SWEEP_START (first index, default 0), SWEEP_PROGRESS (file: "idx<TAB>path" written before each item),
#      SWEEP_OUT (result file, appended)
import os, sys, io, json, time, traceback, contextlib
sys.path.insert(0, os.path.join(os.environ["COOT_PREFIX"], "tests"))
import gui_harness as H
import _gtk2core as _c
g, errs, log = H.load()
import coot
here = os.environ["COOT_PREFIX"]
start = int(os.environ.get("SWEEP_START", "0"))
prog = os.environ.get("SWEEP_PROGRESS", "/tmp/sweep_progress.txt")
outf = os.environ.get("SWEEP_OUT", "/tmp/sweep_out.txt")
imol = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
imap = coot.make_and_draw_map(os.path.join(here, "test-data", "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
g["imol"] = imol; g["imol_map"] = imap
coot.set_go_to_atom_molecule(imol); coot.set_go_to_atom_chain_residue_atom_name("A", 40, " CA ")
coot.set_imol_refinement_map(imap)

def label_of(item):
    for k in item.get_children():
        for m in ("get_text", "get_label"):
            if hasattr(k, m):
                try: return getattr(k, m)()
                except Exception: pass
    return ""
def norm(s): return s.replace("_", "").strip()

def static_paths():
    spec = json.load(open(os.path.join(here, "tests", "menubar.json")))
    out = set()
    def w(n, path):
        lab = norm(n.get("label", ""))
        p = path + [lab] if lab else path
        out.add(" > ".join(p))
        for k in n.get("children", []): w(k, p)
        if "submenu" in n: w(n["submenu"], p)
    w(spec, [])
    out |= {"Help" + p[len("About"):] for p in out if p == "About" or p.startswith("About > ")}   # (build 28) coot0 renames "About" to "Help"
    return out
STATIC = static_paths()

items = []
def collect(menu_shell, path):
    for it in menu_shell.get_children():
        cls = type(it).__name__
        if cls == "SeparatorMenuItem": continue
        lab = norm(label_of(it))
        if not lab and cls == "MenuItem" and not (hasattr(it, "get_submenu") and it.get_submenu() is not None): continue   # (an empty menu item is a separator, e.g. in the Restraints menu)
        p = path + [lab]
        sub = it.get_submenu() if hasattr(it, "get_submenu") else None
        if sub is not None: collect(sub, p)
        else: items.append((" > ".join(p), it))
collect(g["_menubar"], [])
# Several menus (Glyco, CCP4, Cryo-EM, Restraints, Refine, PDBe, ProSMART, SHELX, RCrane) are only created when their entry under
# "Calculate > Modules..." is used (builds 12-13: also "RCrane launch"; since build 14 "Calculate > RCrane" exists from start-up).  Create them first so that their items are swept too (builds up to 11 skipped
# ~95 items; in the first run they showed the failing "RCrane > New trace ..." entries, "Restraints > Generate Local Self Restraints 6" and
# "Cryo-EM > Multi-sharpen using Refmac...").
for p, it in list(items):
    if p.startswith("Calculate > Modules... > "):
        try:
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()): it.activate()
        except BaseException as e:
            print("SWEEP menu creator failed:", p, repr(e)[:120], flush=True)
items[:] = []
collect(g["_menubar"], [])
py_items = [(p, it) for p, it in items if p not in STATIC]
print("SWEEP total leaf items:", len(items), "python-added:", len(py_items), flush=True)

sid = _c.call("g_signal_lookup", "activate", _c.type_from_name("GtkMenuItem"))
SKIP = ("exit", "quit")
BUTTONS = os.environ.get("SWEEP_BUTTONS", "1") != "0"
import threading
ITEM_TIMEOUT = float(os.environ.get("SWEEP_ITEM_TIMEOUT", "60"))
_wd = [None]
def arm():
    if _wd[0]: _wd[0].cancel()
    def die():
        sys.stdout.flush(); os._exit(7)
    _wd[0] = threading.Timer(ITEM_TIMEOUT, die); _wd[0].daemon = True; _wd[0].start()
def btn_label(b):
    for m in ("get_label",):
        try: return getattr(b, m)() or ""
        except Exception: pass
    return ""
n_btn = n_btn_err = 0
n_ok = n_err = n_nohandler = n_skip = 0
for idx, (path, it) in enumerate(py_items):
    if idx < start: continue
    open(prog, "w").write("%d\t%s\n" % (idx, path))
    arm()
    if any(s in path.lower() for s in SKIP):
        res = "SKIP"; n_skip += 1
    else:
        has = _c.call("g_signal_has_handler_pending", it._ptr, sid, 0, True)
        if not has:
            res = "NO-HANDLER"; n_nohandler += 1
        else:
            n0 = len(_c.CALLBACK_ERRORS); w0 = len(H.windows)
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                    it.activate()
                    for _ in range(3): pass
            except BaseException as e:
                res = "EXC " + repr(e)[:160]; n_err += 1
            else:
                if len(_c.CALLBACK_ERRORS) > n0:
                    full = _c.CALLBACK_ERRORS[-1][1].strip()
                    last = full.splitlines()
                    res = "ERR " + last[-1][:200]; n_err += 1
                    open(outf + ".tracebacks", "a").write("== %d %s\n%s\n" % (idx, path, full))
                else:
                    res = "ok (%d windows)" % (len(H.windows) - w0); n_ok += 1
            if BUTTONS:
                for w in list(H.windows[w0:]):
                    for x in H.walk(w):
                        if type(x).__name__ != "Button": continue
                        bl = btn_label(x)
                        open(prog, "w").write("%d\t%s\tbutton %r\n" % (idx, path, bl))
                        e0 = len(_c.CALLBACK_ERRORS); b2 = io.StringIO()
                        try:
                            with contextlib.redirect_stdout(b2), contextlib.redirect_stderr(b2):
                                x.clicked()
                        except BaseException as e:
                            r2 = "EXC " + repr(e)[:160]
                        else:
                            r2 = "ok"
                            if len(_c.CALLBACK_ERRORS) > e0:
                                full = _c.CALLBACK_ERRORS[-1][1].strip()
                                r2 = "ERR " + full.splitlines()[-1][:200]
                                open(outf + ".tracebacks", "a").write("== BUTTON %d %s [%s]\n%s\n" % (idx, path, bl, full))
                        n_btn += 1
                        if r2 != "ok":
                            n_btn_err += 1
                            line = "BTN   %3d | %s | [%s] | %s" % (idx, path, bl, r2)
                            print(line, flush=True); open(outf, "a").write(line + "\n")
            for w in H.windows[w0:]:
                try: w.destroy()
                except Exception: pass
    line = "SWEEP %3d | %s | %s" % (idx, path, res)
    print(line, flush=True)
    open(outf, "a").write(line + "\n")
print("SWEEP summary: ok=%d err=%d nohandler=%d skip=%d buttons clicked=%d with errors=%d" % (n_ok, n_err, n_nohandler, n_skip, n_btn, n_btn_err), flush=True)
open(prog, "w").write("DONE\n")
coot.coot_real_exit(0)
