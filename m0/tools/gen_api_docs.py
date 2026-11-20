#!/usr/bin/env python3
"""gen_api_docs.py INDEX.json RESULTS.jsonl OUTDIR  (build 26; build 30: Python/Scheme agreement)

Writes the scripting reference (Markdown) from the function index (gen_api_index.py) and the results of trying
every example (tests/run-api-examples.sh):
  OUTDIR/README.md            how to read it, counts, list of sections
  OUTDIR/sections/<slug>.md   one page per section of Coot's headers, every function with both examples + result
  OUTDIR/A-Z.md               all functions alphabetically (Python and Scheme names), with links
  OUTDIR/one-language-only.md functions that exist only in Python or only in Scheme
  OUTDIR/api-index.json       the index (used by the test)
"""
import json, os, re, sys, shutil, collections

IDX, RES, OUT = sys.argv[1:4]
VERSION = sys.argv[4] if len(sys.argv) > 4 else ""
entries = json.load(open(IDX))
res = {}
for l in open(RES):
    try: d = json.loads(l)
    except Exception: continue
    if d.get("ev") == "end": res[(d["key"], d["lang"])] = d

os.makedirs(os.path.join(OUT, "sections"), exist_ok=True)
for f in os.listdir(os.path.join(OUT, "sections")):
    if f.endswith(".md"): os.remove(os.path.join(OUT, "sections", f))
if os.path.abspath(IDX) != os.path.abspath(os.path.join(OUT, "api-index.json")): shutil.copy(IDX, os.path.join(OUT, "api-index.json"))

def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "other"

def kind(t):
    t = (t or "").replace("const", "").replace("&", "").strip()
    if t in ("void", ""): return "nothing"
    if t in ("int", "short int", "short", "unsigned int", "long", "unsigned short int", "unsigned long", "short unsigned int", "size_t", "unsigned short"): return "a whole number"
    if t in ("float", "double"): return "a number"
    if t == "bool": return "true or false"
    if "char" in t or "string" in t and "vector" not in t: return "text"
    if t in ("PyObject *", "PyObject*", "SCM"): return "a value (see the result of the example)"
    if t.startswith("std::vector") or t.startswith("std::pair"): return "a list"
    return "`%s`" % t

def argdesc(args, scheme=False):
    out = []
    for t, n in args:
        nm = n.replace("_", "-") if scheme else n
        k = kind(t)
        if k == "a value (see the result of the example)": k = "a list or value"
        out.append("%s (%s)" % (nm or "?", k))
    return ", ".join(out) if out else "none"

def cell(s, n=160):
    s = (s or "").replace("\n", " ").replace("|", "\\|").strip()
    if len(s) > n: s = s[:n] + " ..."
    return s

STATUS = {"ok": "ran", "error": "error", "crash": "stopped Coot (no window)", "hung": "no answer within 60 s", "skipped": "not run"}
def scrub(v):
    """No machine paths in the published pages: the package folder becomes <coot0>, other absolute paths <folder>."""
    v = re.sub(r"(/private)?/(tmp|var|Users)/[^'\"\s]*?/(bundle|coot0-[0-9][^/'\"\s]*|Coot-0\.9\.8\.96-arm64)/", "<coot0>/", v)
    v = re.sub(r"(/private)?/(tmp|var|Users)/[^'\"\s]*/", "<folder>/", v)
    return v

def result_cell(key, lang):
    r = res.get((key, lang))
    if r:
        r = dict(r); r["value"] = scrub(r.get("value", "") or ""); r["why"] = scrub(r.get("why", "") or "")
    if not r: return "not tried"
    st = r["status"]
    if st == "ok":
        v = r.get("value", "")
        if v in ("", "None"): return "ran (no return value)"
        return "ran, returned `%s`" % cell(v, 120).replace("`", "'")
    if st == "error":
        return "error: %s" % cell(r.get("value", ""), 140).replace("`", "'")
    if st == "crash":
        return "stopped Coot when tried without a window (not checked with a window)"
    if st == "hung":
        return "no answer within 60 s (slow, or waits for something)"
    return "not run: %s" % cell(r.get("why", ""), 120)

# ---- build 30: do Python and Scheme give the same answer?  Python's repr and Scheme's printed value are brought
# to one form (lists as ( ), True/#t, None/False/#f, numbers to 3 decimals) and compared.
def _num(s):
    if s in ("+nan.0", "-nan.0", "nan"): return "nan"
    try: x = float(s)
    except ValueError: return s
    if x != x: return "nan"
    if x == int(x) and abs(x) < 1e15 and not re.search(r"[.eE]", s): return str(int(x))
    return ("%.3f" % x).rstrip("0").rstrip(".").replace("-0", "0") if abs(x) < 1e12 else "%.3g" % x
