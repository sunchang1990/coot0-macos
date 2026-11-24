# 10. Ligands

*Each recipe stands alone and loads its own copy of the test files (run recipe 1.1 once first; with your own data use
your molecule numbers instead: [How to use a recipe](README.md#how-to-use-a-recipe)).*

coot0 includes the CCP4 monomer library, so any three-letter code it knows (ATP, NAG, HEM, ...) can be made
from its dictionary.

### 10.1 Make a ligand from the dictionary

The new molecule is placed at the centre of the screen.

```python
imol_lig = get_monomer("ATP")
print("ATP is molecule", imol_lig, "with residues", het_group_residues(imol_lig))
```

```scheme
(define imol-lig (get-monomer "ATP"))
(format #t "ATP is molecule ~a~%" imol-lig)
```
<!-- check-py: is_valid_model_molecule(imol_lig) -->
<!-- check-scm: (valid-model-molecule? imol-lig) -->

### 10.2 Read your own dictionary (from acedrg, grade, eLBOW...)

```python
# write a dictionary for the test first: the monomer library's own NAG file (coot0 sets COOT_MONOMER_LIB_DIR to the library it uses)
import os, shutil
lib = os.path.join(os.environ["COOT_MONOMER_LIB_DIR"], "n", "NAG.cif")
shutil.copy(lib, "my-ligand.cif")

read_cif_dictionary("my-ligand.cif")
imol_lig = get_monomer("NAG")
```

```scheme
(copy-file (string-append (getenv "COOT_MONOMER_LIB_DIR") "/n/NAG.cif") "my-ligand.cif")
(read-cif-dictionary "my-ligand.cif")
(define imol-lig (get-monomer "NAG"))
```
<!-- check-py: is_valid_model_molecule(imol_lig) -->
<!-- check-scm: (valid-model-molecule? imol-lig) -->

### 10.3 Put a ligand at a place and add it to the protein

Move the ligand to a point (here: next to residue A41), then merge it into the protein model.

```python
imol = read_pdb("tutorial-modern.pdb")
imol_lig = get_monomer("NAG")
set_go_to_atom_molecule(imol)
set_go_to_atom_chain_residue_atom_name("A", 41, " CA ")
move_molecule_to_screen_centre(imol_lig)
merge_molecules([imol_lig], imol)
print("ligands in the model:", het_group_residues(imol))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-lig (get-monomer "NAG"))
(set-go-to-atom-molecule imol)
(set-go-to-atom-chain-residue-atom-name "A" 41 " CA ")
(move-molecule-to-screen-centre imol-lig)
(merge-molecules (list imol-lig) imol)
(format #t "ligands in the model: ~a~%" (het-group-residues imol))
```
<!-- check-py: len(het_group_residues(imol)) == 1 -->
<!-- check-scm: (= (length (het-group-residues imol)) 1) -->

### 10.4 Residues around a ligand

```python
imol = read_pdb("tutorial-modern.pdb")
imol_lig = get_monomer("NAG")
set_go_to_atom_molecule(imol)
set_go_to_atom_chain_residue_atom_name("A", 41, " CA ")
move_molecule_to_screen_centre(imol_lig)
merge_molecules([imol_lig], imol)
lig = het_group_residues(imol)[0][1:]          # [chain, resno, ins]
print("ligand", lig, "contacts:", residues_near_residue(imol, lig, 4.0))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-lig (get-monomer "NAG"))
(set-go-to-atom-molecule imol)
(set-go-to-atom-chain-residue-atom-name "A" 41 " CA ")
(move-molecule-to-screen-centre imol-lig)
(merge-molecules (list imol-lig) imol)
(define lig (cdr (car (het-group-residues imol))))
(format #t "ligand ~a contacts: ~a~%" lig (residues-near-residue imol lig 4.0))
```
<!-- check-py: len(residues_near_residue(imol, lig, 4.0)) > 0 -->

### 10.5 Fit a ligand into the density (Find Ligands from a script)

Searches the map for places where the ligand fits, away from the model, and makes a new molecule per solution.

```python
imol = read_pdb("tutorial-modern.pdb")
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
imol_lig = get_monomer("NAG")
add_ligand_clear_ligands()
set_ligand_search_protein_molecule(imol)
set_ligand_search_map_molecule(imol_map)
add_ligand_search_ligand_molecule(imol_lig)
set_find_ligand_n_top_ligands(3)
n_before = graphics_n_molecules()
execute_ligand_search()
print("solutions:", list(range(n_before, graphics_n_molecules())))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(define imol-lig (get-monomer "NAG"))
(add-ligand-clear-ligands)
(set-ligand-search-protein-molecule imol)
(set-ligand-search-map-molecule imol-map)
(add-ligand-search-ligand-molecule imol-lig)
(set-find-ligand-n-top-ligands 3)
(execute-ligand-search)
```

### 10.6 Geometry of a ligand

How well the ligand matches its dictionary (bonds, angles...). Needs a refinement map.

```python
set_imol_refinement_map(make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0))
imol_lig = get_monomer("ATP")
d = residues_distortions(imol_lig, [het_group_residues(imol_lig)[0][1:]])
print(len(d), "restraints; worst:", max(x["distortion_score"] for x in d))
```

```scheme
(set-imol-refinement-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(define imol-lig (get-monomer "ATP"))
(format #t "~a restraints~%" (length (residues-distortions-scm imol-lig (list (cdr (car (het-group-residues imol-lig)))))))
```
<!-- check-py: len(d) > 20 -->
