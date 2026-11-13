
# Headless tests of the Glyco module (Calculate > Modules > Carbohydrate) dialog logic and of the colour-bar sliders (ligand metric sliders,
# PDBe validation): PyGTK compatibility layer on real GTK 2, no display. (The pictures themselves can only be checked on screen.)
import os, sys, io, ctypes, contextlib, traceback, tempfile
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
import coot, __main__ as m
here = os.environ["COOT_PREFIX"]
td = os.path.join(here, "test-data")
imol = coot.read_pdb(os.path.join(td, "tutorial-modern.pdb"))
imap = coot.make_and_draw_map(os.path.join(td, "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
coot.set_imol_refinement_map(imap)
CHO = ("NAG", "BMA", "MAN", "GAL", "FUC", "SIA", "XYP", "FUL")
def cho():
    return [(c, coot.seqnum_from_serial_number(imol, c, i), coot.resname_from_serial_number(imol, c, i)) for c in m.chain_ids(imol)
            for i in range(coot.chain_n_residues(c, imol)) if coot.resname_from_serial_number(imol, c, i) in CHO]
def first_asn():
    for c in m.chain_ids(imol):
        for i in range(coot.chain_n_residues(c, imol)):
            if coot.resname_from_serial_number(imol, c, i) == "ASN": return c, coot.seqnum_from_serial_number(imol, c, i)
asn = first_asn()
def centre(c, n, an=" CA "):
    coot.set_go_to_atom_molecule(imol); coot.set_go_to_atom_chain_residue_atom_name(c, n, an)
def label_of(item):
    for k in item.get_children():
        for mm in ("get_text", "get_label"):
            if hasattr(k, mm):
                try: return getattr(k, mm)()
                except Exception: pass
    return ""
def find_item(path):
    def walk(ms, p):
        for it in ms.get_children():
            if type(it).__name__ == "SeparatorMenuItem": continue
            lab = label_of(it).replace("_", "").strip(); sub = it.get_submenu() if hasattr(it, "get_submenu") else None
            if p + [lab] == path: return it
            if sub is not None:
                r = walk(sub, p + [lab])
                if r is not None: return r
    return walk(g["_menubar"], [])
def activate(path):
    it = find_item(path); assert it is not None, "menu item not found: %r" % (path,)
    n0 = len(_c.CALLBACK_ERRORS); w0 = len(H.windows)
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()): it.activate()
    errs_ = [e[1].strip().splitlines()[-1] for e in _c.CALLBACK_ERRORS[n0:]]
    assert not errs_, errs_
    return H.windows[w0:]
def button(wins, label):
    for w in wins:
        for x in H.walk(w):
            if type(x).__name__ == "Button" and (x.get_label() or "") == label: return x
def click(wins, label):
    b = button(wins, label); assert b is not None, "button not found: " + label
    n0 = len(_c.CALLBACK_ERRORS)
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()): b.clicked()
    errs_ = [e[1].strip().splitlines()[-1] for e in _c.CALLBACK_ERRORS[n0:]]
    assert not errs_, errs_
def delete_all():
    for c, n, r in cho(): coot.delete_residue(imol, c, n, "")

# --- the menu and the dialog
state = {}
def open_dialog():
    activate(["Calculate", "Modules...", "Carbohydrate"])
    state["wins"] = activate(["Glyco", "N-linked Glycan Addition..."])
    return True if state["wins"] else "no dialog window"
check("Calculate > Modules > Carbohydrate adds the Glyco menu; N-linked Glycan Addition opens its dialog", open_dialog)
def hook_runs():
    # the dialog re-evaluates which buttons make sense whenever the centre moves: it iterates over a gtk.Table (needs Container iteration)
    delete_all(); centre(*asn)
    r = m.post_set_rotation_centre_script()      # (returns nothing; raises if the glue is broken)
    sens = {b: button(state["wins"], b).get_sensitive() for b in ("Add a NAG-ASN NAG", "Add a BETA1-4 NAG", "Add a BETA1-4 BMA", "Add an ALPHA1-3 MAN")}
    want = {"Add a NAG-ASN NAG": True, "Add a BETA1-4 NAG": False, "Add a BETA1-4 BMA": False, "Add an ALPHA1-3 MAN": False}
    return True if sens == want else "sensitivity on an ASN: %r" % sens
check("Glyco dialog: only the matching button is enabled on an ASN (centre hook works)", hook_runs)
def add_chain():
    delete_all(); centre(*asn)
    click(state["wins"], "Add a NAG-ASN NAG")
    s = cho()
    if len(s) != 1: return "after NAG-ASN: %r" % s
    centre(s[0][0], s[0][1], " C1 "); m.post_set_rotation_centre_script()
    if not button(state["wins"], "Add a BETA1-4 NAG").get_sensitive(): return "BETA1-4 NAG not enabled on the first NAG"
    if button(state["wins"], "Add a NAG-ASN NAG").get_sensitive(): return "NAG-ASN NAG still enabled on a NAG"
    click(state["wins"], "Add a BETA1-4 NAG")
    s = cho()
    return True if [x[2] for x in s] == ["NAG", "NAG"] else "after BETA1-4 NAG: %r" % s
