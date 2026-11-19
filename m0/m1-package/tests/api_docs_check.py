# api_docs_check.py  (build 26) -- quick check that docs/api matches this Coot: every Python name in the reference
# is callable here, every Scheme name is defined, every example parses.  (The slow check that RUNS every example is
# tests/run-api-examples.sh.)
import os, sys, json, ast
import coot
here = os.environ["COOT_PREFIX"]
res = []
def check(name, fn):
    try:
        v = fn(); ok = v is True
        res.append((name, ok, "" if ok else repr(v)[:300]))
    except Exception as e:
        res.append((name, False, "EXC %r" % e))

idx = json.load(open(os.path.join(here, "docs", "api", "api-index.json")))
g = globals()
def py_names():
    missing = [e["py"] for e in idx if e["py"] and not callable(g.get(e["py"], getattr(coot, e["py"], None)))]
    return True if not missing else "%d missing: %s" % (len(missing), missing[:10])
def scm_names():
    names = [e["scm"] for e in idx if e["scm"]]
    lst = "(list %s)" % " ".join("'" + n for n in names)
    r = coot.run_scheme_command("(let loop ((l %s) (acc '())) (if (null? l) (reverse acc) (loop (cdr l) (if (defined? (car l)) acc (cons (symbol->string (car l)) acc)))))" % lst)
    if r is False or r is None: return "Scheme gave no answer"
    return True if not r else "%d missing: %s" % (len(r), r[:10])
def py_examples_parse():
    bad = []
    for e in idx:
        if e.get("py_ex"):
            try: ast.parse(e["py_ex"], mode="eval")
            except SyntaxError: bad.append(e["py_ex"])
    return True if not bad else bad[:5]
def counts():
    n = len(idx); npy = sum(1 for e in idx if e["py"]); nscm = sum(1 for e in idx if e["scm"])
    return True if n > 1600 and npy > 1600 and nscm > 1600 else (n, npy, nscm)
def pages():
    secs = os.listdir(os.path.join(here, "docs", "api", "sections"))
    need = ["README.md", "A-Z.md", "one-language-only.md"]
    miss = [f for f in need if not os.path.exists(os.path.join(here, "docs", "api", f))]
    return True if len(secs) > 100 and not miss else (len(secs), miss)
check("docs/api: more than 1600 functions in each language", counts)
check("docs/api: README, A-Z, one-language-only and the section pages are there", pages)
check("docs/api: every Python name in the reference exists in this Coot", py_names)
check("docs/api: every Scheme name in the reference exists in this Coot", scm_names)
check("docs/api: every Python example is valid Python", py_examples_parse)
for name, ok, why in res:
    print("%s %-90s %s" % ("PASS" if ok else "FAIL", name, why))
print("SUMMARY %d / %d" % (sum(1 for r in res if r[1]), len(res)))
coot.coot_real_exit(0)
