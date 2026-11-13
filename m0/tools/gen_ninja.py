#!/usr/bin/env python3
"""Generate a ninja build for the GUI-free Coot libraries by parsing each Makefile.am.
Usage: gen_ninja.py <srcroot> <builddir> <std> [extra cxxflags...]"""
import os, re, sys, json
src = os.path.abspath(sys.argv[1]); bld = os.path.abspath(sys.argv[2]); std = sys.argv[3]
extra = sys.argv[4:]
conda = os.environ["CONDA_PREFIX"]
DIRS = ["utils","mini-mol","lidia-core","geometry","protein_db","coot-utils","coords","analysis","angles",
        "ccp4mg-utils","db-main","density-contour","cootaneer","high-res","ligand","ideal","pli"]

def parse_am(path):
    txt = open(path, errors="ignore").read().replace("\\\n", " ")
    stack = []   # list of bool "active"
    vars_ = {}
    for line in txt.split("\n"):
        s = line.strip()
        if not s or s.startswith("#"): continue
        m = re.match(r"^(if|else|endif)\b\s*(\w*)", s)
        if m:
            kw, cond = m.groups()
            if kw == "if":
                # we are not Windows, no python, no enhanced ligand tools, no guile in baseline
                stack.append(False if cond != "" and not cond.startswith("OS_WIN32") and cond else False)
                if cond.startswith("OS_WIN32"): stack[-1] = False
            elif kw == "else":
                stack[-1] = (not stack[-1]) if stack[-1] is False and True else False
            elif kw == "endif":
                stack.pop()
            continue
        if stack and not all(stack): continue
        m = re.match(r"^([A-Za-z0-9_]+)\s*(\+?=)\s*(.*)$", s)
        if m:
            k, op, v = m.groups()
            vars_[k] = (vars_.get(k, "") + " " + v) if op == "+=" else v
    def expand(s, depth=0):
        if depth > 5: return s
        return re.sub(r"\$\(([A-Za-z0-9_]+)\)", lambda m: expand(vars_.get(m.group(1), ""), depth+1), s)
    return {k: expand(v) for k, v in vars_.items()}

libs = []   # (dir, name, [sources])
for d in DIRS:
    am = os.path.join(src, d, "Makefile.am")
    if not os.path.exists(am): continue
    v = parse_am(am)
    for k, val in v.items():
        m = re.match(r"^(lib[A-Za-z0-9_]+)_la_SOURCES$", k)
        if not m: continue
        srcs = [t for t in val.split() if re.search(r"\.(cc|cpp|c)$", t)]
        srcs = [t for t in srcs if os.path.exists(os.path.join(src, d, t))]
        libs.append((d, m.group(1), srcs))

defs = ["-DHAVE_CXX11","-DHAVE_CXX_THREAD","-DHAVE_GSL","-DHAVE_BOOST","-DUSE_SQLITE3","-DUSE_LIBPNG=1",
        "-DPKGDATADIR=\\\"/usr/local/share/coot\\\"", "-DDATADIR=\\\"/usr/local/share\\\""]
incs = [f"-I{src}", f"-I{conda}/include", f"-I{conda}/include/mmdb2", f"-I{conda}/include/ccp4", f"-I{conda}/include/ssm"]
cxxflags = [f"-std={std}", "-O1", "-g0", "-fPIC", "-fno-common"] + defs + incs + extra
os.makedirs(bld, exist_ok=True)
lines = ["ninja_required_version = 1.5", f"cxx = /usr/bin/clang++", f"cc = /usr/bin/clang",
         f"cxxflags = {' '.join(cxxflags)}", "cflags = -O1 -g0 -fPIC " + " ".join(defs+incs),
         "rule cxx", "  command = $cxx $dirinc $cxxflags -MMD -MF $out.d -c $in -o $out", "  depfile = $out.d", "  deps = gcc", "  description = CXX $in",
         "rule cc", "  command = $cc $dirinc $cflags -MMD -MF $out.d -c $in -o $out", "  depfile = $out.d", "  deps = gcc", "  description = CC $in", ""]
allobjs = []; manifest = []
for d, name, srcs in libs:
    objs = []
    for s in srcs:
        o = f"obj/{d}/{name}.{os.path.basename(s)}.o"
        rule = "cc" if s.endswith(".c") else "cxx"
        lines.append(f"build {o}: {rule} {os.path.join(src,d,s)}")
        lines.append(f"  dirinc = -I{os.path.join(src,d)}")
        objs.append(o)
    allobjs += objs
    manifest.append({"dir": d, "lib": name, "n_sources": len(srcs), "sources": srcs})
json.dump(manifest, open(os.path.join(bld,"manifest.json"),"w"), indent=1)
lines.append("build all_objs: phony " + " ".join(allobjs))
lines.append("default all_objs")
open(os.path.join(bld,"build.ninja"),"w").write("\n".join(lines)+"\n")
print(f"{len(libs)} libraries, {len(allobjs)} translation units, std={std}")
for m in manifest: print(f"  {m['dir']:16s} {m['lib']:32s} {m['n_sources']:3d}")