check("Glyco dialog: Add a NAG-ASN NAG, then Add a BETA1-4 NAG (button states follow the residue)", add_chain)
def menu_items():
    delete_all(); centre(*asn)
    activate(["Glyco", "N-link add NAG, NAG, BMA"])
    names = sorted(x[2] for x in cho())
    if names != ["BMA", "NAG", "NAG"]: return "N-link add NAG, NAG, BMA gave %r" % names
    c, n, r = cho()[0]; centre(c, n, " C1 ")
    n_models = sum(1 for i in range(30) if coot.is_valid_model_molecule(i))
    activate(["Glyco", "Extract this Tree"])
    n_models2 = sum(1 for i in range(30) if coot.is_valid_model_molecule(i))
    if n_models2 != n_models + 1: return "Extract this Tree: molecules %d -> %d" % (n_models, n_models2)
    new_imol = max(i for i in range(30) if coot.is_valid_model_molecule(i))
    names = sorted(coot.resname_from_serial_number(new_imol, ch, i) for ch in m.chain_ids(new_imol) for i in range(coot.chain_n_residues(ch, new_imol)))
    if names != ["ASN", "BMA", "NAG", "NAG"]: return "Extract this Tree made a molecule of %r (expected the ASN and its three sugars)" % names
    coot.close_molecule(new_imol)
    activate(["Glyco", "Delete All Carbohydrate"])
    if cho(): return "Delete All Carbohydrate left %r" % cho()
    return True
check("Glyco menu: N-link add NAG, NAG, BMA, Extract this Tree, and Delete All Carbohydrate", menu_items)
def small_items():
    centre(*asn)
    for lab in ("Add synthetic pyranose plane restraints", "Use Unimodal ring torsion restraints", "Display Extra Restraints", "Undisplay Extra Restraints"):
        activate(["Glyco", lab])
    return True
check("Glyco menu: restraint switches run", small_items)

# --- colour-bar sliders (Ligand > Ligand Metric Sliders window, PDBe validation sliders): drawing code with a recording stand-in for the window
class Rec:
    def __init__(self): self.calls = []
    def __getattr__(self, n):
        def f(*a, **k): self.calls.append((n, a)); return None
        return f
class Cmap:
    def alloc_color(self, c): return c
class GC(Rec):
    def get_colormap(self): return Cmap()
class FakeDA:
    def __init__(self):
        class Style: pass
        self.window = Rec(); st = Style(); st.fg_gc = {gtk.STATE_NORMAL: GC()}; self._st = st
    def get_style(self): return self._st
    def create_pango_layout(self, t=""): return Rec()
def sliders_draw():
    cls = m.ligand_validation_metrics_gui; o = cls.__new__(cls)
    o.bar_length = 300; o.bar_height = 10; o.abs_bar_height = 16; o.x_bar_offset = 160; o.y_bar_offset = 20; o.y_pixels_bar_spacing = 30; o.abs_bar_width = 6
    o.setup_colour_bar_buff(); ls = m.ligand_stats()
    for nm, pc, v in (("Direct map density correl.", 9.07, 0.689), (" Diff map density correl.", 50.0, 0.05), ("Dictionary-based-geom.", 40.0, 11.2), ("             Bad contacts", 70.0, 3)):
        ls.add_metric(nm, pc, v)
    o.lvs = ls; da = FakeDA(); o.on_drawing_area_expose(da, None)
    imgs = [a for n, a in da.window.calls if n == "draw_rgb_image"]
    if len(imgs) != 4: return "%d colour bars drawn" % len(imgs)
    buf = imgs[0][6]
    if not isinstance(buf, bytes) or len(buf) != 9000: return "colour bar buffer: %s of length %d" % (type(buf).__name__, len(buf))
    if tuple(buf[0:3]) != (255, 0, 0): return "first pixel %r" % (tuple(buf[0:3]),)
    return True
check("ligand metric sliders: drawing code runs and builds a byte pixel buffer for the colour bars", sliders_draw)
def pdbe_bar():
    cls = [v for k, v in vars(m).items() if isinstance(v, type) and hasattr(v, "setup_colour_bar_buff") and v.__module__ == "__main__" and v is not m.ligand_validation_metrics_gui]
    if not cls: return "no PDBe slider class found"
    o = cls[0].__new__(cls[0]); o.bar_length = 300; o.bar_height = 10; o.setup_colour_bar_buff()
    return True if (isinstance(o.colour_bar_buff, bytes) and len(o.colour_bar_buff) == 9000) else type(o.colour_bar_buff).__name__
