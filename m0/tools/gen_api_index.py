#!/usr/bin/env python3
"""gen_api_index.py SRC OUT.json  (build 26; build 30: Python bool arguments as True/False)

Builds the index of every function that Coot 0.9.8.96 exposes to Python and Scheme through SWIG:
  - Python names from src/coot_wrap_python.cc (+ the short aliases in python/redefine_functions.py),
  - Scheme names from src/coot_wrap_guile_pre.cc,
  - signature, section and doxygen text from the headers that src/coot.i includes.
Each entry gets a concrete example (arguments filled in from the test data: molecule 0 = tutorial-modern.pdb,
molecule 1 = the map from rnasa-1.8-all_refmac1.mtz, chain "A", residue 41, ...) in both languages.
The examples are run by tests/api_examples_run.py; gen_api_docs.py turns index + run results into Markdown.
"""
import json, os, re, sys

SRC = sys.argv[1]; OUT = sys.argv[2]
S = lambda *p: os.path.join(SRC, *p)

def wrapped(path, pat):
    txt = open(path, encoding="utf-8", errors="replace").read()
    return txt, re.findall(pat, txt)

pytxt, py = wrapped(S("src", "coot_wrap_python.cc"), r'\{ "(\w+)", (?:\(PyCFunction\))?_wrap_(\w+)')
scmtxt, scm = wrapped(S("src", "coot_wrap_guile_pre.cc"), r'scm_c_define_gsubr\("([^"]+)", (\d+), (\d+), (\d+), \(swig_guile_proc\) _wrap_(\w+)\)')

# SWIG classes (constructors/destructors/members are not functions for users)
classes = set(re.findall(r'"new_(\w+)"', pytxt)) | set(c.replace("-", "_") for c in re.findall(r'"new-([\w-]+)"', scmtxt))
def is_member(cname):
    m = re.match(r"(new|delete)_(\w+)$", cname)
    if (m and m.group(2) in classes) or cname.endswith(("_swigregister", "_swiginit")) or cname.startswith("SWIG_"):
        return True
    return any(cname.startswith(c + "_") for c in classes)

def key_of(cname):
    for suf in ("_py", "_scm"):
        if cname.endswith(suf): return cname[: -len(suf)]
    return cname

aliases = {}   # C name (xxx_py) -> short alias(es)
for line in open(S("python", "redefine_functions.py"), encoding="utf-8"):
    m = re.match(r"\s*(\w+)\s*=\s*(\w+)\s*(#.*)?$", line)
    if m: aliases.setdefault(m.group(2), []).append(m.group(1))

E = {}
def ent(k):
    return E.setdefault(k, {"key": k, "py": None, "py_c": None, "py_alias": [], "scm": None, "scm_c": None, "scm_nargs": None})
for pyname, cname in py:
    if is_member(cname) or cname.startswith(("SwigPyIterator", "delete_SwigPyIterator")): continue
    e = ent(key_of(cname))
    if e["py_c"] and e["py_c"] == e["key"]: continue      # the plain C name wins over xxx_py
    e["py_c"] = cname
    al = [a for a in aliases.get(cname, [])]
    e["py"] = al[0] if al else pyname
    e["py_alias"] = [a for a in al[1:]] + ([pyname] if al else [])
CONSTANTS = []
for sname, nreq, nopt, rest, cname in scm:
    if cname.endswith("_rest"): cname = cname[:-5]          # SWIG Guile wrapper for many-argument functions
    if is_member(cname): continue
    if sname.upper() == sname and re.search(r"[A-Z]", sname): CONSTANTS.append(sname); continue   # #define constants
    e = ent(key_of(cname))
    if e["scm_c"] and e["scm_c"] == e["key"]: continue    # the plain name wins over xxx-scm
    e["scm"] = sname; e["scm_c"] = cname; e["scm_nargs"] = (int(nreq), int(nopt))

