#!/usr/bin/env python3
"""m0_build.py -- compile/syntax-check every translation unit of src/, lbg/, tw/, goograph/ for Coot on Apple Silicon.
Usage: m0_build.py <syntax|compile> <out.json> [--stubs gl,gtkglext,canvas] [--prefix EXTRA_PREFIX]... [--objdir DIR] [--noscript]
Run with the coot-deps env active (CONDA_PREFIX set, PKG_CONFIG_PATH including its lib/pkgconfig)."""
import os, re, sys, json, subprocess, argparse
from concurrent.futures import ThreadPoolExecutor
ap = argparse.ArgumentParser(); ap.add_argument("mode"); ap.add_argument("out")
ap.add_argument("--stubs", default="gl,gtkglext,canvas"); ap.add_argument("--prefix", action="append", default=[])
ap.add_argument("--objdir", default="obj"); ap.add_argument("--noscript", action="store_true"); ap.add_argument("--only", default="")
ap.add_argument("--rdkit", default="", help="RDKit prefix (conda env with include/rdkit, include/boost): enables MAKE_ENHANCED_LIGAND_TOOLS"); ap.add_argument("--pygtk", action="store_true", help="scripted GUI via Python (gtk2compat): -DUSE_PYGTK -DCOOT_GUI_VIA_PYTHON"); ap.add_argument("--src", default=None); ap.add_argument("--preprocess", default=""); ap.add_argument("--with-libs", action="store_true"); a = ap.parse_args()
HERE = os.path.dirname(os.path.abspath(__file__)); src = os.path.abspath(a.src or os.path.join(HERE, "..", "coot-src"))
conda = os.environ["CONDA_PREFIX"]; ENABLED = {"COOT_USE_PYTHON", "COOT_USE_GUILE"}
def parse_am(path):
    txt = open(path, errors="ignore").read().replace("\\\n", " "); stack = []; v = {}
    for line in txt.split("\n"):
        s = line.strip()
        if not s or s.startswith("#"): continue
        m = re.match(r"^(if|else|endif)\b\s*(\w*)", s)
        if m:
            kw, c = m.groups()
            if kw == "if": stack.append(c in ENABLED)
            elif kw == "else": stack[-1] = (not stack[-1]) if c == "" and not stack[-1] else False
            else: stack.pop()
            continue
        if stack and not all(stack): continue
        m = re.match(r"^([A-Za-z0-9_]+)\s*(\+?=)\s*(.*)$", s)
        if m: k, op, val = m.groups(); v[k] = (v.get(k, "") + " " + val) if op == "+=" else val
    def ex(s, d=0): return s if d > 5 else re.sub(r"\$\(([A-Za-z0-9_]+)\)", lambda m: ex(v.get(m.group(1), ""), d + 1), s)
    return {k: ex(x) for k, x in v.items()}
targets = [("src","coot_bin_SOURCES","coot-bin"),("lbg","libcoot_lidia_la_SOURCES","lib"),("lbg","lidia_bin_SOURCES","lidia-bin"),("tw","libcoot_tw_la_SOURCES","tw"),("goograph","libcoot_goograph_la_SOURCES","lib")]
# directories whose libcoot-*.la are in COOT_EXTRA_LIBS (src/Makefile.am) -> needed to link coot-bin
LIBDIRS = ["pli","ligand","lidia-core","density-contour","build","skeleton","angles","db-main","high-res","ideal","geometry","coords",
           "ccp4mg-utils","coot-utils","utils","mini-mol","analysis","protein_db","cootilus","cootaneer","compat"]
role = {}; tus = []
for d, var, rl in targets:
    v = parse_am(os.path.join(src, d, "Makefile.am"))
    for t in v.get(var, "").split():
        if re.search(r"\.(cc|cpp|c)$", t) and os.path.exists(os.path.join(src, d, t)): tus.append((d, t)); role.setdefault((d, t), rl)
if a.with_libs:
    for d in LIBDIRS:
        v = parse_am(os.path.join(src, d, "Makefile.am"))
        for k, val in v.items():
            if re.match(r"^lib[A-Za-z0-9_]+_la_SOURCES$", k):
                for t in val.split():
                    if re.search(r"\.(cc|cpp|c)$", t) and os.path.exists(os.path.join(src, d, t)): tus.append((d, t)); role.setdefault((d, t), "lib")