TOK = re.compile(r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'|[()\[\]#]|[^\s()\[\],#]+')
def canon(v, lang):
    v = (v or "").strip()
    if lang == "scm" and v.startswith("#("): v = v[1:]                 # a Scheme vector prints as #( )
    out = []
    for m in TOK.finditer(v):
        s = m.group(0)
        if s[0] in "\"'":
            body = s[1:-1]
            if s[0] == "'": body = body.replace('\\\'', "'").replace('"', '\\"')
            out.append('"' + body + '"'); continue
        if s in "([": out.append("("); continue
        if s in ")]": out.append(")"); continue
        if s == "#": out.append("#"); continue
        if lang == "py":
            s = {"True": "#t", "False": "#f", "None": "#f"}.get(s, s)
        out.append(_num(s))
    t = " ".join(out).replace("# t", "#t").replace("# f", "#f").replace("( ", "(").replace(" )", ")")
    return t
def agreement(key):
    """'same' | 'different' | None (not both ran with a value)"""
    a, b = res.get((key, "py")), res.get((key, "scm"))
    if not (a and b and a["status"] == "ok" and b["status"] == "ok"): return None
    va, vb = a.get("value", "") or "", b.get("value", "") or ""
    if va in ("", "None") and vb in ("", "#<unspecified>"): return None   # nothing returned in either
    if "<" in va or "#<" in vb: return None                              # objects/pointers: not comparable
    ca, cb = canon(va, "py"), canon(vb, "scm")
    if va.endswith(" ...") or vb.endswith(" ..."):                       # cut at 300 characters: compare what is there
        n = min(len(ca), len(cb)) - 12
        return "same" if n > 20 and ca[:n] == cb[:n] else "different"
    return "same" if ca == cb else "different"

def clean_doc(d):
    d = re.sub(r"\\(param|p|c|b|e)\s+", "", d or "")
    d = d.replace("@return", "Returns").replace("\\return", "Returns").replace("\\note", "Note:")
    d = re.sub(r"[ \t]+", " ", d)
    d = re.sub(r"\n\s*\n+", "\n\n", d).strip()
    return d

secs = collections.OrderedDict()
for e in sorted(entries, key=lambda e: (e["section"].lower(), e["key"])):
    secs.setdefault(e["section"], []).append(e)

# counts
tot = collections.Counter()
for (k, lang), r in res.items(): tot[r["status"]] += 1

def fn_md(e):
    L = []
    L.append("### %s" % (e["py"] or e["scm"]))
    L.append("")
    names = []
    if e["py"]:
        names.append("Python: `%s(%s)`" % (e["py"], ", ".join(n for t, n in e.get("py_args", e["args"]))))
    if e["scm"]:
        names.append("Scheme: `(%s%s)`" % (e["scm"], "".join(" " + n.replace("_", "-") for t, n in e.get("scm_args", e["args"]))))
    L.append("  \n".join(names))
    L.append("")
    doc = clean_doc(e["doc"])
    if doc: L.append(doc); L.append("")
    if e["py"]:
        L.append("Arguments: %s. Returns: %s." % (argdesc(e.get("py_args", e["args"])), kind(e.get("py_ret", e["ret"]))))
    elif e["scm"]:
        L.append("Arguments: %s. Returns: %s." % (argdesc(e.get("scm_args", e["args"]), True), kind(e.get("scm_ret", e["ret"]))))
    al = list(e.get("py_alias") or [])
    if al: L.append("Also available in Python as `%s`." % "`, `".join(al))
    if e.get("scm_alias"): L.append("Also available in Scheme as `%s`." % "`, `".join(e["scm_alias"]))
    if not e["py"]: L.append("**Scheme only** (see [one-language-only](../one-language-only.md)).")
    if not e["scm"]: L.append("**Python only** (see [one-language-only](../one-language-only.md)).")
    L.append("")
    L.append("| | Example | When tried (test data, no window) |")
    L.append("|---|---|---|")
    if e["py"]:
        L.append("| Python | %s | %s |" % ("`%s`" % cell(e["py_ex"], 200) if e.get("py_ex") else "(no automatic example)", result_cell(e["key"], "py")))
    if e["scm"]:
        L.append("| Scheme | %s | %s |" % ("`%s`" % cell(e["scm_ex"], 200) if e.get("scm_ex") else "(no automatic example)", result_cell(e["key"], "scm")))
    ag = agreement(e["key"])
    if ag == "same": L.append(""); L.append("Python and Scheme gave the same answer.")
    elif ag == "different": L.append(""); L.append("Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).")
    L.append("")
    return "\n".join(L)

