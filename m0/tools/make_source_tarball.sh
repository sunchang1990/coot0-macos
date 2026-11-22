#!/bin/bash
# make_source_tarball.sh VERSION OUTDIR  (build 32)
# Writes OUTDIR/coot0-VERSION-source.tar.gz: the Corresponding Source of the coot0 part of the binary package, to attach to
# each GitHub Release next to the Mac package (GPL v3 section 6d: the source offered from the same place).  It holds:
#   coot-0.9.8.96-patched/   the exact Coot source tree that was compiled (release tarball + m0/patches, as m0/setup.sh makes it)
#   coot0-macos/             this repository at HEAD: patches, build/packaging tools, launcher, tests, docs, pinned environments
#   README-SOURCE.txt        what is where, and where the bundled third-party libraries' source is (CORRESPONDING_SOURCE.md)
# Committed files only (git archive): nothing ignored (local notes, evidence/local, build outputs) gets in.
set -e
V="${1:?usage: make_source_tarball.sh VERSION OUTDIR}"; OUT="${2:?usage: make_source_tarball.sh VERSION OUTDIR}"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"; export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1
[ -z "$(git -C "$ROOT/m0/coot-src" status --porcelain)" ] || { echo "m0/coot-src has unrecorded changes: record a patch first" >&2; exit 2; }
[ -z "$(git -C "$ROOT" status --porcelain -- m0/patches)" ] || { echo "m0/patches has uncommitted changes: commit first" >&2; exit 2; }
N="coot0-$V-source"; T="$(mktemp -d)"; trap 'rm -rf "${T:?}"' EXIT
mkdir -p "$T/$N"
git -C "$ROOT/m0/coot-src" archive --prefix="coot-0.9.8.96-patched/" HEAD | tar -x -C "$T/$N"
git -C "$ROOT" archive --prefix="coot0-macos/" HEAD | tar -x -C "$T/$N"
cat > "$T/$N/README-SOURCE.txt" <<EOF
coot0 $V: source code
=====================

coot0 is Coot 0.9.8.96 modified to run on macOS on Apple Silicon.  This archive is the source of the coot0 package
coot0-$V-macos-arm64.tar.gz.

  coot-0.9.8.96-patched/   the Coot source tree that was compiled: the Coot 0.9.8.96 release tarball with the
                           numbered patches of coot0-macos/m0/patches/ applied (coot0-macos/m0/setup.sh does this).
  coot0-macos/             the coot0 repository (git commit $(git -C "$ROOT" rev-parse --short HEAD)): patches, build and packaging tools
                           (m0/tools/), launcher, installer, tests and documents (m0/m1-package/), pinned build
                           environments (env/).  Build notes: coot0-macos/m0/README-m0.txt.

Licences: coot0-macos/LICENSING.md and coot0-macos/LICENSE (GNU GPL version 3).
The bundled third-party libraries (GTK 2, Python, Guile, RDKit, ...) are not in this archive; where to get the source of
each is in coot0-macos/CORRESPONDING_SOURCE.md, which also has the written offer to provide it.
Repository and problem reports: https://github.com/sunchang1990/coot0-macos
EOF
mkdir -p "$OUT"
( cd "$T" && COPYFILE_DISABLE=1 tar --no-mac-metadata --no-xattrs -czf "$N.tar.gz" "$N" )
mv "$T/$N.tar.gz" "$OUT/"
ls -l "$OUT/$N.tar.gz" | awk '{print $5, $9}'
