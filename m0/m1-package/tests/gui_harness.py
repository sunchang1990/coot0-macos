
# Shared headless harness for the Python GUI-layer tests (used by gui_audit.py etc.).
# Builds a faithful copy of Coot's main menubar (tests/menubar.json, generated from gtk2-interface.c),
# loads the Coot Python GUI modules exactly as coot_load_modules.py does, and records every window created.
import os, sys, io, types, json, traceback, contextlib
os.environ["COOT_GTK2COMPAT_HEADLESS"] = "1"
prefix = os.environ["COOT_PREFIX"]
import gtk
import _gtk2core as _c

def _build(n):
    k = n["kind"]
    if k == "menubar": w = gtk.MenuBar()
    elif k == "menu": w = gtk.Menu()
    elif k == "separator": w = gtk.SeparatorMenuItem()
    elif k == "imageitem": w = gtk.ImageMenuItem(); w.set_property("label", n["label"]); w.set_use_underline(True)
    elif k == "checkitem": w = gtk.CheckMenuItem(n["label"])
    else: w = gtk.MenuItem(n["label"])
    if k in ("menubar", "menu"):
        for c in n.get("children", []): w.append(_build(c))
    if "submenu" in n: w.set_submenu(_build(n["submenu"]))
    return w

windows = []
def _track(cls):
    orig = cls.__init__
    def init(self, *a, **k):
        orig(self, *a, **k); windows.append(self)
    cls.__init__ = init

def load(quiet=True):
    """returns (globals_dict, load_errors)"""
    spec = json.load(open(os.path.join(prefix, "tests", "menubar.json")))
    mb = _build(spec); tb = gtk.Toolbar(); sb = gtk.Statusbar(); hb = gtk.HBox()
    native = types.ModuleType("_coot_python_native")
    native.main_menubar = lambda: mb._ptr; native.main_toolbar = lambda: tb._ptr
    native.main_statusbar = lambda: sb._ptr; native.main_hbox = lambda: hb._ptr
    sys.modules["_coot_python_native"] = native
    for cls in (gtk.Window, gtk.Dialog): _track(cls)
    import __main__
    __main__.use_gui_qm = 1; __main__.have_guile_gtk = False
    path = os.path.join(prefix, "share/coot/python/coot_load_modules.py")
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(open(path).read(), path, "exec"), __main__.__dict__)
    errs = [l for l in buf.getvalue().splitlines() if "couldn't load" in l or "Traceback" in l]
    __main__.__dict__["_menubar"] = mb
    return __main__.__dict__, errs, buf.getvalue()

def walk(w, out=None):
    if out is None: out = []
    out.append(w)
    try: kids = w.get_children()
    except Exception: kids = []
    for k in kids: walk(k, out)
    return out
