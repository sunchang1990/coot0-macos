# Dock Sidechains

[Scripting reference](../README.md) > Dock Sidechains (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### cootaneer

Python: `cootaneer(imol_map, imol_model, atom_in_fragment_atom_spec)`  
Scheme: `(cootaneer imol-map imol-model atom-in-fragment-atom-spec)`

Arguments: imol_map (a whole number), imol_model (a whole number), atom_in_fragment_atom_spec (a list or value). Returns: a whole number.
Also available in Python as `cootaneer_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `cootaneer(1, 0, ["A", 41, "", " CA ", ""])` | ran, returned `0` |
| Scheme | `(cootaneer 1 0 (list "A" 41 "" " CA " ""))` | ran, returned `0` |

