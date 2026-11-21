# SHELXL Functions

[Scripting reference](../README.md) > SHELXL Functions (6 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_shelx_string_to_molecule

Python: `add_shelx_string_to_molecule(imol, string)`  
Scheme: `(add-shelx-string-to-molecule imol string)`

Arguments: imol (a whole number), string (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `write_shelx_ins_file(0, "tut.ins")`, then `imol_s = read_shelx_ins_file("tut.ins", 0)`, then `add_shelx_string_to_molecule(imol_s, "DFIX 1.54 C_41 CA_41")` | ran (no return value, nothing visible changed) |
| Scheme | first `(write-shelx-ins-file 0 "tut.ins")`, then `(define imol-s (read-shelx-ins-file "tut.ins" 0))`, then `(add-shelx-string-to-molecule imol-s "DFIX 1.54 C_41 CA_41")` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: adds the line to the SHELX molecule's instructions; it appears in the next written .ins file.

### chain_id_for_shelxl_residue_number

Python: `chain_id_for_shelxl_residue_number(imol, resno)`  
Scheme: `(chain-id-for-shelxl-residue-number imol resno)`

Returns the chain id for the given residue. Return Py_False if
 can't do it/fail.

Arguments: imol (a whole number), resno (a whole number). Returns: a value (see the result of the example).
Also available in Python as `chain_id_for_shelxl_residue_number_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `write_shelx_ins_file(0, "tut.ins")`, then `imol_s = read_shelx_ins_file("tut.ins", 0)`, then `chain_id_for_shelxl_residue_number(imol_s, 1041)` | ran, returned `'B'` |
| Scheme | first `(write-shelx-ins-file 0 "tut.ins")`, then `(define imol-s (read-shelx-ins-file "tut.ins" 0))`, then `(chain-id-for-shelxl-residue-number imol-s 1041)` | ran, returned `"B"` |

Example written and checked by hand on the test data. Expected: the chain that holds SHELXL residue number 1041 (chain B's residues get +1000 in the .ins file); False if none.

Python and Scheme gave the same answer.

### handle_shelx_fcf_file_internal

Python: `handle_shelx_fcf_file_internal(filename)`  
Scheme: `(handle-shelx-fcf-file-internal filename)`

for shelx fcf file that needs to be filtered:

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_shelx_fcf_file_internal("rnasa-sm-data.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sm-data.cif SigmaA); new molecule 4 (map, rnasa-sm-data.cif Diff-SigmaA); graphics_n_molecules(): 3 -> 5; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(handle-shelx-fcf-file-internal "rnasa-sm-data.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sm-data.cif SigmaA); new molecule 4 (map, rnasa-sm-data.cif Diff-SigmaA); graphics_n_molecules(): 3 -> 5; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: same as read_small_molecule_data_cif (that is all it does in 0.9.8.96): returns the SigmaA map molecule number of a SHELXL .fcf (LIST 6) / data CIF.

Note: rnasa-sm.cif and rnasa-sm-data.cif (in test-data) are a small-molecule style CIF made from residues A39-41 of the test model and the rnasa reflections, only to show the call.

Python and Scheme gave the same answer.

### is_shelx_molecule

Python: `is_shelx_molecule(imol)`  
Scheme: `(is-shelx-molecule imol)`

return 1 for yes, 0 for invalid imol or no.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `write_shelx_ins_file(0, "tut.ins")`, then `imol_s = read_shelx_ins_file("tut.ins", 0)`, then `is_shelx_molecule(imol_s)` | ran, returned `1` |
| Scheme | first `(write-shelx-ins-file 0 "tut.ins")`, then `(define imol-s (read-shelx-ins-file "tut.ins" 0))`, then `(is-shelx-molecule imol-s)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: 1 for a molecule read from a SHELXL .ins file, 0 for a PDB model such as molecule 0.

Python and Scheme gave the same answer.

### read_shelx_ins_file

Python: `read_shelx_ins_file(filename, recentre_flag)`  
Scheme: `(read-shelx-ins-file filename recentre-flag)`

read a SHELXL .ins file

Arguments: filename (text), recentre_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `write_shelx_ins_file(0, "tut.ins")`, then `read_shelx_ins_file("tut.ins", 0)` | ran, returned `3`; changed: new molecule 3 (model, tut.ins); graphics_n_molecules(): 3 -> 4 |
| Scheme | first `(write-shelx-ins-file 0 "tut.ins")`, then `(read-shelx-ins-file "tut.ins" 0)` | ran, returned `3`; changed: new molecule 3 (model, tut.ins); graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the new molecule number of the model read from the .ins file (recentre flag 0: the view stays).

Python and Scheme gave the same answer.

### write_shelx_ins_file

Python: `write_shelx_ins_file(imol, filename)`  
Scheme: `(write-shelx-ins-file imol filename)`

write a SHELXL .ins file for molecule number imol

Arguments: imol (a whole number), filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_shelx_ins_file(0, "tut.ins")` | ran, returned `1` |
| Scheme | `(write-shelx-ins-file 0 "tut.ins")` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 and writes molecule 0 as a SHELXL .ins file.

Python and Scheme gave the same answer.

