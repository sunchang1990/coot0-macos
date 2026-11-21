# Drag and Drop Functions

[Scripting reference](../README.md) > Drag and Drop Functions (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### handle_drag_and_drop_string

Python: `handle_drag_and_drop_string(uri)`  
Scheme: `(handle-drag-and-drop-string uri)`

Arguments: uri (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_drag_and_drop_string("standard-residues.pdb")` | ran, returned `1`; changed: new molecule 3 (model, standard-residues.pdb); rotation centre moved 40.1 A to (4.0, -0.8, 3.0); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | `(handle-drag-and-drop-string "nag_only.pdb")` | ran, returned `1`; changed: new molecule 3 (model, nag_only.pdb); rotation centre moved 44.4 A to (-0.0, -0.0, -0.0); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns 1 and opens the dropped file (coordinates, MTZ or map) as a new molecule.

Python and Scheme gave the same answer.

