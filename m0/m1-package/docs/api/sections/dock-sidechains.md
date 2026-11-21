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
| Python | first `assign_sequence_from_string(0, "A", "DVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLIDQTC")`, then `cootaneer(1, 0, ["A", 41, "", " CA ", ""])` | ran, returned `1`; changed: molecule 0: atoms of 83 residue(s) (A2, A3, A5, A6 ...); molecule 0: coordinates of 10 residue(s) (A1, A4, A26, A34 ...); n_atoms(0): 1465 -> 1466 |
| Scheme | first `(assign-sequence-from-string 0 "A" "DVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLIDQTC")`, then `(cootaneer 1 0 (list "A" 41 "" " CA " ""))` | ran, returned `1`; changed: molecule 0: atoms of 83 residue(s) (A2, A3, A5, A6 ...); molecule 0: coordinates of 10 residue(s) (A1, A4, A26, A34 ...); n_atoms(0): 1465 -> 1466 |

Example written and checked by hand on the test data. Expected: returns 1 when the fragment containing A41 CA was docked to the assigned sequence (side chains rebuilt), 0 on failure.

Python and Scheme gave the same answer.

