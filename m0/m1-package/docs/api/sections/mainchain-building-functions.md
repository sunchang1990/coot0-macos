# Mainchain Building Functions

[Scripting reference](../README.md) > Mainchain Building Functions (3 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### db_mainchain

Python: `db_mainchain(imol, chain_id, iresno_start, iresno_end, direction)`  
Scheme: `(db-mainchain imol chain-id iresno-start iresno-end direction)`

CA -> mainchain conversion

direction is either "forwards" or "backwards"

See also the function below.

return the new molecule number

Arguments: imol (a whole number), chain_id (text), iresno_start (a whole number), iresno_end (a whole number), direction (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `db_mainchain(0, "A", 10, 30, "forwards")` | ran, returned `3`; changed: new molecule 3 (model, mainchain-forwards); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | `(db-mainchain 0 "A" 10 30 "forwards")` | ran, returned `3`; changed: new molecule 3 (model, mainchain-forwards); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns a new molecule with main chain built from the CA trace of the range by database fragments; -1 on error.

Python and Scheme gave the same answer.

### db_mainchains_fragment

Python: `db_mainchains_fragment(imol, chain_id, res_no)`  
Scheme: `(db-mainchains-fragment imol chain-id res-no)`

CA-Zone to Mainchain for a fragment based on the given residue.

Both directions are built. This is the modern interface.

Arguments: imol (a whole number), chain_id (text), res_no (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `db_mainchains_fragment(0, "A", 41)` | ran, returned `3`; changed: new molecule 3 (model, mainchain-forwards); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(db-mainchains-fragment 0 "A" 41)` | ran, returned `3`; changed: new molecule 3 (model, mainchain-forwards); graphics_n_molecules(): 3 -> 4 |

Python and Scheme gave the same answer.

### do_db_main

Python: `do_db_main(state)`  
Scheme: `(do-db-main state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_db_main(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(do-db-main 1)` | ran (no return value, nothing visible changed) |