anchors = {}
for sec, es in secs.items():
    s = slug(sec)
    L = ["# %s" % sec, "", "[Scripting reference](../README.md) > %s (%d functions)" % (sec, len(es)), "",
         "Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from "
         "`rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).", ""]
    for e in es:
        L.append(fn_md(e))
        anchors[e["key"]] = "sections/%s.md#%s" % (s, re.sub(r"[^a-z0-9_-]", "", (e["py"] or e["scm"]).lower()))
    open(os.path.join(OUT, "sections", s + ".md"), "w").write("\n".join(L) + "\n")

# A-Z
L = ["# All functions, A to Z", "", "[Scripting reference](README.md) > A-Z. Python name, Scheme name, section.", "",
     "| Python | Scheme | Section |", "|---|---|---|"]
for e in sorted(entries, key=lambda e: (e["py"] or e["scm"]).lower()):
    L.append("| %s | %s | [%s](%s) |" % ("`%s`" % e["py"] if e["py"] else "-", "`%s`" % e["scm"] if e["scm"] else "-", e["section"], anchors[e["key"]]))
open(os.path.join(OUT, "A-Z.md"), "w").write("\n".join(L) + "\n")

# one language only
COUNTERPART = {
    "atom-spec-from-scm-expression": "atom_spec_from_python_expression", "scm-to-residue-specs": "py_to_residue_specs",
    "rtop-to-scm": "rtop_to_python", "scm-symop-strings-to-space-group": "py_symop_strings_to_space_group",
    "residue-records-list-scm-to-residue-specs": "residue_records_list_py_to_residue_specs",
    "get-input-model-was-cif-state-scm": "get_input_molecule_was_in_mmcif_state", "run-python-command": "run_scheme_command",
    "coot-has-python-p": "coot_has_guile", "try-load-scheme-extras-dir": "try_load_python_extras_dir",
    "safe-scheme-command-test": "safe_python_command_test", "map-to-model-correlation-stats-per-residue-scm": "map_to_model_correlation_stats_per_residue_range_py",
    "set-temperature-factors-for-atoms-in-residue-scm": "set_b_factor_residues", "test-mol-triangles-scm": "",
}
so = [e for e in entries if e["scm"] and not e["py"]]
po = [e for e in entries if e["py"] and not e["scm"]]
L = ["# Functions in only one language", "",
     "Almost every scripting function of Coot exists in both Python and Scheme, with the same name "
     "(Python `residue_name`, Scheme `residue-name`). These %d exist only in Scheme and these %d only in Python. "
     "Most of them convert values between the language and Coot (for example a Scheme list into a residue "
     "specification) and have a counterpart with a different name in the other language; the table says which." % (len(so), len(po)), "",
     "From Scheme you can call any Python-only function with `run-python-command`, for example "
     "`(run-python-command \"all_molecule_ramachandran_region(0)\")`; from Python any Scheme-only function with "
     "`run_scheme_command`, for example `run_scheme_command('(spherical-density-overlap 0 1)')` (cookbook 7.7).", "",
     "## Only in Scheme", "", "| Scheme | Counterpart in Python | What it does |", "|---|---|---|"]
for e in sorted(so, key=lambda e: e["scm"]):
    cp = COUNTERPART.get(e["scm"], "")
    L.append("| [`%s`](%s) | %s | %s |" % (e["scm"], anchors[e["key"]], "`%s`" % cp if cp else "none", cell(clean_doc(e["doc"]).split("\n")[0], 150) or "(no description in Coot's headers)"))
rev = {v: k for k, v in COUNTERPART.items() if v}
L += ["", "## Only in Python", "", "| Python | Counterpart in Scheme | What it does |", "|---|---|---|"]
for e in sorted(po, key=lambda e: e["py"]):
    cp = rev.get(e["py"], "")
    L.append("| [`%s`](%s) | %s | %s |" % (e["py"], anchors[e["key"]], "`%s`" % cp if cp else "none", cell(clean_doc(e["doc"]).split("\n")[0], 150) or "(no description in Coot's headers)"))
L += ["", "## The script layers", "",
      "On top of these built-in functions, Coot loads helper functions written in Python (`share/coot/python/coot_utils.py`, "
      "`coot_gui.py`, ...) and in Scheme (`share/coot/scheme/coot-utils.scm`, ...), for example `chain_ids`, `all_residues`, "
      "`residues_near_residue`. Most exist in both languages. The menus, windows and toolbar of coot0 are made by the Python "
      "layer only (`coot_menubar_menu`, `coot_toolbar_button`, ...): from Scheme use them through `run-python-script` "
      "(cookbook 6.1 and 6.2)."]
open(os.path.join(OUT, "one-language-only.md"), "w").write("\n".join(L) + "\n")

