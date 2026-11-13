#!/usr/bin/env python3
"""bundle_inventory.py -- what must go into a relocatable Coot bundle.

Walks the Mach-O dependency closure (otool -L, resolving @rpath / @loader_path / @executable_path) from coot-bin and the
canvas libraries, adds the libraries that are dlopen()ed at run time (gdk-pixbuf loaders, GTK modules, Python extension
modules, Guile extension libraries), lists the resource trees needed, and finds every file that has the build
environment's absolute prefix baked in (those need a run-time override or a regenerated cache).

usage: bundle_inventory.py <coot-bin> <env-prefix> <canvas-lib-dir> <out.json>
"""
import os, re, sys, json, subprocess, collections

exe, ENV, CANVAS, OUT = sys.argv[1:5]
ENV = os.path.realpath(ENV)
SYSTEM = ("/usr/lib/", "/System/")

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout

def deps(path):
    out = run(["otool", "-L", path]).splitlines()[1:]
    return [l.strip().split(" (")[0] for l in out if l.strip()]

def rpaths(path):
    out = run(["otool", "-l", path]).splitlines()
    rp = []
    for i, l in enumerate(out):
        if "cmd LC_RPATH" in l:
            m = re.search(r"path (.*) \(offset", out[i + 2]); rp.append(m.group(1))
    return rp

def is_macho(path):
    try:
        with open(path, "rb") as f: return f.read(4) in (b"\xcf\xfa\xed\xfe", b"\xca\xfe\xba\xbe")
    except OSError: return False

exe_dir = os.path.dirname(os.path.realpath(exe))

def expand(p, loader):
    return (p.replace("@loader_path", os.path.dirname(os.path.realpath(loader)))
             .replace("@executable_path", exe_dir))

def resolve(name, loader, inherited):
    if name.startswith(SYSTEM): return "system"
    if name.startswith("@rpath/"):
        base = name[len("@rpath/"):]
        for rp in rpaths(loader) + inherited:
            c = os.path.join(expand(rp, loader), base)
            if os.path.exists(c): return os.path.realpath(c)
        c = os.path.join(ENV, "lib", base)       # last resort: the env's lib dir
        return os.path.realpath(c) if os.path.exists(c) else None
    if name.startswith("@"):
        c = expand(name, loader); return os.path.realpath(c) if os.path.exists(c) else None
    return os.path.realpath(name) if os.path.exists(name) else None

closure = {}            # realpath -> {"names": set(install-name basenames), "needed_by": set}
unresolved = collections.defaultdict(set)
queue = []

def add(real, name, by):
    e = closure.setdefault(real, {"names": set(), "needed_by": set()})
    e["names"].add(os.path.basename(name)); e["needed_by"].add(by)
    return e

roots = [os.path.realpath(exe)] + sorted(os.path.join(CANVAS, f) for f in os.listdir(CANVAS) if f.endswith(".dylib") and not os.path.islink(os.path.join(CANVAS, f)))
inherited_rp = [expand(r, exe) for r in rpaths(exe)]
seen = set()
def walk(path, inh):
    if path in seen: return
    seen.add(path)
    for d in deps(path):
        r = resolve(d, path, inh)
        if r == "system": continue
        if r is None:
            unresolved[d].add(os.path.basename(path)); continue
        if r == path: continue
        add(r, d, os.path.basename(path)); walk(r, inh)

for r in roots: walk(r, inherited_rp)
static_libs = dict(closure)

# ---- libraries loaded at run time
def find_macho(rel_dirs, exts=(".dylib", ".so")):
    found = []
    for rd in rel_dirs:
        top = os.path.join(ENV, rd)
        if not os.path.isdir(top): continue
        for dp, dn, fn in os.walk(top):
            for f in fn:
                p = os.path.join(dp, f)
                if f.endswith(exts) and is_macho(p) and not os.path.islink(p): found.append(p)
    return found

