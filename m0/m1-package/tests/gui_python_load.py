
# Loads Coot's real GUI Python scripts (coot_load_modules.py: coot_gui, extensions, coot_toolbuttons, ...) on the PyGTK compatibility layer.
# A real (headless) GTK widget tree rebuilt from src/gtk2-interface.c (tests/menubar.json) stands in for the main window, because the sandbox has no window server.
import os, sys, io, types, json, traceback, contextlib
os.environ["COOT_GTK2COMPAT_HEADLESS"] = "1"
prefix = os.environ["COOT_PREFIX"]
res = []
def check(name, fn):
    try:
        # (build 20) only None / True pass: before, any returned text counted as a pass, so the "condition or 'message'" checks below could not fail
        v = fn(); ok = (v is None or v is True); res.append((name, ok, "" if ok else repr(v)[:120]))
    except BaseException as e: res.append((name, False, "EXC " + repr(e)[:200] + " " + traceback.format_exc()[-300:].replace("\n", " | ")))
import gtk, _gtk2core as _c
spec = json.load(open(os.path.join(prefix, "tests", "menubar.json")))
def build(n):
    k = n["kind"]
    if k == "menubar": w = gtk.MenuBar()
    elif k == "menu": w = gtk.Menu()
    elif k == "separator": w = gtk.SeparatorMenuItem()
    elif k == "imageitem": w = gtk.ImageMenuItem(); w.set_property("label", n["label"]); w.set_use_underline(True)
    elif k == "checkitem": w = gtk.CheckMenuItem(n["label"])
    else: w = gtk.MenuItem(n["label"])
    if k in ("menubar", "menu"):
        for c in n.get("children", []): w.append(build(c))
    if "submenu" in n: w.set_submenu(build(n["submenu"]))
    return w
mb = build(spec); tb = gtk.Toolbar(); sb = gtk.Statusbar(); hb = gtk.HBox()
native = types.ModuleType("_coot_python_native")
native.main_menubar = lambda: mb._ptr; native.main_toolbar = lambda: tb._ptr; native.main_statusbar = lambda: sb._ptr; native.main_hbox = lambda: hb._ptr
sys.modules["_coot_python_native"] = native
def items(menu, out=None):
    out = out if out is not None else []
    for it in menu.get_children():
        t = type(it).__name__
        if t == "SeparatorMenuItem": continue
        sub = it.get_submenu()
        out.append((it.get_property("label"), it, sub))
        if sub: items(sub, out)
    return out
n_before = len(items(mb))
windows = []                                           # every gtk.Window / Dialog the scripts create from now on
for cls in (gtk.Window, gtk.Dialog):
    def mk(c):
        orig = c.__init__
        def init(self, *a, **k): orig(self, *a, **k); windows.append(self)
        c.__init__ = init
    mk(cls)
import __main__
__main__.use_gui_qm = 1; __main__.have_guile_gtk = False
buf = io.StringIO(); err = []
path = os.path.join(prefix, "share/coot/python/coot_load_modules.py")
with contextlib.redirect_stdout(buf):
    try: exec(compile(open(path).read(), path, "exec"), __main__.__dict__)
    except BaseException: err.append(traceback.format_exc())
out = buf.getvalue()
check("coot_load_modules.py runs to the end", lambda: not err or err[-1][-300:])
check("no GUI script failed to load (\"couldn't load\")", lambda: "couldn't load" not in out or [l for l in out.splitlines() if "couldn't load" in l][:3])
allitems = items(mb)
check("the scripts add menu items to the main menubar (before %d, after %d; expect >= 280)" % (n_before, len(allitems)), lambda: len(allitems) >= 280)
def find(label):
    for l, it, sub in allitems:
        if l == label: return it
for want, minimum in (("All Molecule...", 3), ("Modelling...", 30), ("Modules...", 5)):
    check("Calculate > %s gets its submenu from the scripts (>= %d items)" % (want, minimum), lambda w=want, m=minimum: (find(w) is not None and find(w).get_submenu() is not None and len(find(w).get_submenu().get_children()) >= m) or "missing or too few")
