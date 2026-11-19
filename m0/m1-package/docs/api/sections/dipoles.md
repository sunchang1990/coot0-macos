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
| Python | `add_dipole(0, "A", 41, "")` | ran, returned `[-1, [2.3836891226e-314, 3.0428733255e-314, 2.1617066947e-314]]` |
| Scheme | `(add-dipole 0 "A" 41 "")` | ran, returned `(-1 (5.0e-323 2.1584990723e-314 2.3856689583e-314))` |

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
| Python | `add_dipole_for_residues(0, [["A", 41, ""], ["A", 42, ""]])` | ran, returned `[-1, [1e-323, 2.46527736567e-313, 2.46477814396e-313]]` |
| Scheme | `(add-dipole-for-residues 0 (list (list "A" 41 "") (list "A" 42 "")))` | ran, returned `(-1 (1.0e-323 2.4652773064e-313 2.46477814396e-313))` |

### delete_dipole

Python: `delete_dipole(imol, dipole_number)`  
Scheme: `(delete-dipole imol dipole-number)`

Arguments: imol (a whole number), dipole_number (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_dipole(0, 1)` | ran (no return value) |
| Scheme | `(delete-dipole 0 1)` | ran (no return value) |

### make_and_draw_patterson

Python: `make_and_draw_patterson(mtz_file_name, f_col, sigf_col)`  
Scheme: `(make-and-draw-patterson mtz-file-name f-col sigf-col)`

Make a patterson molecule

Returns a new molecule number or -1 on failure

Arguments: mtz_file_name (text), f_col (text), sigf_col (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_and_draw_patterson("rnasa-1.8-all_refmac1.mtz", "FWT", "hello")` | not tried |
| Scheme | `(make-and-draw-patterson "rnasa-1.8-all_refmac1.mtz" "FWT" "hello")` | not tried |

### make_and_draw_patterson_using_intensities

Python: `make_and_draw_patterson_using_intensities(mtz_file_name, i_col, sigi_col)`  
Scheme: `(make-and-draw-patterson-using-intensities mtz-file-name i-col sigi-col)`

Make a patterson molecule

Returns a new molecule number or -1 on failure

Arguments: mtz_file_name (text), i_col (text), sigi_col (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_and_draw_patterson_using_intensities("rnasa-1.8-all_refmac1.mtz", "hello", "hello")` | not tried |
| Scheme | `(make-and-draw-patterson-using-intensities "rnasa-1.8-all_refmac1.mtz" "hello" "hello")` | not tried |

