
# Headless tests of Calculate > Run Refmac (the Python runner that C++ reaches through the Scheme bridge) and of the Scheme-to-Python
# bridge that replaces the guile-gtk based Scheme GUI functions. A real refmac5 run needs CCP4 (found by the launcher); without
# it that check is reported as skipped (and counts as passed).
import os, sys, io, time, contextlib, traceback, shutil
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

# 1. the Scheme-to-Python bridge
def scm(cmd):
    with contextlib.redirect_stdout(io.StringIO()): return coot.run_scheme_command(cmd)
def literals():
    r = scm('(coot-python-literal (list "a\\"b" 1 2.5 (cons "x" "y") #t #f (list) (quote sym)))')
    want = '["a\\"b", 1, 2.5, ["x", "y"], True, False, [], "sym"]'
    return True if r == want else "got %r" % r
check("Scheme bridge: Scheme values become Python source text", literals)
def refmac_args():
    got = []
    old = m.run_refmac_by_filename; m.run_refmac_by_filename = lambda *a: got.append(a)
    try:
        scm('(run-refmac-by-filename "in.pdb" "out.pdb" "in.mtz" "out.mtz" "" 3 0 1 1 0 "dummy" 5 1 "" "F" "SIGF" "FREE")')
        scm('(run-refmac-by-filename "in.pdb" "out.pdb" "in.mtz" "out.mtz" "" 3 0 1 1 1 (cons "PHIB" "FOM") 5 1 "" "F" "SIGF")')
    finally:
        m.run_refmac_by_filename = old
    want0 = ("in.pdb", "out.pdb", "in.mtz", "out.mtz", "", 3, 0, 1, 1, 0, "dummy", 5, 1, "", "F", "SIGF", "FREE")
    want1 = ("in.pdb", "out.pdb", "in.mtz", "out.mtz", "", 3, 0, 1, 1, 1, ["PHIB", "FOM"], 5, 1, "", "F", "SIGF")
    return True if got == [want0, want1] else "got %r" % (got,)
check("Scheme bridge: (run-refmac-by-filename ...) from C++ reaches the Python runner with the same arguments", refmac_args)
def gln_asn():
    got = []
    old = getattr(m, "interesting_things_with_fix_maybe", None); m.interesting_things_with_fix_maybe = lambda t, l: got.append((t, l))
    m.do_180_degree_side_chain_flip = "FLIP"
    try:
        scm('(interesting-things-with-fix-maybe "T" (list (list "lab 1" 0 "A" 45 "" " OE1" "" (lambda () 1)) (list "lab 2" 0 "B" 7 "" " NE2" "")))')
    finally:
        if old: m.interesting_things_with_fix_maybe = old
    want = [("T", [["lab 1", 0, "A", 45, "", " OE1", "", ["FLIP", 0, "A", 45, "", ""]], ["lab 2", 0, "B", 7, "", " NE2", ""]])]
    return True if got == want else "got %r" % (got,)
check("Scheme bridge: GLN and ASN B-factor outliers window request reaches the Python version", gln_asn)
def ccp4_words():
    w = scm("(%ccp4-env-words)")
    import glob
    home = os.environ.get("CCP4") or os.environ.get("COOT_CCP4_HOME")
    have_ccp4 = bool(home and os.path.isdir(home)) or any(os.path.isdir(d + "/bin") for d in glob.glob("/Applications/ccp4-*"))
    if not have_ccp4: return True if not w else "no CCP4 installed but words %r" % (w,)
    if os.environ.get("CINCL") and os.environ.get("CCP4_SCR"): return True            # the user's shell already has CCP4's environment
    return True if (isinstance(w, list) and any(x.startswith("CINCL=") for x in w) and any(x.startswith("CCP4_SCR=") for x in w)) else "words %r" % (w,)
check("Scheme programs get CCP4's environment (env(1) arguments of the child only)", ccp4_words)

