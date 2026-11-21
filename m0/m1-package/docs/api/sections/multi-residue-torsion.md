# Multi-Residue Torsion

[Scripting reference](../README.md) > Multi-Residue Torsion (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### multi_residue_torsion_fit

Python: `multi_residue_torsion_fit(imol, residues_specs_py, n_trials)`  
Scheme: `(multi-residue-torsion-fit imol residues-specs-scm n-trials)`

fit residues

(note: fit to the current-refinement map)

Arguments: imol (a whole number), residues_specs_py (a list or value), n_trials (a whole number). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `multi_residue_torsion_fit(0, [["A", 41, ""], ["A", 42, ""]], 20)` | ran, returned `True`; changed: molecule 0: coordinates of 2 residue(s) (A41, A42) |
| Scheme | `(multi-residue-torsion-fit 0 (list (list "A" 41 "") (list "A" 42 "")) 20)` | ran, returned `#t`; changed: molecule 0: coordinates of 2 residue(s) (A41, A42) |

Example written and checked by hand on the test data. Expected: fits the side chains/torsions of the listed residues to the refinement map (map 1); returns True and moves the residues.

Note: residues_specs must be a list of residue specs; the old example passed one spec

Python and Scheme gave the same answer.

