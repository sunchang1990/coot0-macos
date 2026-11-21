# Close Molecule Functions

[Scripting reference](../README.md) > Close Molecule Functions (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### close_molecule

Python: `close_molecule(imol)`  
Scheme: `(close-molecule imol)`

close the molecule

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `close_molecule(0)` | ran (no return value); changed: molecule 0 closed; first_coords_imol(): 0 -> -1; first_molecule_with_symmetry_displayed(): 0 -> -1; draw_hydrogens_state(0): 1 -> -1 ... |
| Scheme | `(close-molecule 0)` | ran (no return value); changed: molecule 0 closed; first_coords_imol(): 0 -> -1; first_molecule_with_symmetry_displayed(): 0 -> -1; draw_hydrogens_state(0): 1 -> -1 ... |