tus = sorted(set(tus))
if a.only: tus = [t for t in tus if re.search(a.only, t[0] + "/" + t[1])]
env = dict(os.environ); env["PKG_CONFIG_PATH"] = ":".join([p + "/lib/pkgconfig" for p in a.prefix] + [conda + "/lib/pkgconfig", conda + "/share/pkgconfig", env.get("PKG_CONFIG_PATH", "")])
def sh(c): return subprocess.run(c, shell=True, capture_output=True, text=True, env=env).stdout.split()
mods = "gtk+-2.0 libcurl sqlite3 libpng cairo gsl" + ("" if a.noscript else "") + (" goocanvas libgnomecanvas-2.0" if "canvas" not in a.stubs.split(",") else "")
gtk = sh("pkg-config --cflags " + mods)
py = [] if a.noscript else sh("python3-config --includes"); guile = [] if a.noscript else sh("pkg-config --cflags guile-3.0")
defs = ["-DHAVE_CXX11","-DHAVE_CXX_THREAD","-DHAVE_GSL","-DHAVE_BOOST","-DUSE_SQLITE3","-DUSE_LIBPNG=1","-DUSE_LIBCURL",
        "-DHAVE_GOOCANVAS","-DHAVE_GNOME_CANVAS","-DCOOT_USE_GTK2_INTERFACE","-DHAVE_SSMLIB","-DCLIPPER_HAS_TOP8000","-DMMDB_HAS_LINK_DISTANCE",
        '-DVERSION="0.9.8.96"','-DPACKAGE="coot"','-DPACKAGE_VERSION="0.9.8.96"','-DPACKAGE_NAME="coot"',
        '-DPKGDATADIR="/usr/local/share/coot"','-DPACKAGE_LOCALE_DIR="/usr/local/share/coot/locale"','-DPKGPYTHONDIR="/usr/local/lib/python3/site-packages/coot"',
        '-DDATADIR="/usr/local/share"','-DCOOT_SYS_BUILD_TYPE="Darwin-arm64"','-DCOOT_BUILD_INFO_STRING=""']
if not a.noscript: defs += ["-DUSE_PYTHON", "-DUSE_GUILE"]
if a.rdkit: defs += ["-DMAKE_ENHANCED_LIGAND_TOOLS", "-DRDKIT_HAS_CAIRO_SUPPORT"]
if a.pygtk: defs += ["-DUSE_PYGTK", "-DCOOT_GUI_VIA_PYTHON"]
inc = [f"-I{src}", f"-I{conda}/include", f"-I{conda}/include/mmdb2", f"-I{conda}/include/ccp4", f"-I{conda}/include/ssm"]
for p in a.prefix: inc.append(f"-I{p}/include")
if a.rdkit:
    # RDKit headers + the Boost headers RDKit was built with (one Boost version for every translation unit; they come BEFORE the working env's Boost)
    stage = os.path.abspath(os.path.join(a.objdir, "_rdkit_inc")); os.makedirs(stage, exist_ok=True)
    bl = os.path.join(stage, "boost")
    if os.path.islink(bl): os.remove(bl)
    os.symlink(os.path.join(a.rdkit, "include", "boost"), bl)
    inc.insert(0, f"-I{os.path.join(a.rdkit, 'include', 'rdkit')}"); inc.insert(0, f"-I{stage}")
stubs = [s for s in a.stubs.split(",") if s]
for s in reversed(stubs):
    # "gtkglext" now means the in-tree GtkGLExt replacement headers (compat/gl-seam); other stubs are still tools/stubs-*
    inc.insert(0, "-I" + (os.path.join(src, "compat", "gl-seam") if s == "gtkglext" else os.path.join(HERE, "stubs-" + {"gl":"gl-apple"}.get(s, s))))
os.makedirs(a.objdir, exist_ok=True)
def run(tu):
    d, t = tu; p = os.path.join(src, d, t); c_only = t.endswith(".c")
    out = [] if a.mode == "syntax" else ["-c", "-o", os.path.join(a.objdir, f"{d}__{t}.o")]
    cmd = [("/usr/bin/clang" if c_only else "/usr/bin/clang++")] + (["-fsyntax-only"] if a.mode == "syntax" else ["-O1"]) + ["-w", "-ferror-limit=0", "-fno-color-diagnostics", "-mmacosx-version-min=" + os.environ.get("COOT_MIN_MACOS", "11.0"), f"-I{os.path.join(src, d)}"] \
          + (["-x", "c"] if c_only else ["-std=c++17"]) + defs + inc + gtk + py + guile + out + [p]
    if a.preprocess:
        os.makedirs(a.preprocess, exist_ok=True)
        cmd = [x for x in cmd if x != "-fsyntax-only"] + ["-E", "-o", os.path.join(a.preprocess, f"{d}__{t}.i")]
    r = subprocess.run(cmd, capture_output=True, text=True)
    diags = re.findall(r"^(\S+?):(\d+):\d+: (fatal error|error): (.*)$", r.stderr, re.M)
    return {"dir": d, "file": t, "role": role.get(tu, ""), "rc": r.returncode, "n_errors": len(diags), "diags": [list(x) for x in diags[:20000]]}
with ThreadPoolExecutor(8) as ex: res = list(ex.map(run, tus))
json.dump(res, open(a.out, "w")); ok = sum(1 for r in res if r["rc"] == 0)
print(f"{a.mode}: {len(res)} TUs, {ok} ok, {len(res) - ok} fail, {sum(r['n_errors'] for r in res)} errors  (stubs={a.stubs or 'none'}, noscript={a.noscript})")
