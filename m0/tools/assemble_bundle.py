#!/usr/bin/env python3
"""assemble_bundle.py -- build the relocatable Coot bundle (no conda environment needed at run time).

usage: assemble_bundle.py --coot-bin F --canvas-lib D --env D --stage D --out D

Layout of --out:
  bin/coot-bin                       rpath @executable_path/../lib
  lib/*.dylib                        flat; every non-system dependency is @rpath/<name>
  lib/gdk-pixbuf-2.0/2.10.0/loaders/ , lib/gtk-2.0/2.10.0/engines/ , lib/python3.11/ , lib/guile/3.0/{ccache,extensions}
  share/{guile,glib-2.0/schemas,icons,themes}, etc/fonts, ssl/cacert.pem
  share/coot, test-data, tests, run-coot.sh ...   (copied from --stage; the monomer library is not included: build 37)
  lib/gdk-pixbuf-loaders.cache.in    with @BUNDLE@ placeholders (the launcher fills them in per user)
Every Mach-O is re-signed ad hoc.  Nothing outside --out is modified.
"""
import os, re, sys, shutil, subprocess, argparse, collections, json, functools

ap = argparse.ArgumentParser()
for a in ("coot-bin", "canvas-lib", "env", "stage", "out"): ap.add_argument("--" + a, required=True)
A = ap.parse_args()
ENV = os.path.realpath(A.env); OUT = os.path.abspath(A.out); STAGE = os.path.abspath(A.stage)
SYSTEM = ("/usr/lib/", "/System/")
DROP_PY = {"_tkinter", "_curses", "_curses_panel", "_dbm", "_gdbm"}      # pull in Tcl/Tk, ncurses, gdbm
def run(cmd, **kw): return subprocess.run(cmd, capture_output=True, text=True, **kw)
def macho(p):
    try:
        with open(p, "rb") as f: return f.read(4) in (b"\xcf\xfa\xed\xfe",)
    except OSError: return False
@functools.lru_cache(maxsize=None)
def deps(p):
    out = run(["otool", "-L", p]).stdout.splitlines()[1:]
    names = [l.strip().split(" (")[0] for l in out if l.strip()]
    idn = run(["otool", "-D", p]).stdout.splitlines()
    ident = idn[1].strip() if len(idn) > 1 else None
    return [n for n in names if n != ident], ident
@functools.lru_cache(maxsize=None)
def rpaths(p):
    out = run(["otool", "-l", p]).stdout.splitlines(); r = []
    for i, l in enumerate(out):
        if "cmd LC_RPATH" in l:
            m = re.search(r"path (.*) \(offset", out[i + 2]); r.append(m.group(1))
    return r
exe_real = os.path.realpath(A.coot_bin); exe_dir = os.path.dirname(exe_real)
def expand(x, loader): return x.replace("@loader_path", os.path.dirname(os.path.realpath(loader))).replace("@executable_path", exe_dir)
def resolve(name, loader, inh):
    if name.startswith(SYSTEM): return "system"
    if name.startswith("@rpath/"):
        base = name[7:]
        for rp in list(rpaths(loader)) + inh:
            c = os.path.join(expand(rp, loader), base)
            if os.path.exists(c): return os.path.realpath(c)
        c = os.path.join(ENV, "lib", base)
        return os.path.realpath(c) if os.path.exists(c) else None
    if name.startswith("@"):
        c = expand(name, loader); return os.path.realpath(c) if os.path.exists(c) else None
    return os.path.realpath(name) if os.path.exists(name) else None

# ---------------------------------------------------------------- 1. closure
closure = collections.OrderedDict()   # real -> set(names)
seen = set(); problems = []
inh = [expand(r, A.coot_bin) for r in rpaths(A.coot_bin)]
def walk(p):
    if p in seen: return
    seen.add(p)
    ds, _ = deps(p)
    for d in ds:
        r = resolve(d, p, inh)
        if r == "system" or r == p: continue
        if r is None: problems.append((os.path.basename(p), d)); continue
        closure.setdefault(r, set()).add(os.path.basename(d)); walk(r)
canvas = sorted(os.path.realpath(os.path.join(A.canvas_lib, f)) for f in os.listdir(A.canvas_lib) if f.endswith(".dylib") and not os.path.islink(os.path.join(A.canvas_lib, f)))
for c in canvas: closure.setdefault(c, set()).add(os.path.basename(c))
walk(exe_real)
for c in canvas: walk(c)

