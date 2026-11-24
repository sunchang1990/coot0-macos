#!/bin/bash
# make_binary_tarball.sh BUNDLE [OUTDIR]  (build 37) -- the installer package: OUTDIR/coot0-<VERSION>-macos-arm64.tar.gz
# from a bundle made by m0/tools/build_all.sh (or a working copy of one).  Users unpack it and run ./install.sh.
# Leaves out everything a run makes (logs, work, home, .cache, results, __pycache__, the install marker), any monomer
# library (coot0 uses CCP4's or fetches it), and macOS metadata (._ files).  OUTDIR defaults to the current folder.
# Also see m0/tools/make_source_tarball.sh (the matching source archive, for the same GitHub Release).
set -eu
B="$(cd "${1:?usage: make_binary_tarball.sh BUNDLE [OUTDIR]}" && pwd)"
OUTDIR="${2:-$PWD}"; mkdir -p "$OUTDIR"; OUTDIR="$(cd "$OUTDIR" && pwd)"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
V="$(cat "$B/VERSION")"; N="coot0-$V"
[ -x "$B/bin/coot-bin" ] && [ -x "$B/install.sh" ] || { echo "$B does not look like a coot0 bundle (bin/coot-bin, install.sh)"; exit 1; }
T="$(mktemp -d)"; trap 'rm -rf "${T:?}"' EXIT
rsync -a --exclude /.cache --exclude '/logs/*' --exclude '/work/*' --exclude '/results/*' --exclude '/home/*' --exclude /monomers \
    --exclude __pycache__ --exclude .coot0-installed --exclude coot-backup --exclude .DS_Store --exclude '0-coot-history.*' \
    --exclude '0-coot.state.*' "$B/" "$T/$N/"
mkdir -p "$T/$N/logs" "$T/$N/work" "$T/$N/results" "$T/$N/home"
cp "$ROOT/m0/m1-package/results/answers.txt" "$T/$N/results/answers.txt"
# the compiled Python wrapper of Coot's own functions (one large file): kept when a run already made it, saves the first start
P=share/coot/python/__pycache__/coot.cpython-311.pyc
[ -f "$B/$P" ] && { mkdir -p "$T/$N/$(dirname $P)"; cp -p "$B/$P" "$T/$N/$P"; }
( cd "$T" && COPYFILE_DISABLE=1 tar --no-mac-metadata --no-xattrs -czf "$OUTDIR/$N-macos-arm64.tar.gz" "$N" )
echo "$OUTDIR/$N-macos-arm64.tar.gz"
/usr/bin/shasum -a 256 "$OUTDIR/$N-macos-arm64.tar.gz" | cut -c1-64
