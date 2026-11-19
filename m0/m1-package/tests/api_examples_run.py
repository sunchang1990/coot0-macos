# api_examples_run.py  (build 26) -- runs inside Coot (--python --script), driven by tests/run-api-examples.py.
# Tries the example of every scripting function (docs/api) in Python and in Scheme on the test data:
#   molecule 0 = tutorial-modern.pdb, molecule 1 = map from rnasa-1.8-all_refmac1.mtz (FWT/PHWT).
# One JSON line per call goes to $API_RESULTS ("start" before the call, the result after it), so the driver can
# tell a call that stopped Coot from one that finished.  When an example changed molecule 0 or 1 (or closed them),
# the process ends with code 3 and the driver starts a fresh Coot for the next function.
import os, sys, json, io, contextlib, time
import coot

IDX = os.environ["API_INDEX"]; RES = os.environ["API_RESULTS"]; ONLY = os.environ.get("API_ONLY", "")
g = globals()
f = open(RES, "a")
def log(d):
    f.write(json.dumps(d) + "\n"); f.flush(); os.fsync(f.fileno())

entries = json.load(open(IDX))
done = set()
if os.path.exists(RES):
    for l in open(RES):
        try: d = json.loads(l)
        except Exception: continue
        if d.get("ev") == "end": done.add((d["key"], d["lang"]))

with contextlib.redirect_stdout(io.StringIO()):
    imol = coot.read_pdb("tutorial-modern.pdb")
    imap = coot.make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
    coot.set_imol_refinement_map(imap)
    if not os.path.exists("rnasa-map.map"): coot.export_map(imap, "rnasa-map.map")
if (imol, imap) != (0, 1):
    log({"ev": "fatal", "msg": "setup gave molecules %r" % ((imol, imap),)}); coot.coot_real_exit(4)

def fingerprint():
    try:
        return (coot.graphics_n_molecules(), coot.is_valid_model_molecule(0), coot.is_valid_map_molecule(1),
                coot.chain_n_residues("A", 0), coot.chain_n_residues("B", 0), repr(g["residue_info"](0, "A", 41, "")),
                round(coot.map_sigma_py(1), 4) if hasattr(coot, "map_sigma_py") else None)
    except Exception as e:
        return ("error", str(e))
fp0 = fingerprint()

def short(v, n=300):
    s = repr(v)
    return s if len(s) <= n else s[:n] + " ..."

def run_scheme(text):
    lit = '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
    r = coot.run_scheme_command("(coot0-console-eval %s)" % lit)
    if not isinstance(r, str):
        return "error", "no answer from Scheme: %r" % (r,), ""
    parts = r.split("\x1f")
    if len(parts) < 3: return "error", r, ""
    return ("ok" if parts[1] == "ok" else "error"), parts[2], parts[0]

SKIP_WORDS = ("exit", "quit", "fetch", "network", "curl", "url", "ebi", "pdbe", "pdb_redo", "download", "socket", "listener",
              "sleep", "gtk_main", "wait_for", "_hole", "pisa", "probe", "reduce", "molprobity", "mogul", "refmac", "shelx",
              "acedrg", "pyrogen", "prodrg", "kleywegt", "external", "browser", "ccp4i", "ccp4mg", "raster3d", "povray",
              "render", "screendump", "png", "make_image", "lsq_improve", "clustalw", "align_and_mutate", "run_", "remote")
def skip_reason(e):
    k = e["key"].lower()
    if e.get("gui_internal"): return "used by Coot's own windows (takes a widget or pointer)"
    for w in SKIP_WORDS:
        if w in k: return "not run automatically (%s: exits, uses the network, an external program, files or a screen)" % w.strip("_")
    return None

count = 0
for e in entries:
    if ONLY and ONLY not in e["key"]: continue
    for lang, ex in (("py", e.get("py_ex")), ("scm", e.get("scm_ex"))):
        if not (e["py"] if lang == "py" else e["scm"]): continue
        if (e["key"], lang) in done: continue
        why = skip_reason(e) if ex else "no automatic example (it takes a list, a widget or an object)"
        if why:
            log({"ev": "end", "key": e["key"], "lang": lang, "status": "skipped", "why": why}); continue
        log({"ev": "start", "key": e["key"], "lang": lang, "ex": ex})
        t0 = time.time(); out = io.StringIO()
        try:
            with contextlib.redirect_stdout(out):
                if lang == "py":
                    v = eval(ex, g); st, val = "ok", short(v)
                else:
                    st, val, sout = run_scheme(ex); out.write(sout)
        except Exception as x:
            st, val = "error", "%s: %s" % (type(x).__name__, str(x)[:300])
        try:
            with contextlib.redirect_stdout(io.StringIO()): coot.clear_up_moving_atoms()
        except Exception: pass
        log({"ev": "end", "key": e["key"], "lang": lang, "status": st, "value": val, "secs": round(time.time() - t0, 2),
             "printed": out.getvalue()[-300:]})
        count += 1
        if fingerprint() != fp0:
            log({"ev": "restart", "key": e["key"], "lang": lang}); f.close(); os._exit(3)
log({"ev": "done", "n": count})
f.close()
coot.coot_real_exit(0)
