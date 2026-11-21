# Water Fitting Functions

[Scripting reference](../README.md) > Water Fitting Functions (15 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### execute_find_blobs

Python: `execute_find_blobs(imol_model, imol_for_map, cut_off, interactive_flag)`  
Scheme: `(execute-find-blobs imol-model imol-for-map cut-off interactive-flag)`

find blobs

Arguments: imol_model (a whole number), imol_for_map (a whole number), cut_off (a number), interactive_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `execute_find_blobs(0, 1, 1.5, 0)` | ran (no return value, nothing visible changed) |
| Scheme | `(execute-find-blobs 0 1 1.5 0)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: finds unmodelled density blobs above 1.5 sigma in map 1 (not covered by model 0); with interactive_flag 1 it opens the Blobs dialog (that needs a screen: Coot stopped headless).

Note: interactive_flag 1 stops Coot without a screen.

### execute_find_waters_real

Python: `execute_find_waters_real(imol_for_map, imol_for_protein, new_waters_mol_flag, rmsd_cut_off)`  
Scheme: `(execute-find-waters-real imol-for-map imol-for-protein new-waters-mol-flag rmsd-cut-off)`

find waters

Arguments: imol_for_map (a whole number), imol_for_protein (a whole number), new_waters_mol_flag (a whole number), rmsd_cut_off (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `execute_find_waters_real(1, 0, 1, 1.5)` | ran (no return value); changed: new molecule 3 (model, waters); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | `(execute-find-waters-real 1 0 1 1.5)` | ran (no return value); changed: new molecule 3 (model, waters); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

### find_waters

Python: `find_waters(imol_for_map, imol_for_protein, new_waters_mol_flag, rmsd_cut_off, show_blobs_dialog)`  
Scheme: `(find-waters imol-for-map imol-for-protein new-waters-mol-flag rmsd-cut-off show-blobs-dialog)`

Arguments: imol_for_map (a whole number), imol_for_protein (a whole number), new_waters_mol_flag (a whole number), rmsd_cut_off (a number), show_blobs_dialog (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `find_waters(1, 0, 1, 1.5, 1)` | ran (no return value); changed: new molecule 3 (model, waters); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | `(find-waters 1 0 1 1.5 1)` | ran (no return value); changed: new molecule 3 (model, waters); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

### get_text_for_find_waters_sigma_cut_off

Python: `get_text_for_find_waters_sigma_cut_off()`  
Scheme: `(get-text-for-find-waters-sigma-cut-off)`

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_text_for_find_waters_sigma_cut_off()` | ran, returned `'  1.4'` |
| Scheme | `(get-text-for-find-waters-sigma-cut-off)` | ran, returned `"  1.4"` |

Python and Scheme gave the same answer.

### max_water_distance

Python: `max_water_distance(imol)`  
Scheme: `(max-water-distance imol)`

return the maximum minimum distance of any water atom to
 any protein atom - used in validation of
 move_waters_to_around_protein() funtion.

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `max_water_distance(read_pdb("1ehz.pdb"))` | ran, returned `4.518393516540527`; changed: new molecule 3 (model, 1ehz.pdb); rotation centre moved 51.0 A to (67.6, 49.7, 28.6); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(max-water-distance (read-pdb "1ehz.pdb"))` | ran, returned `4.518393516540527`; changed: new molecule 3 (model, 1ehz.pdb); rotation centre moved 51.0 A to (67.6, 49.7, 28.6); graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: the largest distance of any water to its nearest non-water atom in 1ehz.pdb (4.5 A); -1.0 for a molecule without waters.

Python and Scheme gave the same answer.

### move_hetgroups_to_around_protein

Python: `move_hetgroups_to_around_protein(imol)`  
Scheme: `(move-hetgroups-to-around-protein imol)`

move all hetgroups (including waters) of molecule number
 imol so that they are around the protein.

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `move_hetgroups_to_around_protein(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(move-hetgroups-to-around-protein 0)` | ran (no return value, nothing visible changed) |

### move_waters_to_around_protein

Python: `move_waters_to_around_protein(imol)`  
Scheme: `(move-waters-to-around-protein imol)`

move waters of molecule number imol so that they are around the protein.

Returns the number of moved waters.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `move_waters_to_around_protein(read_pdb("1ehz.pdb"))` | ran, returned `71`; changed: new molecule 3 (model, 1ehz.pdb); rotation centre moved 51.0 A to (67.6, 49.7, 28.6); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(move-waters-to-around-protein (read-pdb "1ehz.pdb"))` | ran, returned `71`; changed: new molecule 3 (model, 1ehz.pdb); rotation centre moved 51.0 A to (67.6, 49.7, 28.6); graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the number of waters moved to their symmetry copy closest to the macromolecule (71 for 1ehz.pdb).

Python and Scheme gave the same answer.

### renumber_waters

Python: `renumber_waters(imol)`  
Scheme: `(renumber-waters imol)`

Renumber the waters of molecule number imol with consecutive numbering

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `renumber_waters(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(renumber-waters 0)` | ran (no return value, nothing visible changed) |

### set_ligand_water_n_cycles

Python: `set_ligand_water_n_cycles(i)`  
Scheme: `(set-ligand-water-n-cycles i)`

set the number of cycles of water searching

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ligand_water_n_cycles(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-ligand-water-n-cycles 1)` | ran (no return value, nothing visible changed) |

### set_ligand_water_to_protein_distance_limits

Python: `set_ligand_water_to_protein_distance_limits(f1, f2)`  
Scheme: `(set-ligand-water-to-protein-distance-limits f1 f2)`

set ligand to protein distance limits

 f1 is the minimum distance, f2 is the maximum distance

Arguments: f1 (a number), f2 (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ligand_water_to_protein_distance_limits(1.0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-ligand-water-to-protein-distance-limits 1.0 1.0)` | ran (no return value, nothing visible changed) |

### set_value_for_find_waters_sigma_cut_off

Python: `set_value_for_find_waters_sigma_cut_off(f)`  
Scheme: `(set-value-for-find-waters-sigma-cut-off f)`

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_value_for_find_waters_sigma_cut_off(1.0)` | ran (no return value); changed: get_text_for_find_waters_sigma_cut_off(): '  1.4' -> '  1.0' |
| Scheme | `(set-value-for-find-waters-sigma-cut-off 1.0)` | ran (no return value, nothing visible changed) |

### set_water_check_spherical_variance_limit

Python: `set_water_check_spherical_variance_limit(f)`  
Scheme: `(set-water-check-spherical-variance-limit f)`

set the limit of interesting variance, above which waters
 are listed (otherwise ignored)

default 0.12.

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_water_check_spherical_variance_limit(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-water-check-spherical-variance-limit 1.0)` | ran (no return value, nothing visible changed) |

### set_write_peaksearched_waters

Python: `set_write_peaksearched_waters()`  
Scheme: `(set-write-peaksearched-waters)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_write_peaksearched_waters()` | ran (no return value, nothing visible changed) |
| Scheme | `(set-write-peaksearched-waters)` | ran (no return value, nothing visible changed) |

### split_water

Python: `split_water(imol, chain_id, res_no, ins_code)`  
Scheme: `(split-water imol chain-id res-no ins-code)`

split the given water and fit to map.

If refinement map is not defined, don't do anything.

If there is more than one atom in the specified resiue, don't do
anything.

If the given atom does not have an alt conf of "", don't do anything.

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `split_water(0, "A", 41, "")` | ran (no return value, nothing visible changed) |
| Scheme | `(split-water 0 "A" 41 "")` | ran (no return value, nothing visible changed) |

### wrapped_create_find_waters_dialog

Python: `wrapped_create_find_waters_dialog()`  
Scheme: `(wrapped-create-find-waters-dialog)`

create a dialog for water fitting

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `wrapped_create_find_waters_dialog()` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(wrapped-create-find-waters-dialog)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens the Find Waters dialog (Calculate > Other Modelling Tools > Find Waters...).