# 2. a real refmac run, as the Run Refmac dialog starts it
def real_run(with_free):
    from shutil import which
    exe = None
    for d in (os.environ.get("CBIN"), os.environ.get("COOT_CCP4_HOME") and os.environ["COOT_CCP4_HOME"] + "/bin"):
        if d and os.path.isfile(os.path.join(d, "refmac5")): exe = os.path.join(d, "refmac5")
    exe = exe or which("refmac5")
    if not exe: return "skipped"
    pdb = os.path.join(td, "tutorial-modern.pdb"); mtz = os.path.join(td, "rnasa-1.8-all_refmac1.mtz")
    imap = coot.make_and_draw_map(mtz, "FWT", "PHWT", "", 0, 0)
    f, sf, rf = m.mtz_file_name2refinement_column_labels(mtz)
    if not f: return "skipped"
    out = os.path.abspath("coot-refmac"); os.makedirs(out, exist_ok=True)
    tag = "free" if with_free else "nofree"
    po = os.path.join(out, "run-%s.pdb" % tag); mo = os.path.join(out, "run-%s.mtz" % tag)
    n0 = sum(1 for i in range(30) if coot.is_valid_model_molecule(i)); maps0 = sum(1 for i in range(30) if coot.is_valid_map_molecule(i))
    buf = io.StringIO()
    cmd = '(run-refmac-by-filename "%s" "%s" "%s" "%s" "" 0 0 %d 1 0 "dummy" 1 1 "" "%s" "%s"%s)' % (pdb, po, mtz, mo, imap, f, sf, (' "%s"' % rf) if with_free else "")
    with contextlib.redirect_stdout(buf): coot.run_scheme_command(cmd)
    t0 = time.time()
    while time.time() - t0 < 180:
        while _c.call("g_main_context_iteration", None, False): pass
        if sum(1 for i in range(30) if coot.is_valid_model_molecule(i)) > n0: break
        time.sleep(0.3)
    n1 = sum(1 for i in range(30) if coot.is_valid_model_molecule(i)); maps1 = sum(1 for i in range(30) if coot.is_valid_map_molecule(i))
    logs = [x for x in os.listdir(out) if x.endswith(".log")]
    labin = [l for l in buf.getvalue().splitlines() if "LABIN" in l]
    if n1 != n0 + 1: return "no new model after %.0f s (models %d -> %d); labin %r" % (time.time() - t0, n0, n1, labin[:1])
    if maps1 < maps0 + 2: return "new maps: %d -> %d" % (maps0, maps1)
    if with_free != any("FREE=" in l for l in labin): return "FREE in LABIN is wrong: %r" % (labin[:1],)
    out_txt = buf.getvalue()
    if "not set !" in out_txt: return "the run still prints 'not set !' warnings about environment variables"
    if "environment for refmac5:" not in out_txt: return "the environment of refmac5 is not shown in the log"
    return True
def skip_ok(name, fn):
    r = None
    try: r = fn()
    except BaseException as e:
        res.append((name, False, "EXC " + repr(e)[:160] + " " + traceback.format_exc()[-300:].replace("\n", " | "))); return
    if r == "skipped": res.append((name + "  (skipped: no CCP4 program found)", True, ""))
    else: res.append((name, r is True, "" if r is True else repr(r)[:300]))
skip_ok("Run Refmac (Scheme request -> Python runner -> refmac5): new model and maps are read in", lambda: real_run(True))
skip_ok("Run Refmac without an R-free column: LABIN has no empty FREE=", lambda: real_run(False))
def env_report():
    # the refmac5 environment is reported from ccp4_child_env (build 11 printed "environment variable: ... not set !" for variables that
    # Coot deliberately keeps out of its own environment)
    src = open(os.path.join(here, "share", "coot", "python", "refmac.py")).read()
    return True if ("not set !" not in src and "environment for refmac5" in src) else "refmac.py still has the old environment diagnostics"
check("Run Refmac reports the child environment instead of 'not set !' warnings", env_report)
# 3. Ligand Builder (Lidia) "Apply" -> acedrg (build 16)
BENZENE = "benzene\n  test\n\n  6  6  0  0  0  0  0  0  0  0999 V2000\n" + "".join(
    "%10.4f%10.4f%10.4f C   0  0\n" % xy for xy in ((1.2124, 0.7, 0.0), (1.2124, -0.7, 0.0), (0.0, -1.4, 0.0),
                                                   (-1.2124, -0.7, 0.0), (-1.2124, 0.7, 0.0), (0.0, 1.4, 0.0))) + \
    "  1  2  2  0\n  2  3  1  0\n  3  4  2  0\n  4  5  1  0\n  5  6  2  0\n  6  1  1  0\nM  END\n"
