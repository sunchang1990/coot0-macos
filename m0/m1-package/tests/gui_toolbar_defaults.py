
# Headless tests of the default toolbar buttons (Sphere Refine, Sphere Refine +, Sphere Regularization, Sphere Regularization +):
# first-run installation into ~/.coot-preferences/coot_toolbuttons.py, the buttons Coot creates from that file, what they do when
# clicked, and that "Remove a Button" is permanent and exact (removing "Sphere Refine" must not also remove "Sphere Refine +").
import os, sys, io, math, contextlib, traceback, tempfile
sys.path.insert(0, os.path.join(os.environ["COOT_PREFIX"], "tests"))
import gui_harness as H
import _gtk2core as _c
res = []
def check(name, fn):
    try:
        v = fn(); ok = (v is None or v is True)
        res.append((name, ok, "" if ok else repr(v)[:300]))
    except BaseException as e:
        res.append((name, False, "EXC " + repr(e)[:160] + " " + traceback.format_exc()[-300:].replace("\n", " | ")))
g, errs, log = H.load()
import coot, __main__ as m
here = os.environ["COOT_PREFIX"]; td = os.path.join(here, "test-data")
LABELS = ["Sphere Refine", "Sphere Refine +", "Sphere Regularization", "Sphere Regularization +"]
home = tempfile.mkdtemp(prefix="coot-toolbar-test-")
prefs = os.path.join(home, ".coot-preferences"); tbfile = os.path.join(prefs, "coot_toolbuttons.py"); marker = os.path.join(prefs, ".default-toolbar-buttons-v1")
def toolbar_labels():
    return [f[0] for f in (m.toolbar_label_list() or [])]

def off_by_default():
    os.environ["HOME"] = home
    os.environ.pop("COOT_DEFAULT_TOOLBAR", None); os.environ.pop("COOT_NO_DEFAULT_TOOLBAR", None)
    r = m.install_default_toolbar_buttons()
    if not (r is False and not os.path.exists(prefs)): return "installed without COOT_DEFAULT_TOOLBAR: %r, prefs exists %r" % (r, os.path.exists(prefs))
    os.environ["COOT_DEFAULT_TOOLBAR"] = "1"; os.environ["COOT_NO_DEFAULT_TOOLBAR"] = "1"
    r = m.install_default_toolbar_buttons()
    os.environ.pop("COOT_NO_DEFAULT_TOOLBAR")
    return True if (r is False and not os.path.exists(prefs)) else "installed although COOT_NO_DEFAULT_TOOLBAR=1: %r" % (r,)
check("no changes to the preferences unless the launcher asked for the default buttons (COOT_DEFAULT_TOOLBAR; COOT_NO_DEFAULT_TOOLBAR=1 switches them off)", off_by_default)
def first_run():
    os.environ["COOT_DEFAULT_TOOLBAR"] = "1"
    r = m.install_default_toolbar_buttons()
    if r is not True: return "install returned %r" % (r,)
    txt = open(tbfile).read()
    bad = [l for l in LABELS if ('coot_toolbar_button("%s",' % l) not in txt]
    if bad: return "missing in coot_toolbuttons.py: %r" % bad
    if not os.path.exists(marker): return "no marker file"
    return True
check("first start writes the four sphere buttons into ~/.coot-preferences/coot_toolbuttons.py", first_run)
def second_run():
    before = open(tbfile).read()
    r = m.install_default_toolbar_buttons()
    return True if (r is False and open(tbfile).read() == before) else "second call returned %r / file changed" % (r,)
check("later starts leave the file alone", second_run)
def buttons_created():
    n0 = len(toolbar_labels())
    exec(compile(open(tbfile).read(), tbfile, "exec"), m.__dict__)      # what Coot does with every *.py in ~/.coot-preferences
    labs = toolbar_labels()
    missing = [l for l in LABELS if l not in labs]
    if missing: return "buttons not on the toolbar: %r (toolbar: %r)" % (missing, labs)
    exec(compile(open(tbfile).read(), tbfile, "exec"), m.__dict__)      # (a second execution must not duplicate them)
    labs2 = toolbar_labels()
    return True if (len(labs2) == len(labs) and len(labs) >= n0 + 4) else "duplicates: %d -> %d" % (len(labs), len(labs2))
check("Coot's preference scripts turn them into toolbar buttons (no duplicates)", buttons_created)

