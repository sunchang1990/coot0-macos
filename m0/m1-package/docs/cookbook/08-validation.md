# 8. Validation

### 8.1 Ramachandran: residues outside the allowed regions

`all_molecule_ramachandran_region` gives every residue with a region number: 2 = preferred, 1 = allowed, 0 = outlier.

```python
imol = read_pdb("tutorial-modern.pdb")
regions = all_molecule_ramachandran_region(imol)
outliers = [spec[1:] for spec, region in regions if region == 0]
allowed = [spec[1:] for spec, region in regions if region == 1]
print(len(regions), "residues;", len(allowed), "allowed;", len(outliers), "outliers:", outliers)
```

This function exists only in Python; from Scheme, ask Python for the list:

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define regions
  (run-python-command (format #f "[[s[1], s[2], r] for s, r in all_molecule_ramachandran_region(~a)]" imol)))
(define outliers (filter (lambda (r) (= (list-ref r 2) 0)) regions))
(format #t "~a residues; ~a outliers: ~a~%" (length regions) (length outliers) outliers)
```
<!-- check-py: len(regions) > 150 -->
<!-- check-scm: (> (length regions) 150) -->

### 8.2 Fit to the map: the worst residues

Correlation of model and map per residue (1 = perfect). The 0 means: use all atoms of the residue.

```python
imol = read_pdb("tutorial-modern.pdb")
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
specs = [r[1:] for r in all_residues(imol)]
cc = map_to_model_correlation_per_residue(imol, specs, 0, imol_map)
for spec, c in sorted(cc, key=lambda x: x[1])[:5]:
    print("%s %d  CC %.2f" % (spec[1], spec[2], c))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(define specs (map cdr (all-residues imol)))
(define cc (map-to-model-correlation-per-residue imol specs 0 imol-map))
(for-each (lambda (x) (format #t "~a CC ~,2f~%" (car x) (cadr x)))
          (list-head (sort cc (lambda (a b) (< (cadr a) (cadr b)))) 5))
```
<!-- check-py: len(cc) == 189 -->
<!-- check-scm: (= (length cc) 189) -->

### 8.3 Rotamers

Score of one side chain and of the whole model (higher is better).

```python
imol = read_pdb("tutorial-modern.pdb")
print("A41:", rotamer_score(imol, "A", 41, "", ""))
score, n = all_molecule_rotamer_score(imol)
print("whole model: %.1f over %d side chains" % (score, n))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(format #t "A41: ~a~%" (rotamer-score imol "A" 41 "" ""))
(format #t "whole model: ~a~%" (all-molecule-rotamer-score imol))
```
<!-- check-py: n == 160 -->

### 8.4 Geometry: the worst restraints of a residue

Needs a refinement map (it returns `False` / `#f` without one).

```python
imol = read_pdb("tutorial-modern.pdb")
set_imol_refinement_map(make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0))
d = residues_distortions(imol, [["A", 41, ""]])
for item in sorted(d, key=lambda x: -x["distortion_score"])[:3]:
    print(item["restraint"]["restraint_type"], "distortion %.1f" % item["distortion_score"])
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(set-imol-refinement-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(display (length (residues-distortions-scm imol (list (list "A" 41 ""))))) (display " restraints scored\n")
```
<!-- check-py: len(d) > 5 -->

### 8.5 Cis peptides and wrong chiral centres

```python
imol = read_pdb("tutorial-modern.pdb")
for first, second, omega in cis_peptides(imol):
    print("cis peptide %s%d-%s%d  omega %.0f" % (first[1], first[2], second[1], second[2], omega))
print("chiral volume problems:", chiral_volume_errors(imol))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(for-each (lambda (c) (format #t "cis peptide ~a~%" c)) (cis-peptides imol))
(format #t "chiral volume problems: ~a~%" (chiral-volume-errors imol))
```
<!-- check-py: len(cis_peptides(imol)) == 3 -->
<!-- check-scm: (= (length (cis-peptides imol)) 3) -->

### 8.6 Atoms that overlap (clashes)

```python
imol = read_pdb("tutorial-modern.pdb")
overlaps = molecule_atom_overlaps(imol)
for o in sorted(overlaps, key=lambda x: -x["overlap-volume"])[:5]:
    a, b = o["atom-1-spec"], o["atom-2-spec"]
    print("%s%d %s - %s%d %s  overlap %.1f A^3" % (a[1], a[2], a[4], b[1], b[2], b[4], o["overlap-volume"]))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(format #t "~a overlapping atom pairs~%" (length (molecule-atom-overlaps imol)))
```
<!-- check-py: len(overlaps) > 0 -->

### 8.7 Peaks in the difference map

Positions (x, y, z) of difference-map peaks above 4 rmsd.

```python
imol_diff = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "DELFWT", "PHDELWT", "", 0, 1)
peaks = map_peaks(imol_diff, 4.0)
print(len(peaks), "peaks; first:", peaks[:2])
```

```scheme
(define imol-diff (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "DELFWT" "PHDELWT" "" 0 1))
(define peaks (map-peaks imol-diff 4.0))
(format #t "~a peaks~%" (length peaks))
```
<!-- check-py: len(peaks) > 0 -->
<!-- check-scm: (> (length peaks) 0) -->

### 8.8 Density not explained by the model (unmodelled blobs)

Blobs above 1.0 rmsd in the 2Fo-Fc map that are not near the model: position and size.

```python
imol = read_pdb("tutorial-modern.pdb")
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
blobs = find_blobs(imol, imol_map, 1.0)
for pos, size in blobs[:3]:
    print("blob at %.1f %.1f %.1f  size %.0f" % (pos[0], pos[1], pos[2], size))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(format #t "~a blobs~%" (length (find-blobs imol imol-map 1.0)))
```
<!-- check-py: len(blobs) > 0 -->