# README
n_py = sum(1 for e in entries if e["py"]); n_scm = sum(1 for e in entries if e["scm"])
py_ok = sum(1 for (k, l), r in res.items() if l == "py" and r["status"] == "ok")
scm_ok = sum(1 for (k, l), r in res.items() if l == "scm" and r["status"] == "ok")
L = ["# Coot scripting reference (coot0%s)" % (" " + VERSION if VERSION else ""), "",
     "Every function that Coot 0.9.8.96 offers to Python and Scheme scripts: %d functions, %d in Python and %d in Scheme. "
     "For each one: its Python and Scheme names, what Coot's own source says about it, a concrete example on the "
     "test data, and what happened when the example was tried." % (len(entries), n_py, n_scm), "",
     "For recipes that do whole tasks (refine, edit, customize the toolbar, batch scripts...), see the "
     "[cookbook](../cookbook/README.md).", "",
     "## How to read it", "",
     "- **Names.** Python uses `_`, Scheme uses `-`: Python `residue_name(0, \"A\", 41, \"\")` is Scheme "
     "`(residue-name 0 \"A\" 41 \"\")`.",
     "- **Examples** use the test data in the package (`test-data/`): molecule **0** is `tutorial-modern.pdb` "
     "(chains A and B, residues 1-93 and 1-96; residue A41 is a glutamate), molecule **1** is the 2Fo-Fc map made from "
     "`rnasa-1.8-all_refmac1.mtz` (`make_and_draw_map(\"rnasa-1.8-all_refmac1.mtz\", \"FWT\", \"PHWT\", \"\", 0, 0)`). "
     "Load them in this order in a new Coot and every example runs as written. With your own data, change the "
     "molecule number, chain, residue number and file names.",
     "- **Residue specs** are lists: `[\"A\", 41, \"\"]` in Python, `(list \"A\" 41 \"\")` in Scheme (chain, "
     "residue number, insertion code). **Atom names** have 4 characters as in a PDB file: `\" CA \"`.",
     "- **The examples were made by a program** from the argument names (a chain gets `\"A\"`, a residue number 41, "
     "a flag 1, ...). For most functions that gives a sensible call; for some the values are only placeholders "
     "(`\"hello\"` for a text, 1 for a number) that you should replace.",
     "- **\"When tried\"** is what happened when the example was run on the test data by `tests/run-api-examples.sh`, "
     "without a window: *ran* (with the value it returned), *error* (with Coot's message; usually the example "
     "needs other values), *stopped Coot (no window)* (the function needs the graphics window; it was not checked "
     "with one), *not run* (it would quit Coot, use the network, run an external program, or needs a widget). "
     "*Ran* means that Coot accepted the call; the value itself was checked only by comparing the two languages "
     "(next section) and, for the functions the cookbook uses, by the cookbook's own checks.", "",
     "## Results of trying the examples", "",
     "| | Ran | Error | Stopped Coot (no window) | No answer in 60 s | Not run |", "|---|---|---|---|---|---|"]
for lang, nm in (("py", "Python"), ("scm", "Scheme")):
    c = collections.Counter(r["status"] for (k, l), r in res.items() if l == lang)
    L.append("| %s | %d | %d | %d | %d | %d |" % (nm, c["ok"], c["error"], c["crash"], c["hung"], c["skipped"]))
ags = collections.Counter(agreement(e["key"]) for e in entries if e["py"] and e["scm"])
L += ["", "Where both languages ran and returned a value that can be compared (%d functions), Python and Scheme gave the "
      "same answer for %d. The other %d are listed on their pages as *different answers*; mostly that is because the "
      "Python example ran first and changed the data (a counter, a new molecule, a restraint added), or because one "
      "language returns the same information in another shape. Values that are objects (pointers) are not compared."
      % (ags["same"] + ags["different"], ags["same"], ags["different"])]
L += ["", "## Sections", "", "Coot's own section names, in alphabetical order. Also: [all functions A-Z](A-Z.md), "
      "[functions in only one language](one-language-only.md).", "", "| Section | Functions |", "|---|---|"]
for sec, es in secs.items():
    L.append("| [%s](sections/%s.md) | %d |" % (sec, slug(sec), len(es)))
L += ["", "## How this reference is made", "",
      "`m0/tools/gen_api_index.py` reads Coot's SWIG wrappers (the functions really available) and its headers "
      "(signatures and descriptions); `tests/run-api-examples.sh` tries every example in Python and Scheme; "
      "`m0/tools/gen_api_docs.py` writes these pages. To check your own installation run "
      "`tests/run-api-examples.sh` (30-90 minutes)."]
open(os.path.join(OUT, "README.md"), "w").write("\n".join(L) + "\n")
print("sections", len(secs), "functions", len(entries), "results", len(res), dict(tot))
