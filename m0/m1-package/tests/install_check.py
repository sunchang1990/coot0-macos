# Quick start test run by install.sh (about 30 s): Coot starts without a window, Python and Scheme work, a model and a map are read.
# Prints "INSTALL-CHECK OK ..." or "INSTALL-CHECK FAIL ...".
import os, sys, io, contextlib
fails, notes = [], []
try:
    import coot
    data = os.path.join(os.environ["COOT_PREFIX"], "share", "coot", "data")
    imol = coot.read_pdb(os.path.join(data, "tutorial-modern.pdb"))
    if not coot.is_valid_model_molecule(imol):
        fails.append("model not read")
    else:
        notes.append("model %d atoms" % coot.n_atoms(imol) if hasattr(coot, "n_atoms") else "model read")
    imap = coot.make_and_draw_map(os.path.join(data, "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
    if not coot.is_valid_map_molecule(imap):
        fails.append("map not made")
    else:
        notes.append("map")
    with contextlib.redirect_stdout(io.StringIO()):
        r = coot.run_scheme_command("(+ 1 2)")
    if str(r).strip() != "3":
        fails.append("Scheme (+ 1 2) gave %r" % (r,))
    else:
        notes.append("Scheme")
    notes.append("Python %s" % sys.version.split()[0])
    if not os.path.isdir(os.environ.get("CLIBD_MON", "/nonexistent")):
        fails.append("monomer library not found")
    else:
        notes.append("monomer library")
except Exception as e:
    fails.append("exception %r" % (e,))
if fails:
    print("INSTALL-CHECK FAIL " + "; ".join(fails), flush=True)
else:
    print("INSTALL-CHECK OK Coot starts: " + ", ".join(notes), flush=True)
coot.coot_real_exit(0 if not fails else 1)
