# Dipoles

[Scripting reference](../README.md) > Dipoles (5 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_dipole

Python: `add_dipole(imol, chain_id, res_no, ins_code)`  
Scheme: `(add-dipole imol chain-id res-no ins-code)`

generate a dipole from all atoms in the given residues.

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text). Returns: a value (see the result of the example).
Also available in Python as `add_dipole_py`.
Also available in Scheme as `add-dipole-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_dipole(0, "A", 41, "")` | ran, returned `[-1, [0.0, 6.519311867879e-311, 3.56e-322]]` |
| Scheme | `(add-dipole 0 "A" 41 "")` | ran, returned `(-1 (0.0 6.519311867879e-311 3.56e-322))` |

Python and Scheme gave the same answer.

### add_dipole_for_residues

Python: `add_dipole_for_residues(imol, residue_specs)`  
Scheme: `(add-dipole-for-residues imol residue-specs)`

add a dipole given a set of residues. Return a dipole
 description.

Arguments: imol (a whole number), residue_specs (a list or value). Returns: a value (see the result of the example).
Also available in Python as `add_dipole_for_residues_py`.
Also available in Scheme as `add-dipole-for-residues-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_dipole_for_residues(0, [["A", 41, ""], ["A", 42, ""]])` | ran, returned `[-1, [1e-323, 2.19576134326e-313, 2.19574026167e-313]]` |
| Scheme | `(add-dipole-for-residues 0 (list (list "A" 41 "") (list "A" 42 "")))` | ran, returned `(-1 (1.0e-323 2.19576134326e-313 2.1957402854e-313))` |

Python and Scheme gave the same answer.

### delete_dipole

Python: `delete_dipole(imol, dipole_number)`  
Scheme: `(delete-dipole imol dipole-number)`

Arguments: imol (a whole number), dipole_number (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_dipole(0, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(delete-dipole 0 1)` | ran (no return value, nothing visible changed) |

### make_and_draw_patterson

Python: `make_and_draw_patterson(mtz_file_name, f_col, sigf_col)`  
Scheme: `(make-and-draw-patterson mtz-file-name f-col sigf-col)`

Make a patterson molecule

Returns a new molecule number or -1 on failure

Arguments: mtz_file_name (text), f_col (text), sigf_col (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_and_draw_patterson("rnasa-1.8-all_refmac1.mtz", "FGMP18", "SIGFGMP18")` | ran, returned `3`; changed: new molecule 3 (map, Patterson rnasa-1.8-all_refmac1.mtz FGMP18); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(make-and-draw-patterson "rnasa-1.8-all_refmac1.mtz" "FGMP18" "SIGFGMP18")` | ran, returned `3`; changed: new molecule 3 (map, Patterson rnasa-1.8-all_refmac1.mtz FGMP18); graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number of the Patterson map.

Python and Scheme gave the same answer.

### make_and_draw_patterson_using_intensities

Python: `make_and_draw_patterson_using_intensities(mtz_file_name, i_col, sigi_col)`  
Scheme: `(make-and-draw-patterson-using-intensities mtz-file-name i-col sigi-col)`

Make a patterson molecule

Returns a new molecule number or -1 on failure

Arguments: mtz_file_name (text), i_col (text), sigi_col (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_and_draw_patterson_using_intensities("two-sigma-columns.mtz", "I-obs", "SIGI-obs")` | ran, returned `3`; changed: new molecule 3 (map, Patterson two-sigma-columns.mtz I-obs); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(make-and-draw-patterson-using-intensities "two-sigma-columns.mtz" "I-obs" "SIGI-obs")` | ran, returned `3`; changed: new molecule 3 (map, Patterson two-sigma-columns.mtz I-obs); graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number of the Patterson map made from intensities.

Python and Scheme gave the same answer.

