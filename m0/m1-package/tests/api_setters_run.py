# api_setters_run.py  (build 31) -- runs inside Coot, driven by tests/run-api-examples.sh (API_SCRIPT=this file).
# For every set_X function that has a getter (X, get_X, X_state, ...): read the value, set a DIFFERENT value, read it
# back, put the old value back.  In Python and in Scheme.  One JSON line per check in $API_RESULTS:
#   {"ev": "end", "key": "set_X", "lang": "py", "status": "ok", "check": "setter", "getter": "X_state", "before": 1,
#    "set": 0, "after": 0, "verdict": "read back" | "not read back" | "not checked: <why>"}
# Molecule 0 = tutorial-modern.pdb, molecule 1 = the rnasa map, as in the examples.
import os, sys, json, io, contextlib
import coot
g = globals()
IDX = os.environ["API_INDEX"]; RES = os.environ["API_RESULTS"]
f = open(RES, "a")
def log(d): f.write(json.dumps(d) + "\n"); f.flush(); os.fsync(f.fileno())
done = set()
for l in open(RES):
    try: d = json.loads(l)
    except Exception: continue
    if d.get("ev") == "end": done.add((d["key"], d["lang"]))
with contextlib.redirect_stdout(io.StringIO()):
    imol = coot.read_pdb("tutorial-modern.pdb")
    imap = coot.make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
    coot.set_imol_refinement_map(imap)
if (imol, imap) != (0, 1):
    log({"ev": "fatal", "msg": "setup gave %r" % ((imol, imap),)}); coot.coot_real_exit(4)

entries = json.load(open(IDX)); E = {e["key"]: e for e in entries}
INT = ("int", "short int", "short", "unsigned int", "bool", "long")
FLT = ("float", "double")
def base(t): return t.replace("const", "").strip()

def plan(e):
    """(getter entry, setter takes imol?, value type) or a reason"""
    k = e["key"]; b = k[4:]
    for c in (b, "get_" + b, b + "_state", "get_" + b + "_state", b + "_p", b.replace("_state", ""), "get_" + b.replace("_state", ""),
              b + "_flag", "get_" + b + "_flag"):
        gt = E.get(c)
        if not gt or c == k: continue
        sa = e.get("py_args") or e.get("args") or []; ga = gt.get("py_args") or gt.get("args") or []
        if len(sa) == 1 and not ga and base(sa[0][0]) in INT + FLT: return gt, False, base(sa[0][0])
        if (len(sa) == 2 and len(ga) == 1 and base(sa[0][0]) == "int" and "mol" in sa[0][1] and base(ga[0][0]) == "int"
                and base(sa[1][0]) in INT + FLT): return gt, True, base(sa[1][0])
    return None

def other(v, t):
    if t in FLT: return round(float(v) * 1.5 + 0.5, 3) if isinstance(v, (int, float)) else 2.5
    if t == "bool": return not v if isinstance(v, bool) else (0 if v else 1)
    return 0 if v else 1

def num_eq(a, b):
    try: return abs(float(a) - float(b)) < 1e-3 * max(1.0, abs(float(b)))
    except Exception: return a == b

def scm(text):
    lit = '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
    r = coot.run_scheme_command("(coot0-console-eval %s)" % lit)
    p = r.split("\x1f") if isinstance(r, str) else []
    if len(p) < 3 or p[1] != "ok": raise RuntimeError(p[2] if len(p) > 2 else repr(r))
    v = p[2].strip()
    if v in ("#t", "#f"): return v == "#t"
    try: return int(v)
    except ValueError:
        try: return float(v)
        except ValueError: return v

def lit_scm(v): return ("#t" if v else "#f") if isinstance(v, bool) else repr(v)

for e in entries:
    if not e["key"].startswith("set_") or e.get("gui_internal") or e.get("skip"): continue
    p = plan(e)
    if not p: continue
    gt, with_imol, t = p
    for lang in ("py", "scm"):
        if (e["key"], lang) in done or not e[lang] or not gt[lang]: continue
        log({"ev": "start", "key": e["key"], "lang": lang, "check": "setter"})
        rec = {"ev": "end", "key": e["key"], "lang": lang, "status": "ok", "check": "setter", "getter": gt[lang]}
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                im = [imap if "map" in e["key"] or "contour" in e["key"] else imol] if with_imol else []
                if lang == "py":
                    get = lambda: g[gt["py"]](*im); sset = lambda v: g[e["py"]](*(im + [v]))
                else:
                    get = lambda: scm("(%s%s)" % (gt["scm"], "".join(" %d" % i for i in im)))
                    sset = lambda v: scm("(%s%s %s)" % (e["scm"], "".join(" %d" % i for i in im), lit_scm(v)))
                v0 = get()
                if not isinstance(v0, (int, float, bool)):
                    rec.update(verdict="not checked: the getter returned %r" % (v0,)); raise StopIteration
                v1 = other(v0, t)
                if t == "bool" and lang == "py": v1 = bool(v1)
                sset(v1); after = get(); sset(v0); back = get()
                rec.update(before=v0, set=v1, after=after, restored=back,
                           verdict="read back" if num_eq(after, v1) else "not read back")
        except StopIteration: pass
        except Exception as x:
            rec.update(status="error", verdict="error: %s" % str(x)[:200])
        log(rec)
log({"ev": "done"})
f.close()
coot.coot_real_exit(0)