dyn_groups = {
    "gdk-pixbuf loaders": ["lib/gdk-pixbuf-2.0"],
    "gtk-2.0 modules/engines/immodules": ["lib/gtk-2.0"],
    "python extension modules (lib-dynload)": ["lib/python3.11/lib-dynload"],
    "guile extensions": ["lib/guile/3.0/extensions"] ,
    "gio modules": ["lib/gio"],
}
dynamic = {}
for g, dirs in dyn_groups.items():
    mods = find_macho(dirs)
    dynamic[g] = [os.path.relpath(m, ENV) for m in mods]
    for m in mods:
        walk(m, [os.path.join(ENV, "lib")])
guile_ext = [os.path.join(ENV, "lib", f) for f in os.listdir(os.path.join(ENV, "lib")) if re.match(r"libguile-srfi.*\.dylib|guile-readline.*|libguilereadline.*", f)]
for m in guile_ext:
    if os.path.exists(m) and not os.path.islink(m):
        dynamic.setdefault("guile srfi/readline libraries", []).append(os.path.relpath(m, ENV)); walk(m, [os.path.join(ENV, "lib")])

# ---- resource trees
def du(path):
    tot = 0
    for dp, dn, fn in os.walk(path):
        for f in fn:
            try: tot += os.lstat(os.path.join(dp, f)).st_size
            except OSError: pass
    return tot
trees = {}
for rel in ["lib/python3.11", "share/guile", "lib/guile", "lib/gdk-pixbuf-2.0", "lib/gtk-2.0", "share/glib-2.0/schemas", "etc/fonts",
            "share/icons", "share/themes", "share/locale", "share/fontconfig", "ssl", "etc/ssl", "share/gtk-2.0", "etc/gtk-2.0", "lib/pango", "etc/pango", "share/mime", "lib/gio"]:
    p = os.path.join(ENV, rel)
    if os.path.exists(p): trees[rel] = du(p)

# ---- files with the absolute prefix baked in
needle = ENV.encode()
needle_raw = os.path.dirname(ENV).encode()  # parent, to also catch relative-looking variants
baked = []
scan_roots = [os.path.join(ENV, r) for r in ["etc", "ssl", "share/glib-2.0", "share/guile", "lib/guile", "lib/gtk-2.0", "lib/gdk-pixbuf-2.0", "lib/pkgconfig"]] + \
             [os.path.join(ENV, "lib", "python3.11", f) for f in ["_sysconfigdata__darwin_darwin.py", "config-3.11-darwin"] if os.path.exists(os.path.join(ENV, "lib", "python3.11", f))]
files = []
for sr in scan_roots:
    if os.path.isfile(sr): files.append(sr)
    for dp, dn, fn in os.walk(sr):
        for f in fn:
            p = os.path.join(dp, f)
            if not os.path.islink(p): files.append(p)
for real in list(closure):
    files.append(real)
for p in files:
    try:
        with open(p, "rb") as fh: data = fh.read()
    except OSError: continue
    n = data.count(needle)
    if n: baked.append({"file": os.path.relpath(p, ENV) if p.startswith(ENV) else p, "count": n, "macho": is_macho(p)})

result = {
    "env": ENV, "n_static_closure": len(static_libs), "n_total_libs": len(closure),
    "libs": sorted(({"file": os.path.relpath(k, ENV) if k.startswith(ENV) else k, "names": sorted(v["names"])} for k, v in closure.items()), key=lambda x: x["file"]),
    "outside_env": sorted(k for k in closure if not k.startswith(ENV)),
    "unresolved": {k: sorted(v) for k, v in unresolved.items()},
    "dynamic": dynamic, "resource_tree_bytes": trees,
    "baked_prefix_files": sorted(baked, key=lambda x: -x["count"]),
    "rpaths_of_exe": rpaths(exe),
    "total_lib_bytes": sum(os.path.getsize(k) for k in closure),
}
json.dump(result, open(OUT, "w"), indent=1)
print("static closure:", len(static_libs), "| with run-time loaded modules:", len(closure), "| MB:", round(result["total_lib_bytes"] / 1e6, 1))
print("outside env:", len(result["outside_env"]), "| unresolved:", len(unresolved))
print("baked-prefix files:", len(baked), "(", sum(1 for b in baked if b["macho"]), "Mach-O )")
