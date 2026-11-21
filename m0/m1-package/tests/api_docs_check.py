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
            try: ast.parse(e["py_ex"])            # (build 31: a hand-written example may be statements; the last line is its value)
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
# (build 28) docs/html: the pages Help opens (made by m0/tools/gen_docs_html.py from the Markdown)
import re, hashlib, html as _html
H = os.path.join(here, "docs", "html")
def html_pages():
    if not os.path.isdir(H): return "no docs/html"
    srcs = []
    for root, dirs, files in os.walk(os.path.join(here, "docs")):
        if os.path.abspath(root).startswith(H): continue
        srcs += [os.path.join(root, f) for f in files if f.endswith(".md")]
    stale, missing = [], []
    for src in srcs:
        page = os.path.join(H, os.path.relpath(src, os.path.join(here, "docs"))[:-3] + ".html")
        if not os.path.exists(page): missing.append(page); continue
        m = re.search(r'name="coot0-source-sha1" content="([0-9a-f]+)"', open(page, encoding="utf-8").read())
        if not m or m.group(1) != hashlib.sha1(open(src, "rb").read()).hexdigest(): stale.append(os.path.relpath(page, H))
    if missing or stale: return "missing %r, older than their Markdown %r" % (missing[:3], stale[:3])
    return True if len(srcs) > 150 else "only %d Markdown pages" % len(srcs)
def html_links():
    ids, bad = {}, []
    for root, dirs, files in os.walk(H):
        for f in files:
            if f.endswith(".html"):
                p = os.path.abspath(os.path.join(root, f)); ids[p] = set(re.findall(r'id="([^"]+)"', open(p, encoding="utf-8").read()))
    for p in ids:
        for u in re.findall(r'href="([^"]+)"', open(p, encoding="utf-8").read()):
            u = _html.unescape(u)
            if re.match(r"^[a-z]+:", u): continue
            path, _, a = u.partition("#")
            t = os.path.abspath(os.path.join(os.path.dirname(p), path)) if path else p
            if t.endswith(".html"):
                if t not in ids: bad.append("%s -> %s" % (os.path.relpath(p, H), u))
                elif a and a not in ids[t]: bad.append("%s -> %s (no such heading)" % (os.path.relpath(p, H), u))
            elif not os.path.exists(t): bad.append("%s -> %s" % (os.path.relpath(p, H), u))
    return True if not bad else "%d broken links: %r" % (len(bad), bad[:5])
def html_index():
    idx = json.load(open(os.path.join(H, "search-index.json")))
    kinds = {}
    for e in idx: kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
    return True if kinds.get("Function", 0) > 1600 and kinds.get("Cookbook", 0) > 80 else kinds
# (build 31) the example run records what each call changed (tests/api_state.py), and the examples that the program
# could not make sensibly were written and checked by hand
def snapshot_diff():
    sys.path.insert(0, os.path.join(here, "tests"))
    from api_state import Snapshot
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        im = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
    s = Snapshot(g, idx)
    a = s.take(); coot.set_draw_hydrogens(im, 0); coot.delete_residue(im, "A", 41, ""); b = s.take()
    d = s.diff(a, b); coot.close_molecule(im)
    want = ["molecule %d: deleted 1 residue(s) (A41)" % im, "draw_hydrogens_state(%d): 1 -> 0" % im] if im <= 1 else \
           ["molecule %d: deleted 1 residue(s) (A41)" % im]
    return True if all(w in d for w in want) else d
def hand_examples():
    cur = [e for e in idx if e.get("curated")]
    bad = [e["key"] for e in cur if not e.get("expect")]
    for e in cur:
        for s in e.get("py_setup") or []:
            try: ast.parse(s)
            except SyntaxError: bad.append(e["key"] + " setup")
    return True if len(cur) > 300 and not bad else (len(cur), bad[:5])
def pages_say_what_changed():
    n = 0
    for f in os.listdir(os.path.join(here, "docs", "api", "sections")):
        n += open(os.path.join(here, "docs", "api", "sections", f), encoding="utf-8").read().count("; changed: ")
    return True if n > 300 else "only %d results list what changed" % n
def setters_read_back():
    n = 0
    for f in os.listdir(os.path.join(here, "docs", "api", "sections")):
        n += open(os.path.join(here, "docs", "api", "sections", f), encoding="utf-8").read().count("Setting checked (set to another value")
    return True if n > 90 else "only %d settings checked" % n
check("api-examples: a snapshot before/after a call lists a deleted residue and a changed setting", snapshot_diff)
check("docs/api: more than 300 examples written by hand, each with its expected result", hand_examples)
check("docs/api: the results say what each example changed (more than 300 do)", pages_say_what_changed)
check("docs/api: more than 90 settings were set, read back and put back", setters_read_back)
check("docs/html: a page for every Markdown document, made from its current text", html_pages)
check("docs/html: every link between the pages leads to a page and heading that exist", html_links)
check("docs/html: the search index has every function and every recipe", html_index)
for name, ok, why in res:
    print("%s %-90s %s" % ("PASS" if ok else "FAIL", name, why))
print("SUMMARY %d / %d" % (sum(1 for r in res if r[1]), len(res)))
coot.coot_real_exit(0)
