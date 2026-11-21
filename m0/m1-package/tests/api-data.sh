#!/bin/bash
# api-data.sh DIR   (build 31) -- fresh copies of the test files the scripting examples of docs/api use, in DIR:
# test-data/*.pdb, *.mtz, *.fasta, *.cif (structure factors and a small molecule, build 31) and two dictionaries from the monomer library (NAG.cif, ATP.cif).
# (The map file rnasa-map.map is written by the example run itself, from molecule 1.)
HERE="$(cd "$(dirname "$0")/.." && pwd)"; D="$1"; mkdir -p "$D"
rm -f "$D/rnasa-map.map"
cp "$HERE"/test-data/*.pdb "$HERE"/test-data/*.mtz "$HERE"/test-data/*.fasta "$HERE"/test-data/*.cif "$D/"
cp "$HERE"/monomers/n/NAG.cif "$HERE"/monomers/a/ATP.cif "$D/" 2>/dev/null
exit 0
