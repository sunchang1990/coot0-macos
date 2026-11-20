# graphics 2D ligand view

[Scripting reference](../README.md) > graphics 2D ligand view (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### set_show_graphics_ligand_view

Python: `set_show_graphics_ligand_view(state)`  
Scheme: `(set-show-graphics-ligand-view state)`

set the graphics ligand view state

 (default is 1 (on)).

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_graphics_ligand_view(1)` | ran (no return value) |
| Scheme | `(set-show-graphics-ligand-view 1)` | ran (no return value) |