def acedrg_env_without_ccp4_shell():
    # Coot started from Finder / a shell that did not source CCP4's setup: no CBIN in Coot's own environment
    saved = {k: os.environ.pop(k) for k in ("CBIN", "CCP4_BIN") if k in os.environ}
    try:
        env = m.acedrg_env()
    finally:
        os.environ.update(saved)
    if "PYTHONPATH" in env or env.get("PYTHONHOME"): return "Coot's PYTHONPATH/PYTHONHOME passed on to CCP4's Python"
    first = env["PATH"].split(os.pathsep)[0]
    if env.get("CBIN") and first != env["CBIN"]: return "CCP4's bin is not first on PATH: %r" % env["PATH"][:120]
    if ";" in env["PATH"]: return "PATH joined with ';': %r" % env["PATH"][:120]
    return True
check("Lidia/acedrg: acedrg's environment can be made when Coot was not started from a CCP4 shell", acedrg_env_without_ccp4_shell)
def lidia_empty_sketch():
    d = os.path.abspath("lidia-empty"); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "coot-lidia.mdl"), "w").close()      # what Lidia writes when nothing is drawn
    ran, said = [], []
    old_p, old_i = m.popen_command, m.info_dialog
    m.popen_command = lambda *a, **k: ran.append(a) or 0
    m.info_dialog = lambda t: said.append(t)
    try:
        r = m.import_from_3d_generator_from_mdl(os.path.join(d, "coot-lidia.mdl"), "LIG")
    finally:
        m.popen_command, m.info_dialog = old_p, old_i
    if ran: return "a ligand generator was started on an empty sketch: %r" % (ran[0][:1],)
    if not any("Draw a molecule" in t for t in said): return "no message for an empty sketch: %r" % said
    return True if r is False else "returned %r" % (r,)
check("Lidia Apply with an empty sketch: says 'draw a molecule first', no acedrg run", lidia_empty_sketch)
def lidia_acedrg_benzene():
    if not m.command_in_path_qm("acedrg") and not (m.ccp4_child_env().get("CBIN") and
                                                   os.path.isfile(os.path.join(m.ccp4_child_env()["CBIN"], "acedrg"))):
        return "skipped"
    d = os.path.abspath("lidia-benzene"); os.makedirs(d, exist_ok=True); cwd = os.getcwd(); os.chdir(d)
    saved = {k: os.environ.pop(k) for k in ("CBIN", "CCP4_BIN") if k in os.environ}
    said = []; old_i = m.info_dialog; m.info_dialog = lambda t: said.append(t)
    try:
        open("coot-lidia.mdl", "w").write(BENZENE)
        n0 = sum(1 for i in range(60) if coot.is_valid_model_molecule(i))
        with contextlib.redirect_stdout(io.StringIO()):
            m.import_from_3d_generator_from_mdl("coot-lidia.mdl", "LIG")
        n1 = sum(1 for i in range(60) if coot.is_valid_model_molecule(i))
    finally:
        m.info_dialog = old_i; os.environ.update(saved); os.chdir(cwd)
    if said: return "message: %r" % said[:1]
    if n1 != n0 + 1: return "no ligand read in (models %d -> %d); files %r" % (n0, n1, sorted(os.listdir(d))[:12])
    return True if os.path.isfile(os.path.join(d, "acedrg-LIG.cif")) else "no acedrg-LIG.cif"
skip_ok("Lidia Apply -> acedrg on benzene (CCP4 not in Coot's own environment): ligand and dictionary are read in", lidia_acedrg_benzene)
check("no exception in any GTK signal handler", lambda: True if not _c.CALLBACK_ERRORS else [e[1][-300:] for e in _c.CALLBACK_ERRORS][:2])
w = max(len(r[0]) for r in res)
for n, ok, v in res: print(("PASS " if ok else "FAIL ") + n.ljust(w) + (("  " + v) if v else ""))
print("SUMMARY", sum(1 for r in res if r[1]), "/", len(res), flush=True)
coot.coot_real_exit(0)
