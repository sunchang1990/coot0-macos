#!/bin/bash
# relink_b31.sh OBJDIR BINDIR -- link coot-bin from OBJDIR and relocate it (canvas install names -> @rpath, build rpaths
# -> @executable_path/../lib, ad hoc signature), as done by hand for builds 26-30 (README-m0 Round 26/28).
set -e
cd "$(dirname "$0")/../.."
OBJ="$1"; BIN="$2"; E=~/.claude-science/conda/envs
export CONDA_PREFIX=$E/coot-deps PATH=$E/coot-deps/bin:$PATH
cp m0/obj_b26/out.json out.json; mkdir -p "$BIN"
python m0/tools/m0_link.py out.json "$OBJ" "$BIN/coot-bin" --prefix $PWD/canvas/prefix --seam m0/coot-src/compat/gl-seam/coot-gl-seam.mm --rdkit $E/coot-rdkit | tail -1
cp "$BIN/coot-bin" "$BIN/coot-bin.reloc"
OLD=$(otool -L "$BIN/coot-bin" | awk '/libgoocanvas/{print $1}' | xargs dirname)
for l in libart_lgpl_2.2 libgnomecanvas-2.0 libgoocanvas.3; do install_name_tool -change "$OLD/$l.dylib" "@rpath/$l.dylib" "$BIN/coot-bin.reloc" 2>/dev/null; done
for r in $E/coot-deps/lib $PWD/canvas/prefix/lib $E/coot-rdkit/lib; do install_name_tool -delete_rpath "$r" "$BIN/coot-bin.reloc" 2>/dev/null; done
install_name_tool -add_rpath @executable_path/../lib "$BIN/coot-bin.reloc" 2>/dev/null
codesign --force -s - "$BIN/coot-bin.reloc" 2>/dev/null
echo "absolute install names left: $(otool -L "$BIN/coot-bin.reloc" | grep -c /Users/)"
