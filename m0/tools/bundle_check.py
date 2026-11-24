#!/usr/bin/env python3
"""bundle_check.py BUNDLE_DIR  -- fail if the bundle is not self-contained.

For every Mach-O: dependencies are system (/usr/lib, /System) or @rpath/x that resolves (through that file's own rpaths) to a file inside
the bundle; no rpath or install name points outside the bundle; minimum macOS <= 11.0; codesign --verify passes.
Also lists text/config files that still contain an absolute user path of the build machine.
(build 37) The CCP4 monomer library is not part of the package (coot0 uses CCP4's, or fetches it: fetch-monomers.sh).
"""
import os, re, sys, subprocess
B = os.path.realpath(sys.argv[1]); MAXMIN = (11, 0)
def run(c): return subprocess.run(c, capture_output=True, text=True)
def macho(p):
    try:
        with open(p, "rb") as f: return f.read(4) == b"\xcf\xfa\xed\xfe"
    except OSError: return False
bad = []; n = 0; minos_max = (0, 0)
for dp, dn, fn in os.walk(B):
    if os.path.relpath(dp, B).split(os.sep)[0] in ("share", "test-data"): continue
    for f in fn:
        p = os.path.join(dp, f)
        if os.path.islink(p) or not macho(p): continue
        n += 1
        out = run(["otool", "-l", p]).stdout.splitlines()
        rps = []
        for i, l in enumerate(out):
            if "cmd LC_RPATH" in l: rps.append(re.search(r"path (.*) \(offset", out[i + 2]).group(1))
            if "LC_BUILD_VERSION" in l or "LC_VERSION_MIN_MACOSX" in l:
                for k in range(i, i + 6):
                    m = re.search(r"minos (\d+)\.(\d+)|version (\d+)\.(\d+)", out[k])
                    if m and "minos" in out[k]:
                        v = (int(m.group(1)), int(m.group(2))); minos_max = max(minos_max, v)
                        if v > MAXMIN: bad.append((p, "minos %d.%d" % v))
                        break
        for rp in rps:
            if not rp.startswith(("@loader_path", "@executable_path")): bad.append((p, "absolute rpath " + rp))
        dl = os.path.dirname(os.path.realpath(p))
        names = run(["otool", "-L", p]).stdout.splitlines()[1:]
        ident = (run(["otool", "-D", p]).stdout.splitlines() + [None, None])[1]
        for l in names:
            d = l.strip().split(" (")[0]
            if d == ident or d.startswith(("/usr/lib/", "/System/")): continue
            if not d.startswith("@rpath/"): bad.append((p, "dependency not @rpath: " + d)); continue
            ok = False
            for rp in rps:
                c = os.path.normpath(os.path.join(rp.replace("@loader_path", dl).replace("@executable_path", os.path.join(B, "bin")), d[7:]))
                if os.path.exists(c) and os.path.realpath(c).startswith(B + os.sep): ok = True; break
            if not ok: bad.append((p, "unresolved " + d))
        if ident and not ident.startswith("@rpath/"): bad.append((p, "install name " + ident))
        if run(["codesign", "--verify", "--strict", p]).returncode != 0: bad.append((p, "codesign verify failed"))
# dangling symlinks
dangling = []
for dp, dn, fn in os.walk(B):
    for f in fn + dn:
        q = os.path.join(dp, f)
        if os.path.islink(q) and not os.path.exists(q): dangling.append(os.path.relpath(q, B))
for d in dangling[:20]: bad.append((os.path.join(B, d), "dangling symlink"))
print("Mach-O files checked:", n, "| highest minos:", "%d.%d" % minos_max, "| dangling symlinks:", len(dangling))
# absolute build paths left in text files that the runtime reads
pat = re.compile(rb"/Users/[A-Za-z0-9._-]+/(\.claude-science|phenix|Desktop|Downloads)[^\s\"']*")
leaks = []
for sub in ("etc", "lib/gdk-pixbuf-loaders.cache.in", "share/glib-2.0", "run-coot.sh"):
    p = os.path.join(B, sub)
    for dp, dn, fn in (os.walk(p) if os.path.isdir(p) else [(os.path.dirname(p), [], [os.path.basename(p)])]):
        for f in fn:
            q = os.path.join(dp, f)
            try: data = open(q, "rb").read()
            except OSError: continue
            if not macho(q) and pat.search(data): leaks.append((os.path.relpath(q, B), pat.search(data).group(0).decode()[:90]))
# (build 37) the monomer library stays out of the package; the helper that fetches it is in
if os.path.lexists(os.path.join(B, "monomers")): bad.append((os.path.join(B, "monomers"), "the monomer library must not be in the package (coot0 --fetch-monomers / CCP4's)"))
if not os.access(os.path.join(B, "fetch-monomers.sh"), os.X_OK): bad.append((os.path.join(B, "fetch-monomers.sh"), "missing or not executable"))
print("monomer library in the package:", "yes (BAD)" if os.path.lexists(os.path.join(B, "monomers")) else "no", "| fetch-monomers.sh:", "ok" if os.access(os.path.join(B, "fetch-monomers.sh"), os.X_OK) else "missing")
for b in bad[:40]: print("BAD", os.path.relpath(b[0], B), "|", b[1])
for l in leaks[:20]: print("LEAK", l)
print("RESULT:", "OK" if not bad and not leaks else "FAIL (%d problems, %d text leaks)" % (len(bad), len(leaks)))
sys.exit(1 if bad or leaks else 0)