modules = []   # (real file, destination relative to OUT)
def add_modules(rel_dir, keep=lambda f: True):
    top = os.path.join(ENV, rel_dir)
    for dp, dn, fn in os.walk(top):
        for f in sorted(fn):
            p = os.path.join(dp, f)
            if not os.path.islink(p) and macho(p) and keep(f): modules.append((p, os.path.relpath(p, ENV)))
add_modules("lib/gdk-pixbuf-2.0")
add_modules("lib/gtk-2.0/2.10.0/engines")
add_modules("lib/python3.11/lib-dynload", keep=lambda f: f.split(".")[0] not in DROP_PY)
add_modules("lib/guile/3.0/extensions")
for f in sorted(os.listdir(os.path.join(ENV, "lib"))):
    if re.match(r"libguile-srfi.*\.dylib$", f):
        p = os.path.realpath(os.path.join(ENV, "lib", f)); closure.setdefault(p, set()).add(f)
for p, rel in modules: walk(p)
if problems: print("UNRESOLVED:", problems)

# ---------------------------------------------------------------- 2. copy
if os.path.exists(OUT): shutil.rmtree(OUT)
for d in ("bin", "lib"): os.makedirs(os.path.join(OUT, d))
shutil.copy2(exe_real, os.path.join(OUT, "bin", "coot-bin"))
copied = {}
for real, names in closure.items():
    if real == exe_real: continue
    names = sorted(names, key=lambda n: (-len(n), n))   # the longest (most specific) name is the file, the others link to it
    dest = os.path.join(OUT, "lib", names[0]); shutil.copy2(real, dest); os.chmod(dest, 0o755)
    copied[real] = dest
    for alias in names[1:]:
        l = os.path.join(OUT, "lib", alias)
        if not os.path.lexists(l): os.symlink(names[0], l)
for p, rel in modules:
    dest = os.path.join(OUT, rel); os.makedirs(os.path.dirname(dest), exist_ok=True); shutil.copy2(p, dest); os.chmod(dest, 0o755)

def rsync(src, dst, *excl):
    os.makedirs(dst, exist_ok=True)
    cmd = ["rsync", "-a"] + [x for e in excl for x in ("--exclude", e)] + [src.rstrip("/") + "/", dst.rstrip("/") + "/"]
    r = run(cmd); assert r.returncode == 0, r.stderr
rsync(os.path.join(ENV, "lib/python3.11"), os.path.join(OUT, "lib/python3.11"), "test", "tests", "idlelib", "tkinter", "turtledemo", "turtle.py",
      "site-packages", "config-3.11-darwin", "lib-dynload", "ensurepip", "lib2to3", "distutils", "*.a")
os.makedirs(os.path.join(OUT, "lib/python3.11/site-packages"), exist_ok=True)
rsync(os.path.join(ENV, "lib/guile/3.0/ccache"), os.path.join(OUT, "lib/guile/3.0/ccache"))
rsync(os.path.join(ENV, "share/guile"), os.path.join(OUT, "share/guile"))
rsync(os.path.join(ENV, "share/glib-2.0/schemas"), os.path.join(OUT, "share/glib-2.0/schemas"), "*.xml")
rsync(os.path.join(ENV, "share/icons"), os.path.join(OUT, "share/icons"))
rsync(os.path.join(ENV, "share/themes"), os.path.join(OUT, "share/themes"))
rsync(os.path.join(ENV, "etc/fonts"), os.path.join(OUT, "etc/fonts"))
rsync(os.path.join(ENV, "share/fontconfig"), os.path.join(OUT, "share/fontconfig"))   # etc/fonts/conf.d/*.conf are links into it
os.makedirs(os.path.join(OUT, "ssl"), exist_ok=True); shutil.copy2(os.path.join(ENV, "ssl/cacert.pem"), os.path.join(OUT, "ssl/cacert.pem"))
# fontconfig: drop the one baked-in absolute cache directory (the xdg one remains)
fc = os.path.join(OUT, "etc/fonts/fonts.conf"); s = open(fc).read()
s2 = re.sub(r"[ \t]*<cachedir>" + re.escape(ENV) + r"[^<]*</cachedir>\n", "", s); assert s2 != s; open(fc, "w").write(s2)
rd = os.path.join(OUT, "etc/fonts/conf.d/README")
if os.path.exists(rd): os.remove(rd)

