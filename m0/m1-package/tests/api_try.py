# api_try.py  (build 31) -- try scripting calls on the test data and see what they return AND what they changed.
# Run by tests/api-try.sh FILE (one block = lines separated by a blank line; each block runs in a fresh Coot with
#   molecule 0 = tutorial-modern.pdb, molecule 1 = map from rnasa-1.8-all_refmac1.mtz FWT/PHWT (the refinement map)).
# Lines:  py: <python expression or statement>      scm: <scheme expression>      # comment
# Output (stdout of the driver, also $API_TRY_OUT): for each line the value, what it printed, and what changed.
import os, sys, json, io, contextlib, time
import coot
g = globals()
HERE = os.path.dirname(os.path.abspath(os.environ["API_TRY_HERE"] + "/x"))
sys.path.insert(0, HERE)
from api_state import Snapshot

OUT = open(os.environ["API_TRY_OUT"], "a")
def say(s): OUT.write(s + "\n"); OUT.flush()
block = json.loads(os.environ["API_TRY_BLOCK"])

with contextlib.redirect_stdout(io.StringIO()):
    imol = coot.read_pdb("tutorial-modern.pdb")
    imap = coot.make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
    coot.set_imol_refinement_map(imap)
    coot.export_map(imap, "rnasa-map.map")
snap = Snapshot(g, json.load(open(os.environ["API_INDEX"])))

def run_scheme(text):
    lit = '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
    r = coot.run_scheme_command("(coot0-console-eval %s)" % lit)
    if not isinstance(r, str): return "error", "no answer from Scheme: %r" % (r,), ""
    p = r.split("\x1f")
    if len(p) < 3: return "error", r, ""
    return ("ok" if p[1] == "ok" else "error"), p[2], p[0]

ns = dict(g)   # the lines' own names (a, b, e ...) never touch this script's variables
for line in block:
    lang, _, text = line.partition(":"); text = text.strip(); lang = lang.strip()
    before = snap.take(); out = io.StringIO(); t0 = time.time()
    try:
        with contextlib.redirect_stdout(out):
            if lang == "py":
                try: v = repr(eval(compile(text, "<try>", "eval"), ns))
                except SyntaxError: exec(compile(text, "<try>", "exec"), ns); v = "(statement)"
                st = "ok"
            else:
                st, v, so = run_scheme(text); out.write(so)
    except Exception as x:
        st, v = "error", "%s: %s" % (type(x).__name__, str(x)[:300])
    try:
        with contextlib.redirect_stdout(io.StringIO()): coot.clear_up_moving_atoms()
    except Exception: pass
    after = snap.take()
    say("%s> %s\n   %s %s  (%.2f s)" % (lang, text, st, v[:500], time.time() - t0))
    p = out.getvalue().strip()
    if p: say("   printed: " + p[-300:].replace("\n", " | "))
    for c in snap.diff(before, after): say("   changed: " + c)
say("--- end of block")
OUT.close()
coot.coot_real_exit(0)
