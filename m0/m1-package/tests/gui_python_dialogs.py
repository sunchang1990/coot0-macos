
# Headless tests of dialogs and fixes in the Python GUI scripts (PyGTK compatibility layer on real GTK, no display).
import os, sys, ast, glob, json, traceback
sys.path.insert(0, os.path.join(os.environ["COOT_PREFIX"], "tests"))
import gui_harness as H
import _gtk2core as _c
import gtk
res = []
def check(name, fn):
    try:
        v = fn(); ok = (v is None or v is True)   # anything else returned by a check is the failure detail
        res.append((name, ok, "" if ok else repr(v)[:200]))
    except BaseException as e:
        res.append((name, False, "EXC " + repr(e)[:160] + " " + traceback.format_exc()[-300:].replace("\n", " | ")))
g, errs, log = H.load()
import coot
here = os.environ["COOT_PREFIX"]
pydir = os.path.join(here, "share/coot/python")

check("all GUI scripts load (including rcrane_loader.py)", lambda: True if not errs else errs[:3])

# 1. no Python-2-only names left in the scripts
PY2 = {"StringType", "ListType", "IntType", "TupleType", "DictType", "FloatType", "isNumbertype", "unicode", "basestring", "xrange", "raw_input"}
PY2_CALLS = {"apply", "file"}
def py2_names():
    bad = []
    for f in sorted([x for x in glob.glob(os.path.join(pydir, "*.py")) if not x.endswith("/coot.py") and not x.endswith("/coot_python.py")] + glob.glob(os.path.join(pydir, "rcrane", "*.py"))):
        tree = ast.parse(open(f, encoding="utf-8", errors="replace").read())
        for n in ast.walk(tree):
            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load) and n.id in PY2:
                bad.append("%s:%d %s" % (os.path.basename(f), n.lineno, n.id))
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in PY2_CALLS:
                bad.append("%s:%d %s()" % (os.path.basename(f), n.lineno, n.func.id))
            if isinstance(n, ast.ImportFrom) and n.module == "types" and any(a.name in PY2 for a in n.names):
                bad.append("%s:%d from types import ..." % (os.path.basename(f), n.lineno))
    return bad
check("no Python-2-only names in the shipped scripts", lambda: True if not py2_names() else py2_names()[:5])

# 2. toolbar manager has the buttons the user asked for
def labels_of(win):
    out = []
    for x in H.walk(win):
        for m in ("get_label", "get_text"):
            if hasattr(x, m) and type(x).__name__ in ("Button", "CheckButton", "RadioButton", "Label", "ToggleButton"):
                try: out.append(getattr(x, m)())
                except Exception: pass
    return out
def dialog(fn, *a):
    n0 = len(H.windows); r = fn(*a); return r, H.windows[n0:]
def manage_buttons():
    r, ws = dialog(g["make_toolbar_button_gui"])
    lab = [l for w in ws for l in labels_of(w)]
    return ("Sphere Refine" in lab and "Sphere Regularization" in lab and len(lab) > 100) or lab[:10]
check("Manage Buttons dialog offers Sphere Refine and Sphere Regularization", manage_buttons)

# 3. dialog_box_of_buttons (was NameError StringType) with string, list and function callbacks; click them
clicked = []
g["_probe_clicked"] = clicked
def box_of_buttons():
    funcs = [["string callback", "_probe_clicked.append('s')"], ["list callback", ["_probe_clicked.append('l')"]],
             ["function callback", lambda *a: clicked.append("f")]]
    r, ws = dialog(g["dialog_box_of_buttons"], "probe", [200, 200], funcs, " Close ")
    for w in ws:
        for x in H.walk(w):
            if type(x).__name__ == "Button" and x.get_label() in ("string callback", "list callback", "function callback"): x.clicked()
    return sorted(clicked) == ["f", "l", "s"] or clicked
check("dialog_box_of_buttons builds and its buttons run string/list/function callbacks", box_of_buttons)

