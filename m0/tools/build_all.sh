#!/bin/bash
# build_all.sh [OUTDIR]  (build 37) -- from a bootstrapped clone (./bootstrap.sh) to a self-contained coot0 folder:
#   1. compile Coot (412 files, a few minutes)   2. link bin/coot-bin with the macOS OpenGL view (compat/gl-seam)
#   3. stage: the package files (m0/m1-package) + Coot's data tree (tools/assemble_m1_data.sh)
#   4. bundle: copy every library Coot needs, relocated and signed (tools/assemble_bundle.py), then tools/bundle_check.py
# OUTDIR defaults to m0/build; the result is OUTDIR/bundle (run it: OUTDIR/bundle/run-coot.sh).  Make the installer from it:
#   m0/tools/make_binary_tarball.sh OUTDIR/bundle
set -eu
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="${1:-$ROOT/m0/build}"; mkdir -p "$OUT"; OUT="$(cd "$OUT" && pwd)"
case "$ROOT" in *" "*) echo "the clone's path contains a space ($ROOT): move it to a path without spaces (see BUILDING.md)"; exit 1;; esac
ENVS="${COOT0_ENVS:-$ROOT/envs}"
DEPS="$ENVS/coot-deps"; RDKIT="$ENVS/coot-rdkit"
[ -d "$DEPS" ] && [ -d "$RDKIT" ] || { echo "conda environments not found in $ENVS: run ./bootstrap.sh --make-envs first"; exit 1; }
[ -f "$ROOT/canvas/prefix/lib/libgoocanvas.3.dylib" ] || { echo "canvas libraries not found: run ./bootstrap.sh first"; exit 1; }
[ -d "$ROOT/m0/coot-src/.git" ] || { echo "m0/coot-src not found: run ./bootstrap.sh first"; exit 1; }
export CONDA_PREFIX="$DEPS" PATH="$DEPS/bin:$PATH"
export PKG_CONFIG_PATH="$DEPS/lib/pkgconfig:$DEPS/share/pkgconfig"
T="$ROOT/m0/tools"; SRC="$ROOT/m0/coot-src"; CAN="$ROOT/canvas/prefix"

echo "== 1. compile ($OUT/obj)"
python "$T/m0_build.py" compile "$OUT/compile.json" --stubs gtkglext --prefix "$CAN" --with-libs --objdir "$OUT/obj" \
    --src "$SRC" --rdkit "$RDKIT" --pygtk | tail -3
echo "== 2. link ($OUT/bin/coot-bin)"
mkdir -p "$OUT/bin"
python "$T/m0_link.py" "$OUT/compile.json" "$OUT/obj" "$OUT/bin/coot-bin" --prefix "$CAN" \
    --seam "$SRC/compat/gl-seam/coot-gl-seam.mm" --rdkit "$RDKIT" | tail -2
[ -x "$OUT/bin/coot-bin" ] || { echo "link failed"; exit 1; }
echo "== 3. stage ($OUT/stage)"
rm -rf "${OUT:?}/stage"; mkdir -p "$OUT/stage"
rsync -a --exclude logs --exclude work --exclude home --exclude .cache --exclude results --exclude monomers --exclude __pycache__ \
    "$ROOT/m0/m1-package/" "$OUT/stage/"
mkdir -p "$OUT/stage/results"; cp "$ROOT/m0/m1-package/results/answers.txt" "$OUT/stage/results/"
for f in LICENSE LICENSING.md CORRESPONDING_SOURCE.md README.md; do cp "$ROOT/$f" "$OUT/stage/"; done
bash "$T/assemble_m1_data.sh" "$SRC" "$OUT/stage" | tail -2
# the start-up picture window (AppKit), shown until Coot's main window is up (run-coot.sh)
mkdir -p "$OUT/stage/bin"
/usr/bin/clang -O2 -fobjc-arc -arch arm64 -mmacosx-version-min="${COOT_MIN_MACOS:-11.0}" -framework Cocoa \
    -o "$OUT/stage/bin/coot-splash" "$SRC/compat/splash/coot-splash.m"
echo "== 4. bundle ($OUT/bundle)"
rm -rf "${OUT:?}/bundle"
python "$T/assemble_bundle.py" --coot-bin "$OUT/bin/coot-bin" --canvas-lib "$CAN/lib" --env "$DEPS" --stage "$OUT/stage" --out "$OUT/bundle" | tail -3
/usr/bin/python3 "$T/bundle_check.py" "$OUT/bundle" | tail -3
echo "== done: $OUT/bundle  (version $(cat "$OUT/bundle/VERSION"))"
echo "   try it:          $OUT/bundle/run-coot.sh"
echo "   self-test:       $OUT/bundle/tests/run-headless-tests.sh"
echo "   the installer:   m0/tools/make_binary_tarball.sh $OUT/bundle"
