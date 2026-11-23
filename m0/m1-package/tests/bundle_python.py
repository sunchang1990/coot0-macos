
# Checks that matter for a relocated, self-contained bundle: everything loads from inside COOT_PREFIX.
import os, sys, re, ssl, glob, ctypes, importlib
res = []
def check(name, fn):
    try:
        v = fn(); ok = True if v is None else bool(v); res.append((name, ok, repr(v)[:110]))
    except Exception as e:
        res.append((name, False, "EXC " + repr(e)[:150]))
here = os.path.realpath(os.environ["COOT_PREFIX"])
def inside(p): return os.path.realpath(p).startswith(here + os.sep)

check("sys.prefix is the bundle", lambda: inside(sys.prefix) or os.path.realpath(sys.prefix) == here)
check("every sys.path entry that exists is inside the bundle", lambda: all(inside(p) or os.path.realpath(p) == here for p in sys.path if p and os.path.exists(p)))
mods = sorted(os.path.basename(f).split(".")[0] for f in glob.glob(os.path.join(here, "lib/python3.11/lib-dynload/*.so")))
failed = []
for m in mods:
    try: importlib.import_module(m)
    except Exception as e: failed.append((m, repr(e)[:60]))
check("all %d bundled Python extension modules import (failed: %s)" % (len(mods), failed[:3]), lambda: not failed)
check("ssl default context loads the bundled CA file", lambda: ssl.create_default_context().cert_store_stats()["x509_ca"] > 100)
check("the private HOME has .local/share (GTK recently-used list; build 15)", lambda: os.environ.get("COOT_USE_HOME") or os.path.isdir(os.path.join(os.environ.get("HOME", "/nonexistent"), ".local", "share")))
check("ctypes works (needed for the Python GTK layer)", lambda: ctypes.CDLL(None) is not None)

# gdk-pixbuf through the bundle's loader cache: every pixmap, SVG included
pb = ctypes.CDLL(os.path.join(here, "lib/libgdk_pixbuf-2.0.0.dylib"))
pb.gdk_pixbuf_new_from_file.restype = ctypes.c_void_p; pb.gdk_pixbuf_new_from_file.argtypes = [ctypes.c_char_p, ctypes.c_void_p]
files = sorted(glob.glob(os.path.join(here, "share/coot/pixmaps/*")))
files = [f for f in files if f.lower().endswith((".png", ".svg", ".jpg", ".jpeg"))]
bad = [os.path.basename(f) for f in files if not pb.gdk_pixbuf_new_from_file(f.encode(), None)]
check("gdk-pixbuf loads %d of %d pixmaps (%d svg); failures: %s" % (len(files) - len(bad), len(files), sum(f.endswith(".svg") for f in files), bad[:3]), lambda: not bad and len(files) > 100)
# (build 34) the cache FILE is in this folder (unpacked) or in the state folder's .cache (a copy installed by install.sh keeps
# it in ~/Library/Application Support/coot0, so the installed folder is never written to); what matters is that every loader
# it lists is one of this folder's.  Build 33's check wanted the file itself inside the folder and failed from installed copies.
def pixbuf_cache():
    f = os.environ["GDK_PIXBUF_MODULE_FILE"]
    cache_dir = os.path.realpath(os.environ.get("XDG_CACHE_HOME", "/nonexistent"))
    where_ok = inside(f) or os.path.realpath(f).startswith(cache_dir + os.sep)
    loaders = [m.group(1) for m in (re.match(r'"(/[^"]+\.(?:so|dylib))"', l) for l in open(f)) if m]
    outside = [l for l in loaders if not os.path.realpath(l).startswith(here + os.sep)]
    return True if (where_ok and len(loaders) >= 10 and not outside) else (f, len(loaders), outside[:2])
check("pixbuf loader cache in use lists this folder's loaders (cache file in the folder or in the state folder)", pixbuf_cache)

# fontconfig with the bundled configuration
fc = ctypes.CDLL(os.path.join(here, "lib/libfontconfig.1.dylib"))
fc.FcInitLoadConfigAndFonts.restype = ctypes.c_void_p
cfg = fc.FcInitLoadConfigAndFonts()
fc.FcConfigGetFonts.restype = ctypes.c_void_p; fc.FcConfigGetFonts.argtypes = [ctypes.c_void_p, ctypes.c_int]
fc.FcFontSetCount = getattr(fc, "FcFontSetCount", None)
def nfonts():
    class FcFontSet(ctypes.Structure): _fields_ = [("nfont", ctypes.c_int), ("sfont", ctypes.c_int), ("fonts", ctypes.c_void_p)]
    s = ctypes.cast(fc.FcConfigGetFonts(cfg, 0), ctypes.POINTER(FcFontSet)); return s.contents.nfont
