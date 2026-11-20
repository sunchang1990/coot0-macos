# Change Chain ID

[Scripting reference](../README.md) > Change Chain ID (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### change_chain_id

Python: `change_chain_id(imol, from_chain_id, to_chain_id, use_res_range_flag, from_resno, to_resno)`  
Scheme: `(change-chain-id imol from-chain-id to-chain-id use-res-range-flag from-resno to-resno)`

change the chain id of the specified residue

Arguments: imol (a whole number), from_chain_id (text), to_chain_id (text), use_res_range_flag (a whole number), from_resno (a whole number), to_resno (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `change_chain_id(0, "A", "A", 1, 41, 41)` | ran (no return value) |
| Scheme | `(change-chain-id 0 "A" "A" 1 41 41)` | ran (no return value) |

### change_chain_id_with_result

Python: `change_chain_id_with_result(imol, from_chain_id, to_chain_id, use_res_range_flag, from_resno, to_resno)`  
Scheme: `(change-chain-id-with-result-scm imol from-chain-id to-chain-id use-res-range-flag from-resno to-resno)`

Arguments: imol (a whole number), from_chain_id (text), to_chain_id (text), use_res_range_flag (a whole number), from_resno (a whole number), to_resno (a whole number). Returns: a value (see the result of the example).
Also available in Python as `change_chain_id_with_result_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `change_chain_id_with_result(0, "A", "A", 1, 41, 41)` | ran, returned `[0, 'CONFLICT!  Residue 41 already exists in chain A\nChange chain ID of residue range failed.\n']` |
| Scheme | `(change-chain-id-with-result-scm 0 "A" "A" 1 41 41)` | ran, returned `(0 "CONFLICT!  Residue 41 already exists in chain A\nChange chain ID of residue range failed.\n")` |

Python and Scheme gave the same answer.

