# Dictionary Functions

[Scripting reference](../README.md) > Dictionary Functions (5 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### SMILES_for_comp_id

Python: `SMILES_for_comp_id(comp_id)`  
Scheme: `(SMILES-for-comp-id comp-id)`

this can throw an exception

Arguments: comp_id (text). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `SMILES_for_comp_id("ALA")` | ran, returned `'C[C@H](N)C(O)=O'` |
| Scheme | `(SMILES-for-comp-id "ALA")` | ran, returned `"C[C@H](N)C(O)=O"` |

Python and Scheme gave the same answer.

### cif_file_for_comp_id

Python: `cif_file_for_comp_id(comp_id)`  
Scheme: `(cif-file-for-comp-id comp-id)`

Arguments: comp_id (text). Returns: a value (see the result of the example).
Also available in Python as `cif_file_for_comp_id_py`.
Also available in Scheme as `cif-file-for-comp-id-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `cif_file_for_comp_id("ALA")` | ran, returned `'<coot0>/monomers/a/ALA.cif'` |
| Scheme | `(cif-file-for-comp-id "ALA")` | ran, returned `"<coot0>/monomers/a/ALA.cif"` |

Python and Scheme gave the same answer.

### debug_dictionary

Python: `debug_dictionary()`  
Scheme: `(debug-dictionary)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `debug_dictionary()` | ran (no return value) |
| Scheme | `(debug-dictionary)` | ran (no return value) |

### dictionaries_read

Python: `dictionaries_read()`  
Scheme: `(dictionaries-read)`

return a list of all the dictionaries read

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `dictionaries_read_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `dictionaries_read()` | ran, returned `[]` |
| Scheme | `(dictionaries-read)` | ran, returned `()` |

Python and Scheme gave the same answer.

### dictionary_entries

Python: `dictionary_entries()`  
Scheme: `(dictionary-entries)`

Arguments: none. Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `dictionary_entries()` | ran, returned `['ALA', 'ASP', 'ASN', 'CYS', 'GLN', 'GLY', 'GLU', 'PHE', 'HIS', 'ILE', 'LYS', 'LEU', 'MET', 'MSE', 'PRO', 'ARG', 'SER',  ...` |
| Scheme | `(dictionary-entries)` | ran, returned `("ALA" "ASP" "ASN" "CYS" "GLN" "GLY" "GLU" "PHE" "HIS" "ILE" "LYS" "LEU" "MET" "MSE" "PRO" "ARG" "SER" "THR" "VAL" "TRP" ...` |

Python and Scheme gave the same answer.

