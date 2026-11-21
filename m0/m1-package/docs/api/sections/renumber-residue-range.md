# Renumber Residue Range

[Scripting reference](../README.md) > Renumber Residue Range (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### change_residue_number

Python: `change_residue_number(imol, chain_id, current_resno, current_inscode, new_resno, new_inscode)`  
Scheme: `(change-residue-number imol chain-id current-resno current-inscode new-resno new-inscode)`

change chain id, residue number or insertion code for given
 residue

Arguments: imol (a whole number), chain_id (text), current_resno (a whole number), current_inscode (text), new_resno (a whole number), new_inscode (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `change_residue_number(0, "A", 41, "", 41, "")` | ran, returned `1` |
| Scheme | `(change-residue-number 0 "A" 41 "" 41 "")` | ran, returned `1` |

Python and Scheme gave the same answer.

### renumber_residue_range

Python: `renumber_residue_range(imol, chain_id, start_res, last_res, offset)`  
Scheme: `(renumber-residue-range imol chain-id start-res last-res offset)`

renumber the given residue range by offset residues

Arguments: imol (a whole number), chain_id (text), start_res (a whole number), last_res (a whole number), offset (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `renumber_residue_range(0, "A", 41, 45, 100)` | ran, returned `1`; changed: molecule 0: added 5 residue(s) (A141, A142, A143, A144 ...); molecule 0: deleted 5 residue(s) (A41, A42, A43, A44 ...) |
| Scheme | `(renumber-residue-range 0 "A" 41 45 100)` | ran, returned `1`; changed: molecule 0: added 5 residue(s) (A141, A142, A143, A144 ...); molecule 0: deleted 5 residue(s) (A41, A42, A43, A44 ...) |

Example written and checked by hand on the test data. Expected: returns 1 and adds the offset to the residue numbers of A41-A45.

Python and Scheme gave the same answer.