# ---- headers: declaration, doxygen text, section
inc = re.findall(r'^%include "([^"]+\.h+)"', open(S("src", "coot.i")).read(), re.M)
decl_re = re.compile(r'(?:^|\n)[ \t]*((?:const\s+)?[\w:<>,\s\*&]+?[\s\*&])(\w+)\s*\(([^;{}()]*(?:\([^()]*\)[^;{}()]*)*)\)\s*(?:const\s*)?;')
info = {}
for h in inc:
    p = S("src", h)
    if not os.path.exists(p): continue
    txt = open(p, encoding="utf-8", errors="replace").read()
    # positions of section names
    secs = [(m.start(), re.sub(r"\s+", " ", m.group(1)).strip()) for m in re.finditer(r'\\name\s+([^*\n]+)', txt)]
    for m in decl_re.finditer(txt):
        ret, name, args = m.group(1), m.group(2), m.group(3)
        if name in ("if", "while", "for", "return", "switch"): continue
        ret = re.sub(r"\s+", " ", ret).strip()
        if ret.startswith(("return", "else", "#")) or "=" in ret: continue
        start = m.start(1)
        # comment directly above (allow blank lines / #ifdef lines in between)
        before = txt[:start]
        doc = ""
        tail = before.rstrip()
        # strip trailing preprocessor lines
        lines = tail.split("\n")
        while lines and (lines[-1].strip().startswith("#") or not lines[-1].strip()):
            lines.pop()
        tail = "\n".join(lines)
        cm = re.search(r'(/\*(?:(?!\*/).)*\*/)\s*$', tail, re.S)
        if cm:
            doc = cm.group(1)
        else:
            cl = []
            for l in reversed(lines):
                if l.strip().startswith("//"): cl.insert(0, l.strip())
                else: break
            doc = "\n".join(cl)
        doc = re.sub(r"^/\*!?|\*/$", "", doc.strip()).strip()
        doc = re.sub(r"^\s*//[!/]?\s?", "", doc, flags=re.M)
        doc = re.sub(r"^\s*\*\s?", "", doc, flags=re.M)
        if re.match(r"^-{5,}|^\s*$", doc) or "\\name" in doc or doc.startswith("\\{") or doc.startswith("\\}"): doc = ""
        doc = doc.replace("\\brief", "").replace("\\return", "Returns").replace("\\p ", "").strip()
        sec = ""
        for pos, nm in secs:
            if pos < start: sec = nm
        arglist = []
        a = re.sub(r"\s+", " ", args).strip()
        if a and a != "void":
            for part in [x.strip() for x in re.split(r",(?![^<]*>)", a)]:
                part = part.split("=")[0].strip()
                mm = re.match(r"(.*?)([\w]+)$", part)
                if mm and mm.group(1).strip():
                    arglist.append([re.sub(r"\s+", " ", mm.group(1)).strip(), mm.group(2)])
                else:
                    arglist.append([part, ""])
        if name not in info or (not info[name]["doc"] and doc):
            info[name] = {"ret": ret, "args": arglist, "doc": doc, "section": sec, "header": h}

# ---- concrete example values (molecule 0 = tutorial-modern.pdb, molecule 1 = map from rnasa-1.8-all_refmac1.mtz)
def val(t, n):
    t0 = t.replace("const", "").replace("&", "").strip(); ln = n.lower()
    isstr = "string" in t0 or "char *" in t0 or t0 == "char*"
    isint = t0 in ("int", "short int", "short", "unsigned int", "long", "unsigned short int", "bool", "unsigned long", "short unsigned int", "size_t")
    isflt = t0 in ("float", "double")
    if isint:
        if "imol" in ln or ln in ("mol", "molecule", "molecule_number"):
            return 1 if "map" in ln else 0
        if ("resno" in ln or "res_no" in ln or ln.endswith("resno")) and re.search(r"(2|end|last|high|stop)", ln): return 45
        if "resno" in ln or "res_no" in ln: return 41
        if ln in ("resno", "res_no", "resno_1", "resno_start", "start_resno", "resno_low", "start_res", "res_start", "ires", "residue_number", "resno_1st", "res_no_1", "resno1", "first_res"): return 41
        if ln in ("resno_2", "resno_end", "end_resno", "resno_high", "last_res", "res_end", "stop_res", "resno2", "res_no_2", "resno_last"): return 45
        if "state" in ln or "flag" in ln or ln.startswith(("on", "i_on", "is_")) or ln in ("istate", "i", "show", "status"): return 1
        if "colour" in ln or "color" in ln: return 1
        if "width" in ln: return 2
        if "size" in ln: return 10
        if "atom_index" in ln or ln == "iat": return 0
        return 1
    if isflt:
        if ln in ("x", "xpos"): return 54.5
        if ln in ("y", "ypos"): return 9.4
        if ln in ("z", "zpos"): return 12.3
        if "radius" in ln or ln in ("r", "rad"): return 5.0 if ln != "r" else 0.5
        if ln in ("g", "b", "red", "green", "blue"): return 0.5
        if "sigma" in ln or "level" in ln or "rmsd" in ln: return 1.5
        if "weight" in ln: return 1.0
        if "occ" in ln: return 1.0
        if "b_factor" in ln or ln in ("bf", "b_fac", "bfactor"): return 20.0
        if "angle" in ln or ln in ("phi", "psi", "theta", "chi"): return 10.0
        if "resolution" in ln or "reso" in ln: return 2.0
        if "zoom" in ln: return 100.0
        if "fraction" in ln or "frac" in ln: return 0.5
        return 1.0
    if isstr:
        if "chain" in ln: return "B" if ln.endswith(("_2", "2", "_to", "_new", "new_chain_id", "to_chain")) else "A"
        if "ins" in ln: return ""
        if "alt" in ln: return ""
        if ln in ("atom_name", "atname", "atom_name_1", "at_name") or "atom_name" in ln: return " CA "
        if "mtz" in ln or "hkl" in ln: return "rnasa-1.8-all_refmac1.mtz"
        if ln in ("f_col", "fcol", "f", "col_f", "amplitudes_col", "f_label", "fobs_col") or ln.startswith("f_col"): return "FWT"
        if ln in ("phi_col", "phicol", "phi", "col_phi", "phase_col", "phases_col", "phi_label"): return "PHWT"
        if "weight" in ln or "fom" in ln: return ""
        if "map" in ln and ("file" in ln or "name" in ln): return "rnasa-map.map"
        if ("file" in ln or "filename" in ln or ln in ("pdb_name", "coords", "pdb_file", "fn")) and "dir" not in ln: return "tutorial-modern.pdb"
        if "dir" in ln: return "."
        if "res_type" in ln or "residue_type" in ln or "resname" in ln or "res_name" in ln: return "ALA"
        if ln in ("res_name", "resname", "comp_id", "tlc", "residue_type", "res_type", "monomer_type", "three_letter_code", "type", "residue_name", "new_residue_type"): return "ALA"
        if "seq" in ln: return "ACDEFGHIKLMNPQRSTVWY"
        if "selection" in ln or "atom_sel" in ln or "mmdb" in ln: return "//A/41-45"
        if ln in ("text", "s", "str", "label", "txt", "message", "msg", "title"): return "hello"
        if "name" in ln: return "my-name"
        return "hello"
    return None   # no automatic example (lists, widgets, pointers...)

