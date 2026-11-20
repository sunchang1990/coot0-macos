# cookbook_run.py  (build 26; key and refinement-mode checks build 27) -- runs every recipe of docs/cookbook/*.md inside Coot, without a window.
# A recipe is a "### " heading followed by a ```python block and a ```scheme block.  Optional hidden checks:
#   <!-- check-py: EXPRESSION -->    evaluated after the Python block, must be true
#   <!-- check-scm: EXPRESSION -->   evaluated after the Scheme block, must give #t
#   <!-- not-run: REASON -->         the recipe is shown but not run here (e.g. it needs a screen or a program)
# Each recipe starts in the work folder with fresh copies of the test files, all molecules closed.
import os, sys, re, glob, io, contextlib, shutil, traceback
sys.path.insert(0, os.path.join(os.environ["COOT_PREFIX"], "tests"))
import gui_harness as H
g, errs, log = H.load()
import coot

here = os.environ["COOT_PREFIX"]
docs = os.path.join(here, "docs", "cookbook")
work = os.environ.get("COOKBOOK_WORK") or os.path.join(os.getcwd(), "cookbook-work")
only = os.environ.get("COOKBOOK_ONLY", "")
os.makedirs(work, exist_ok=True)
# recipe 6.8 writes into $HOME/.coot-preferences: give the test its own home so a real coot0 home is never changed
os.environ["HOME"] = os.path.join(work, "home"); os.makedirs(os.environ["HOME"], exist_ok=True)

def recipes():
    for path in sorted(glob.glob(os.path.join(docs, "*.md"))):
        txt = open(path, encoding="utf-8").read()
        parts = re.split(r"^### ", txt, flags=re.M)
        for p in parts[1:]:
            title = p.split("\n", 1)[0].strip()
            py = re.findall(r"```python\n(.*?)```", p, re.S)
            scm = re.findall(r"```scheme\n(.*?)```", p, re.S)
            cpy = re.findall(r"<!-- check-py: (.*?) -->", p, re.S)
            cscm = re.findall(r"<!-- check-scm: (.*?) -->", p, re.S)
            nr = re.findall(r"<!-- not-run: (.*?) -->", p, re.S)
            yield os.path.basename(path), title, py, scm, cpy, cscm, nr

def scheme(text):
    lit = '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
    r = coot.run_scheme_command("(coot0-console-eval %s)" % lit)
    if not isinstance(r, str): return "error", "no answer from Scheme", ""
    p = r.split("\x1f")
    return ("ok" if p[1] == "ok" else "error"), p[2], p[0]

def fresh():
    with contextlib.redirect_stdout(io.StringIO()):
        for i in list(coot_utils_model_list()):
            coot.close_molecule(i)
    for f in ("tutorial-modern.pdb", "rnasa-1.8-all_refmac1.mtz", "1ehz.pdb", "standard-residues.pdb"):
        src = os.path.join(here, "test-data", f)
        if os.path.exists(src): shutil.copy(src, os.path.join(work, f))
    os.chdir(work)

def coot_utils_model_list():
    return [i for i in range(coot.graphics_n_molecules()) if coot.is_valid_model_molecule(i) or coot.is_valid_map_molecule(i)]

# (build 27) keys that Coot's own key handler takes before any script binding sees them (globjects.cc): a recipe must not
# bind these (build 26 bound F5, which opens Model/Fit/Refine instead)
# Keys Coot's C++ key handler (globjects.cc key_press_event / key_release_event) acts on itself.  Build 28: o, O (next / previous
# NCS chain), p (update Go To Atom), c (crosshairs), s / S (re-contour), I and Ctrl-c/d/i/x were missing (user, 20 Nov: 6.3's "o").
TAKEN_KEYS = set("F5 F6 F7 F8 i I u d f n m l o O p c s S space Return Escape period comma minus plus equal Left Right Up Down".split()) \
    | set("0123456789") | {"Control_" + c for c in "cdgilrsxyz"}
def bound_keys(blocks):
    return re.findall(r'add[_-]key[_-]binding\s*\(?\s*"[^"]*"\s*,?\s*"([^"]+)"', "\n".join(blocks))

res = []
n_rec = 0
for fname, title, py, scm, cpy, cscm, nr in recipes():
    if only and only not in fname + " " + title: continue
    n_rec += 1
    name = "%s: %s" % (fname[:-3], title)
    if nr:
        res.append(("SKIP", name, "not run: " + nr[0])); continue
    for lang, blocks, checks in (("python", py, cpy), ("scheme", scm, cscm)):
        if not blocks:
            res.append(("FAIL", "%s [%s]" % (name, lang), "no %s block" % lang)); continue
        fresh(); out = io.StringIO(); why = ""
        taken = [k for k in bound_keys(blocks) if k in TAKEN_KEYS]
        if taken:
            res.append(("FAIL", "%s [%s]" % (name, lang), "binds %s, a key Coot itself uses (the binding never runs)" % taken)); continue
        try:
            with contextlib.redirect_stdout(out):
                if lang == "python":
                    for b in blocks: exec(compile(b, name, "exec"), g)
                    for c in checks:
                        if not eval(c, g): why = "check failed: %s" % c; break
                else:
                    for b in blocks:
                        st, val, sout = scheme(b)
                        if st != "ok": why = "Scheme error: %s" % val.strip()[:300]; break
                    if not why:
                        for c in checks:
                            st, val, sout = scheme(c)
                            if st != "ok" or val.strip() != "#t": why = "check failed: %s -> %s" % (c, val.strip()[:200]); break
        except BaseException as e:
            why = "%s: %s | %s" % (type(e).__name__, str(e)[:200], traceback.format_exc()[-300:].replace("\n", " | "))
        # (build 27) a recipe must not leave "immediate replacement" on: afterwards every refinement made with the mouse
        # gets no Accept/Reject window and its moving atoms stay on the screen (user report 19 Nov)
        try:
            if not why and coot.refinement_immediate_replacement_state() != 0:
                why = "leaves set_refinement_immediate_replacement on (later refinements get no Accept window)"
            coot.set_refinement_immediate_replacement(0)
        except Exception: pass
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                coot.clear_up_moving_atoms()
        except Exception: pass
        res.append(("FAIL" if why else "PASS", "%s [%s]" % (name, lang), why))

for st, name, why in res:
    print("%s %-110s %s" % (st, name[:110], why))
npass = sum(1 for r in res if r[0] == "PASS"); nfail = sum(1 for r in res if r[0] == "FAIL")
print("recipes: %d, skipped (not run): %d" % (n_rec, sum(1 for r in res if r[0] == "SKIP")))
print("SUMMARY %d / %d" % (npass, npass + nfail))
coot.coot_real_exit(0)
