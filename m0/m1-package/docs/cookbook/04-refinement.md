# 4. Refinement

*Each recipe stands alone and loads its own copy of the test files (run recipe 1.1 once first; with your own data use
your molecule numbers instead: [How to use a recipe](README.md#how-to-use-a-recipe)).*

Refinement needs a map (recipe 1.5 chooses it). From a script you usually want the result accepted at once,
without the "Accept Refinement?" window: `set_refinement_immediate_replacement(1)`, then the refinement, then
`accept_regularizement()`. **Switch it off again at the end** with `set_refinement_immediate_replacement(0)`, as every
recipe here does: while it is on, refinements you start with the mouse or a key get no Accept window either, and their
moving atoms stay on the screen. (If that happened: type `accept_regularizement()` or `clear_up_moving_atoms()`, then
`set_refinement_immediate_replacement(0)`.)

### 4.1 Refine a range of residues against the map

```python
imol = read_pdb("tutorial-modern.pdb")
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
set_imol_refinement_map(imol_map)
set_refinement_immediate_replacement(1)
refine_zone(imol, "A", 40, 45, "")          # chain A, residues 40-45, no alt conf
accept_regularizement()
print("fit of A41 to the map: %.3f" % density_score_residue(imol, ["A", 41, ""], imol_map))
set_refinement_immediate_replacement(0)      # back to normal: the Accept window again
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(set-imol-refinement-map imol-map)
(set-refinement-immediate-replacement 1)
(refine-zone imol "A" 40 45 "")
(accept-regularizement)
(format #t "fit of A41 to the map: ~a~%" (density-score-residue imol (list "A" 41 "") imol-map))
(set-refinement-immediate-replacement 0)   ; back to normal
```
<!-- check-py: density_score_residue(imol, ["A", 41, ""], imol_map) > 0 -->
<!-- check-scm: (> (density-score-residue imol (list "A" 41 "") imol-map) 0) -->

### 4.2 Refine a list of residues (they need not be next to each other)

```python
imol = read_pdb("tutorial-modern.pdb")
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
set_imol_refinement_map(imol_map)
set_refinement_immediate_replacement(1)
refine_residues(imol, [["A", 41, ""], ["A", 42, ""], ["A", 85, ""]])
accept_regularizement()
set_refinement_immediate_replacement(0)      # back to normal: the Accept window again
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(set-imol-refinement-map imol-map)
(set-refinement-immediate-replacement 1)
(refine-residues imol (list (list "A" 41 "") (list "A" 42 "") (list "A" 85 "")))
(accept-regularizement)
(set-refinement-immediate-replacement 0)   ; back to normal
```

### 4.3 Sphere refine: a residue and everything around it

```python
imol = read_pdb("tutorial-modern.pdb")
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
set_imol_refinement_map(imol_map)
set_refinement_immediate_replacement(1)
centre = ["A", 41, ""]
residues = [centre] + residues_near_residue(imol, centre, 4.0)
refine_residues(imol, residues)
accept_regularizement()
print("refined", len(residues), "residues")
set_refinement_immediate_replacement(0)      # back to normal: the Accept window again
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(set-imol-refinement-map imol-map)
(set-refinement-immediate-replacement 1)
(define centre (list "A" 41 ""))
(define residues (cons centre (residues-near-residue imol centre 4.0)))
(refine-residues imol residues)
(accept-regularizement)
(format #t "refined ~a residues~%" (length residues))
(set-refinement-immediate-replacement 0)   ; back to normal
```
<!-- check-py: len(residues) > 4 -->
<!-- check-scm: (> (length residues) 4) -->

### 4.4 Geometry only (regularize, no map)

```python
imol = read_pdb("tutorial-modern.pdb")
set_refinement_immediate_replacement(1)
regularize_zone(imol, "A", 40, 45, "")
accept_regularizement()
set_refinement_immediate_replacement(0)      # back to normal: the Accept window again
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(set-refinement-immediate-replacement 1)
(regularize-zone imol "A" 40 45 "")
(accept-regularizement)
(set-refinement-immediate-replacement 0)   ; back to normal
```

### 4.5 Map weight and restraints

A smaller weight trusts the geometry more (default 60). Ramachandran and torsion restraints help at low resolution.

```python
set_matrix(30.0)
set_refine_ramachandran_angles(1)
set_refine_with_torsion_restraints(1)
print("weight", matrix_state(), "rama restraints", refine_ramachandran_angles_state())
```

```scheme
(set-matrix 30.0)
(set-refine-ramachandran-angles 1)
(set-refine-with-torsion-restraints 1)
(format #t "weight ~a rama restraints ~a~%" (matrix-state) (refine-ramachandran-angles-state))
```
<!-- check-py: abs(matrix_state() - 30) < 0.01 and refine_ramachandran_angles_state() == 1 -->
<!-- check-scm: (= (refine-ramachandran-angles-state) 1) -->

### 4.6 Rigid-body fit of a range

Note the argument order: first residue, last residue, chain, molecule.

```python
imol = read_pdb("tutorial-modern.pdb")
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
set_imol_refinement_map(imol_map)
set_refinement_immediate_replacement(1)
rigid_body_refine_zone(30, 45, "A", imol)
accept_regularizement()
set_refinement_immediate_replacement(0)      # back to normal: the Accept window again
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(set-imol-refinement-map imol-map)
(set-refinement-immediate-replacement 1)
(rigid-body-refine-zone 30 45 "A" imol)
(accept-regularizement)
(set-refinement-immediate-replacement 0)   ; back to normal
```

### 4.7 Best rotamer for a side chain

Arguments: residue number, alt conf, insertion code, chain, model, map, clash check (1 = yes), lowest rotamer probability.
Returns a score.

```python
imol = read_pdb("tutorial-modern.pdb")
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
score = auto_fit_best_rotamer(41, "", "", "A", imol, imol_map, 1, 0.01)
print("rotamer score", score, "rotamer now", get_rotamer_name(imol, "A", 41, ""))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(define score (auto-fit-best-rotamer 41 "" "" "A" imol imol-map 1 0.01))
(format #t "rotamer score ~a~%" score)
```
<!-- check-py: isinstance(score, float) -->
<!-- check-scm: (number? score) -->

### 4.8 Flip a peptide

Flips the peptide between residue A41 and A42 (the carbonyl O of A41 points the other way).

```python
imol = read_pdb("tutorial-modern.pdb")
before = atom_info_string(imol, "A", 41, "", " O  ", "")[3:]
pepflip(imol, "A", 41, "", "")
after = atom_info_string(imol, "A", 41, "", " O  ", "")[3:]
print("O of A41 moved from", before, "to", after)
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(pepflip imol "A" 41 "" "")
(display (list-tail (atom-info-string imol "A" 41 "" " O  " "") 3)) (newline)
```
<!-- check-py: before != after -->

### 4.9 Refine every chain in pieces (a whole model)

Refines chain by chain in overlapping pieces of 6 residues. It takes about a second per piece.

```python
imol = read_pdb("tutorial-modern.pdb")
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
set_imol_refinement_map(imol_map)
set_refinement_immediate_replacement(1)
for ch in chain_ids(imol):
    n = chain_n_residues(ch, imol)
    first, last = seqnum_from_serial_number(imol, ch, 0), seqnum_from_serial_number(imol, ch, n - 1)
    for start in range(first, min(last, first + 20), 5):      # (the whole chain: range(first, last, 5))
        refine_zone(imol, ch, start, min(start + 5, last), "")
        accept_regularizement()
print("done")
set_refinement_immediate_replacement(0)      # back to normal: the Accept window again
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(set-imol-refinement-map imol-map)
(set-refinement-immediate-replacement 1)
(for-each
  (lambda (ch)
    (let* ((n (chain-n-residues ch imol))
           (first (seqnum-from-serial-number imol ch 0)) (last (seqnum-from-serial-number imol ch (- n 1))))
      (let loop ((start first))
        (if (< start (min last (+ first 20)))          ; the whole chain: (< start last)
            (begin (refine-zone imol ch start (min (+ start 5) last) "")
                   (accept-regularizement)
                   (loop (+ start 5)))))))
  (chain-ids imol))
(set-refinement-immediate-replacement 0)   ; back to normal
```
