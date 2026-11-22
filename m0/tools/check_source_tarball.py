#!/usr/bin/env python3
# check_source_tarball.py DIR VERSION  (build 32) -- the source archive that goes next to the Mac package in a release.
# Fails when it is missing (builds up to 31 had none) or incomplete.  Prints PASS/FAIL lines and SUMMARY n / m.
import os, sys, tarfile, re
d, v = sys.argv[1], sys.argv[2]
p = os.path.join(d, "coot0-%s-source.tar.gz" % v)
res = []
def check(name, ok): res.append((name, bool(ok)))
names = []
if os.path.isfile(p):
    with tarfile.open(p) as t:
        names = t.getnames()
        def text(n):
            try: return t.extractfile(n).read().decode("latin-1")
            except Exception: return ""
        top = "coot0-%s-source/" % v
        gi = text(top + "coot-0.9.8.96-patched/src/gtk2-interface.c")
        ps = sorted(n for n in names if re.match(re.escape(top) + r"coot0-macos/m0/patches/\d{4}-.*\.patch$", n))
        check("the patched Coot tree has this build's changes (Help > About notice)", "Copyright (C) 2026 Chang Sun" in gi)
        check("the patched Coot tree has Coot's own sources (more than 1,000 files)", sum(1 for n in names if "/coot-0.9.8.96-patched/" in n) > 1000)
        check("all patches are there, numbered without gaps (%d)" % len(ps), ps and [int(os.path.basename(x)[:4]) for x in ps] == list(range(1, len(ps) + 1)))
        for f in ("LICENSE", "LICENSING.md", "CORRESPONDING_SOURCE.md", "m0/setup.sh", "m0/tools/m0_build.py", "env/coot-deps.explicit.txt", "m0/m1-package/run-coot.sh"):
            check("coot0-macos/%s is there" % f, top + "coot0-macos/" + f in names)
        check("README-SOURCE.txt says what is where", "coot-0.9.8.96-patched/" in text(top + "README-SOURCE.txt"))
        check("no local-only files (CLAUDE.md, evidence/local, objects, binaries)",
              not any(re.search(r"/CLAUDE\.md$|/evidence/local/|\.o$|/obj_b\d+/|/bin_b\d+/|\.dylib$", n) for n in names))
        check("no ._ (macOS metadata) files", not any(os.path.basename(n).startswith("._") for n in names))
else:
    check("%s exists" % os.path.basename(p), False)
for n, ok in res: print(("PASS " if ok else "FAIL ") + n)
print("SUMMARY", sum(1 for r in res if r[1]), "/", len(res))
sys.exit(0 if all(r[1] for r in res) else 1)
