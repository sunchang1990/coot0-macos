# 5. Editing a model

*Each recipe stands alone and loads its own copy of the test files (run recipe 1.1 once first; with your own data use
your molecule numbers instead: [How to use a recipe](README.md#how-to-use-a-recipe)).*

Every edit can be undone with Edit > Undo, or `apply_undo()` from a script (see 5.12).
Save your model first (recipe 1.7).

### 5.1 Copy a molecule

```python
imol = read_pdb("tutorial-modern.pdb")
imol_copy = copy_molecule(imol)
print("copy is molecule", imol_copy, molecule_name(imol_copy))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-copy (copy-molecule imol))
(format #t "copy is molecule ~a ~a~%" imol-copy (molecule-name imol-copy))
```
<!-- check-py: chain_n_residues("B", imol_copy) == 96 -->
<!-- check-scm: (= (chain-n-residues "B" imol-copy) 96) -->

### 5.2 Copy one chain or a piece into a new molecule

```python
imol = read_pdb("tutorial-modern.pdb")
imol_chain_b = new_molecule_by_atom_selection(imol, "//B")
imol_loop = new_molecule_by_atom_selection(imol, "//A/20-30")
print(chain_ids(imol_chain_b), chain_n_residues("A", imol_loop))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-chain-b (new-molecule-by-atom-selection imol "//B"))
(define imol-loop (new-molecule-by-atom-selection imol "//A/20-30"))
(format #t "~a ~a~%" (chain-ids imol-chain-b) (chain-n-residues "A" imol-loop))
```
<!-- check-py: chain_ids(imol_chain_b) == ["B"] and chain_n_residues("A", imol_loop) == 11 -->
<!-- check-scm: (equal? (chain-ids imol-chain-b) (list "B")) -->

### 5.3 Delete a residue, a range, a side chain, an atom

```python
imol = read_pdb("tutorial-modern.pdb")
delete_residue(imol, "A", 93, "")                 # one residue
delete_residue_range(imol, "B", 94, 96)           # B94 to B96
delete_residue_sidechain(imol, "A", 41, "", 0)    # side chain of A41 (0 = no dialog)
delete_atom(imol, "A", 40, "", " O  ", "")        # one atom
print("A now has", chain_n_residues("A", imol), "residues; B", chain_n_residues("B", imol))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(delete-residue imol "A" 93 "")
(delete-residue-range imol "B" 94 96)
(delete-residue-sidechain imol "A" 41 "" 0)
(delete-atom imol "A" 40 "" " O  " "")
(format #t "A now has ~a residues; B ~a~%" (chain-n-residues "A" imol) (chain-n-residues "B" imol))
```
<!-- check-py: chain_n_residues("A", imol) == 92 and chain_n_residues("B", imol) == 93 and len(residue_info(imol, "A", 41, "")) == 5 -->
<!-- check-scm: (and (= (chain-n-residues "B" imol) 93) (= (length (residue-info imol "A" 41 "")) 5)) -->

### 5.4 Delete all hydrogens or all waters

```python
imol = read_pdb("tutorial-modern.pdb")
delete_hydrogens(imol)
delete_waters(imol)
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(delete-hydrogens imol)
(delete-waters imol)
```

### 5.5 Renumber residues

Add 100 to the numbers of residues A1-A10 (they become A101-A110).

```python
imol = read_pdb("tutorial-modern.pdb")
renumber_residue_range(imol, "A", 1, 10, 100)
print(residue_name(imol, "A", 101, ""), "is now residue A101")
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(renumber-residue-range imol "A" 1 10 100)
(format #t "~a is now residue A101~%" (residue-name imol "A" 101 ""))
```
<!-- check-py: residue_name(imol, "A", 101, "") == "ASP" -->
<!-- check-scm: (string=? (residue-name imol "A" 101 "") "ASP") -->

### 5.6 Change a chain ID

Whole chain B becomes chain C (the 0 means: all residues, so the two numbers after it are not used).
Use 1, 10, 20 to change only residues 10-20.

```python
imol = read_pdb("tutorial-modern.pdb")
change_chain_id(imol, "B", "C", 0, 0, 0)
print(chain_ids(imol))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(change-chain-id imol "B" "C" 0 0 0)
(display (chain-ids imol)) (newline)
```
<!-- check-py: chain_ids(imol) == ["A", "C"] -->
<!-- check-scm: (equal? (chain-ids imol) (list "A" "C")) -->

### 5.7 Merge molecules

Adds the chains of the other molecules to the first one (a chain ID that is already used gets a new letter).

```python
imol = read_pdb("tutorial-modern.pdb")
imol_b = new_molecule_by_atom_selection(imol, "//B")
delete_chain(imol, "B")
merge_molecules([imol_b], imol)
print(chain_ids(imol))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-b (new-molecule-by-atom-selection imol "//B"))
(delete-chain imol "B")
(merge-molecules (list imol-b) imol)
(display (chain-ids imol)) (newline)
```
<!-- check-py: chain_ids(imol) == ["A", "B"] -->
<!-- check-scm: (= (length (chain-ids imol)) 2) -->

### 5.8 Mutate a residue

Three-letter code of the new residue. Follow with 4.7 to fit the new side chain.

```python
imol = read_pdb("tutorial-modern.pdb")
mutate(imol, "A", 41, "", "ALA")
print(residue_name(imol, "A", 41, ""))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(mutate imol "A" 41 "" "ALA")
(display (residue-name imol "A" 41 "")) (newline)
```
<!-- check-py: residue_name(imol, "A", 41, "") == "ALA" -->
<!-- check-scm: (string=? (residue-name imol "A" 41 "") "ALA") -->

### 5.9 Mutate a range to a new sequence

```python
imol = read_pdb("tutorial-modern.pdb")
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
set_imol_refinement_map(imol_map)
mutate_residue_range(imol, "A", 40, 42, "AAA")     # three residues -> three letters
print([residue_name(imol, "A", r, "") for r in (40, 41, 42)])
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(set-imol-refinement-map imol-map)
(mutate-residue-range imol "A" 40 42 "AAA")
(display (map (lambda (r) (residue-name imol "A" r "")) (list 40 41 42))) (newline)
```
<!-- check-py: [residue_name(imol, "A", r, "") for r in (40, 41, 42)] == ["ALA", "ALA", "ALA"] -->
<!-- check-scm: (string=? (residue-name imol "A" 41 "") "ALA") -->

### 5.10 Add a residue at the end of a chain

Adds residue A94 after A93, fitted into the map. `"auto"` lets Coot pick the type (alanine); the last 1 adds it at once.

```python
imol = read_pdb("tutorial-modern.pdb")
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
set_imol_refinement_map(imol_map)
add_terminal_residue(imol, "A", 93, "auto", 1)
print("A94:", residue_name(imol, "A", 94, ""))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(set-imol-refinement-map imol-map)
(add-terminal-residue imol "A" 93 "auto" 1)
(format #t "A94: ~a~%" (residue-name imol "A" 94 ""))
```
<!-- check-py: chain_n_residues("A", imol) == 94 -->
<!-- check-scm: (= (chain-n-residues "A" imol) 94) -->

### 5.11 Set B-factors and occupancies

```python
imol = read_pdb("tutorial-modern.pdb")
set_b_factor_residue_range(imol, "A", 40, 45, 30.0)
set_occupancy_residue_range(imol, "A", 40, 45, 0.5)
set_atom_attribute(imol, "A", 41, "", " CA ", "", "B", 50.0)    # one atom
print(atom_info_string(imol, "A", 41, "", " CA ", "")[:2])      # [occupancy, B]
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(set-b-factor-residue-range imol "A" 40 45 30.0)
(set-occupancy-residue-range imol "A" 40 45 0.5)
(set-atom-attribute imol "A" 41 "" " CA " "" "B" 50.0)
(display (list-head (atom-info-string imol "A" 41 "" " CA " "") 2)) (newline)
```
<!-- check-py: atom_info_string(imol, "A", 41, "", " CA ", "")[:2] == [0.5, 50.0] -->
<!-- check-scm: (equal? (list-head (atom-info-string imol "A" 41 "" " CA " "") 2) (list 0.5 50.0)) -->

### 5.12 Undo

`apply_undo` undoes the last change of the molecule chosen with `set_undo_molecule`.

```python
imol = read_pdb("tutorial-modern.pdb")
mutate(imol, "A", 41, "", "ALA")
set_undo_molecule(imol)
apply_undo()
print(residue_name(imol, "A", 41, ""))      # GLU again
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(mutate imol "A" 41 "" "ALA")
(set-undo-molecule imol)
(apply-undo)
(display (residue-name imol "A" 41 "")) (newline)
```
<!-- check-py: residue_name(imol, "A", 41, "") == "GLU" -->
<!-- check-scm: (string=? (residue-name imol "A" 41 "") "GLU") -->

### 5.13 Move a molecule

Shift by x, y, z in Å.

```python
imol = read_pdb("tutorial-modern.pdb")
x0 = atom_info_string(imol, "A", 41, "", " CA ", "")[3]
translate_molecule_by(imol, 10.0, 0.0, 0.0)
print("x of CA A41: %.2f -> %.2f" % (x0, atom_info_string(imol, "A", 41, "", " CA ", "")[3]))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(translate-molecule-by imol 10.0 0.0 0.0)
(display (atom-info-string imol "A" 41 "" " CA " "")) (newline)
```
<!-- check-py: abs(atom_info_string(imol, "A", 41, "", " CA ", "")[3] - x0 - 10) < 0.01 -->

### 5.14 Rename a residue (no new atoms)

Changes only the name, for example after you changed the atoms yourself.

```python
imol = read_pdb("tutorial-modern.pdb")
set_residue_name(imol, "A", 41, "", "GLN")
print(residue_name(imol, "A", 41, ""))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(set-residue-name imol "A" 41 "" "GLN")
(display (residue-name imol "A" 41 "")) (newline)
```
<!-- check-py: residue_name(imol, "A", 41, "") == "GLN" -->
<!-- check-scm: (string=? (residue-name imol "A" 41 "") "GLN") -->
