# SHELXL Functions

[Scripting reference](../README.md) > SHELXL Functions (6 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_shelx_string_to_molecule

Python: `add_shelx_string_to_molecule(imol, string)`  
Scheme: `(add-shelx-string-to-molecule imol string)`

Arguments: imol (a whole number), string (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_shelx_string_to_molecule(0, "hello")` | not run: not run automatically (shelx: exits, uses the network, an external program, files or a screen) |
| Scheme | `(add-shelx-string-to-molecule 0 "hello")` | not run: not run automatically (shelx: exits, uses the network, an external program, files or a screen) |

### chain_id_for_shelxl_residue_number

Python: `chain_id_for_shelxl_residue_number(imol, resno)`  
Scheme: `(chain-id-for-shelxl-residue-number imol resno)`

Returns the chain id for the given residue. Return Py_False if
 can't do it/fail.

Arguments: imol (a whole number), resno (a whole number). Returns: a value (see the result of the example).
Also available in Python as `chain_id_for_shelxl_residue_number_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `chain_id_for_shelxl_residue_number(0, 41)` | not run: not run automatically (shelx: exits, uses the network, an external program, files or a screen) |
| Scheme | `(chain-id-for-shelxl-residue-number 0 41)` | not run: not run automatically (shelx: exits, uses the network, an external program, files or a screen) |

### handle_shelx_fcf_file_internal

Python: `handle_shelx_fcf_file_internal(filename)`  
Scheme: `(handle-shelx-fcf-file-internal filename)`

for shelx fcf file that needs to be filtered:

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_shelx_fcf_file_internal("tutorial-modern.pdb")` | not run: not run automatically (shelx: exits, uses the network, an external program, files or a screen) |
| Scheme | `(handle-shelx-fcf-file-internal "tutorial-modern.pdb")` | not run: not run automatically (shelx: exits, uses the network, an external program, files or a screen) |

### is_shelx_molecule

Python: `is_shelx_molecule(imol)`  
Scheme: `(is-shelx-molecule imol)`

return 1 for yes, 0 for invalid imol or no.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `is_shelx_molecule(0)` | not tried |
| Scheme | `(is-shelx-molecule 0)` | not tried |

### read_shelx_ins_file

Python: `read_shelx_ins_file(filename, recentre_flag)`  
Scheme: `(read-shelx-ins-file filename recentre-flag)`

read a SHELXL .ins file

Arguments: filename (text), recentre_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_shelx_ins_file("tutorial-modern.pdb", 1)` | not tried |
| Scheme | `(read-shelx-ins-file "tutorial-modern.pdb" 1)` | not tried |

### write_shelx_ins_file

Python: `write_shelx_ins_file(imol, filename)`  
Scheme: `(write-shelx-ins-file imol filename)`

write a SHELXL .ins file for molecule number imol

Arguments: imol (a whole number), filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_shelx_ins_file(0, "tutorial-modern.pdb")` | not tried |
| Scheme | `(write-shelx-ins-file 0 "tutorial-modern.pdb")` | not tried |