HEADER_SECTION = {
    "cc-interface.hh": "General (cc-interface)", "cc-interface-scripting.hh": "Scripting", "c-interface-python.hh": "Scripting",
    "cc-interface-ncs.hh": "NCS", "cc-interface-image.hh": "Images", "c-interface-ligands-swig.hh": "Ligands",
    "c-interface-sequence.hh": "Sequence", "c-interface-database.hh": "Database (Fit Loop)", "c-interface-mogul.hh": "Mogul",
    "c-interface-refmac.h": "Execute Refmac", "c-interface-refine.h": "Regularization and Refinement", "c-interface-refine.hh": "Regularization and Refinement",
    "c-interface-generic-objects.h": "Generic Objects", "cmtz-interface.hh": "MTZ and data handling utilities", "lbg-interface.hh": "Ligand Builder (Lidia)",
    "sdf-interface.hh": "Ligands", "probe-clash-score.hh": "Validation Functions", "get-monomer.hh": "Monomer", "validation.hh": "Validation Functions",
    "cc-interface-molecular-representation.hh": "Molecular Representation", "cc-interface-user-defined-atom-colours.hh": "Colour",
    "cc-interface-alignment.hh": "Sequence", "c-interface-preferences.h": "Interface Preferences", "curlew.hh": "Curlew (extensions)",
    "globularize.hh": "Experimental", "cfc.hh": "Experimental", "../coords/phenix-geo.hh": "Validation Functions",
}
def py_lit(v): return json.dumps(v) if isinstance(v, (str, list)) else repr(v)

# ---- redefinitions in the script layers: python/redefine_functions.py (x = x_py) and scheme/*.scm (define x x-scm)
# replace the plain C function of the same name at run time, so the example must use the redefinition's arguments.
scm_alias = {}
for fn in ("redefine-functions.scm", "coot-utils.scm"):          # (the files loaded at start-up that define such names)
    if os.path.exists(S("scheme", fn)):
        for m in re.finditer(r"^\(define\s+([\w?!<>=*/+-]+)\s+([\w?!<>=*/+-]+-scm)\s*\)", open(S("scheme", fn), encoding="utf-8", errors="replace").read(), re.M):
            scm_alias[m.group(1)] = m.group(2)
scm_c_of = {sname: (cname[:-5] if cname.endswith("_rest") else cname) for sname, a, b, c, cname in scm}
py_redef = {a: c for c, al in aliases.items() for a in al}
for k, e in E.items():
    if e["py"] and e["py"] in py_redef and py_redef[e["py"]] != e["py_c"]:
        e["py_c"] = py_redef[e["py"]]; e["py_redefined"] = True
    rev = [a for a, t in scm_alias.items() if t == e["scm"]]
    if e["scm"] and e["scm"].endswith("-scm") and rev:          # the user calls the short name
        e["scm_alias"] = [e["scm"]]; e["scm"] = rev[0]
    if e["scm"] and e["scm"] in scm_alias and scm_alias[e["scm"]] in scm_c_of and scm_c_of[scm_alias[e["scm"]]] != e["scm_c"]:
        e["scm_c"] = scm_c_of[scm_alias[e["scm"]]]; e["scm_redefined"] = True

