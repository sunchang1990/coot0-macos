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
| Python | `multi_residue_torsion_fit(0, ["A", 41, ""], 1)` | error: SystemError: <built-in function multi_residue_torsion_fit_py> returned a result with an exception set |
| Scheme | `(multi-residue-torsion-fit 0 (list "A" 41 "") 1)` | error: In procedure length: Wrong type argument in position 1: "A" |

