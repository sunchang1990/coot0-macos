# 3. Selections and information

*Each recipe stands alone and loads its own copy of the test files (run recipe 1.1 once first; with your own data use
your molecule numbers instead: [How to use a recipe](README.md#how-to-use-a-recipe)).*

A residue is named by a *residue spec*: chain, residue number and insertion code, for example `["A", 41, ""]`
(Python) or `(list "A" 41 "")` (Scheme). Some functions return specs with a leading `True` / `#t`:
`[True, "A", 41, ""]`. Atom selections use the MMDB syntax `"//A/30-45"` (chain A, residues 30 to 45),
`"//A/41/CA"` (one atom), `"//B"` (a whole chain).

### 3.1 Chains, residues and the sequence

```python
imol = read_pdb("tutorial-modern.pdb")
for ch in chain_ids(imol):
    print("chain", ch, chain_n_residues(ch, imol), "residues")
print(get_sequence_as_fasta_for_chain(imol, "A"))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(for-each (lambda (ch) (format #t "chain ~a ~a residues~%" ch (chain-n-residues ch imol))) (chain-ids imol))
(display (get-sequence-as-fasta-for-chain imol "A"))
```
<!-- check-py: chain_n_residues("A", imol) == 93 and chain_n_residues("B", imol) == 96 -->
<!-- check-scm: (= (chain-n-residues "B" imol) 96) -->

### 3.2 Name and atoms of one residue

`residue_info` gives one entry per atom: `[[name, alt-conf], [occupancy, B-factor, element, segid], [x, y, z], atom index]`.

```python
imol = read_pdb("tutorial-modern.pdb")
print(residue_name(imol, "A", 41, ""))           # GLU
for atom in residue_info(imol, "A", 41, ""):
    name, alt = atom[0]
    occ, b = atom[1][0], atom[1][1]
    x, y, z = atom[2]
    print("%s  occ %.2f  B %5.1f  at %.2f %.2f %.2f" % (name, occ, b, x, y, z))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(display (residue-name imol "A" 41 "")) (newline)
(for-each (lambda (atom)
            (format #t "~a  occ ~a  B ~a  at ~a~%"
                    (car (car atom)) (car (cadr atom)) (cadr (cadr atom)) (caddr atom)))
          (residue-info imol "A" 41 ""))
```
<!-- check-py: residue_name(imol, "A", 41, "") == "GLU" and len(residue_info(imol, "A", 41, "")) == 9 -->
<!-- check-scm: (and (string=? (residue-name imol "A" 41 "") "GLU") (= (length (residue-info imol "A" 41 "")) 9)) -->

### 3.3 Find all residues of one type

```python
imol = read_pdb("tutorial-modern.pdb")
tyrosines = [r for r in all_residues(imol) if residue_name(imol, r[1], r[2], r[3]) == "TYR"]
print(len(tyrosines), "TYR:", [(r[1], r[2]) for r in tyrosines])
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define tyrosines
  (filter (lambda (r) (string=? (residue-name imol (list-ref r 1) (list-ref r 2) (list-ref r 3)) "TYR"))
          (all-residues imol)))
(format #t "~a TYR~%" (length tyrosines))
```
<!-- check-py: len(tyrosines) == 16 -->
<!-- check-scm: (= (length tyrosines) 16) -->

### 3.4 Residues near a residue

All residues with an atom within 5 Å of residue A41.

```python
imol = read_pdb("tutorial-modern.pdb")
near = residues_near_residue(imol, ["A", 41, ""], 5.0)
print(len(near), "residues:", near)
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define near (residues-near-residue imol (list "A" 41 "") 5.0))
(format #t "~a residues: ~a~%" (length near) near)
```
<!-- check-py: ["A", 40, ""] in near and ["A", 42, ""] in near -->
<!-- check-scm: (> (length near) 3) -->

### 3.5 Distance between two atoms

```python
import math
imol = read_pdb("tutorial-modern.pdb")
a = atom_info_string(imol, "A", 41, "", " CA ", "")   # [occ, B, element, x, y, z]
b = atom_info_string(imol, "B", 41, "", " CA ", "")
d = math.sqrt(sum((a[i] - b[i]) ** 2 for i in (3, 4, 5)))
print("CA A41 - CA B41: %.2f A" % d)
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define (xyz chain) (list-tail (atom-info-string imol chain 41 "" " CA " "") 3))
(define d (sqrt (apply + (map (lambda (p q) (* (- p q) (- p q))) (xyz "A") (xyz "B")))))
(format #t "CA A41 - CA B41: ~,2f A~%" d)
```
<!-- check-py: d > 5 -->
<!-- check-scm: (> d 5) -->

### 3.6 Make a new molecule from a selection

```python
imol = read_pdb("tutorial-modern.pdb")
imol_part = new_molecule_by_atom_selection(imol, "//A/30-45")
print("new molecule", imol_part, "with", chain_n_residues("A", imol_part), "residues")
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-part (new-molecule-by-atom-selection imol "//A/30-45"))
(format #t "new molecule ~a with ~a residues~%" imol-part (chain-n-residues "A" imol-part))
```
<!-- check-py: chain_n_residues("A", imol_part) == 16 -->
<!-- check-scm: (= (chain-n-residues "A" imol-part) 16) -->

### 3.7 Residues with alternative conformations or missing atoms

```python
imol = read_pdb("tutorial-modern.pdb")
print("alt confs:", residues_with_alt_confs(imol))
print("missing atoms:", missing_atom_info(imol))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(format #t "alt confs: ~a~%" (residues-with-alt-confs imol))
(format #t "missing atoms: ~a~%" (missing-atom-info-scm imol))
```
<!-- check-py: residues_with_alt_confs(imol) == [[True, "B", 72, ""]] -->
<!-- check-scm: (= (length (residues-with-alt-confs imol)) 1) -->

### 3.8 Average and median B-factor

```python
imol = read_pdb("tutorial-modern.pdb")
print("average B %.1f, median B %.1f" % (average_temperature_factor(imol), median_temperature_factor(imol)))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(format #t "average B ~,1f, median B ~,1f~%" (average-temperature-factor imol) (median-temperature-factor imol))
```
<!-- check-py: 5 < average_temperature_factor(imol) < 100 -->
<!-- check-scm: (> (average-temperature-factor imol) 5) -->