labels = {l for l, it, sub in allitems}
for want in ("Copy Molecule...", "Copy Fragment...", "SMILES -> 2D", "SMILES -> simple 3D"):
    check("menu item %r exists" % want, lambda w=want: any(w.replace("...", "") in (l or "") for l in labels) or "not found")
# (build 20) Calculate > All Molecule... > Refine/Improve Ramachandran Plot...: in the 0.9.8.96 source the line that adds this entry is indented into
# the function the entry calls, so the entry never appeared.  It must be in the All Molecule submenu, and choosing it opens the molecule chooser.
def rama_menu_entry():
    am = find("All Molecule...")
    if am is None or am.get_submenu() is None: return "no All Molecule submenu"
    kids = [k for k in am.get_submenu().get_children() if k.get_children() and hasattr(k.get_children()[0], "get_text")]
    it = [k for k in kids if k.get_children()[0].get_text() == "Refine/Improve Ramachandran Plot..."]
    if not it: return "not in Calculate > All Molecule...: %r" % [k.get_children()[0].get_text() for k in kids]
    n0 = len(windows); it[0].activate()
    return True if len(windows) > n0 else "choosing it opened no window"
check("Calculate > All Molecule... > 'Refine/Improve Ramachandran Plot...' exists and opens the molecule chooser", rama_menu_entry)
# (build 21) the new entry that also tries the flipped orientation of every peptide
def rama_flip_menu_entry():
    am = find("All Molecule...")
    if am is None or am.get_submenu() is None: return "no All Molecule submenu"
    kids = [k for k in am.get_submenu().get_children() if k.get_children() and hasattr(k.get_children()[0], "get_text")]
    labels_ = [k.get_children()[0].get_text() for k in kids]
    it = [k for k in kids if k.get_children()[0].get_text() == "Refine/Improve Ramachandran Plot (try peptide flips)..."]
    if not it: return "not in Calculate > All Molecule...: %r" % labels_
    if "Refine/Improve Ramachandran Plot..." not in labels_: return "the original entry is gone: %r" % labels_
    n0 = len(windows); it[0].activate()
    return True if len(windows) > n0 else "choosing it opened no window"
check("Calculate > All Molecule... > 'Refine/Improve Ramachandran Plot (try peptide flips)...' exists next to the original and opens the molecule chooser", rama_flip_menu_entry)
# toolbar: the buttons the user could not find (Sphere Refine ...) are created by coot_toolbar_button()
check("coot_toolbar_button('Sphere Refine', ...) adds a toolbar button", lambda: (__main__.coot_toolbar_button("Sphere Refine", "sphere_refine()", "reset-view.svg", "RSR around active residue"), len(tb.get_children()) == 1 and tb.get_children()[0] is not None)[1])
def all_widgets(w, out):
    out.append(w)
    try: kids = w.get_children()
    except Exception: kids = []
    for k in kids: all_widgets(k, out)
    return out
def toolbar_manager():
    before = len(windows)
    __main__.make_toolbar_button_gui_for_test() if hasattr(__main__, "make_toolbar_button_gui_for_test") else None
    return True
# the "Manage Buttons" dialog is reached through the toolbar's right-click menu; find what the toolbar connected
check("main toolbar has a button-press handler (right-click menu: Manage Buttons / Add / Remove)", lambda: _c.call("g_signal_handler_find", tb._ptr, 1, _c.call("g_signal_lookup", "button-press-event", _c.instance_gtype(tb._ptr)), 0, None, None, None) != 0 or "no handler")
# dialogs the scripts build (the real functions, with a headless window)
for fname, args in (("molecule_chooser_gui", ("Molecule to Copy...", lambda imol: None)), ):
    check("%s builds its dialog (Copy molecule)" % fname, lambda f=fname, a=args: (len(windows), getattr(__main__, f)(*a), len(windows))[2] >= 1 or "no window created")
check("no exception in any GTK signal handler so far", lambda: not _c.CALLBACK_ERRORS or [e[1][-200:] for e in _c.CALLBACK_ERRORS][:2])
w = max(len(r[0]) for r in res)
for n, ok, v in res: print(("PASS " if ok else "FAIL ") + n.ljust(w) + ("  " + v if v else ""))
print("SUMMARY", sum(1 for r in res if r[1]), "/", len(res), flush=True)
import coot; coot.coot_real_exit(0)
