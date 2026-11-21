# PDB Functions

[Scripting reference](../README.md) > PDB Functions (7 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_write_conect_record_state

Python: `get_write_conect_record_state()`  
Scheme: `(get-write-conect-record-state)`

return the state of the write_conect_records_flag.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_write_conect_record_state()` | ran, returned `0` |
| Scheme | `(get-write-conect-record-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### quick_save

Python: `quick_save()`  
Scheme: `(quick-save)`

save all modified coordinates molecules to the default
 names and save the state too.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `delete_residue(0, "A", 41, "")`, then `quick_save()` | ran, returned `0`; changed: molecule 0 renamed to tutorial-modern-coot-0.pdb; molecule_name(0): 'tutorial-modern.pdb' -> 'tutorial-modern-coot-0.pdb' |
| Scheme | first `(delete-residue 0 "A" 41 "")`, then `(quick-save)` | ran, returned `0`; changed: molecule 0 renamed to tutorial-modern-coot-0.pdb; molecule_name(0): 'tutorial-modern.pdb' -> 'tutorial-modern-coot-0.pdb' |

Example written and checked by hand on the test data. Expected: saves every modified model to <name>-coot-N.pdb (and the state files); returns 0; unmodified models are not written.

Python and Scheme gave the same answer.

### set_write_conect_record_state

Python: `set_write_conect_record_state(state)`  
Scheme: `(set-write-conect-record-state state)`

set the flag to write (or not) conect records to the PDB file.

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_write_conect_record_state(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-write-conect-record-state 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_write_conect_record_state was 0, set to 1, read back 1; Scheme: get-write-conect-record-state was 0, set to 1, read back 1.

### write_chain_to_pdb_file

Python: `write_chain_to_pdb_file(imol, chainid, filename)`  
Scheme: `(write-chain-to-pdb-file imol chainid filename)`

return 0 on success, -1 on error.

Arguments: imol (a whole number), chainid (text), filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_chain_to_pdb_file(0, "A", "chain-a.pdb")` | ran, returned `0` |
| Scheme | `(write-chain-to-pdb-file 0 "B" "chain-b.pdb")` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns 0 and writes only that chain to the file (-1 on error).

Python and Scheme gave the same answer.

### write_cif_file

Python: `write_cif_file(imol, file_name)`  
Scheme: `(write-cif-file imol file-name)`

return 0 on success, 1 on error.

Arguments: imol (a whole number), file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_cif_file(0, "out.cif")` | ran, returned `0` |
| Scheme | `(write-cif-file 0 "out.cif")` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns 0 and writes molecule 0 as an mmCIF file.

Note: Fixed in coot0 build 31: in Coot 0.9.8.96 each call on the same molecule wrote the model once more (140, 275, 410 kB; reading the third file gave three copies of every atom). File > Save Coordinates was not affected.

Python and Scheme gave the same answer.

### write_pdb_file

Python: `write_pdb_file(imol, file_name)`  
Scheme: `(write-pdb-file imol file-name)`

return 0 on success, 1 on error.

Arguments: imol (a whole number), file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_pdb_file(0, "out.pdb")` | ran, returned `0` |
| Scheme | `(write-pdb-file 0 "out.pdb")` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns 0 and writes molecule 0 as a PDB file (1 on error).

Python and Scheme gave the same answer.

### write_residue_range_to_pdb_file

Python: `write_residue_range_to_pdb_file(imol, chainid, resno_start, resno_end, filename)`  
Scheme: `(write-residue-range-to-pdb-file imol chainid resno-start resno-end filename)`

return 0 on success, 1 on error.

Arguments: imol (a whole number), chainid (text), resno_start (a whole number), resno_end (a whole number), filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_residue_range_to_pdb_file(0, "A", 41, 45, "a41-45.pdb")` | ran, returned `0` |
| Scheme | `(write-residue-range-to-pdb-file 0 "A" 41 45 "a41-45.pdb")` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns 0 and writes residues A41-A45 to the file.

Python and Scheme gave the same answer.

