# Trim

[Scripting reference](../README.md) > Trim (3 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### pLDDT_to_b_factor

Python: `pLDDT_to_b_factor(imol)`  
Scheme: `(pLDDT-to-b-factor imol)`

convert the value in the B-factor column (typically pLDDT for AlphaFold models) to a temperature factor

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `pLDDT_to_b_factor(0)` | ran (no return value); changed: molecule 0: B-factors of 189 residue(s) (A1, A2, A3, A4 ...) |
| Scheme | `(pLDDT-to-b-factor 0)` | ran (no return value); changed: molecule 0: B-factors of 189 residue(s) (A1, A2, A3, A4 ...) |

### trim_molecule_by_b_factor

Python: `trim_molecule_by_b_factor(imol, limit, keep_higher)`  
Scheme: `(trim-molecule-by-b-factor imol limit keep-higher)`

trim the molecule by the value in the B-factor column.

If an atom in a residue has a "B-factor" above (or below, if keep_higher is true) limit, then the whole residue is deleted

Arguments: imol (a whole number), limit (a number), keep_higher (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `trim_molecule_by_b_factor(0, 1.0, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(trim-molecule-by-b-factor 0 1.0 1)` | ran (no return value, nothing visible changed) |

### trim_molecule_by_map

Python: `trim_molecule_by_map(imol_coords, imol_map, map_level, delete_or_zero_occ_flag)`  
Scheme: `(trim-molecule-by-map imol-coords imol-map map-level delete-or-zero-occ-flag)`

cut off (delete or give zero occupancy) atoms in the given
 molecule if they are below the given map (absolute) level.

Arguments: imol_coords (a whole number), imol_map (a whole number), map_level (a number), delete_or_zero_occ_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `trim_molecule_by_map(0, 1, 1.5, 1)` | ran (no return value); changed: molecule 0: occupancies of 189 residue(s) (A1, A2, A3, A4 ...) |
| Scheme | `(trim-molecule-by-map 0 1 1.5 1)` | ran (no return value); changed: molecule 0: occupancies of 189 residue(s) (A1, A2, A3, A4 ...) |