def lval(t, n):
    """examples for list arguments (PyObject * / SCM)"""
    ln = re.sub(r"_(scm|py)$", "", n.lower())
    if "atom_spec" in ln or ln in ("atom_in", "atom"): return ["A", 41, "", " CA ", ""]
    if ln in ("residue_specs", "res_specs", "residues", "r", "residue_specs_py", "residue_specs_scm", "specs", "residue_list", "res_spec_list", "residues_in"):
        return [["A", 41, ""], ["A", 42, ""]]
    if "spec" in ln or ln in ("residue_in", "res_in", "residue"): return ["A", 41, ""]
    if ln in ("add_molecules", "molecule_list", "mol_list", "imols", "molecules"): return [0]
    return None

def ex_args(cname, fallback):
    i = info.get(cname) or fallback
    vals = []
    for t, n in i.get("args", []):
        v = val(t, n)
        if v is None and ("PyObject" in t or t.strip() == "SCM"): v = lval(t, n)
        vals.append(v)
    return i, vals

def scm_lit(v):
    if isinstance(v, list): return "(list%s)" % "".join(" " + scm_lit(x) for x in v)
    return json.dumps(v) if isinstance(v, str) else repr(v)

out = []
for k, e in sorted(E.items()):
    cn = e["py_c"] or e["scm_c"]
    inf = info.get(cn) or info.get(e["py_c"] or "") or info.get(e["scm_c"] or "") or info.get(k) or {}
    plain = info.get(k) or inf          # the doc text usually sits on the plain C declaration
    doc = inf.get("doc") or plain.get("doc", "")
    sec = plain.get("section") or inf.get("section", "")
    hdr = plain.get("header") or inf.get("header", "")
    e.update({"ret": inf.get("ret", ""), "args": inf.get("args", []), "doc": doc,
              "section": sec or HEADER_SECTION.get(hdr, "Other functions"), "header": hdr})
    if e["py"]:
        pi, vals = ex_args(e["py_c"], inf)
        e["py_args"] = pi.get("args", []); e["py_ret"] = pi.get("ret", "")
        # build 30: SWIG's Python wrapper takes True/False (not 1/0) for a bool argument
        vals = [bool(v) if (isinstance(v, int) and t.replace("const", "").strip() == "bool") else v
                for (t, n), v in zip(pi.get("args", []), vals)] if len(vals) == len(pi.get("args", [])) else vals
        e["py_ex"] = None if any(v is None for v in vals) else "%s(%s)" % (e["py"], ", ".join(py_lit(v) for v in vals))
    if e["scm"]:
        si, svals = ex_args(e["scm_c"], inf)
        e["scm_args"] = si.get("args", []); e["scm_ret"] = si.get("ret", "")
        e["scm_ex"] = None if any(v is None for v in svals) else "(%s)" % " ".join([e["scm"]] + [scm_lit(v) for v in svals])
    alla = (e.get("py_args") or []) + (e.get("scm_args") or [])
    e["gui_internal"] = any(re.search(r"Gtk|Gdk|GtkWidget|void \*|GLArea", t) for t, n in alla)
    out.append(e)

# ---- build 31: hand-written examples (m0/tools/api_examples_curated.json), each tried on the test data in both
# languages: real arguments instead of the placeholders above, set-up lines, what a correct result is, and the
# functions that must not be run automatically (with the reason).
CUR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "api_examples_curated.json")
if os.path.exists(CUR):
    cur = json.load(open(CUR)); n_cur = 0
    for e in out:
        c = cur.get(e["key"])
        if not c: continue
        n_cur += 1; e["curated"] = True
        if e["py"] and c.get("py"): e["py_ex"] = c["py"]
        if e["scm"] and c.get("scm"): e["scm_ex"] = c["scm"]
        for f in ("py_setup", "scm_setup", "expect", "skip", "note"):
            if c.get(f): e[f] = c[f]
    print("hand-written examples:", n_cur, "of", len(cur))
json.dump(out, open(OUT, "w"), indent=1)
n_py = sum(1 for e in out if e["py"]); n_scm = sum(1 for e in out if e["scm"])
print("functions: %d (Python %d, Scheme %d); with header text %d; with an automatic example: Python %d, Scheme %d"
      % (len(out), n_py, n_scm, sum(1 for e in out if e["doc"]), sum(1 for e in out if e.get("py_ex")), sum(1 for e in out if e.get("scm_ex"))))
print("Scheme only:", sum(1 for e in out if e["scm"] and not e["py"]), " Python only:", sum(1 for e in out if e["py"] and not e["scm"]))
print("no header found:", sum(1 for e in out if not e["header"]))
