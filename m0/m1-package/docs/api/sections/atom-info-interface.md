# Atom Info Interface

[Scripting reference](../README.md) > Atom Info Interface (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### output_atom_info_as_text

Python: `output_atom_info_as_text(imol, chain_id, resno, ins_code, atname, altconf)`  
Scheme: `(output-atom-info-as-text imol chain-id resno ins-code atname altconf)`

output to the terminal the Atom Info for the give atom specs

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), atname (text), altconf (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `output_atom_info_as_text(0, "A", 41, "", " CA ", "")` | not tried |
| Scheme | `(output-atom-info-as-text 0 "A" 41 "" " CA " "")` | not tried |

