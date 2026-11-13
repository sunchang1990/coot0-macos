#!/usr/bin/env python3
import os, re, sys, json, subprocess, shlex
from concurrent.futures import ThreadPoolExecutor
src = os.path.abspath("../coot-src"); conda = os.environ["CONDA_PREFIX"]
use_stubs = sys.argv[1] in ("stubs","noscript"); noscript = sys.argv[1]=="noscript"; out = sys.argv[2]
ENABLED = {"COOT_USE_PYTHON", "COOT_USE_GUILE"}     # MAKE_ENHANCED_LIGAND_TOOLS stays off (needs RDKit)
def parse_am(path):
    txt = open(path, errors="ignore").read().replace("\\\n", " "); stack=[]; v={}
    for line in txt.split("\n"):
        s=line.strip()
        if not s or s.startswith("#"): continue
        m=re.match(r"^(if|else|endif)\b\s*(\w*)", s)
        if m:
            kw,c=m.groups()
            if kw=="if": stack.append(c in ENABLED)
            elif kw=="else": stack[-1]=not stack[-1] if c=="" and not stack[-1] else False
            else: stack.pop()
            continue
        if stack and not all(stack): continue
        m=re.match(r"^([A-Za-z0-9_]+)\s*(\+?=)\s*(.*)$", s)
        if m:
            k,op,val=m.groups(); v[k]=(v.get(k,"")+" "+val) if op=="+=" else val
    def ex(s,d=0):
        return s if d>5 else re.sub(r"\$\(([A-Za-z0-9_]+)\)", lambda m: ex(v.get(m.group(1),""),d+1), s)
    return {k:ex(x) for k,x in v.items()}
targets = [("src","coot_bin_SOURCES"),("lbg","libcoot_lidia_la_SOURCES"),("lbg","lidia_bin_SOURCES"),
           ("tw","libcoot_tw_la_SOURCES"),("goograph","libcoot_goograph_la_SOURCES")]
tus=[]
for d,var in targets:
    v=parse_am(os.path.join(src,d,"Makefile.am"))
    for t in v.get(var,"").split():
        if re.search(r"\.(cc|cpp|c)$", t) and os.path.exists(os.path.join(src,d,t)): tus.append((d,t))
tus = sorted(set(tus))
def sh(c): return subprocess.run(c, shell=True, capture_output=True, text=True).stdout.split()
gtk  = sh("pkg-config --cflags gtk+-2.0 libcurl sqlite3 libpng cairo gsl")
py   = sh("python3-config --includes")
guile= sh("pkg-config --cflags guile-3.0")
defs = ["-DHAVE_CXX11","-DHAVE_CXX_THREAD","-DHAVE_GSL","-DHAVE_BOOST","-DUSE_SQLITE3","-DUSE_LIBPNG=1","-DUSE_LIBCURL",
        "-DUSE_PYTHON","-DUSE_GUILE","-DHAVE_GOOCANVAS","-DHAVE_GNOME_CANVAS","-DCOOT_USE_GTK2_INTERFACE",
        '-DPKGDATADIR="/usr/local/share/coot"','-DPACKAGE_LOCALE_DIR="/usr/local/share/coot/locale"','-DPKGPYTHONDIR="/usr/local/lib/python3/site-packages/coot"',
        '-DDATADIR="/usr/local/share"','-DCOOT_SYS_BUILD_TYPE="Darwin-arm64"','-DCOOT_BUILD_INFO_STRING=""']
inc = [f"-I{src}", f"-I{conda}/include", f"-I{conda}/include/mmdb2", f"-I{conda}/include/ccp4", f"-I{conda}/include/ssm"]
if use_stubs: inc.insert(0, "-I"+os.path.abspath("syn-stubs"))
if noscript:
    defs = [d for d in defs if d not in ("-DUSE_PYTHON","-DUSE_GUILE","-DHAVE_GOOCANVAS","-DHAVE_GNOME_CANVAS")] + ['-DVERSION="0.9.8.96"']
    py = []; guile = []
def run(tu):
    d,t=tu; p=os.path.join(src,d,t)
    lang = ["-x","c"] if t.endswith(".c") else ["-std=c++17"]
    cmd = ["/usr/bin/clang++" if not t.endswith(".c") else "/usr/bin/clang","-fsyntax-only","-w","-ferror-limit=0","-fno-color-diagnostics",f"-I{os.path.join(src,d)}"]+lang+defs+inc+gtk+py+guile+[p]
    r=subprocess.run(cmd,capture_output=True,text=True)
    diags=re.findall(r"^(\S+?):(\d+):\d+: (fatal error|error): (.*)$", r.stderr, re.M)
    return {"dir":d,"file":t,"rc":r.returncode,"n_errors":len(diags),"diags":[list(x) for x in diags[:20000]]}
with ThreadPoolExecutor(8) as ex: res=list(ex.map(run,tus))
json.dump(res,open(out,"w"))
ok=sum(1 for r in res if r["rc"]==0)
print(f"{len(res)} TUs: {ok} pass, {len(res)-ok} fail, total errors {sum(r['n_errors'] for r in res)}")