check("fontconfig finds system fonts with the bundled fonts.conf", lambda: nfonts() > 10)

# Coot's own data resolves inside the bundle
import coot
check("coot reports its version", lambda: isinstance(coot.coot_version(), str))
check("COOT_DATA_DIR files exist (cootrc, syminfo, rama-data)", lambda: all(os.path.exists(os.path.join(here, "share/coot", f)) for f in ("cootrc", "syminfo.lib", "rama-data")))
# UI defaults and icon completeness (build 5): no broken-image placeholders in the ligand builder, environment distances on at start
def lbg_icons_ok():
    txt = open(os.path.join(here, "share/coot/lbg.glade"), errors="ignore").read()
    refs = sorted(set(os.path.basename(x) for x in re.findall(r'pixmaps/([^"<>]+?\.(?:svg|png))', txt)))
    missing = [r for r in refs if not os.path.exists(os.path.join(here, "share/coot/pixmaps", r))]
    return (len(refs) >= 15 and not missing), (len(refs), missing[:3])
check("every pixmap that lbg.glade (Lidia) refers to is installed", lambda: lbg_icons_ok()[0])
check("environment distances are on by default", lambda: coot.show_environment_distances_state() == 1)
check("model toolbar show/hide API present", lambda: callable(coot.show_modelling_toolbar) and callable(coot.hide_modelling_toolbar))
# Start-up picture (build 12): bin/coot-splash shows share/coot/pixmaps/coot-splash@2x.png at half its pixel size (Retina)
import struct, subprocess, tempfile
def png_size(p):
    d = open(p, "rb").read(24); return struct.unpack(">II", d[16:24])
def splash_pictures():
    d = os.path.join(here, "share/coot/pixmaps")
    a, b = png_size(os.path.join(d, "coot-0.9.8.96.png")), png_size(os.path.join(d, "coot-splash@2x.png"))
    return b == (a[0] * 2, a[1] * 2) and a == (580, 478), (a, b)
check("splash pictures: 580 x 478 for Coot's own window, exactly 2x that for bin/coot-splash", lambda: splash_pictures()[0])
def splash_helper():
    exe = os.path.join(here, "bin", "coot-splash"); pic = os.path.join(here, "share/coot/pixmaps/coot-splash@2x.png")
    out = os.path.join(tempfile.mkdtemp(prefix="coot-splash-test-"), "splash.png")
    r = subprocess.run([exe, "--selftest", pic, out], capture_output=True, text=True, timeout=60)
    if r.returncode != 0: return "exit %d: %s" % (r.returncode, r.stderr[-200:])
    if "1160x956 pixels -> 580x478 points" not in r.stdout: return "output: %r" % r.stdout[-200:]
    return True if png_size(out) == (1160, 956) else "bitmap size %r" % (png_size(out),)
check("bin/coot-splash loads the 2x picture as 580 x 478 points and draws it into a 1160 x 956 pixel bitmap", splash_helper)
def splash_links():
    out = subprocess.run(["/usr/bin/otool", "-L", os.path.join(here, "bin", "coot-splash")], capture_output=True, text=True).stdout.splitlines()[1:]
    libs = [l.split()[0] for l in out]
    bad = [l for l in libs if not (l.startswith("/System/") or l.startswith("/usr/lib/"))]
    return True if (libs and not bad) else bad
check("bin/coot-splash uses only macOS's own libraries", splash_links)
def launcher_wiring():
    t = open(os.path.join(here, "run-coot.sh")).read()
    return True if ("bin/coot-splash" in t and "--no-splash-screen" in t and "COOT_NO_SPLASH" in t) else "run-coot.sh does not start the splash helper"
check("run-coot.sh starts the splash helper (and switches Coot's own splash off)", launcher_wiring)
check("no 'Goodbye Old Coot' picture: the 1x splash differs from the original 0.9.8.96 picture", lambda: os.path.getsize(os.path.join(here, "share/coot/pixmaps/coot-0.9.8.96.png")) != 534263)

w = max(len(r[0]) for r in res)
for n, ok, v in res: print(("PASS " if ok else "FAIL ") + n.ljust(w) + "  " + v)
print("SUMMARY", sum(1 for r in res if r[1]), "/", len(res), flush=True)
coot.coot_real_exit(0)
