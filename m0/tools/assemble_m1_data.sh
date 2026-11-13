#!/bin/bash
# Assemble the runtime data tree Coot 0.9.8.96 expects (the layout `make install` would give under share/coot).
# usage: assemble_m1_data.sh <coot-src> <dest-package-dir>      (run in env coot-deps: needs $CONDA_PREFIX for syminfo.lib)
set -eu
SRC=$(cd "$1" && pwd); PKG=$2
D=$PKG/share/coot
mkdir -p "$D" "$PKG/test-data" "$PKG/lib" "$PKG/bin" "$PKG/logs"
cp "$SRC/standard-residues.pdb" "$SRC/colours.def" "$SRC/mtrix-to-ncs-matrix.awk" "$D/"
cp "$SRC/src/dynarama.glade" "$SRC/lbg/lbg.glade" "$D/"
# cootrc: the template sets an X11 (XLFD) font for every widget, which Pango on macOS cannot interpret -> use a Pango description
sed 's|font = "-adobe-helvetica-medium-r-normal--\*-75-\*-\*-\*-\*-\*-\*,\*"|font = "Helvetica 10"|' "$SRC/cootrc.template" > "$D/cootrc"
grep -c 'font = "Helvetica 10"' "$D/cootrc" > /dev/null || { echo "cootrc font substitution failed"; exit 1; }
printf '\n# macOS port: icon theme for the file dialogs (installed with the conda dependencies: adwaita-icon-theme, hicolor-icon-theme)\ngtk-icon-theme-name = "Adwaita"\n' >> "$D/cootrc"
# syminfo.lib from libccp4 (same file Coot's configure/make install uses)
cp "$CONDA_PREFIX/share/syminfo.lib" "$D/syminfo.lib"
for sub in data pixmaps rama-data scheme; do
  mkdir -p "$D/$sub"
  rsync -a --exclude 'Makefile*' --exclude '*.am' --exclude '*.in' --exclude 'ChangeLog' "$SRC/$sub/" "$D/$sub/"
