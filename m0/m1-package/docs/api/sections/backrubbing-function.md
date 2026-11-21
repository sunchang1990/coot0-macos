# Backrubbing function

[Scripting reference](../README.md) > Backrubbing function (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### backrub_rotamer

Python: `backrub_rotamer(imol, chain_id, res_no, ins_code, alt_conf)`  
Scheme: `(backrub-rotamer imol chain-id res-no ins-code alt-conf)`

Do a back-rub rotamer search (with autoaccept).

Returns the success status, 0 for fail, 1 for successful fit.

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), alt_conf (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `backrub_rotamer(0, "A", 41, "", "")` | ran, returned `1`; changed: molecule 0: coordinates of 3 residue(s) (A40, A41, A42) |
| Scheme | `(backrub-rotamer 0 "A" 41 "" "")` | ran, returned `1`; changed: molecule 0: coordinates of 3 residue(s) (A40, A41, A42) |

Python and Scheme gave the same answer.

### backrub_rotamer_intermediate_atoms

Python: `backrub_rotamer_intermediate_atoms()`  
Scheme: `(backrub-rotamer-intermediate-atoms)`

apply rotamer backrub to the active atom of the intermediate atoms

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `refine_zone(0, "A", 41, 41, "")`, then `backrub_rotamer_intermediate_atoms()` | ran, returned `0` |
| Scheme | first `(refine-zone 0 "A" 41 41 "")`, then `(backrub-rotamer-intermediate-atoms)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns 1 when a backrub rotamer fit of the intermediate atoms' residue succeeds, 0 otherwise.

Note: Returned 0 even with intermediate atoms present (headless; probably needs an active atom chosen in the graphics window).

Python and Scheme gave the same answer.

