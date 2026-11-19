# Partial Charges

[Scripting reference](../README.md) > Partial Charges (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### show_partial_charge_info

Python: `show_partial_charge_info(imol, chain_id, resno, ins_code)`  
Scheme: `(show-partial-charge-info imol chain-id resno ins-code)`

show the partial charges for the residue of the given specs
 (charges are read from the dictionary)

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_partial_charge_info(0, "A", 41, "")` | not tried |
| Scheme | `(show-partial-charge-info 0 "A" 41 "")` | not tried |

