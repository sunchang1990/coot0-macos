# Terminal OXT Atom

[Scripting reference](../README.md) > Terminal OXT Atom (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_OXT_to_residue

Python: `add_OXT_to_residue(imol, chain_id, reso, insertion_code)`  
Scheme: `(add-OXT-to-residue imol chain-id reso insertion-code)`

Arguments: imol (a whole number), chain_id (text), reso (a whole number), insertion_code (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_OXT_to_residue(0, "A", 1, "")` | ran, returned `1` |
| Scheme | `(add-OXT-to-residue 0 "A" 1 "")` | ran, returned `1` |

