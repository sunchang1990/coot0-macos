# Nucleotides

[Scripting reference](../README.md) > Nucleotides (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### find_nucleic_acids_local

Python: `find_nucleic_acids_local(radius)`  
Scheme: `(find-nucleic-acids-local radius)`

autobuild nucleic acid chains

 Find secondary structure local to current view in the current map.
 Add to a molecule called "NuclAcid", create it if needed.

 Returns the index of the new molecule.

Arguments: radius (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `find_nucleic_acids_local(5.0)` | ran, returned `3`; changed: new molecule 3 (model, NuclAcid); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | `(find-nucleic-acids-local 5.0)` | ran, returned `3`; changed: new molecule 3 (model, NuclAcid); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

Python and Scheme gave the same answer.

