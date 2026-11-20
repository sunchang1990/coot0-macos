# Unit Cell interface

[Scripting reference](../README.md) > Unit Cell interface (4 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_show_unit_cell

Python: `get_show_unit_cell(imol)`  
Scheme: `(get-show-unit-cell imol)`

return the stage of show unit cell for molecule number imol

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_show_unit_cell(0)` | ran, returned `0` |
| Scheme | `(get-show-unit-cell 0)` | ran, returned `0` |

Python and Scheme gave the same answer.

### set_show_unit_cell

Python: `set_show_unit_cell(imol, istate)`  
Scheme: `(set-show-unit-cell imol istate)`

set the state of show unit cell for the particular molecule number imol

1 for displayed
0 for undisplayed

Arguments: imol (a whole number), istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_unit_cell(0, 1)` | ran (no return value) |
| Scheme | `(set-show-unit-cell 0 1)` | ran (no return value) |

### set_show_unit_cells_all

Python: `set_show_unit_cells_all(istate)`  
Scheme: `(set-show-unit-cells-all istate)`

set the state of show unit cell for all molecules

1 for displayed
0 for undisplayed

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_unit_cells_all(1)` | ran (no return value) |
| Scheme | `(set-show-unit-cells-all 1)` | ran (no return value) |

### set_unit_cell_colour

Python: `set_unit_cell_colour(red, green, blue)`  
Scheme: `(set-unit-cell-colour red green blue)`

Arguments: red (a number), green (a number), blue (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_unit_cell_colour(0.5, 0.5, 0.5)` | ran (no return value) |
| Scheme | `(set-unit-cell-colour 0.5 0.5 0.5)` | ran (no return value) |