# stage = the Coot data, tests, launcher (not the old canvas libs / pixbuf cache)
# (build 37) the CCP4 monomer library is not part of the bundle: coot0 uses CCP4's or fetches it (fetch-monomers.sh)
rsync(STAGE, OUT, "logs", "work", "results", ".cache", "monomers", "lib/gdk-pixbuf-loaders.cache", "lib/*.dylib", "bin/coot-bin", "coot-backup", ".DS_Store")

os.makedirs(os.path.join(OUT, "results"), exist_ok=True)
if os.path.exists(os.path.join(STAGE, "results/answers.txt")): shutil.copy2(os.path.join(STAGE, "results/answers.txt"), os.path.join(OUT, "results/answers.txt"))

# pixbuf loader cache template (paths relative to the bundle via a placeholder)
loaders = sorted(os.path.join(ENV, rel) for _, rel in [(0, r) for p, r in modules if "gdk-pixbuf-2.0" in r])
r = run([os.path.join(ENV, "bin/gdk-pixbuf-query-loaders")] + loaders)
assert r.returncode == 0 and r.stdout.strip(), r.stderr
# gdk-pixbuf-query-loaders writes the module paths relative to the prefix ("lib/gdk-pixbuf-2.0/..."), which gdk-pixbuf cannot
# resolve in a relocated tree (the SVG loader then fails to load): make every path absolute through the placeholder.
tmpl = r.stdout.replace(os.path.join(ENV, "lib") + "/", "@BUNDLE@/lib/")
tmpl = re.sub(r'(?m)^"lib/', '"@BUNDLE@/lib/', tmpl)
assert ENV not in tmpl and not re.search(r'(?m)^"(?!@BUNDLE@/)[^"]*\.(?:so|dylib)"$', tmpl), "unexpected loader path form"
assert len(re.findall(r'(?m)^"@BUNDLE@/lib/[^"]+\.(?:so|dylib)"$', tmpl)) == len(loaders), "loader path count mismatch"
open(os.path.join(OUT, "lib/gdk-pixbuf-loaders.cache.in"), "w").write(tmpl)

# ---------------------------------------------------------------- 3. rewrite install names, rpaths; sign
files = []
for dp, dn, fn in os.walk(OUT):
    if os.path.realpath(dp).startswith(os.path.realpath(STAGE) + os.sep) and os.path.islink(dp): continue
    for f in fn:
        p = os.path.join(dp, f)
        if not os.path.islink(p) and macho(p): files.append(p)
libdir = os.path.join(OUT, "lib")
changed = 0
for p in sorted(files):
    ds, ident = deps(p)
    args = []
    top = os.path.dirname(p) == libdir
    if p.endswith(".dylib") and top: args += ["-id", "@rpath/" + os.path.basename(p)]
    elif ident and not top: args += ["-id", "@rpath/" + os.path.basename(p)]
    for d in ds:
        if d.startswith(SYSTEM): continue
        new = "@rpath/" + os.path.basename(d)
        if d != new: args += ["-change", d, new]
        if not os.path.lexists(os.path.join(libdir, os.path.basename(d))): problems.append((os.path.basename(p), "missing in bundle: " + new))
    if os.path.basename(p) == "coot-bin" and os.path.dirname(p) == os.path.join(OUT, "bin"): newrp = "@executable_path/../lib"
    else:
        rel = os.path.relpath(libdir, os.path.dirname(p)); newrp = "@loader_path" + ("/" + rel if rel != "." else "")
    existing = list(rpaths(p))
    for rp in existing:
        if rp != newrp: args += ["-delete_rpath", rp]      # (install_name_tool cannot delete and add the same rpath in one call)
    if newrp not in existing: args += ["-add_rpath", newrp]
    r = run(["install_name_tool"] + args + [p]); assert r.returncode == 0, (p, r.stderr)
    changed += 1
for p in sorted(files):
    r = run(["codesign", "--force", "--sign", "-", "--timestamp=none", p]); assert r.returncode == 0, (p, r.stderr)
print("bundle:", OUT)
print("Mach-O files rewritten and re-signed:", changed, "| libs in lib/:", len([f for f in os.listdir(libdir) if f.endswith('.dylib')]))
if problems: print("PROBLEMS:", problems); sys.exit(1)
