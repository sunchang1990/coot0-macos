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
| Python | `execute_find_blobs(0, 1, 1.0, 1)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(execute-find-blobs 0 1 1.0 1)` | stopped Coot when tried without a window (not checked with a window) |

### execute_find_waters_real

Python: `execute_find_waters_real(imol_for_map, imol_for_protein, new_waters_mol_flag, rmsd_cut_off)`  
Scheme: `(execute-find-waters-real imol-for-map imol-for-protein new-waters-mol-flag rmsd-cut-off)`

find waters

Arguments: imol_for_map (a whole number), imol_for_protein (a whole number), new_waters_mol_flag (a whole number), rmsd_cut_off (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `execute_find_waters_real(1, 0, 1, 1.5)` | ran (no return value) |
| Scheme | `(execute-find-waters-real 1 0 1 1.5)` | ran (no return value) |

### find_waters

Python: `find_waters(imol_for_map, imol_for_protein, new_waters_mol_flag, rmsd_cut_off, show_blobs_dialog)`  
Scheme: `(find-waters imol-for-map imol-for-protein new-waters-mol-flag rmsd-cut-off show-blobs-dialog)`

Arguments: imol_for_map (a whole number), imol_for_protein (a whole number), new_waters_mol_flag (a whole number), rmsd_cut_off (a number), show_blobs_dialog (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `find_waters(1, 0, 1, 1.5, 1)` | ran (no return value) |
| Scheme | `(find-waters 1 0 1 1.5 1)` | ran (no return value) |

### get_text_for_find_waters_sigma_cut_off

Python: `get_text_for_find_waters_sigma_cut_off()`  
Scheme: `(get-text-for-find-waters-sigma-cut-off)`

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_text_for_find_waters_sigma_cut_off()` | ran, returned `'  1.4'` |
| Scheme | `(get-text-for-find-waters-sigma-cut-off)` | ran, returned `"  1.4"` |

### max_water_distance

Python: `max_water_distance(imol)`  
Scheme: `(max-water-distance imol)`

return the maximum minimum distance of any water atom to
 any protein atom - used in validation of
 move_waters_to_around_protein() funtion.

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `max_water_distance(0)` | not tried |
| Scheme | `(max-water-distance 0)` | not tried |

### move_hetgroups_to_around_protein

Python: `move_hetgroups_to_around_protein(imol)`  
Scheme: `(move-hetgroups-to-around-protein imol)`

move all hetgroups (including waters) of molecule number
 imol so that they are around the protein.

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `move_hetgroups_to_around_protein(0)` | not tried |
| Scheme | `(move-hetgroups-to-around-protein 0)` | not tried |

### move_waters_to_around_protein

Python: `move_waters_to_around_protein(imol)`  
Scheme: `(move-waters-to-around-protein imol)`

move waters of molecule number imol so that they are around the protein.

Returns the number of moved waters.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `move_waters_to_around_protein(0)` | not tried |
| Scheme | `(move-waters-to-around-protein 0)` | not tried |

### renumber_waters

Python: `renumber_waters(imol)`  
Scheme: `(renumber-waters imol)`

Renumber the waters of molecule number imol with consecutive numbering

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `renumber_waters(0)` | not tried |
| Scheme | `(renumber-waters 0)` | not tried |

### set_ligand_water_n_cycles

Python: `set_ligand_water_n_cycles(i)`  
Scheme: `(set-ligand-water-n-cycles i)`

set the number of cycles of water searching

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ligand_water_n_cycles(1)` | not tried |
| Scheme | `(set-ligand-water-n-cycles 1)` | not tried |

### set_ligand_water_to_protein_distance_limits

Python: `set_ligand_water_to_protein_distance_limits(f1, f2)`  
Scheme: `(set-ligand-water-to-protein-distance-limits f1 f2)`

set ligand to protein distance limits

 f1 is the minimum distance, f2 is the maximum distance

Arguments: f1 (a number), f2 (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ligand_water_to_protein_distance_limits(1.0, 1.0)` | not tried |
| Scheme | `(set-ligand-water-to-protein-distance-limits 1.0 1.0)` | not tried |

### set_value_for_find_waters_sigma_cut_off

Python: `set_value_for_find_waters_sigma_cut_off(f)`  
Scheme: `(set-value-for-find-waters-sigma-cut-off f)`

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_value_for_find_waters_sigma_cut_off(1.0)` | not tried |
| Scheme | `(set-value-for-find-waters-sigma-cut-off 1.0)` | not tried |

### set_water_check_spherical_variance_limit

Python: `set_water_check_spherical_variance_limit(f)`  
Scheme: `(set-water-check-spherical-variance-limit f)`

set the limit of interesting variance, above which waters
 are listed (otherwise ignored)

default 0.12.

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_water_check_spherical_variance_limit(1.0)` | not tried |
| Scheme | `(set-water-check-spherical-variance-limit 1.0)` | not tried |

### set_write_peaksearched_waters

Python: `set_write_peaksearched_waters()`  
Scheme: `(set-write-peaksearched-waters)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_write_peaksearched_waters()` | not tried |
| Scheme | `(set-write-peaksearched-waters)` | not tried |

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
| Python | `split_water(0, "A", 41, "")` | not tried |
| Scheme | `(split-water 0 "A" 41 "")` | not tried |

### wrapped_create_find_waters_dialog

Python: `wrapped_create_find_waters_dialog()`  
Scheme: `(wrapped-create-find-waters-dialog)`

create a dialog for water fitting

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `wrapped_create_find_waters_dialog()` | not tried |
| Scheme | `(wrapped-create-find-waters-dialog)` | not tried |

