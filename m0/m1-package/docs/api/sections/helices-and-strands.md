# Helices and Strands

[Scripting reference](../README.md) > Helices and Strands (8 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### find_helices

Python: `find_helices()`  
Scheme: `(find-helices)`

autobuild helices

 Find secondary structure in the current map.
 Add to a molecule called "Helices", create it if
 needed.

 Returns the index of the new molecule.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `find_helices()` | ran, returned `3`; changed: new molecule 3 (model, SecStruc); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | `(find-helices)` | ran, returned `3`; changed: new molecule 3 (model, SecStruc); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

Python and Scheme gave the same answer.

### find_secondary_structure

Python: `find_secondary_structure(use_helix, helix_length, helix_target, use_strand, strand_length, strand_target)`  
Scheme: `(find-secondary-structure use-helix helix-length helix-target use-strand strand-length strand-target)`

autobuild secondary structure

 Find secondary structure in the current map.
 Add to a molecule called "SecStruc", create it if needed.

 Returns the index of the new molecule.

Arguments: use_helix (a whole number), helix_length (a whole number), helix_target (a whole number), use_strand (a whole number), strand_length (a whole number), strand_target (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `find_secondary_structure(1, 6, 2, 1, 4, 2)` | not run: searches the whole map: no answer in 60 s on the test map (use find_secondary_structure_local) |
| Scheme | `(find-secondary-structure 1 6 2 1 4 2)` | not run: searches the whole map: no answer in 60 s on the test map (use find_secondary_structure_local) |

Example written and checked by hand on the test data. Expected: finds helices (min length 6) and strands (min length 4) in the whole refinement map and adds them to a molecule 'SecStruc'.

### find_secondary_structure_local

Python: `find_secondary_structure_local(use_helix, helix_length, helix_target, use_strand, strand_length, strand_target, radius)`  
Scheme: `(find-secondary-structure-local use-helix helix-length helix-target use-strand strand-length strand-target radius)`

autobuild secondary structure

 Find secondary structure local to current view in the current map.
 Add to a molecule called "SecStruc", create it if needed.

 Returns the index of the new molecule.

Arguments: use_helix (a whole number), helix_length (a whole number), helix_target (a whole number), use_strand (a whole number), strand_length (a whole number), strand_target (a whole number), radius (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `set_rotation_centre(47.1, 10.6, 17.4)`, then `find_secondary_structure_local(1, 6, 2, 1, 4, 2, 6.0)` | ran, returned `3`; changed: new molecule 3 (model, SecStruc); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | first `(set-rotation-centre 47.1 10.6 17.4)`, then `(find-secondary-structure-local 1 6 2 1 4 2 6.0)` | ran, returned `3`; changed: new molecule 3 (model, SecStruc); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the molecule 'SecStruc' holding the helices/strands found in the map within the radius of the centre.

Python and Scheme gave the same answer.

### find_strands

Python: `find_strands()`  
Scheme: `(find-strands)`

autobuild strands

 Find secondary structure in the current map.
 Add to a molecule called "Strands", create it if
 needed.

 Returns the index of the new molecule.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `find_strands()` | ran, returned `3`; changed: new molecule 3 (model, SecStruc); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | `(find-strands)` | ran, returned `3`; changed: new molecule 3 (model, SecStruc); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

Python and Scheme gave the same answer.

### place_helix_here

Python: `place_helix_here()`  
Scheme: `(place-helix-here)`

add a helix

 Add a helix somewhere close to this point in the map, try to fit
 the orientation. Add to a molecule called "Helix", create it if
 needed. Create another moecule called "Reverse Helix" if the helix
 orientation isn't completely unequivocal.

 Returns the index of the new molecule.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `place_helix_here()` | ran, returned `4`; changed: new molecule 3 (model, Helix-3); new molecule 4 (model, Reverse-Helix-4); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 5 |
| Scheme | `(place-helix-here)` | ran, returned `3`; changed: new molecule 3 (model, Helix-3); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### place_strand_here

Python: `place_strand_here(n_residues, n_sample_strands)`  
Scheme: `(place-strand-here n-residues n-sample-strands)`

add a strands

 Add a strand close to this point in the map, try to fit
 the orientation. Add to a molecule called "Strand", create it if needed.
 n_residues is the estimated number of residues in the strand.

 n_sample_strands is the number of strands from the database tested
 to fit into this strand density. 8 is a suggested number. 20 for
 a more rigourous search, but it will be slower.

 Returns the index of the new molecule.

Arguments: n_residues (a whole number), n_sample_strands (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `place_strand_here(5, 5)` | ran, returned `3`; changed: new molecule 3 (model, Strand-3); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | `(place-strand-here 5 5)` | ran, returned `3`; changed: new molecule 3 (model, Strand-3); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns a new molecule with a strand fitted to the map at the rotation centre; -1 when no strand fits.

Python and Scheme gave the same answer.

### place_strand_here_dialog

Python: `place_strand_here_dialog()`  
Scheme: `(place-strand-here-dialog)`

show the strand placement gui.

 Choose the python version in there, if needed. Call scripting
 function, display it in place, don't return a widget.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `place_strand_here_dialog()` | ran (no return value, nothing visible changed) |
| Scheme | `(place-strand-here-dialog)` | ran (no return value, nothing visible changed) |

### set_place_helix_here_fudge_factor

Python: `set_place_helix_here_fudge_factor(ff)`  
Scheme: `(set-place-helix-here-fudge-factor ff)`

Arguments: ff (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_place_helix_here_fudge_factor(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-place-helix-here-fudge-factor 1.0)` | ran (no return value, nothing visible changed) |