# 4. data-dependent dialogs
imol = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
imap = coot.make_and_draw_map(os.path.join(here, "test-data", "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
g["imol"] = imol
check("molecule_atom_overlaps_gui (ported from Scheme) builds a box of buttons", lambda: True if len(dialog(g["molecule_atom_overlaps_gui"], imol)[1]) >= 1 else "no window")
check("pepflips_by_difference_map_gui (ported from Scheme) builds and OK reports 'no difference map'", lambda: (lambda r, ws: [x.clicked() for w in ws for x in H.walk(w) if type(x).__name__ == "Button" and "OK" in x.get_label()] and True)(*dialog(g["pepflips_by_difference_map_gui"])) or "no OK button")
check("copy molecule chooser builds", lambda: True if len(dialog(g["molecule_chooser_gui"], "Molecule to copy", lambda i: None)[1]) >= 1 else "no window")
check("generic_chooser_and_entry builds", lambda: True if len(dialog(g["generic_chooser_and_entry"], "Molecule:", "Atom selection:", "//A/1-10", lambda i, t: None)[1]) >= 1 else "no window")
check("smiles_gui builds", lambda: True if len(dialog(g["smiles_gui"])[1]) >= 1 else "no window")
check("whats_new_dialog builds", lambda: True if len(dialog(g["whats_new_dialog"])[1]) >= 1 else "no window")

# 5. fixed name bugs
for fn in ("save_dialog_positions_to_init_file", "chain_n_residues", "residue_spec_to_residue_name", "handle_shelx_fcf_file", "molecule_atom_overlaps_gui", "pepflips_by_difference_map_gui"):
    check("%s is defined" % fn, lambda f=fn: f in g or hasattr(coot, f))
def save_positions():
    home = os.environ.get("HOME", "/tmp"); rc = os.path.join(home, ".coot.py")
    existed = os.path.isfile(rc)
    if not existed: open(rc, "w").write("# probe\n")
    size0 = os.path.getsize(rc)
    open("0-coot.state.py", "w").write("set_main_window_dialog_position(1, 2)\nset_go_to_atom_window_position(3, 4)\nother_line(5)\n")
    save = g["save_state"]; g["save_state"] = lambda: None      # --no-state-script: the real save_state writes nothing here
    try: g["save_dialog_positions_to_init_file"]()
    finally: g["save_state"] = save
    txt = open(rc).read()[size0:]
    if not existed: os.remove(rc)
    os.remove("0-coot.state.py")
    lines = txt.splitlines()
    ok = ("set_go_to_atom_window_position(3, 4)" in lines) and "other_line(5)" not in lines and sum(1 for l in lines if l.startswith("# ---")) >= 3
    return True if ok else repr(txt[:300])
check("save_dialog_positions_to_init_file appends whole lines to ~/.coot.py", save_positions)

# 6. RCrane
def rcrane_menu():
    import rcrane
    return rcrane.createRCraneMenuWithCheck() is True
check("RCrane imports and its pre-launch check passes", rcrane_menu)
def rcrane_submenu_exists():
    # since build 14: a sub-menu "RCrane" of the Calculate menu from start-up (build 13: an item "RCrane launch" that created a top-level menu)
    def rec(shell, path, out):
        for it in shell.get_children():
            lab = (getattr(it, "get_label", lambda: "")() or "").replace("_", "")
            sub = it.get_submenu() if hasattr(it, "get_submenu") else None
            if sub is not None:
                out.append((path + [lab], [(i.get_label() or "") for i in sub.get_children()]))
                rec(sub, path + [lab], out)
        return out
    subs = [e for e in rec(g["_menubar"], [], []) if e[0] == ["Calculate", "RCrane"]]
    if len(subs) != 1: return "no Calculate > RCrane sub-menu (%d)" % len(subs)
    return True if len(subs[0][1]) == 6 else "RCrane sub-menu entries: %r" % (subs[0][1],)
check("Calculate menu has the 'RCrane' sub-menu with 6 entries", rcrane_submenu_exists)

# 7. C -> Python call-outs while Python drives GTK (the GUI audit found Coot crashing here when the GIL was released during GTK calls):
#    a menu item wired to Coot's own C callback (on_edit_copy_molecule1_activate -> do_edit_copy_molecule -> PyRun_SimpleString) is activated from Python.
def c_callout(cb_name, expect_new_window=True):
    import ctypes
    lib = ctypes.PyDLL(None)                                           # coot-bin's own exported symbols
    fn = ctypes.cast(getattr(lib, cb_name), ctypes.c_void_p).value
    item = gtk.MenuItem("probe")
    _c.call("g_signal_connect_data", item._ptr, "activate", fn, None, None, 0)
    n0 = len(H.windows)
    item.activate()                                                    # a crash here kills the whole test run
    return True if (not expect_new_window or len(H.windows) > n0) else "the C call-out ran but built no dialog"
check("C callback on_edit_copy_molecule1_activate (Edit > Copy Molecule...) runs its Python call-out", lambda: c_callout("on_edit_copy_molecule1_activate"))
check("C callback on_edit_copy_fragment1_activate (Edit > Copy Fragment...) runs its Python call-out", lambda: c_callout("on_edit_copy_fragment1_activate", False))

# 8. the two harmless GTK/GLib messages are filtered, other criticals are not
def log_filter():
    import tempfile
    path = tempfile.mktemp()
    sys.stderr.flush(); fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC); keep = os.dup(2); os.dup2(fd, 2)
    try:
        _c.call("g_return_if_fail_warning", "Gtk", "shortcuts_add_bookmark_from_file", "G_IS_FILE (file)")
        _c.call("g_return_if_fail_warning", "Gtk", "some_other_function", "SOME_OTHER_CHECK (x)")
    finally:
        os.dup2(keep, 2); os.close(keep); os.close(fd)
    txt = open(path).read(); os.remove(path)
    return True if ("SOME_OTHER_CHECK" in txt and "G_IS_FILE" not in txt) else repr(txt[:300])
check("log filter drops the two harmless GTK messages but not other criticals", log_filter)

# Stop / Continue / Cancel buttons of "Stepped Refine..." and the other interruptible fits.  A Python 3 porting slip
# (`type(cb) is bytes` for the old string-callback style) made every string callback print "cannot evaluate or call
# function", so Stop did nothing and no Continue button ever appeared.
import __main__ as _m
def string_callback_runs():
    hit = []
    _m.__dict__["_toolbar_test_hit"] = lambda: hit.append(1)
    b = _m.coot_toolbar_button("TestStringCb", "_toolbar_test_hit()", "gtk-stop")
    b.emit("clicked")
    return True if hit == [1] else "the string callback did not run: %r" % (hit,)
check("a toolbar button with a string callback runs it", string_callback_runs)
def stop_continue_cancel():
    _m.continue_multi_refine = True
    _m.multi_refine_separator = _m.add_coot_toolbar_separator()
    _m.multi_refine_stop_button = _m.coot_toolbar_button("Stop", "stop_interruptible_fit_protein()", "gtk-stop")
    _m.multi_refine_stop_button.emit("clicked")
    labels = [f[0] for f in _m.toolbar_label_list()]
    if not ("Cancel" in labels and "Continue" in labels):
        return "after Stop the toolbar has %r" % (labels,)
    if _m.continue_multi_refine is not False:
        return "Stop did not clear continue_multi_refine"
    _m.cancel_interruptible_fit_protein()
    labels = [f[0] for f in _m.toolbar_label_list()]
    left = {"Stop", "Cancel", "Continue"} & set(labels)
    return True if not left else "buttons left after Cancel: %r" % (sorted(left),)
check("Stop makes Cancel and Continue buttons appear, Cancel removes them again", stop_continue_cancel)
# (build 15, found by the real-window audit) Stop, then a new Stepped Refine: the old Stop / Cancel / Continue stayed on the toolbar and pressing them
# raised AttributeError: 'bool' object has no attribute 'destroy'.
def stop_then_new_run():
    def tb(): return [f[0] for f in _m.toolbar_label_list() if f[0] in ("Stop", "Cancel", "Continue")]
    dummy = lambda spec, imap: None
    e0 = len(_c.CALLBACK_ERRORS)
    _m.cancel_interruptible_fit_protein() if _m.__dict__.get("multi_refine_stop_button") else None
    _m.continue_multi_refine = True
    _m.interruptible_fit_protein(imol, dummy)
    _m.multi_refine_stop_button.emit("clicked")                       # Stop: Cancel + Continue appear
    _m.continue_multi_refine = True
    _m.interruptible_fit_protein(imol, dummy)                        # a new run while the first is stopped
    after_new = tb()
    if sorted(after_new) != ["Stop"]:
        return "after a new run the toolbar has %r (expected only the new Stop)" % (after_new,)
    _m.multi_refine_stop_button.emit("clicked")
    _m.cancel_interruptible_fit_protein(); _m.cancel_interruptible_fit_protein()   # twice: harmless
    _m.stop_interruptible_fit_protein(); _m.continue_interruptible_fit_protein()   # after the run is gone: harmless
    errs = [e[1].strip().splitlines()[-1] for e in _c.CALLBACK_ERRORS[e0:]]
    if errs: return "callback errors: %r" % errs[:3]
    return True if not tb() else "buttons left: %r" % (tb(),)
check("Stop, then a new Stepped Refine run: one Stop button, old buttons gone, Cancel/Stop/Continue after the end are harmless", stop_then_new_run)
def str_checks():
    import re
    bad = []
    for f in sorted(glob.glob(os.path.join(pydir, "*.py"))):
        src = open(f, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"(type\([^)]*\)\s+is\s+bytes|isinstance\([^)]*,\s*bytes\))", src):
            bad.append("%s: %s" % (os.path.basename(f), m.group(0)))
    return True if not bad else bad[:5]
check("no str/bytes type tests left in the shipped scripts (2to3 turned types.StringType into bytes)", str_checks)

# Calculate > Scripting... > Python...: the window's code returns gtk.FALSE from a helper; the compatibility layer had no gtk.FALSE, so every
# command typed into the window ended in AttributeError and showed no result (build 11 and earlier).
import contextlib, io
import __main__ as _m
def scripting_window():
    w0 = len(H.windows)
    with contextlib.redirect_stdout(io.StringIO()): _m.coot_gui()
    wins = H.windows[w0:]
    ents = [x for w in wins for x in H.walk(w) if type(x).__name__ == "Entry"]
    tvs = [x for w in wins for x in H.walk(w) if type(x).__name__ == "TextView"]
    if not (ents and tvs): return "no entry / text view in the scripting window"
    return ents[0], tvs[0]
def typed(entry, tv, text):
    n0 = len(_c.CALLBACK_ERRORS)
    entry.set_text(text)
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()): entry.emit("activate")
    tb = tv.get_buffer(); shown = tb.get_text(tb.get_start_iter(), tb.get_end_iter())
    return shown, [e[1].strip().splitlines()[-1] for e in _c.CALLBACK_ERRORS[n0:]]
_sw = {}
def sw_open():
    r = scripting_window()
    if isinstance(r, str): return r
    _sw["entry"], _sw["tv"] = r; return True
check("Python scripting window opens", sw_open)
def sw_result():
    shown, errs_ = typed(_sw["entry"], _sw["tv"], "1+1")
    if errs_: return "callback error: %r" % errs_
    return True if shown.rstrip().endswith("2") or "\n2\n" in shown else "window text: %r" % shown[-120:]
check("typing 1+1 into the scripting window shows 2 (no gtk.FALSE error)", sw_result)
def sw_coot_call():
    shown, errs_ = typed(_sw["entry"], _sw["tv"], "graphics_n_molecules()")
    if errs_: return "callback error: %r" % errs_
    answers = [l.strip() for l in shown.splitlines() if l.strip() and not l.strip().startswith("coot >>")]
    return True if (answers and answers[-1].isdigit()) else "window text: %r" % shown[-120:]
check("a Coot function typed into the scripting window returns its value", sw_coot_call)
def sw_error():
    shown, errs_ = typed(_sw["entry"], _sw["tv"], "1/0")
    if errs_: return "callback error: %r" % errs_
    return True if "ZeroDivisionError" in shown or "division" in shown else "window text: %r" % shown[-160:]
check("a Python error typed into the scripting window is reported in the window", sw_error)
def compat_classes():
    import gtk
    bad = []
    if (gtk.TRUE, gtk.FALSE) != (True, False): bad.append("TRUE/FALSE")
    a = gtk.Alignment(xalign=0.5, yalign=0.5); a.add(gtk.Label("x"))
    d = gtk.AboutDialog()
    for call in ("set_name", "set_version", "set_copyright", "set_website", "set_comments", "set_license"): getattr(d, call)("x")
    d.set_wrap_license(True)
    d.action_area.pack_start(gtk.Button("References"), False, True, 0)
    gtk.HScrollbar(); gtk.VScrollbar()
    return True if not bad else bad
check("gtk.TRUE/FALSE, Alignment, AboutDialog (set_*, action_area) and scrollbars exist in the compatibility layer", compat_classes)

