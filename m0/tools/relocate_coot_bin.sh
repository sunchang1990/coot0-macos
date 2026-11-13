#!/bin/bash
# relocate_coot_bin.sh LINKED_COOT_BIN OUT_COOT_BIN CANVAS_PREFIX_LIB CONDA_DEPS_ENV CONDA_RDKIT_ENV
# Turns the output of m0_link.py into the coot-bin of the bundle: canvas libraries -> @rpath, the three build rpaths -> @executable_path/../lib,
# ad hoc signature.  (assemble_bundle.py does the same while it builds a whole bundle; this is the shortcut when only coot-bin changed.)
# Install it with   rm -f bundle/bin/coot-bin; cp OUT_COOT_BIN bundle/bin/coot-bin     (never cp over the old file: stale code-signature cache -> SIGKILL)
set -e
IN=$1; OUT=$2; CANVAS=$3; DEPS=$4; RDKIT=$5
cp "$IN" "$OUT"
for l in libart_lgpl_2.2.dylib libgnomecanvas-2.0.dylib libgoocanvas.3.dylib; do install_name_tool -change "$CANVAS/$l" "@rpath/$l" "$OUT"; done
for rp in "$DEPS/lib" "$CANVAS" "$RDKIT/lib"; do install_name_tool -delete_rpath "$rp" "$OUT"; done
install_name_tool -add_rpath @executable_path/../lib "$OUT"
codesign --force -s - "$OUT"
codesign -v "$OUT" && echo "relocated and signed: $OUT"
otool -L "$OUT" | grep -v "@rpath\|/usr/lib\|/System" | tail -n +2 || true
