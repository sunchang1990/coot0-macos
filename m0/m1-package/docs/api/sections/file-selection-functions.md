# File Selection Functions

[Scripting reference](../README.md) > File Selection Functions (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### save_coords_name_suggestion

Python: `save_coords_name_suggestion(imol)`  
Scheme: `(save-coords-name-suggestion-scm imol)`

Return the default file name suggestion (that would come up in the
 save coordinates dialog) or Python false if imol is not a valid
 model molecule.

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `save_coords_name_suggestion_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_coords_name_suggestion(0)` | ran, returned `'tutorial-modern-coot-0.pdb'` |
| Scheme | `(save-coords-name-suggestion-scm 0)` | ran, returned `"tutorial-modern-coot-0.pdb"` |

Python and Scheme gave the same answer.

