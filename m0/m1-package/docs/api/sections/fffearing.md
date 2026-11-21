# FFFearing

[Scripting reference](../README.md) > FFFearing (3 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### fffear_angular_resolution

Python: `fffear_angular_resolution()`  
Scheme: `(fffear-angular-resolution)`

return the fffear angular resolution in degrees

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fffear_angular_resolution()` | ran, returned `15.0` |
| Scheme | `(fffear-angular-resolution)` | ran, returned `15.0` |

Python and Scheme gave the same answer.

### fffear_search

Python: `fffear_search(imol_model, imol_map)`  
Scheme: `(fffear-search imol-model imol-map)`

fffear search model in molecule number imol_model in map
 number imol_map

Arguments: imol_model (a whole number), imol_map (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `imol = new_molecule_by_atom_selection(0, "//A/41-45")`, then `fffear_search(imol, 1)` | not run: long run: 203 s even for a 5-residue search model |
| Scheme | first `(new-molecule-by-atom-selection 0 "//A/41-45")`, then `(fffear-search 3 1)` | not run: long run: 203 s even for a 5-residue search model |

Example written and checked by hand on the test data. Expected: returns the new map molecule of the FFFear search score of the model fragment in map 1.

### set_fffear_angular_resolution

Python: `set_fffear_angular_resolution(f)`  
Scheme: `(set-fffear-angular-resolution f)`

set and return the fffear angular resolution in degrees

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_fffear_angular_resolution(1.0)` | ran (no return value); changed: fffear_angular_resolution(): 15 -> 1 |
| Scheme | `(set-fffear-angular-resolution 1.0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: fffear_angular_resolution was 15.0, set to 23.0, read back 23.0; Scheme: fffear-angular-resolution was 15.0, set to 23.0, read back 23.0.