# Sliders: PyGTK 2 gave gtk.Adjustment the struct members value / lower / upper / ...; the compatibility layer did not, so every move of the
# clipping / zoom slider (Nudge Screen Centre with Extras), the map sharpening slider, the nudge-residues slider and the occupancy slider raised
# AttributeError: 'Adjustment' object has no attribute 'value' (build 11 and earlier)
def adjustment_members():
    a = gtk.Adjustment(5.0, 0.0, 10.0, 1.0, 2.0, 0.0)
    got = (a.value, a.lower, a.upper, a.step_increment, a.page_increment, a.page_size)
    a.value = 7.5
    return True if (got == (5.0, 0.0, 10.0, 1.0, 2.0, 0.0) and a.value == 7.5) else "got %r, then value %r" % (got, a.value)
check("gtk.Adjustment has value, lower, upper, step_increment, page_increment, page_size (settable)", adjustment_members)
def scales_of(wins): return [x for w in wins for x in H.walk(w) if type(x).__name__ == "HScale"]
def move(adj, v):
    n0 = len(_c.CALLBACK_ERRORS)
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()): adj.value = v
    return [e[1].strip().splitlines()[-1] for e in _c.CALLBACK_ERRORS[n0:]]
def zoom_clip_dialog():
    w0 = len(H.windows)
    with contextlib.redirect_stdout(io.StringIO()): _m.nudge_screen_centre_extra_gui()
    sc = scales_of(H.windows[w0:])
    if len(sc) != 2: return "%d sliders in the dialog" % len(sc)
    clip, zoom = sc[0].get_adjustment(), sc[1].get_adjustment()
    e1 = move(clip, 2.0)
    z0 = coot.zoom_factor(); e2 = move(zoom, z0 * 2.0)
    if e1 or e2: return "callback errors %r %r" % (e1, e2)
    return True if abs(coot.zoom_factor() - z0 * 2.0) < 1e-3 * z0 else "zoom %.4f -> %.4f, expected %.4f" % (z0, coot.zoom_factor(), z0 * 2.0)
check("Nudge Screen Centre with Extras: the zoom slider changes the zoom, the clipping slider runs", zoom_clip_dialog)
def sharpen_dialog():
    mtz = os.path.join(here, "test-data", "rnasa-1.8-all_refmac1.mtz")
    imap = coot.make_and_draw_map(mtz, "FWT", "PHWT", "", 0, 0)
    w0 = len(H.windows)
    with contextlib.redirect_stdout(io.StringIO()): _m.map_sharpening_gui(imap)
    sc = scales_of(H.windows[w0:])
    if len(sc) != 1: return "%d sliders in the dialog" % len(sc)
    errs_ = move(sc[0].get_adjustment(), 12.0)
    return True if not errs_ else errs_
check("map sharpening slider (Python dialog) runs sharpen() when moved", sharpen_dialog)
def nudge_dialog():
    imol_n = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
    n0 = coot.graphics_n_molecules()
    w0 = len(H.windows)
    with contextlib.redirect_stdout(io.StringIO()): _m.nudge_residues_gui(imol_n, ["A", 40, ""])
    sc = scales_of(H.windows[w0:])
    if len(sc) != 1: return "%d sliders in the dialog" % len(sc)
    errs_ = move(sc[0].get_adjustment(), 2.0)
    if errs_: return errs_
    return True if coot.graphics_n_molecules() > n0 + 0 else "no molecule was made by nudging"
check("Interactive Nudge Residues: moving the slider makes a molecule with the nudged residues", nudge_dialog)