imol = coot.read_pdb(os.path.join(td, "tutorial-modern.pdb"))
imap = coot.make_and_draw_map(os.path.join(td, "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
coot.set_imol_refinement_map(imap); coot.set_refinement_immediate_replacement(1)
def atoms(fn):
    d = {}
    for l in open(fn):
        if l.startswith(("ATOM", "HETATM")) and l[16] in " A":
            d[(l[21], int(l[22:26]), l[12:16].strip())] = (float(l[30:38]), float(l[38:46]), float(l[46:54]))
    return d
def moved_residues():
    coot.write_pdb_file(imol, "tb_before.pdb")
    return atoms("tb_before.pdb")
def click(label):
    btn = [f[1] for f in m.toolbar_label_list() if f[0] == label][0]
    coot.set_go_to_atom_molecule(imol); coot.set_go_to_atom_chain_residue_atom_name(coot.chain_id_py(imol, 0), 43, " CA ")
    b = moved_residues(); n0 = len(_c.CALLBACK_ERRORS)
    with contextlib.redirect_stdout(io.StringIO()): btn.emit("clicked")
    coot.accept_regularizement()
    errs_ = [e[1].strip().splitlines()[-1] for e in _c.CALLBACK_ERRORS[n0:]]
    if errs_: return "callback error: %r" % errs_
    coot.write_pdb_file(imol, "tb_after.pdb"); a = atoms("tb_after.pdb")
    mv = sorted(set(k[1] for k in a if k in b and math.dist(a[k], b[k]) > 1e-4))
    return mv
def sphere(label, plus):
    mv = click(label)
    if isinstance(mv, str): return mv
    if 43 not in mv or len(mv) < 4: return "residues moved: %r" % (mv,)
    if plus and not (38 in mv or 46 in mv): return "the + button did not extend the zone by a residue: %r" % (mv,)
    return True
check("clicking Sphere Refine refines the residues around the centred residue", lambda: sphere("Sphere Refine", False))
check("clicking Sphere Refine + also refines the neighbouring residues in sequence", lambda: sphere("Sphere Refine +", True))
check("clicking Sphere Regularization regularizes the residues around the centred residue", lambda: sphere("Sphere Regularization", False))
check("clicking Sphere Regularization + also regularizes the neighbouring residues in sequence", lambda: sphere("Sphere Regularization +", True))
def remove_one():
    n0 = len(_c.CALLBACK_ERRORS)
    m.remove_toolbar_from_init_file("Sphere Refine")
    txt = open(tbfile).read()
    if 'coot_toolbar_button("Sphere Refine",' in txt: return "Sphere Refine still in the file"
    others = [l for l in LABELS[1:] if ('coot_toolbar_button("%s",' % l) not in txt]
    return True if not others else "removing Sphere Refine also removed %r" % others
check("removing a button from the preferences removes exactly that button (not Sphere Refine +)", remove_one)
def stays_removed():
    r = m.install_default_toolbar_buttons()
    return True if (r is False and 'coot_toolbar_button("Sphere Refine",' not in open(tbfile).read()) else "button came back / install returned %r" % (r,)
check("a removed default button stays removed at the next start", stays_removed)
def save_roundtrip():
    m.save_toolbar_to_init_file("Sphere Refine", "sphere_refine()", icon="refine-1.svg", tooltip="RSR around active residue")
    txt = open(tbfile).read()
    return True if (txt.count('coot_toolbar_button("Sphere Refine",') == 1 and txt.count('coot_toolbar_button("Sphere Refine +",') == 1) else txt
check("Manage Buttons can bring a button back (save_toolbar_to_init_file keeps the other lines)", save_roundtrip)
def icons_exist():
    d = os.path.join(here, "share", "coot", "pixmaps")
    used = set()
    for grp in m.list_of_toolbar_functions():
        for e in grp[1:]:
            if e and e[0] in LABELS and len(e) > 3: used.add(e[3])
    miss = [i for i in used if not os.path.isfile(os.path.join(d, i))]
    return True if (used and not miss) else "icons missing: %r" % miss
check("the icons of the four buttons are installed", icons_exist)
check("no exception in any GTK signal handler", lambda: True if not _c.CALLBACK_ERRORS else [e[1][-300:] for e in _c.CALLBACK_ERRORS][:2])
w = max(len(r[0]) for r in res)
for n, ok, v in res: print(("PASS " if ok else "FAIL ") + n.ljust(w) + (("  " + v) if v else ""))
print("SUMMARY", sum(1 for r in res if r[1]), "/", len(res), flush=True)
coot.coot_real_exit(0)
