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
| Python | `water_chain(0)` | not tried |
| Scheme | `(water-chain 0)` | not tried |

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
| Python | `water_chain_from_shelx_ins(0)` | not tried |
| Scheme | `(water-chain-from-shelx-ins 0)` | not tried |