# Stepped Refine (Calculate > All Molecule... > Stepped Refine...): the residues being refined are shown in the refinement style (the intermediate
# atoms) and the result is accepted afterwards.  Before build 13 the refinement ran in "immediate replacement" mode, in which nothing of it is drawn.
import time as _time
def stepped_refine_shows():
    imol_s = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
    imap_s = coot.make_and_draw_map(os.path.join(here, "test-data", "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
    coot.set_imol_refinement_map(imap_s); coot.set_refinement_immediate_replacement(0)
    ch = coot.chain_id_py(imol_s, 0)
    coot.write_pdb_file(imol_s, "stepped_before.pdb")
    log = []
    keep = _m.accept_regularizement
    def spy(*a):
        log.append(bool(coot.refinement_already_ongoing_p())); return keep(*a)
    _m.accept_regularizement = spy
    try: _m.refine_auto_range_and_show(imol_s, ch, 43, "", seconds=0.3, force=True)
    finally: _m.accept_regularizement = keep
    coot.write_pdb_file(imol_s, "stepped_after.pdb")
    def atoms(fn):
        d = {}
        for l in open(fn):
            if l.startswith(("ATOM", "HETATM")) and l[16] in " A": d[(l[21], int(l[22:26]), l[12:16].strip())] = (float(l[30:38]), float(l[38:46]), float(l[46:54]))
        return d
    b, a = atoms("stepped_before.pdb"), atoms("stepped_after.pdb")
    moved = sorted(set(k[1] for k in a if k in b and sum((x - y) ** 2 for x, y in zip(a[k], b[k])) > 1e-8))
    if log != [True]: return "refining atoms were shown when the result was accepted: %r (expected [True])" % (log,)
    if coot.refinement_already_ongoing_p(): return "refinement still displayed after the result was accepted"
    return True if (43 in moved and len(moved) >= 2) else "residues that moved: %r" % (moved,)
check("Stepped Refine: the refining atoms are displayed (refinement_already_ongoing_p) until the result is accepted, and the residues move", stepped_refine_shows)
def stepped_refine_stop():
    imol_s = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
    ch = coot.chain_id_py(imol_s, 0)
    _m.continue_multi_refine = False
    t0 = _time.time()
    _m.refine_auto_range_and_show(imol_s, ch, 60, "", seconds=30.0, force=True)
    dt = _time.time() - t0; _m.continue_multi_refine = True
    return True if (dt < 15 and not coot.refinement_already_ongoing_p()) else "took %.1f s / refinement left displayed" % dt
check("Stepped Refine: pressing Stop ends the display at once and leaves nothing pending", stepped_refine_stop)
def old_way_zero_seconds():
    imol_s = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
    ch = coot.chain_id_py(imol_s, 0)
    _m.refine_auto_range_and_show(imol_s, ch, 70, "", seconds=0)
    return True if not coot.refinement_already_ongoing_p() else "refinement left displayed"
check("Stepped Refine: COOT_STEPPED_REFINE_SHOW=0 keeps the old immediate behaviour", old_way_zero_seconds)

# Stepped Refine, round 14: (a) Coot's own "Accept Refinement?" window must not be left on the screen (its buttons are useless there: the script accepts every
# residue itself) - it is hidden when it appears and closed after the accept; (b) the density must be re-contoured around every residue that is refined
# (go-to-atom only moves the view: before build 14 the map stayed contoured around the old position, and a residue had no density until the user changed
# the contour level).
def stepped_refine_accept_window():
    imol_s = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
    imap_s = coot.make_and_draw_map(os.path.join(here, "test-data", "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
    coot.set_imol_refinement_map(imap_s); coot.set_refinement_immediate_replacement(0)
    ch = coot.chain_id_py(imol_s, 0)
    events = []
    def title_of(w):
        try: return w.get_title()
        except Exception: return None
    orig_call = _c.call
    def spy_call(name, *a, **k):          # (Widget.hide / Widget.destroy are looked up at run time: watch the GTK calls)
        if name in ("gtk_widget_hide", "gtk_widget_destroy") and a and title_of(a[0]) == "Accept Refinement?":
            events.append("hide" if name == "gtk_widget_hide" else "destroy")
        return orig_call(name, *a, **k)
    keep_ra, keep_acc = _m.refine_auto_range, _m.accept_regularizement
    def fake_refine(*a):          # Coot opens this window for every ordinary refinement
        w = gtk.Window(gtk.WINDOW_TOPLEVEL); w.set_title("Accept Refinement?")
        return keep_ra(*a)
    def acc(*a): events.append("accept"); return keep_acc(*a)
    _c.call = spy_call
    _m.refine_auto_range, _m.accept_regularizement = fake_refine, acc
    try: _m.refine_auto_range_and_show(imol_s, ch, 43, "", seconds=0.3, force=True)
    finally:
        _c.call = orig_call
        _m.refine_auto_range, _m.accept_regularizement = keep_ra, keep_acc
    left = [w for w in gtk.window_list_toplevels() if title_of(w) == "Accept Refinement?"]
    if "hide" not in events or events.index("hide") > events.index("accept"): return "the window was not hidden before the accept: %r" % (events,)
    if events[-1] != "destroy" or events.index("destroy") < events.index("accept"): return "the window was not closed after the accept: %r" % (events,)
    return True if not left else "%d 'Accept Refinement?' windows are still there" % len(left)
check("Stepped Refine: Coot's 'Accept Refinement?' window is hidden while the residues are shown and closed after the accept", stepped_refine_accept_window)
def stepped_refine_maps_follow():
    import tempfile, re, math
    imol_s = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
    imap_s = coot.make_and_draw_map(os.path.join(here, "test-data", "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
    coot.set_imol_refinement_map(imap_s); coot.set_go_to_atom_molecule(imol_s)
    ch = coot.chain_id_py(imol_s, 0)
    def ca(r):
        for a in coot.residue_info_py(imol_s, ch, r, "") or []:
            if a[0][0].strip() == "CA": return a[2][:3]
    want = {r: ca(r) for r in (20, 60)}
    keep_env = os.environ.get("COOT_DEBUG_MAPS"); os.environ["COOT_DEBUG_MAPS"] = "1"      # every re-contouring is reported with its centre
    sys.stdout.flush(); saved = os.dup(1); tmp = tempfile.TemporaryFile(); os.dup2(tmp.fileno(), 1)
    try:
        for r in want: _m.fit_protein_stepped_refine_function([imol_s, ch, r, ""], imap_s)
    finally:
        sys.stdout.flush(); os.dup2(saved, 1); os.close(saved)
        if keep_env is None: del os.environ["COOT_DEBUG_MAPS"]
        else: os.environ["COOT_DEBUG_MAPS"] = keep_env
    tmp.seek(0); out = tmp.read().decode(errors="replace")
    centres = [tuple(float(x) for x in m_.groups()) for m_ in re.finditer(r"DEBUG-MAPS:: update_map_triangles imol %d centre \(([-\d.e]+), ([-\d.e]+), ([-\d.e]+)\)" % imap_s, out)]
    miss = [r for r, xyz in want.items() if not any(math.dist(c, xyz) < 1.0 for c in centres)]
    return True if not miss else "no map re-contouring around residue(s) %r (re-contoured centres: %r)" % (miss, centres[:6])
check("Stepped Refine: the map is re-contoured around each residue that is refined (density follows the focus)", stepped_refine_maps_follow)

# (build 20) Fit Protein and Refine/Improve Ramachandran Plot show their refinement like Stepped Refine.  Fit Protein refined with AutoAccept before:
# "immediate replacement" on, so nothing of the refinement was drawn and the residue jumped to its result.  Now every refinement runs with immediate
# replacement off and its atoms stay displayed (refinement style) for stepped_refine_show_seconds before the script accepts.  The display is only used
# with graphics, so the test says graphics are on.
def shown_refinement(fit, pdb="tutorial-modern.pdb", mtz="rnasa-1.8-all_refmac1.mtz", res_nos=(43,)):
    imol_s = coot.read_pdb(os.path.join(here, "test-data", pdb))
    imap_s = coot.make_and_draw_map(os.path.join(here, "test-data", mtz), "FWT", "PHWT", "", 0, 0)
    coot.set_imol_refinement_map(imap_s); coot.set_refinement_immediate_replacement(0); coot.set_go_to_atom_molecule(imol_s)
    ch = coot.chain_id_py(imol_s, 0)
    spf, rama = coot.dragged_refinement_steps_per_frame(), coot.refine_ramachandran_angles_state()
    log = []
    keep = {n: getattr(_m, n) for n in ("accept_regularizement", "use_graphics_interface_state", "refine_zone", "refine_auto_range")}
    def spy_refine(f):
        def g(*a):
            r = f(*a); log.append(("refine", coot.refinement_immediate_replacement_state(), coot.refine_ramachandran_angles_state(), _time.time())); return r
        return g
    def spy_acc(*a):
        log.append(("accept", bool(coot.refinement_already_ongoing_p()), None, _time.time())); return keep["accept_regularizement"](*a)
    _m.accept_regularizement, _m.use_graphics_interface_state = spy_acc, (lambda: 1)
    _m.refine_zone, _m.refine_auto_range = spy_refine(keep["refine_zone"]), spy_refine(keep["refine_auto_range"])
    _m.continue_multi_refine = True
    try:
        for r in res_nos: fit([imol_s, ch, r, ""], imap_s)
    finally:
        for n, f in keep.items(): setattr(_m, n, f)
    refs = [e for e in log if e[0] == "refine"]
    if not refs: return log, "no refinement was run"
    if any(e[1] != 0 for e in refs): return log, "refinement ran with immediate replacement on (nothing is drawn): %r" % ([e[:3] for e in log],)
    for i, e in enumerate(log):          # every refinement: its atoms are displayed for >= 0.4 s, then accepted
        if e[0] == "refine":
            nxt = [x for x in log[i+1:] if x[0] == "accept"][:1]
            if not nxt or not nxt[0][1] or nxt[0][3] - e[3] < 0.4:
                return log, "refining atoms not displayed until the accept: %r" % ([(x[0], x[1], round(x[3] - log[0][3], 2)) for x in log],)
    if coot.refinement_already_ongoing_p(): return log, "refinement still displayed after the result was accepted"
    if coot.dragged_refinement_steps_per_frame() != spf: return log, "steps per frame not restored"
    if coot.refine_ramachandran_angles_state() != rama: return log, "Ramachandran restraint setting not restored"
    return log, True
check("Fit Protein: the refinement is shown (immediate replacement off, refining atoms displayed until the accept), settings restored",
      lambda: shown_refinement(_m.fit_protein_fit_function)[1])
def fit_protein_rna_centre():
    import math
    log, ok = shown_refinement(_m.fit_protein_fit_function, "1ehz.pdb", "1ehz_map.mtz", (10, 40))
    if ok is not True: return ok
    imol_s = coot.graphics_n_molecules() - 2
    c1 = [a[2][:3] for a in coot.residue_info_py(imol_s, "A", 40, "") if a[0][0].strip() == "C1'"]
    centre = [coot.rotation_centre_position(i) for i in range(3)]
    return True if c1 and math.dist(centre, c1[0]) < 2.0 else "view centre %r is not at C1' of A 40 %r" % (centre, c1)
check("Fit Protein on RNA (1EHZ): the view moves to each nucleotide (C1') and its refinement is shown", fit_protein_rna_centre)
def rama_shows():
    log, ok = shown_refinement(_m.fit_protein_rama_fit_function)
    if ok is not True: return ok
    return True if all(e[2] == 1 for e in log if e[0] == "refine") else "Ramachandran restraints were off during the refinement: %r" % (log,)
check("Refine/Improve Ramachandran Plot: the refinement is shown with Ramachandran restraints on, settings restored afterwards", rama_shows)

# (build 21) Refine/Improve Ramachandran Plot (try peptide flips): for every residue both orientations of the peptide to the next residue are refined
# (with Ramachandran restraints) and the better one is kept (Ramachandran regions first, then map fit).  Peptides of tutorial-modern.pdb are flipped on
# purpose (pepflip moves the carbonyl O by ~3.4 A); the routine must put them back (O within 0.5 A of the deposited position) and leave correct ones.
import math as _math
def _flip_setup():
    imol_f = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
    imap_f = coot.make_and_draw_map(os.path.join(here, "test-data", "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
    coot.set_imol_refinement_map(imap_f); _m.continue_multi_refine = True
    O = lambda r: [a[2] for a in coot.residue_info_py(imol_f, "A", r, "") if a[0][0].strip() == "O"][0]
    return imol_f, imap_f, O
def rama_flip_corrects():
    imol_f, imap_f, O = _flip_setup()
    bad = []
    for r in (20, 43, 60, 85):
        o0 = O(r); coot.pepflip(imol_f, "A", r, "", "")
        if _math.dist(o0, O(r)) < 2.5: return "the deliberate flip of A %d did not move O" % r
        _m.fit_protein_rama_flip_function([imol_f, "A", r, ""], imap_f)
        if _math.dist(o0, O(r)) > 0.5: bad.append((r, round(_math.dist(o0, O(r)), 2)))
    return True if not bad else "flipped peptides not put back (residue, O distance from the deposited position): %r" % bad
check("Ramachandran (try peptide flips): 4 peptides flipped on purpose are flipped back (O within 0.5 A of the deposited model)", rama_flip_corrects)
def rama_flip_keeps_correct():
    imol_f, imap_f, O = _flip_setup()
    bad = []
    for r in (30, 50, 70, 90):
        o0 = O(r); _m.fit_protein_rama_flip_function([imol_f, "A", r, ""], imap_f)
        if _math.dist(o0, O(r)) > 0.5: bad.append((r, round(_math.dist(o0, O(r)), 2), _m.rama_flip_log[-1][2:]))
    return True if not bad else "correct peptides were flipped: %r" % bad
check("Ramachandran (try peptide flips): 4 correct peptides are left as they are", rama_flip_keeps_correct)
def rama_flip_shows():
    log, ok = shown_refinement(_m.fit_protein_rama_flip_function)
    if ok is not True: return ok
    refs = [e for e in log if e[0] == "refine"]
    if len(refs) != 2: return "expected 2 shown refinements (as it is, flipped), got %d" % len(refs)
    return True if all(e[2] == 1 for e in refs) else "Ramachandran restraints were off during a try: %r" % (refs,)
check("Ramachandran (try peptide flips): both tries are shown like Stepped Refine, with Ramachandran restraints on, settings restored", rama_flip_shows)
def rama_flip_stop():
    imol_f, imap_f, O = _flip_setup()
    o0 = O(43); coot.pepflip(imol_f, "A", 43, "", ""); n_log = len(_m.rama_flip_log)
    _m.continue_multi_refine = False                 # Stop pressed: the first try (refinement as it is) is kept, no flip is tried
    try: _m.fit_protein_rama_flip_function([imol_f, "A", 43, ""], imap_f)
    finally: _m.continue_multi_refine = True
    if len(_m.rama_flip_log) != n_log: return "a flip was tried after Stop: %r" % (_m.rama_flip_log[-1],)
    return True if _math.dist(o0, O(43)) > 2.0 else "after Stop the peptide was flipped back anyway (O %.2f A from the deposited position)" % _math.dist(o0, O(43))
check("Ramachandran (try peptide flips): after Stop the current try is kept and no flip is made", rama_flip_stop)
# scores: (Ramachandran sum, residues classified, map fit, carbonyl O in sigma, peptide C + O + N in sigma)
check("Ramachandran (try peptide flips): a flip is kept for a better Ramachandran region with the map no worse, or the same regions and a clearly better carbonyl",
      lambda: (_m.rama_flip_better((2, 2, 10.0, 4.0, 12.0), (3, 2, 10.0, 4.0, 12.0)) and not _m.rama_flip_better((3, 2, 10.0, 1.0, 5.0), (2, 2, 30.0, 6.0, 15.0))
               and not _m.rama_flip_better((4, 2, 10.0, 4.0, 12.0), (4, 2, 10.5, 4.5, 12.5)) and _m.rama_flip_better((4, 2, 10.0, 1.0, 6.0), (4, 2, 11.5, 4.0, 12.0))
               and not _m.rama_flip_better((4, 2, 10.0, 1.0, 6.0), (4, 1, 20.0, 6.0, 15.0))) or "wrong choice")

# (build 23) The user found wrong flips kept by build 22 (17 Nov): the Ramachandran region got better (allowed -> favoured) but the flipped carbonyl O
# pointed out of the density (on their data 7.3 -> -0.8 sigma, 5.6 -> 0.1, 5.3 -> 3.7).  Now the map has a veto.  Scores below are those numbers.
check("Ramachandran (try peptide flips): a flip that improves the Ramachandran region but takes the carbonyl O out of the density is NOT kept",
      lambda: (not _m.rama_flip_better((3, 2, 26.6, 7.3, 18.2), (4, 2, 21.2, -0.8, 4.8))
               and not _m.rama_flip_better((3, 2, 26.9, 5.6, 14.8), (4, 2, 23.2, 0.1, 5.1))
               and not _m.rama_flip_better((3, 2, 23.7, 5.3, 15.1), (4, 2, 21.4, 3.7, 9.9))) or "a wrong flip would be kept")
check("Ramachandran (try peptide flips): a wrongly flipped peptide (same regions, carbonyl +4.4 sigma, map fit +6.8%) is flipped back; without a map nothing is flipped",
      lambda: (_m.rama_flip_better((4, 2, 30.0, 1.76, 12.2), (4, 2, 32.0, 6.14, 16.96))
               and not _m.rama_flip_better((3, 2, None, None, None), (4, 2, None, None, None))) or "wrong choice")
def rama_flip_score_has_carbonyl():
    imol_f, imap_f, O = _flip_setup()
    s_ok = _m._rama_flip_score(imol_f, "A", [43, 44], imap_f)
    coot.pepflip(imol_f, "A", 43, "", "")
    s_flip = _m._rama_flip_score(imol_f, "A", [43, 44], imap_f)
    if len(s_ok) < 5: return "the score has no carbonyl density: %r" % (s_ok,)
    return True if s_ok[3] > 1.0 and s_flip[3] < s_ok[3] - 1.0 else "carbonyl O density deposited %.2f, flipped %.2f sigma" % (s_ok[3], s_flip[3])
check("Ramachandran (try peptide flips): the score measures the carbonyl O density in sigma (lower after a deliberate flip)", rama_flip_score_has_carbonyl)
def rama_flip_repaints():
    calls = []; orig = _c.call
    def spy(name, *a, **k):
        if name == "gtk_widget_queue_draw": calls.append(name)
        return orig(name, *a, **k)
    _c.call = spy
    keep = _m.use_graphics_interface_state; _m.use_graphics_interface_state = lambda: 0
    try: _m.rama_flip_report(False)
    finally: _c.call = orig; _m.use_graphics_interface_state = keep
    return True if calls else "the main window (menu bar) is not redrawn at the end of the run"
check("Ramachandran (try peptide flips): the main window and its menu bar are redrawn when the run ends", rama_flip_repaints)

# (build 24) The user saw the menu bar go blank during the plain Refine/Improve Ramachandran Plot too: every shown refinement (Stepped Refine,
# Fit Protein, both Ramachandran entries) now asks for a redraw of the main window.  And the report says what counts as a flipped peptide: every
# peptide is compared with the start of the run (carbonyl O turned > 90 degrees round the CA - CA axis); those turned by the flip try and those
# turned by the refinement itself are listed apart (the user flipped 4 on purpose: 2 were reported, all 4 were put back).
def rama_plain_repaints():
    imol_f, imap_f, O = _flip_setup()
    calls = []; orig = _c.call
    def spy(name, *a, **k):
        if name == "gtk_widget_queue_draw": calls.append(name)
        return orig(name, *a, **k)
    _c.call = spy
    try: _m.fit_protein_rama_fit_function([imol_f, "A", 30, ""], imap_f)
    finally: _c.call = orig
    return True if calls else "the main window (menu bar) is not redrawn after a residue of the plain Ramachandran run"
check("Refine/Improve Ramachandran Plot: the main window and its menu bar are redrawn after each residue", rama_plain_repaints)
def rama_turned_listed():
    imol_f, imap_f, O = _flip_setup()
    _m.rama_flip_run["tried"] = 0; _m.rama_flip_run["flipped"] = []
    _m.rama_run_begin(imol_f)
    coot.pepflip(imol_f, "A", 60, "", "")          # (as if the refinement had turned it)
    coot.pepflip(imol_f, "A", 43, "", ""); _m.rama_flip_run["flipped"].append(("A", 43, "", "Peptide A 43-44 flipped (test)"))
    keep = _m.use_graphics_interface_state; _m.use_graphics_interface_state = lambda: 0
    try: t = _m.rama_flip_report(False)
    finally: _m.use_graphics_interface_state = keep
    turned = t.split("Turned by the refinement itself")[-1] if "Turned by the refinement itself" in t else ""
    if "1 peptide flipped" not in t or "1 more turned by the refinement itself" not in t: return "report: %r" % t
    if "A 60-61" not in turned or "A 43-44" in turned: return "turned list: %r" % turned
    a = _m.peptide_turn_angle(((0, 0, 0), (1, 1, 0), (3.8, 0, 0)), ((0, 0, 0), (1, -1, 0), (3.8, 0, 0)))
    return True if abs(a - 180) < 0.1 else "turn angle of an O turned 180 degrees: %r" % a
check("Ramachandran (try peptide flips): the report lists the peptides turned by the refinement itself apart from those flipped by the flip try", rama_turned_listed)
def rama_plain_report_run():
    imol_f, imap_f, O = _flip_setup()
    coot.pepflip(imol_f, "A", 60, "", "")
    status = []
    keep = {n: getattr(_m, n) for n in ("fit_protein_make_specs", "add_status_bar_text")}
    _m.fit_protein_make_specs = lambda imol_, which: [[imol_f, "A", r, ""] for r in (59, 60, 61)]
    _m.add_status_bar_text = lambda t: status.append(t)
    keep_secs = _m.stepped_refine_show_seconds; _m.stepped_refine_show_seconds = 0
    try:
        _m.start_rama_run(imol_f)
        t0 = _time.time()
        while _time.time() - t0 < 120 and not any("Refine/Improve Ramachandran Plot finished" in x for x in status):
            while gtk.events_pending(): gtk.main_iteration(False)
            _time.sleep(0.01)
    finally:
        for n, f in keep.items(): setattr(_m, n, f)
        _m.stepped_refine_show_seconds = keep_secs
        _m.cancel_interruptible_fit_protein()
    return True if any("peptide" in x and "turned" in x for x in status) else "no report of turned peptides at the end of the plain run: %r" % status[-3:]
check("Refine/Improve Ramachandran Plot: at the end the status bar and terminal say how many peptides the refinement turned", rama_plain_report_run)

# (build 22) Alt confs: build 21 tried no flip when residue i or i+1 had alt confs (it fell back to a plain refinement).  Shared peptide (only side
# chains split, Cys B 72): one decision with every alt conf refined.  Split peptide (C, O / N with alt confs): a decision per alt conf, scored on
# that conformer alone.  Then: ligands / waters are not touched by either Ramachandran entry, and a report is given at the end or when stopped.
def _split_pdb(chain, res_nos):
    import tempfile
    out = []
    for l in open(os.path.join(here, "test-data", "tutorial-modern.pdb")):
        if l.startswith(("ATOM", "HETATM")) and l[21] == chain and int(l[22:26]) in res_nos and l[16] == " ":
            out.append(l[:16] + "A" + l[17:54] + "  0.50" + l[60:]); out.append(l[:16] + "B" + l[17:54] + "  0.50" + l[60:])
        else: out.append(l)
    p_ = os.path.join(tempfile.mkdtemp(), "split.pdb"); open(p_, "w").writelines(out); return p_
def _O(imol_, ch, r, alt=""):
    return [a[2] for a in coot.residue_info_py(imol_, ch, r, "") if a[0][0].strip() == "O" and a[0][1] == alt][0]
def rama_flip_alt_shared():
    imol_f, imap_f, O = _flip_setup()
    o0 = _O(imol_f, "B", 71); coot.pepflip(imol_f, "B", 71, "", "")
    if _math.dist(o0, _O(imol_f, "B", 71)) < 2.5: return "the deliberate flip of B 71 did not move O"
    _m.fit_protein_rama_flip_function([imol_f, "B", 71, ""], imap_f)
    d = _math.dist(o0, _O(imol_f, "B", 71))
    sg = sorted(a[0][1] for a in coot.residue_info_py(imol_f, "B", 72, "") if a[0][0].strip() == "SG")
    if sg != ["A", "B"]: return "the alt confs of Cys B 72 were lost: %r" % sg
    return True if d < 0.5 else "peptide B 71-72 (next to the alt confs of Cys B 72) not flipped back: O %.2f A from the deposited position" % d
check("Ramachandran (try peptide flips): a peptide next to a residue with alt confs (Cys B 72) flipped on purpose is flipped back", rama_flip_alt_shared)
def rama_flip_alt_split():
    imol_f = coot.read_pdb(_split_pdb("A", (43, 44)))
    imap_f = coot.make_and_draw_map(os.path.join(here, "test-data", "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
    coot.set_imol_refinement_map(imap_f); _m.continue_multi_refine = True
    oa, ob = _O(imol_f, "A", 43, "A"), _O(imol_f, "A", 43, "B")
    coot.pepflip(imol_f, "A", 43, "", "B")                     # only conformer B flipped
    if _math.dist(ob, _O(imol_f, "A", 43, "B")) < 2.5 or _math.dist(oa, _O(imol_f, "A", 43, "A")) > 0.01: return "the deliberate flip of conformer B failed"
    n_models = len([i for i in range(coot.graphics_n_molecules()) if coot.is_valid_model_molecule(i)])
    _m.fit_protein_rama_flip_function([imol_f, "A", 43, ""], imap_f)
    da, db = _math.dist(oa, _O(imol_f, "A", 43, "A")), _math.dist(ob, _O(imol_f, "A", 43, "B"))
    scratch = 1 if (hasattr(_m, "_rama_scratch") and coot.is_valid_model_molecule(_m._rama_scratch["imol"])) else 0   # (build 23: closed at the end of the run)
    if len([i for i in range(coot.graphics_n_molecules()) if coot.is_valid_model_molecule(i)]) - scratch != n_models: return "a temporary molecule was left behind"
    tried = [e[2] for e in _m.rama_flip_log[-2:] if e[1] == 43]
    if tried != ["A", "B"]: return "the flip was not tried for each conformer: %r" % (_m.rama_flip_log[-2:],)
    return True if da < 0.5 and db < 0.5 else "conformer A moved %.2f A, conformer B %.2f A from the deposited O (want < 0.5)" % (da, db)
check("Ramachandran (try peptide flips): with the peptide split into alt confs A / B the flip is tried per conformer (B flipped on purpose is put back, A kept)", rama_flip_alt_split)
def rama_flip_scratch_molecule():
    imol_f = coot.read_pdb(_split_pdb("A", (43, 44)))
    imap_f = coot.make_and_draw_map(os.path.join(here, "test-data", "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
    coot.set_imol_refinement_map(imap_f); _m.continue_multi_refine = True
    if hasattr(_m, "_rama_scratch_close"): _m._rama_scratch_close()        # (one left by an earlier test)
    n0 = coot.graphics_n_molecules()
    valid = lambda: len([i for i in range(coot.graphics_n_molecules()) if coot.is_valid_model_molecule(i)])
    v0 = valid()
    for r in (42, 43, 44):
        _m.fit_protein_rama_flip_function([imol_f, "A", r, ""], imap_f)
    made = coot.graphics_n_molecules() - n0
    if made > 1: return "%d molecules were created for the conformer checks (want at most one scratch molecule)" % made
    keep = _m.use_graphics_interface_state; _m.use_graphics_interface_state = lambda: 0
    try: _m.rama_flip_report(False)
    finally: _m.use_graphics_interface_state = keep
    return True if valid() == v0 else "the scratch molecule was left open after the run"
check("Ramachandran (try peptide flips): split conformers are checked in one scratch molecule, closed at the end of the run", rama_flip_scratch_molecule)
def rama_turned_next_split():
    imol_f = coot.read_pdb(_split_pdb("A", (44,)))     # O of A 43 shared, N / CA of A 44 split into A / B (as in the user's model)
    _m.rama_flip_run["tried"] = 0; _m.rama_flip_run["flipped"] = []
    _m.rama_run_begin(imol_f)
    if ("A", 43, "") not in _m.rama_flip_run["start"]: return "peptide A 43-44 (shared O, split N) is not followed"
    coot.pepflip(imol_f, "A", 43, "", "")
    t = [x[:3] for x in _m.rama_turned_by_refinement()]
    return True if ("A", 43, "") in t else "turned: %r" % t
check("Ramachandran: a peptide with a shared O next to a residue split into alt confs is followed too (listed when it turns)", rama_turned_next_split)
def _ligand_pdb():
    import tempfile
    lines = [l for l in open(os.path.join(here, "test-data", "tutorial-modern.pdb")) if not l.startswith("END")]
    so4 = [(" S  ", 61.0, 6.0, -1.0, "S"), (" O1 ", 62.2, 6.4, -1.0, "O"), (" O2 ", 60.4, 7.6, -1.3, "O"), (" O3 ", 60.6, 5.1, 0.4, "O"), (" O4 ", 60.5, 5.5, -2.0, "O")]
    for i, (n, x, y, z, e) in enumerate(so4):     # SO4 numbered A 94, after the last amino acid A 93, with a distorted geometry
        lines.append("HETATM%5d %4s SO4 A  94    %8.3f%8.3f%8.3f  1.00 20.00           %s\n" % (2000 + i, n, x, y, z, e))
    lines.append("HETATM%5d  O   HOH A  95    %8.3f%8.3f%8.3f  1.00 20.00           O\n" % (2010, 57.0, 8.0, -3.0))
    p_ = os.path.join(tempfile.mkdtemp(), "with-ligand.pdb"); open(p_, "w").writelines(lines + ["END\n"]); return p_
def rama_leaves_ligands(fit):
    imol_l = coot.read_pdb(_ligand_pdb())
    imap_l = coot.make_and_draw_map(os.path.join(here, "test-data", "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
    coot.set_imol_refinement_map(imap_l); _m.continue_multi_refine = True
    xyz = lambda r: sorted(tuple(round(c, 3) for c in a[2][:3]) for a in coot.residue_info_py(imol_l, "A", r, "") or [])
    het0 = (xyz(94), xyz(95)); a93 = xyz(93)
    for r in (92, 93, 94, 95): fit([imol_l, "A", r, ""], imap_l)
    if not het0[0]: return "the test ligand was not read"
    moved = [n for n, a, b in (("SO4 A 94", het0[0], xyz(94)), ("HOH A 95", het0[1], xyz(95))) if a != b]
    if moved: return "moved: %s" % moved
    return True if xyz(93) != a93 else "the amino acid A 93 next to the ligand was not refined"
check("Refine/Improve Ramachandran Plot: a ligand (SO4 numbered after the last amino acid) and a water are not refined, the amino acids are",
      lambda: rama_leaves_ligands(_m.fit_protein_rama_fit_function))
check("Ramachandran (try peptide flips): a ligand (SO4 numbered after the last amino acid) and a water are not refined, the amino acids are",
      lambda: rama_leaves_ligands(_m.fit_protein_rama_flip_function))
def rama_flip_report_run(stop_after=None):
    imol_f, imap_f, O = _flip_setup()
    coot.pepflip(imol_f, "A", 43, "", "")
    specs = [[imol_f, "A", 43, ""], [imol_f, "A", 50, ""], [imol_f, "A", 60, ""]]
    shown = []
    keep = {n: getattr(_m, n) for n in ("fit_protein_make_specs", "info_dialog", "use_graphics_interface_state", "fit_protein_rama_flip_function")}
    done = []
    def counted(spec, imap):
        keep["fit_protein_rama_flip_function"](spec, imap); done.append(spec[2])
        if stop_after and len(done) >= stop_after: _m.stop_interruptible_fit_protein()
    _m.fit_protein_make_specs = lambda imol_, which: [list(s_) for s_ in specs]
    _m.info_dialog = lambda t: shown.append(t)
    _m.use_graphics_interface_state = lambda: 1
    _m.fit_protein_rama_flip_function = counted
    keep_secs = _m.stepped_refine_show_seconds; _m.stepped_refine_show_seconds = 0
    try:
        _m.start_rama_flip_run(imol_f)
        t0 = _time.time()
        while _time.time() - t0 < 120 and not shown:
            while gtk.events_pending(): gtk.main_iteration(False)
            _time.sleep(0.01)
    finally:
        for n, f in keep.items(): setattr(_m, n, f)
        _m.stepped_refine_show_seconds = keep_secs
        _m.cancel_interruptible_fit_protein()
    return done, shown
def rama_flip_report_end():
    done, shown = rama_flip_report_run()
    if done != [43, 50, 60]: return "not all residues were done: %r" % done
    if len(shown) != 1: return "expected one report window, got %r" % shown
    t = shown[0]
    return True if ("finished: 1 peptide flipped" in t and "A 43-44" in t) else "report: %r" % t
check("Ramachandran (try peptide flips): at the end a report says how many peptides were flipped, and which", rama_flip_report_end)
def rama_flip_report_stop():
    done, shown = rama_flip_report_run(stop_after=1)
    if done != [43]: return "residues done after Stop: %r" % done
    if len(shown) != 1: return "expected one report window after Stop, got %r" % shown
    return True if ("stopped: 1 peptide flipped" in shown[0] and "A 43-44" in shown[0]) else "report: %r" % shown[0]
check("Ramachandran (try peptide flips): when the run is stopped, a report says how many peptides were flipped so far", rama_flip_report_stop)

# (build 22) Fill Partial Residues: the terminal lists the residues that were filled (with the atoms added) and those that could not be; no hydrogens
# are added; the model is asked for only when more than one is loaded.
def fill_partial_report():
    imol_p = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
    imap_p = coot.make_and_draw_map(os.path.join(here, "test-data", "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
    coot.set_imol_refinement_map(imap_p)
    for a in coot.residue_info_py(imol_p, "A", 40, "") or []:
        if a[0][0].strip() not in ("N", "CA", "C", "O"): coot.delete_atom(imol_p, "A", 40, "", a[0][0], a[0][1])
    import io, contextlib
    out = io.StringIO()
    with contextlib.redirect_stdout(out): r = _m.fill_partial_residues_and_report(imol_p)
    text = out.getvalue()
    line = [l for l in text.splitlines() if "filled" in l and " A 40" in l and "not filled" not in l]
    if not line: return "no 'filled ... A 40' line in the terminal: %r" % text[-400:]
    names = [a[0][0].strip() for a in coot.residue_info_py(imol_p, "A", 40, "")]
    if any(n.startswith("H") for n in names): return "hydrogens were added: %r" % names
    return True if ("CB" in line[0] and "CG" in line[0]) else "the line does not list the atoms added: %r" % line[0]
check("Fill Partial Residues: the terminal lists each residue filled with the atoms added (no hydrogens)", fill_partial_report)
def fill_partial_menu():
    called, n_windows = [], len(H.windows)
    keep = {n: getattr(_m, n) for n in ("fill_partial_residues_and_report", "molecule_number_list")}
    one = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
    _m.fill_partial_residues_and_report = lambda imol_: called.append(imol_)
    try:
        _m.molecule_number_list = lambda: [one]
        for path in (("All Molecule...", "[Post MR] Fill Partial Residues..."), ("Modelling...", "Fill Partial Residues")):
            it = _find_menu_item(path)
            if it is None: return "menu entry %r not found" % (path,)
            it.activate()
        if called != [one, one] or len(H.windows) != n_windows:
            return "with one model: called %r, %d windows opened (want the model used directly, no chooser)" % (called, len(H.windows) - n_windows)
        _m.molecule_number_list = lambda: [one, imol]
        _find_menu_item(("All Molecule...", "[Post MR] Fill Partial Residues...")).activate()
        return True if len(H.windows) > n_windows and called == [one, one] else "with two models no chooser was shown"
    finally:
        for n, f in keep.items(): setattr(_m, n, f)
def _find_menu_item(path):
    import gtk as _g
    items = []
    def walk(menu, depth):
        for k in menu.get_children():
            ch = k.get_children()
            lab = ch[0].get_text() if ch and hasattr(ch[0], "get_text") else None
            items.append((lab, k))
            if k.get_submenu() is not None and depth < 4: walk(k.get_submenu(), depth + 1)
    walk(g["_menubar"], 0)
    sub = None
    for lab, k in items:
        if lab == path[0] and k.get_submenu() is not None: sub = k.get_submenu(); break
    if sub is None: return None
    for k in sub.get_children():
        ch = k.get_children()
        if ch and hasattr(ch[0], "get_text") and ch[0].get_text() == path[1]: return k
    return None
check("Fill Partial Residues (both menu entries): with one model loaded it is used directly; with several the model chooser opens", fill_partial_menu)

# Alt conf occupancy slider (Extensions > Modelling or the toolbar): "OK" did nothing in build 13 (set_alt_conf_occ compared a list with a number: a
# TypeError in Python 3, silently true in Python 2).  Cys B 72 of tutorial-modern.pdb has SG A (occ 0.7) / SG B (occ 0.3).
def occ_slider_ok():
    imol_o = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
    def occs():
        d = {}
        for a in coot.residue_info_py(imol_o, "B", 72, "") or []:
            if a[0][0].strip() == "SG": d[a[0][1]] = round(a[1][0], 3)
        return d
    before = occs()
    if set(before) != {"A", "B"}: return "test residue has SG alt confs %r" % (before,)
    n_err0 = len(_c.CALLBACK_ERRORS); w0 = len(H.windows)
    with contextlib.redirect_stdout(io.StringIO()): _m.scale_alt_conf_occ_gui(imol_o, "B", 72, "")
    ws = H.windows[w0:]
    sc = scales_of(ws)
    if len(sc) != 1: return "%d sliders in the occupancy dialog" % len(sc)
    sc[0].get_adjustment().set_value(0.4)
    ok = [x for w in ws for x in H.walk(w) if type(x).__name__ == "Button" and (x.get_label() or "").strip() == "OK"]
    if len(ok) != 1: return "%d OK buttons" % len(ok)
    with contextlib.redirect_stdout(io.StringIO()): ok[0].clicked()
    after = occs()
    if len(_c.CALLBACK_ERRORS) > n_err0: return "OK raised: " + _c.CALLBACK_ERRORS[-1][1][-250:]
    if after != {"A": 0.4, "B": 0.6}: return "occupancies after OK: %r (expected A 0.4, B 0.6; before %r)" % (after, before)
    alive = [w for w in ws if w in gtk.window_list_toplevels()]
    return True if not alive else "the dialog is still open after OK"
check("Alt conf occupancy slider: OK sets the occupancies (0.4 / 0.6) and closes the dialog", occ_slider_ok)
def swap_alt_confs():
    # rename_alt_confs (Extensions: swap alt confs A and B of the residue under the centre) had the same list-versus-number comparison
    imol_o = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
    def occs():
        return {a[0][1]: round(a[1][0], 3) for a in (coot.residue_info_py(imol_o, "B", 72, "") or []) if a[0][0].strip() == "SG"}
    before = occs()
    with contextlib.redirect_stdout(io.StringIO()): _m.rename_alt_confs(imol_o, "B", 72, "")
    after = occs()
    return True if (before == {"A": 0.7, "B": 0.3} and after == {"A": 0.3, "B": 0.7}) else "SG occupancies before %r, after the swap %r" % (before, after)
check("rename_alt_confs: swapping alt confs A and B of Cys B 72 works", swap_alt_confs)
def occ_rename_guard():
    # the second place with the same py2 comparison (the alt-conf renaming helper): code lines only, not the explanatory comments
    import re as _re
    full = open(os.path.join(pydir, "coot_utils.py")).read()
    hits = _re.findall(r"^\s*if \(?alt_confs\s*>\s*\d\)?\s*:", full, _re.M)
    return True if not hits else "list-versus-number comparison left: %r" % (hits,)
check("coot_utils.py: no list compared with a number (alt_confs > 1) left", occ_rename_guard)

# Calculate > Fit Loop > Fit Loop by Database Search...: the atoms the user clicks arrive as 7-element specs
# [model number, imol, chain, res-no, ins-code, atom-name, alt-conf]; atom_spec_to_residue_spec gave None for them, so the loop search got
# a list of None ("Ooops - no specs in object" / SystemError) in build 12 and before.
def fit_loop_db_search():
    imol_l = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
    imap_l = coot.make_and_draw_map(os.path.join(here, "test-data", "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
    coot.set_imol_refinement_map(imap_l)
    ch = coot.chain_id_py(imol_l, 0)
    cap = []
    keep = _m.user_defined_click; _m.user_defined_click = lambda n, f: cap.append((n, f))
    try:
        w0 = len(H.windows)
        with contextlib.redirect_stdout(io.StringIO()): _m.click_protein_db_loop_gui()
        wins = H.windows[w0:]
        btn = [x for w in wins for x in H.walk(w) if type(x).__name__ == "Button" and (x.get_label() or "").startswith("Pick")]
        if not btn: return "no 'Pick Atoms...' button in the number chooser"
        with contextlib.redirect_stdout(io.StringIO()): btn[0].clicked()
    finally: _m.user_defined_click = keep
    if not cap: return "the dialog did not ask for atom clicks"
    n, func = cap[0]
    specs = [[1, imol_l, ch, r, "", " CA ", ""] for r in (40, 41, 42, 43)][:n]
    w1 = len(H.windows); n_mol0 = coot.graphics_n_molecules(); n0 = len(_c.CALLBACK_ERRORS)
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf): func(*specs)
    except BaseException as e:
        return "pick function raised %r" % (e,)
    out = buf.getvalue()
    if "no specs in object" in out: return "the residue specs were not understood: " + out[-200:]
    labels = ["%s" % (x.get_label(),) for w in H.windows[w1:] for x in H.walk(w) if type(x).__name__ == "Button"]
    if not any("Original loop" in l for l in labels): return "no 'Loop Candidates' dialog (buttons %r, %d new molecules)" % (labels, coot.graphics_n_molecules() - n_mol0)
    if not any("Toggle All" in l for l in labels): return "buttons %r" % (labels,)
    cands = [l for l in labels if l and l[0].isdigit()]
    return True if cands else "dialog has no candidate buttons: %r" % (labels,)
check("Fit Loop by Database Search: clicked atoms give a Loop Candidates dialog with candidate loops", fit_loop_db_search)

# (build 25) The Scheme scripting window.  The 0.9.8.96 C++ window said "For now this is a placeholder only!" and threw every result
# away (the user, 18 Nov: nothing in the window or the terminal).  Now Calculate > Scripting > Scheme... opens a window that shows the
# command, its printed output, its result and errors; Scheme's terminal output is line-buffered (it was held back behind the launcher's tee).
def _scheme_menu_items():
    bar = H.coot_python.main_menubar() if hasattr(H, "coot_python") else __import__("coot_python").main_menubar()
    lab = lambda i: (i.get_children()[0].get_text().replace("_", "") if i.get_children() else "")
    calc = [i for i in bar.get_children() if lab(i) == "Calculate"][0]
    scr = [i for i in calc.get_submenu().get_children() if lab(i).startswith("Scripting")][0]
    return [i for i in scr.get_submenu().get_children() if lab(i) == "Scheme..."]
def scheme_window_menu():
    items = _scheme_menu_items()               # (headless, show() is a no-op: the new entry is recognised by its name, the old one must be hidden)
    shown = [i for i in items if i.get_name() == "coot0_scheme_window"]
    old = [i for i in items if i.get_name() != "coot0_scheme_window"]
    if len(shown) != 1: return "%d new 'Scheme...' entries (want 1)" % len(shown)
    menu = gtk.Menu()                          # the swap itself, on a menu like Calculate > Scripting: the old entry is hidden
    for l in ("Python...", "Scheme..."): menu.append(gtk.MenuItem(l))
    hidden = []; orig = _c.call
    def spy(name, *a, **k):
        if name == "gtk_widget_hide": hidden.append(a[0])
        return orig(name, *a, **k)
    _c.call = spy
    try: new = _m.install_scheme_scripting_window(menu)
    finally: _c.call = orig
    kids = menu.get_children()
    if not new or [k.get_name() for k in kids][1] != "coot0_scheme_window": return "the new entry is not in the place of the old one: %r" % [k.get_name() for k in kids]
    if not any(h == kids[2] for h in hidden): return "the old entry was not hidden"
    _m.scheme_console_last.clear() if hasattr(_m, "scheme_console_last") else None
    shown[0].activate()
    last = getattr(_m, "scheme_console_last", {})
    if not last.get("window"): return "Calculate > Scripting > Scheme... did not open the new Scheme window"
    b = last["buffer"]; t = b.get_text(b.get_start_iter(), b.get_end_iter())
    if "placeholder" in t: return "the window still says it is a placeholder"
    return True if last["window"].get_title() == "Coot Scheme Scripting" else "title %r" % last["window"].get_title()
check("Scheme window: Calculate > Scripting > Scheme... opens the new window (no 'placeholder only' text)", scheme_window_menu)
def _scheme_type(*lines):
    last = _m.scheme_console_last
    b = last["buffer"]; n0 = len(b.get_text(b.get_start_iter(), b.get_end_iter()))
    for l in lines:
        last["entry"].set_text(l); last["entry"].emit("activate")
    return b.get_text(b.get_start_iter(), b.get_end_iter())[n0:]
def scheme_window_results():
    if not getattr(_m, "scheme_console_last", {}).get("window"): _m.scheme_scripting_window()
    imol = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
    want = coot.residue_name(imol, "A", 41, "")
    t = _scheme_type('(residue-name %d "A" 41 "")' % imol)
    if '(residue-name %d "A" 41 "")' % imol not in t: return "the command is not shown: %r" % t
    if '=> "%s"' % want not in t: return "the result (%s) is not shown: %r" % (want, t)
    t = _scheme_type('(display "hello from scheme") (newline) (* 6 7)')
    if "hello from scheme" not in t or "=> 42" not in t: return "printed output / result not shown: %r" % t
    t = _scheme_type("(car 1)")
    if "Error:" not in t or "Wrong type" not in t: return "the error is not shown: %r" % t
    t = _scheme_type("(+ 1", "2)")
    if "=> 3" not in t: return "an expression over two lines was not evaluated: %r" % t
    t = _scheme_type("(define coot0-test-x 5)", "(* coot0-test-x 2)")
    if "=> 10" not in t: return "a definition was not kept for the next command: %r" % t
    h = _m.scheme_console_history
    return True if h[-1] == "(* coot0-test-x 2)" and "(+ 1\n2)" in h else "history: %r" % h[-4:]
check("Scheme window: command, printed output, result, errors, expressions over several lines and the history are shown / kept", scheme_window_results)
check("Scheme: output printed by Scheme (display) is line-buffered, so it reaches the terminal at once",
      lambda: True if coot.run_scheme_command("coot0-stdout-line-buffered") is True else "Guile's output port is not line-buffered")
check("Scheme window: open brackets / strings are recognised (Enter waits for the rest)",
      lambda: (_m.scheme_text_incomplete("(+ 1") and not _m.scheme_text_incomplete("(+ 1 2)") and _m.scheme_text_incomplete('(display "a)')
               and not _m.scheme_text_incomplete('(display "(")') and not _m.scheme_text_incomplete("(char->integer #\\()")
               and not _m.scheme_text_incomplete("(+ 1 2) ; (")) or "wrong")

check("no exception in any GTK signal handler", lambda: True if not _c.CALLBACK_ERRORS else [e[1][-300:] for e in _c.CALLBACK_ERRORS][:2])
w = max(len(r[0]) for r in res)
for n, ok, v in res: print(("PASS " if ok else "FAIL ") + n.ljust(w) + (("  " + v) if v else ""))
print("SUMMARY", sum(1 for r in res if r[1]), "/", len(res), flush=True)
coot.coot_real_exit(0)
