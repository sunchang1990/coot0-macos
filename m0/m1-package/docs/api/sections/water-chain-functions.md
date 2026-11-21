# Water Chain Functions

[Scripting reference](../README.md) > Water Chain Functions (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### water_chain

Python: `water_chain(imol)`  
Scheme: `(water-chain imol)`

return the chain id of the water chain. Raw interface

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `water_chain_py`.
Also available in Scheme as `water-chain-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `water_chain(0)` | ran, returned `False` |
| Scheme | `(water-chain 0)` | ran, returned `#f` |

Example written and checked by hand on the test data. Expected: the chain id of a chain that holds only waters; False when there is none (as in both test models).

Python and Scheme gave the same answer.

### water_chain_from_shelx_ins

Python: `water_chain_from_shelx_ins(imol)`  
Scheme: `(water-chain-from-shelx-ins imol)`

return the chain id of the water chain from a shelx molecule. Raw interface.

Return False if no chain or bad imol

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `water_chain_from_shelx_ins_py`.
Also available in Scheme as `water-chain-from-shelx-ins-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `write_shelx_ins_file(0, "tut.ins")`, then `imol_s = read_shelx_ins_file("tut.ins", 0)`, then `water_chain_from_shelx_ins(imol_s)` | ran, returned `'B'` |
| Scheme | first `(write-shelx-ins-file 0 "tut.ins")`, then `(define imol-s (read-shelx-ins-file "tut.ins" 0))`, then `(water-chain-from-shelx-ins imol-s)` | ran, returned `"B"` |

Example written and checked by hand on the test data. Expected: the chain id that waters of the SHELX molecule go into; False if no chain or not a SHELX molecule.

Note: Returns 'B' although the model has no waters (B is a protein chain); it seems to report the last chain.

Python and Scheme gave the same answer.