done
# Data files that `make install` puts into $(pkgdatadir) from other source directories (Makefile.am files of pdb-templates, protein_db,
# cootaneer, cootilus, fonts, data/rama-coeffs and ligand).  Missing ones made features fail at run time:
#   pdb-templates/*  glycosylation tools ("Add N-linked ...": link-by-torsion-*.tab, *-decorations.tab, *-via-*.pdb) and helix placement
#   protein_db/protein.db  Fit Loop by database search, merge C- and N-termini      cootaneer-llk-2.40.dat  Cootaneer / assign sequence
#   nautilus_lib.pdb  nucleic acid building     data/rama/zo-tables  Zo Ramachandran restraints
#   data/ligands-2016.db  ligand percentiles (Ligand Metric Sliders)     data/assign-side-chains/useable-grid-points-*.data  side-chain assignment
rsync -a --exclude 'Makefile*' "$SRC/pdb-templates/" "$D/"
mkdir -p "$D/protein_db" "$D/fonts" "$D/data/rama/zo-tables" "$D/data/assign-side-chains"
cp "$SRC/protein_db/protein.db" "$D/protein_db/"
cp "$SRC/cootaneer/cootaneer-llk-2.40.dat" "$SRC/cootilus/nautilus_lib.pdb" "$D/"
rsync -a --exclude 'Makefile*' "$SRC/fonts/" "$D/fonts/"
cp "$SRC/data/rama-coeffs/all-non-pre-pro.tab" "$SRC/data/rama-coeffs/coeffsolution.dat" "$D/data/rama/zo-tables/"
cp "$SRC/ligand/ligands-2016.db" "$D/data/"
cp "$SRC/ligand/useable-grid-points-nstep=5,box_radius=5.0-charybdis.data" "$D/data/assign-side-chains/"
# Lidia (ligand builder) toolbar icons: lbg.glade refers to them as pixmaps/*.svg, `make install` puts lbg/*.svg in $(pkgdatadir)/pixmaps
cp "$SRC"/lbg/*.svg "$D/pixmaps/"
# reference-structures/*.pdb: the PDB files Ca -> Mainchain (db_mainchain) and strand building match against.  The 0.9.8.96 release tarball does
# not contain them (Coot's git repository does: github.com/pemsley/coot/reference-structures, GPL).  Fetched once, checked against
# tools/reference-structures.manifest (git blob sha1), cached in $COOT_REFSTRUCTS_CACHE (default: ${TMPDIR:-/tmp}/coot-refstructs-cache).
TOOLS=$(cd "$(dirname "$0")" && pwd)
RS_CACHE=${COOT_REFSTRUCTS_CACHE:-${TMPDIR:-/tmp}/coot-refstructs-cache}
python - "$TOOLS/reference-structures.manifest" "$RS_CACHE" "$D/reference-structures" "$SRC" <<'PYEOF'
import sys, os, hashlib, shutil, urllib.request
manifest, cache, dest, src = sys.argv[1:5]
os.makedirs(cache, exist_ok=True); os.makedirs(dest, exist_ok=True)
n = 0
for line in open(manifest):
    if line.startswith('#') or not line.strip(): continue
    name, size, blob, sha256 = line.split()
    own = os.path.join(src, 'reference-structures', name)       # a source tree that has the directory (git checkout) wins
    cached = os.path.join(cache, name)
    if os.path.exists(own): data = open(own, 'rb').read()
    elif os.path.exists(cached): data = open(cached, 'rb').read()
    else:
        data = urllib.request.urlopen('https://raw.githubusercontent.com/pemsley/coot/main/reference-structures/' + name, timeout=120).read()
    assert hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest() == blob, 'reference structure %s does not match the manifest' % name
    open(cached, 'wb').write(data); open(os.path.join(dest, name), 'wb').write(data); n += 1
print('reference-structures: %d files verified' % n)
PYEOF
cp "$TOOLS/reference-structures.manifest" "$D/reference-structures/SOURCE.txt"      # (where the files come from, with their checksums)
# start-up pictures (tools/splash: see README.txt there): replace the original 580 x 478 picture, add the 2x one for bin/coot-splash
cp "$TOOLS/splash/coot-0.9.8.96.png" "$TOOLS/splash/coot-splash@2x.png" "$D/pixmaps/"
# python layer: SWIG-generated coot.py + python/*.py (COOT_PYTHON_DIR)
mkdir -p "$D/python"
cp "$SRC/src/coot.py" "$D/python/coot.py"
for f in "$SRC"/python/*.py; do cp "$f" "$D/python/"; done
# test data shipped in the tree
cp "$SRC/data/tutorial-modern.pdb" "$SRC/data/rnasa-1.8-all_refmac1.mtz" "$SRC/standard-residues.pdb" "$PKG/test-data/"
# scripted GUI: the PyGTK 2 compatibility layer (compat/pygtk2) and its generated data (C prototypes and constants from the GTK headers of $CONDA_PREFIX)
PYG="$SRC/compat/pygtk2"
rm -rf "$D/python/gtk"; cp -R "$PYG/gtk" "$D/python/gtk"; rm -rf "$D/python/gtk/__pycache__"   # (rm first: cp -R into an existing dir nests it)
cp "$PYG/gobject.py" "$PYG/pango.py" "$PYG/pygtk.py" "$PYG/coot_python.py" "$PYG/_gtk2core.py" "$D/python/"
python "$PYG/tools/gen_gtk_protos.py" "$CONDA_PREFIX" "$D/python/_gtk2_protos.json"
python "$PYG/tools/gen_gtk_consts.py" "$CONDA_PREFIX" "$D/python/_gtk2_consts.json"
# RCrane (loaded by python/rcrane_loader.py)
rm -rf "$D/python/rcrane"; cp -R "$SRC/rcrane" "$D/python/rcrane"; rm -f "$D/python/rcrane"/Makefile* "$D/python/rcrane"/*.in "$D/python/rcrane/installRCrane.py"   # installRCrane.py = stand-alone installer for old Coots, not needed
mkdir -p "$PKG/tests"
cp "$PYG/tests/selftest.py" "$PKG/tests/gtk2compat_selftest.py"
python "$PYG/tools/gen_menu_structure.py" "$SRC/src/gtk2-interface.c" "$PKG/tests/menubar.json"
echo "data tree assembled in $D"; du -sh "$D" | cut -f1
