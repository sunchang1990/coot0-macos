# 2. The view

*Each recipe stands alone and loads its own copy of the test files (run recipe 1.1 once first; with your own data use
your molecule numbers instead: [How to use a recipe](README.md#how-to-use-a-recipe)).*

These recipes change what you see. Without a window (the automatic test) they run but nothing is drawn.

### 2.1 Go to a residue

Centre the view on the CA atom of residue A41 of a molecule.

```python
imol = read_pdb("tutorial-modern.pdb")
set_go_to_atom_molecule(imol)
set_go_to_atom_chain_residue_atom_name("A", 41, " CA ")
print("centre:", rotation_centre())
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(set-go-to-atom-molecule imol)
(set-go-to-atom-chain-residue-atom-name "A" 41 " CA ")
(format #t "centre: ~a~%" (rotation-centre))
```
<!-- check-py: abs(rotation_centre()[0] - 47.072) < 0.01 -->
<!-- check-scm: (< (abs (- (car (rotation-centre)) 47.072)) 0.01) -->

Atom names have 4 characters as in the PDB file: `" CA "`, `" N  "`, `" OE1"`.

### 2.2 Go to a point (x, y, z in Å)

```python
set_rotation_centre(45.0, 10.0, 15.0)
print(rotation_centre())
```

```scheme
(set-rotation-centre 45.0 10.0 15.0)
(display (rotation-centre)) (newline)
```
<!-- check-py: [round(v, 1) for v in rotation_centre()] == [45.0, 10.0, 15.0] -->
<!-- check-scm: (< (abs (- (cadr (rotation-centre)) 10.0)) 0.01) -->

### 2.3 Zoom

Larger numbers show more (zoom out); the default is 100.

```python
set_zoom(60)
print("zoom", zoom_factor())
```

```scheme
(set-zoom 60)
(format #t "zoom ~a~%" (zoom-factor))
```
<!-- check-py: abs(zoom_factor() - 60) < 0.1 -->
<!-- check-scm: (< (abs (- (zoom-factor) 60)) 0.1) -->

### 2.4 Save views and go back to them

```python
imol = read_pdb("tutorial-modern.pdb")
set_go_to_atom_molecule(imol)
set_go_to_atom_chain_residue_atom_name("A", 41, " CA ")
v1 = add_view_here("Glu A41")
set_go_to_atom_chain_residue_atom_name("B", 72, " CA ")
v2 = add_view_here("Cys B72")
go_to_view_number(v1, 1)        # 1 = jump, 0 = slide there
print(n_views(), "views; back at", rotation_centre())
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(set-go-to-atom-molecule imol)
(set-go-to-atom-chain-residue-atom-name "A" 41 " CA ")
(define v1 (add-view-here "Glu A41"))
(set-go-to-atom-chain-residue-atom-name "B" 72 " CA ")
(define v2 (add-view-here "Cys B72"))
(go-to-view-number v1 1)
(format #t "~a views~%" (n-views))
```
<!-- check-py: abs(rotation_centre()[0] - 47.072) < 0.01 -->
<!-- check-scm: (>= (n-views) 2) -->

### 2.5 Show or hide a molecule or a map

```python
imol = read_pdb("tutorial-modern.pdb")
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
set_mol_displayed(imol, 0)      # hide the model
set_map_displayed(imol_map, 0)  # hide the map
set_mol_displayed(imol, 1)      # show it again
print("model shown:", mol_is_displayed(imol), "map shown:", map_is_displayed(imol_map))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(set-mol-displayed imol 0)
(set-map-displayed imol-map 0)
(set-mol-displayed imol 1)
(format #t "model shown: ~a map shown: ~a~%" (mol-is-displayed imol) (map-is-displayed imol-map))
```
<!-- check-py: mol_is_displayed(imol) == 1 and map_is_displayed(imol_map) == 0 -->
<!-- check-scm: (and (= (mol-is-displayed imol) 1) (= (map-is-displayed imol-map) 0)) -->

### 2.6 Symmetry copies

```python
imol = read_pdb("tutorial-modern.pdb")
set_show_symmetry_master(1)
set_symmetry_size(20)           # Å around the centre
print("symmetry shown:", get_show_symmetry())
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(set-show-symmetry-master 1)
(set-symmetry-size 20)
(format #t "symmetry shown: ~a~%" (get-show-symmetry))
```
<!-- check-py: get_show_symmetry() == 1 -->
<!-- check-scm: (= (get-show-symmetry) 1) -->

### 2.7 CA trace instead of all bonds, and back

```python
imol = read_pdb("tutorial-modern.pdb")
graphics_to_ca_representation(imol)
graphics_to_bonds_representation(imol)
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(graphics-to-ca-representation imol)
(graphics-to-bonds-representation imol)
```

### 2.8 Label atoms

```python
imol = read_pdb("tutorial-modern.pdb")
add_atom_label(imol, "A", 41, " CA ")
add_atom_label(imol, "A", 41, " OE1")
remove_atom_label(imol, "A", 41, " OE1")
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(add-atom-label imol "A" 41 " CA ")
(add-atom-label imol "A" 41 " OE1")
(remove-atom-label imol "A" 41 " OE1")
```

### 2.9 Background colour

Red, green, blue from 0 to 1: white background, then back to black.

```python
set_background_colour(1.0, 1.0, 1.0)
set_background_colour(0.0, 0.0, 0.0)
```

```scheme
(set-background-colour 1.0 1.0 1.0)
(set-background-colour 0.0 0.0 0.0)
```
