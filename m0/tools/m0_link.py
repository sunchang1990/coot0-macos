#!/usr/bin/env python3
"""Link coot-bin from the objects produced by `m0_build.py compile --with-libs`.
Usage: m0_link.py <compile.json> <objdir> <out-binary> [--prefix EXTRA_PREFIX]... [--seam FILE.c] [--extra-obj O]... [--log link.log]
Run in env coot-deps (PKG_CONFIG_PATH set).  Prints the unresolved-symbol list (from ld) to <out>.undef.txt"""
import os, sys, re, json, subprocess, argparse
ap = argparse.ArgumentParser(); ap.add_argument("compile_json"); ap.add_argument("objdir"); ap.add_argument("out")
ap.add_argument("--prefix", action="append", default=[]); ap.add_argument("--seam", default=""); ap.add_argument("--extra-obj", action="append", default=[])
ap.add_argument("--rdkit", default=""); ap.add_argument("--stubs-inc", default=""); ap.add_argument("--log", default=""); a = ap.parse_args()
conda = os.environ["CONDA_PREFIX"]; HERE = os.path.dirname(os.path.abspath(__file__))
env = dict(os.environ); env["PKG_CONFIG_PATH"] = ":".join([p + "/lib/pkgconfig" for p in a.prefix] + [conda + "/lib/pkgconfig", conda + "/share/pkgconfig"])
def sh(c): return subprocess.run(c, shell=True, capture_output=True, text=True, env=env).stdout.split()
res = json.load(open(a.compile_json)); objs = []; seen = set()
for r in res:
    if r.get("role") not in ("coot-bin", "lib") or r["rc"] != 0: continue
    k = (r["dir"], r["file"])
    if k in seen: continue
    seen.add(k); o = os.path.join(a.objdir, f'{r["dir"]}__{r["file"]}.o')
    if os.path.exists(o): objs.append(o)
    else: print("MISSING OBJ", o)
print(f"{len(objs)} objects")
if a.seam:
    so = os.path.join(a.objdir, "gl_seam.o"); inc = sh("pkg-config --cflags gtk+-2.0")
    seam_dir = os.path.dirname(os.path.abspath(a.seam))
    if a.seam.endswith(".mm"):
        cmd = ["/usr/bin/clang++", "-x", "objective-c++", "-std=c++17", "-fobjc-arc", "-O1", "-mmacosx-version-min=" + os.environ.get("COOT_MIN_MACOS", "11.0"), "-c", a.seam, "-o", so, f"-I{seam_dir}"] + inc
    else:
        cmd = ["/usr/bin/clang", "-O1", "-mmacosx-version-min=" + os.environ.get("COOT_MIN_MACOS", "11.0"), "-c", a.seam, "-o", so, f"-I{seam_dir}"] + inc
    r = subprocess.run(cmd, capture_output=True, text=True); print("seam compile rc", r.returncode, r.stderr[:300]); objs.append(so)
objs += a.extra_obj
libs = sh("pkg-config --libs gtk+-2.0 libcurl sqlite3 libpng cairo gsl goocanvas libgnomecanvas-2.0 clipper ssm guile-3.0") + sh("python3-config --ldflags --embed") \
     + ["-framework", "OpenGL", "-framework", "GLUT", "-framework", "Cocoa", "-lz"] + [f"-L{p}/lib" for p in a.prefix] + [f"-Wl,-rpath,{conda}/lib"] + [f"-Wl,-rpath,{p}/lib" for p in a.prefix]
# libart is not in the goocanvas/libgnomecanvas pkg-config Libs line of 0.9-era builds on every platform; make sure it is linked
libs += [f"-L{p}/lib" for p in a.prefix] + ["-lart_lgpl_2"]
RDK_LIBS = ["MolDraw2D","ForceFieldHelpers","Descriptors","ForceField","SubstructMatch","coordgen","Optimizer","DistGeomHelpers","DistGeometry","ChemReactions","Alignment","EigenSolvers","Depictor","MolChemicalFeatures","Subgraphs","PartialCharges","maeparser","FileParsers","RDGeometryLib","GraphMol","ShapeHelpers","Fingerprints","MolAlign","MolTransforms","ChemTransforms","SmilesParse","FilterCatalog","Catalogs","DataStructs","RDGeneral"]  # the list in Coot's configure.ac (--with-rdkit-prefix)
if a.rdkit:
    libs += [f"-L{a.rdkit}/lib", f"-Wl,-rpath,{a.rdkit}/lib"] + [f"-lRDKit{x}" for x in RDK_LIBS] + ["-lboost_serialization", "-lboost_python311"]
MINOS = "-mmacosx-version-min=" + os.environ.get("COOT_MIN_MACOS", "11.0")
cmd = ["/usr/bin/clang++", "-arch", "arm64", MINOS, "-o", a.out] + objs + libs
r = subprocess.run(cmd, capture_output=True, text=True)
log = r.stderr
open(a.log or (a.out + ".link.log"), "w").write(log)
und = []
for m in re.finditer(r'^\s+"(.+?)", referenced from:', log, re.M): und.append(m.group(1))
open(a.out + ".undef.txt", "w").write("\n".join(sorted(set(und))) + "\n")
print("link rc", r.returncode, "| unresolved symbols:", len(set(und)), "| binary exists:", os.path.exists(a.out))
