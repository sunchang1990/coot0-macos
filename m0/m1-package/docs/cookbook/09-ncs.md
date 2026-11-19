# 9. NCS (non-crystallographic symmetry)

Chains A and B of the test model are two copies of the same protein, so Coot finds NCS between them by itself.

### 9.1 Which chains are NCS copies

```python
imol = read_pdb("tutorial-modern.pdb")
print("NCS groups:", ncs_chain_ids(imol), "master:", ncs_master_chains(imol))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(format #t "NCS groups: ~a master: ~a~%" (ncs-chain-ids imol) (ncs-master-chains imol))
```
<!-- check-py: ncs_chain_ids(imol) == [["A", "B"]] -->
<!-- check-scm: (equal? (ncs-chain-ids imol) (list (list "A" "B"))) -->

### 9.2 How different are the copies (per residue)

```python
imol = read_pdb("tutorial-modern.pdb")
moving, master, diffs = ncs_chain_differences(imol, "A")
worst = sorted(diffs, key=lambda d: -d[2])[:5]
for (res_master, ins1), (res_moving, ins2), rmsd in worst:
    print("residue %d: %.2f A" % (res_master, rmsd))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define diffs (list-ref (ncs-chain-differences imol "A") 2))
(format #t "~a residues compared~%" (length diffs))
```
<!-- check-py: len(diffs) > 80 -->
<!-- check-scm: (> (length diffs) 80) -->

### 9.3 Show the NCS copies as ghosts

```python
imol = read_pdb("tutorial-modern.pdb")
make_ncs_ghosts_maybe(imol)
set_draw_ncs_ghosts(imol, 1)
print("ghosts shown:", draw_ncs_ghosts_state(imol))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(make-ncs-ghosts-maybe imol)
(set-draw-ncs-ghosts imol 1)
(format #t "ghosts shown: ~a~%" (draw-ncs-ghosts-state imol))
```
<!-- check-py: draw_ncs_ghosts_state(imol) == 1 -->
<!-- check-scm: (= (draw-ncs-ghosts-state imol) 1) -->

### 9.4 Copy the master chain onto the other copies

After rebuilding chain A, make chain B the same (B keeps its own position).
Here: mutate A41 and copy it to B41.

```python
imol = read_pdb("tutorial-modern.pdb")
mutate(imol, "A", 41, "", "ALA")
copy_residue_range_from_ncs_master_to_others(imol, "A", 41, 41)
print("B41 is now", residue_name(imol, "B", 41, ""))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(mutate imol "A" 41 "" "ALA")
(copy-residue-range-from-ncs-master-to-others imol "A" 41 41)
(format #t "B41 is now ~a~%" (residue-name imol "B" 41 ""))
```
<!-- check-py: residue_name(imol, "B", 41, "") == "ALA" -->
<!-- check-scm: (string=? (residue-name imol "B" 41 "") "ALA") -->

The whole chain: `copy_from_ncs_master_to_others(imol, "A")`.

### 9.5 Superpose one chain onto another

Copy chain B and superpose the copy onto chain A by sequence alignment (SSM). The superposed copy is a new molecule.

```python
imol = read_pdb("tutorial-modern.pdb")
n_before = graphics_n_molecules()
superpose_with_chain_selection(imol, imol, "A", "B", 1, 1, 1)
print("new molecule(s):", list(range(n_before, graphics_n_molecules())))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define n-before (graphics-n-molecules))
(superpose-with-chain-selection imol imol "A" "B" 1 1 1)
(format #t "molecules now: ~a (before ~a)~%" (graphics-n-molecules) n-before)
```
<!-- check-py: graphics_n_molecules() > n_before -->
<!-- check-scm: (> (graphics-n-molecules) n-before) -->

### 9.6 Least-squares fit on chosen residues

Fit residues B10-B60 onto A10-A60 (main-chain atoms: match type 1; 0 = CA only, 2 = all atoms).

```python
imol = read_pdb("tutorial-modern.pdb")
imol_b = new_molecule_by_atom_selection(imol, "//B")
clear_lsq_matches()
add_lsq_match(10, 60, "A", 10, 60, "B", 1)
result = apply_lsq_matches(imol, imol_b)
print("moved; result:", result)
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-b (new-molecule-by-atom-selection imol "//B"))
(clear-lsq-matches)
(add-lsq-match 10 60 "A" 10 60 "B" 1)
(format #t "result: ~a~%" (apply-lsq-matches imol imol-b))
```
