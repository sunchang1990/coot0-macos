#!/bin/bash
# Assemble the M1 test package: data tree + coot-bin + canvas libraries (relocatable install names, ad-hoc signed).
# usage: assemble_m1_package.sh <staging-package-dir> <destination> <coot-bin> <canvas-prefix>      (env coot-deps)
set -eu
STAGE=$1; DEST=$2; BIN=$3; CANVAS=$4
mkdir -p "$DEST"
rsync -a --delete --exclude 'logs/*' --exclude '.cache' --exclude 'work' --exclude 'results' --exclude 'coot-backup' --exclude '.DS_Store' "$STAGE/" "$DEST/"
mkdir -p "$DEST/bin" "$DEST/lib" "$DEST/logs" "$DEST/work" "$DEST/results"
[ -f "$DEST/results/answers.txt" ] || cp "$STAGE/results/answers.txt" "$DEST/results/answers.txt"   # never overwrite the tester's answers
cp "$BIN" "$DEST/bin/coot-bin"
for l in libart_lgpl_2.2.dylib libgnomecanvas-2.0.dylib libgoocanvas.3.dylib; do
  cp -L "$CANVAS/lib/$l" "$DEST/lib/$l"
  chmod u+w "$DEST/lib/$l"
done
fix() {   # make references to the build-tree canvas prefix relocatable
  local f=$1
  otool -L "$f" | awk 'NR>1{print $1}' | grep "/canvas/prefix/lib/" | while read dep; do
    install_name_tool -change "$dep" "@rpath/$(basename "$dep")" "$f"
  done
}
for l in "$DEST"/lib/*.dylib; do
  install_name_tool -id "@rpath/$(basename "$l")" "$l"
  fix "$l"
done
fix "$DEST/bin/coot-bin"
# rpaths: the package lib dir, remove build-tree rpaths that will not exist elsewhere
install_name_tool -add_rpath "@executable_path/../lib" "$DEST/bin/coot-bin" 2>/dev/null || true
for l in "$DEST"/lib/*.dylib; do install_name_tool -add_rpath "@loader_path" "$l" 2>/dev/null || true; done
otool -l "$DEST/bin/coot-bin" | awk '/cmd LC_RPATH/{f=1} f&&/path /{print $2; f=0}' | grep "/canvas/prefix/lib" | while read rp; do
  install_name_tool -delete_rpath "$rp" "$DEST/bin/coot-bin"
done
# modified Mach-O files lose their signature: re-sign ad hoc (required on Apple Silicon) and verify
for f in "$DEST"/lib/*.dylib "$DEST/bin/coot-bin"; do
  codesign --force --sign - "$f" 2>&1 | grep -v "replacing existing signature" || true
  codesign --verify --strict "$f"
done
echo "package assembled in $DEST"
