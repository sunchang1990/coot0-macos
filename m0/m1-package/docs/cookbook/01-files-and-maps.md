# 1. Files and maps

*Each recipe stands alone and loads its own copy of the test files (run recipe 1.1 once first; with your own data use
your molecule numbers instead: [How to use a recipe](README.md#how-to-use-a-recipe)).*

Every recipe works on the test files that come with coot0 (`test-data/` in the package): `tutorial-modern.pdb`
(chains A and B, residues A1-A93 and B1-B96, space group P 2<sub>1</sub>2<sub>1</sub>2<sub>1</sub>) and
`rnasa-1.8-all_refmac1.mtz` (map coefficients `FWT`/`PHWT` and difference map `DELFWT`/`PHDELWT`).
Replace the file names with your own; use the full path (for example `"/Users/me/data/model.pdb"`) when the file is
not in the folder Coot works in.

### 1.1 Copy the test files into the folder Coot works in

Run this once, then the file names of the other recipes work as they are.

```python
import os, shutil
test_data = os.path.join(os.environ["COOT_PREFIX"], "test-data")
for f in ["tutorial-modern.pdb", "rnasa-1.8-all_refmac1.mtz"]:
    shutil.copy(os.path.join(test_data, f), f)
print("Coot works in", os.getcwd())
```

```scheme
(let ((test-data (string-append (getenv "COOT_PREFIX") "/test-data")))
  (for-each (lambda (f) (copy-file (string-append test-data "/" f) f))
            (list "tutorial-modern.pdb" "rnasa-1.8-all_refmac1.mtz")))
(display (getcwd)) (newline)
```
<!-- check-py: os.path.exists("rnasa-1.8-all_refmac1.mtz") -->
<!-- check-scm: (file-exists? "tutorial-modern.pdb") -->

### 1.2 Read a model and keep its molecule number

`read_pdb` reads PDB and mmCIF files and returns the new molecule number (-1 if the file could not be read).
Keep it in a variable: molecule numbers are never reused within a session.

```python
imol = read_pdb("tutorial-modern.pdb")
print("molecule", imol, "chains", chain_ids(imol))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(format #t "molecule ~a chains ~a~%" imol (chain-ids imol))
```
<!-- check-py: chain_ids(imol) == ["A", "B"] -->
<!-- check-scm: (equal? (chain-ids imol) (list "A" "B")) -->

### 1.3 Make the 2Fo-Fc and the difference map from an MTZ file

The last two numbers: use the weight column (0 = no), and is it a difference map (1 = yes).

```python
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
imol_diff = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "DELFWT", "PHDELWT", "", 0, 1)
print("maps", imol_map, imol_diff, "rmsd of the 2Fo-Fc map", map_sigma(imol_map))
```

```scheme
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(define imol-diff (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "DELFWT" "PHDELWT" "" 0 1))
(format #t "maps ~a ~a rmsd ~a~%" imol-map imol-diff (map-sigma imol-map))
```
<!-- check-py: is_valid_map_molecule(imol_map) and is_valid_map_molecule(imol_diff) and map_is_difference_map(imol_diff) -->
<!-- check-scm: (and (valid-map-molecule? imol-map) (= (map-is-difference-map imol-diff) 1)) -->

### 1.4 Read all maps of an MTZ file at once

Finds the usual column pairs (FWT/PHWT, DELFWT/PHDELWT, ...) by itself and returns the new map numbers
(a list in Python, a vector such as `#(1 2)` in Scheme).

```python
maps = auto_read_make_and_draw_maps("rnasa-1.8-all_refmac1.mtz")
print("new maps:", maps)
```

```scheme
(define maps (auto-read-make-and-draw-maps "rnasa-1.8-all_refmac1.mtz"))
(format #t "new maps: ~a~%" maps)
```
<!-- check-py: len(maps) == 2 -->
<!-- check-scm: (= (vector-length maps) 2) -->

### 1.5 Choose the map that refinement uses

```python
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
set_imol_refinement_map(imol_map)
print("refinement map:", imol_refinement_map())
```

```scheme
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(set-imol-refinement-map imol-map)
(format #t "refinement map: ~a~%" (imol-refinement-map))
```
<!-- check-py: imol_refinement_map() == imol_map -->
<!-- check-scm: (= (imol-refinement-map) imol-map) -->

### 1.6 Contour level and map radius

Contour at 1.5 rmsd ("sigma") and draw the map 15 Å around the centre. (Map colour: recipe 6.4.)

```python
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
set_contour_level_in_sigma(imol_map, 1.5)
set_map_radius(15)
print("contour level:", get_contour_level_in_sigma(imol_map), "sigma")
```

```scheme
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(set-contour-level-in-sigma imol-map 1.5)
(set-map-radius 15)
(format #t "contour level: ~a sigma~%" (get-contour-level-in-sigma imol-map))
```
<!-- check-py: abs(get_contour_level_in_sigma(imol_map) - 1.5) < 0.01 -->
<!-- check-scm: (< (abs (- (get-contour-level-in-sigma imol-map) 1.5)) 0.01) -->

### 1.7 Save a model (PDB or mmCIF) and part of it

```python
imol = read_pdb("tutorial-modern.pdb")
write_pdb_file(imol, "model-saved.pdb")
write_cif_file(imol, "model-saved.cif")
write_residue_range_to_pdb_file(imol, "A", 30, 45, "chainA-30-45.pdb")
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(write-pdb-file imol "model-saved.pdb")
(write-cif-file imol "model-saved.cif")
(write-residue-range-to-pdb-file imol "A" 30 45 "chainA-30-45.pdb")
```
<!-- check-py: all(os.path.getsize(f) > 1000 for f in ["model-saved.pdb", "model-saved.cif", "chainA-30-45.pdb"]) -->
<!-- check-scm: (and (file-exists? "model-saved.cif") (file-exists? "chainA-30-45.pdb")) -->

### 1.8 Save a map to a file and read it back

`export_map` writes a CCP4/MRC map; `handle_read_ccp4_map` reads one (second argument: 1 for a difference map).

```python
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
export_map(imol_map, "rnasa-2fofc.map")
imol_again = handle_read_ccp4_map("rnasa-2fofc.map", 0)
print("map read back as molecule", imol_again)
```

```scheme
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(export-map imol-map "rnasa-2fofc.map")
(define imol-again (handle-read-ccp4-map "rnasa-2fofc.map" 0))
(format #t "map read back as molecule ~a~%" imol-again)
```
<!-- check-py: is_valid_map_molecule(imol_again) -->
<!-- check-scm: (valid-map-molecule? imol-again) -->

### 1.9 List what is loaded

```python
read_pdb("tutorial-modern.pdb")
make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
for i in model_molecule_list():
    print("model", i, molecule_name(i))
for i in map_molecule_list():
    print("map  ", i, molecule_name(i))
```

```scheme
(read-pdb "tutorial-modern.pdb")
(make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0)
(for-each (lambda (i) (format #t "model ~a ~a~%" i (molecule-name i))) (model-molecule-list))
(for-each (lambda (i) (format #t "map   ~a ~a~%" i (molecule-name i))) (map-molecule-list))
```
<!-- check-py: len(model_molecule_list()) == 1 and len(map_molecule_list()) == 1 -->
<!-- check-scm: (= (length (map-molecule-list)) 1) -->

### 1.10 Cell, space group and close a molecule

```python
imol = read_pdb("tutorial-modern.pdb")
print("cell", cell(imol), "space group", show_spacegroup(imol))
close_molecule(imol)
print("still valid?", is_valid_model_molecule(imol))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(format #t "cell ~a space group ~a~%" (cell imol) (show-spacegroup imol))
(close-molecule imol)
(format #t "still valid? ~a~%" (valid-model-molecule? imol))
```
<!-- check-py: not is_valid_model_molecule(imol) -->
<!-- check-scm: (not (valid-model-molecule? imol)) -->