check("PDBe validation sliders: colour bar is a byte buffer", pdbe_bar)
def bytes_reach_c():
    buf = bytes([255, 0, 0, 200, 150, 100, 10, 20, 250] * 4)
    pb = _c.call("gdk_pixbuf_new_from_data", buf, 0, False, 8, 6, 2, 18, None, None)
    return True if ctypes.string_at(_c.call("gdk_pixbuf_get_pixels", pb), 36) == buf else "pixel bytes differ"
check("a bytes pixel buffer reaches a guchar* argument of GTK unchanged", bytes_reach_c)
# --- Ligand > Ligand Metric Sliders: refinement maps that cannot give observed F / sigF / R-free (a PDBe/EDS map-coefficient MTZ, a .map file).
# Build 11 raised NameError: name 'imol_map' is not defined (inside the code that reports the problem) and showed nothing.
def label_texts(wins):
    out = []
    for w in wins:
        for x in H.walk(w):
            if type(x).__name__ == "Label":
                try: out.append(x.get_text())
                except Exception: pass
    return "\n".join(out)
def sliders_menu_text():
    # info_dialog is Coot's C++ dialog (no window without a display): capture the text it is given
    shown = []; keep = m.info_dialog; m.info_dialog = lambda t: shown.append(t)
    try: activate(["Ligand", "Ligand Metric Sliders"])
    finally: m.info_dialog = keep
    return "\n".join(shown)
def sliders_ccp4_map():
    f = os.path.join(tempfile.mkdtemp(prefix="coot-slider-test-"), "test.map")
    coot.export_map(imap, f)
    imap2 = coot.handle_read_ccp4_map(f, 0)
    if not coot.is_valid_map_molecule(imap2): return "could not read back the exported map"
    coot.set_imol_refinement_map(imap2)
    txt = sliders_menu_text()
    coot.set_imol_refinement_map(imap)
    if "cannot be calculated" not in txt: return "dialog text: %r" % txt[:300]
    return True
check("Ligand Metric Sliders with a map that has no MTZ: explanatory dialog, no exception", sliders_ccp4_map)
def sliders_map_coeffs():
    mc = coot.make_and_draw_map(os.path.join(td, "map-coefficients-only.mtz"), "FWT", "PHWT", "", 0, 0)
    if not coot.is_valid_map_molecule(mc): return "map from the coefficient-only MTZ not made"
    coot.set_imol_refinement_map(mc)
    txt = sliders_menu_text()
    coot.set_imol_refinement_map(imap)
    if "cannot be calculated" not in txt or "no observed F, sigF and R-free" not in txt:
        return "dialog text: %r" % txt[:400]
    return True
check("Ligand Metric Sliders with a map-coefficient MTZ (PDBe/EDS style): says the observed data are missing", sliders_map_coeffs)
def find_mtz_good():
    f, labels, problems = m.ligand_metrics_find_mtz(imap)
    ok = f and f.endswith("rnasa-1.8-all_refmac1.mtz") and [l.split("/")[-1] for l in labels] == ["FGMP18", "SIGFGMP18", "FreeR_flag"]
    return True if ok else (f, labels, problems)
check("ligand_metrics_find_mtz finds F, sigF and R-free of the refinement MTZ", find_mtz_good)
def labels_empty():
    return True if tuple(m.mtz_file_name2refinement_column_labels("")) == (False, False, False) and tuple(m.mtz_file_name2refinement_column_labels(os.path.join(td, "nonexistent.mtz"))) == (False, False, False) else "unexpected return"
check("mtz_file_name2refinement_column_labels returns (False, False, False) for no file / unreadable file", labels_empty)

def sigma_choice():
    labels = m.mtz_file_name2refinement_column_labels(os.path.join(td, "two-sigma-columns.mtz"))
    got = [l.split("/")[-1] if l else l for l in labels]
    return True if got == ["F-obs-filtered", "SIGF-obs-filtered", "R-free-flags"] else "labels %r (SIGI-obs is listed before SIGF-obs-filtered; the sigma of I is not the sigma of F)" % (labels,)
check("sliders use the sigma that belongs to F (Phenix MTZ: SIGF-obs-filtered, not SIGI-obs)", sigma_choice)

check("no exception in any GTK signal handler", lambda: True if not _c.CALLBACK_ERRORS else [e[1][-300:] for e in _c.CALLBACK_ERRORS][:2])
w = max(len(r[0]) for r in res)
for n, ok, v in res: print(("PASS " if ok else "FAIL ") + n.ljust(w) + (("  " + v) if v else ""))
print("SUMMARY", sum(1 for r in res if r[1]), "/", len(res), flush=True)
coot.coot_real_exit(0)
