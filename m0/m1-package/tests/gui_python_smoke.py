
# gui_python_smoke.py -- run INSIDE the real Coot window, one command, no clicking:
#     ./run-coot.sh --script tests/gui_python_smoke.py
# It checks that the scripted GUI (PyGTK compatibility layer) works on the real main window, really shows each scripted dialog for a moment and closes it,
# and writes PASS / FAIL per item to  results/gui-smoke-<time>.txt  (also printed in the Terminal).  Coot stays open afterwards.
import os, sys, time, types, traceback
prefix = os.environ.get("COOT_PREFIX", "")
out_lines = []
def log(s):
    out_lines.append(s); print(s, flush=True)
results = []
def check(name, fn):
    try:
        v = fn(); ok = True if v is None else bool(v); results.append((name, ok, "" if v is None or v is True else repr(v)[:160]))
    except BaseException as e: results.append((name, False, "EXC " + repr(e)[:160] + " | " + traceback.format_exc()[-400:].replace("\n", " | ")))
def finish():
    w = max(len(r[0]) for r in results) if results else 10
    log("== Coot scripted GUI smoke test " + time.strftime("%Y-%m-%d %H:%M:%S"))
    for n, ok, v in results: log(("PASS " if ok else "FAIL ") + n.ljust(w) + ("  " + v if v else ""))
    log("SUMMARY %d / %d" % (sum(1 for r in results if r[1]), len(results)))
    d = os.path.join(prefix, "results"); os.makedirs(d, exist_ok=True)
    p = os.path.join(d, "gui-smoke-%s.txt" % time.strftime("%Y%m%d-%H%M%S")); open(p, "w").write("\n".join(out_lines) + "\n")
    print("Wrote", p, flush=True)

try:
    import gtk, gobject, pango, coot_python, _gtk2core as _c
except BaseException:
    traceback.print_exc(); results.append(("import gtk, gobject, pango, coot_python (the compatibility layer)", False, traceback.format_exc()[-300:])); finish(); raise SystemExit
check("GTK version", lambda: "%s" % (gtk.gtk_version,))
mb = coot_python.main_menubar(); tb = coot_python.main_toolbar()
check("coot_python.main_menubar() returns the real menubar", lambda: mb is not None and type(mb).__name__ == "MenuBar")
check("coot_python.main_toolbar() returns the real toolbar", lambda: tb is not None)
def items(menu, out=None):
    out = out if out is not None else []
    for it in menu.get_children():
        if type(it).__name__ == "SeparatorMenuItem": continue
        sub = it.get_submenu(); out.append((it.get_property("label"), it, sub))
        if sub: items(sub, out)
    return out
allitems = items(mb)
check("menubar has many items (%d; the C skeleton alone has about 140)" % len(allitems), lambda: len(allitems) >= 280)
def find(label):
    for l, it, sub in allitems:
        if l == label: return it
for want, minimum in (("All Molecule...", 3), ("Modelling...", 30), ("Modules...", 5)):
    check("Calculate > %s has its submenu (>= %d items)" % (want, minimum), lambda w=want, m=minimum: (find(w) is not None and find(w).get_submenu() is not None and len(find(w).get_submenu().get_children()) >= m) or "missing")

# --- real windows: show, let GTK draw them, destroy
created = []
def hook(cls):
    orig = cls.__init__
    def init(self, *a, **k): orig(self, *a, **k); created.append(self)
    cls.__init__ = init
for c in (gtk.Window, gtk.Dialog): hook(c)
def pump(n=80):
    for _ in range(n):
        if not gtk.events_pending(): break
        gtk.main_iteration(False)
def show_and_close(label, builder):
    def run():
        before = len(created)
        builder()
        pump()
        new = created[before:]
        if not new: return "no window was created"
        for w in new:
            try: w.show_all()
            except Exception: pass
        pump(); time.sleep(0.4); pump()
        for w in new:
            try: w.destroy()
            except Exception: pass
        pump()
        return True
    check(label, run)
import __main__
g = __main__.__dict__
if "molecule_chooser_gui" in g:
    show_and_close("Copy molecule: molecule_chooser_gui dialog shows", lambda: g["molecule_chooser_gui"]("Molecule to Copy...", lambda imol: None))
if "generic_chooser_and_entry" in g:
    show_and_close("generic_chooser_and_entry dialog shows", lambda: g["generic_chooser_and_entry"]("Choose", "Name:", "x", [], lambda *a: None))
if "dialog_box_of_buttons" in g:
    show_and_close("dialog_box_of_buttons dialog shows", lambda: g["dialog_box_of_buttons"]("Buttons", [200, 200], [["one", lambda *a: None], ["two", lambda *a: None]], "Close"))
if "make_toolbar_button_gui" in g:
    show_and_close("toolbar 'Manage Buttons' dialog (where Sphere Refine is switched on) shows", lambda: g["make_toolbar_button_gui"]())
check("a toolbar button can be added (Sphere Refine)", lambda: (g["coot_toolbar_button"]("Sphere Refine (smoke test)", "sphere_refine()", "reset-view.svg", "RSR around active residue"), True)[1])
check("no exception inside any GTK signal handler", lambda: not _c.CALLBACK_ERRORS or [e[1][-200:] for e in _c.CALLBACK_ERRORS][:2])
finish()
