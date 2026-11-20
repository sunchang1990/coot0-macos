# Save Coordinates

[Scripting reference](../README.md) > Save Coordinates (4 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### save_coordinates

Python: `save_coordinates(imol, filename)`  
Scheme: `(save-coordinates imol filename)`

save coordinates of molecule number imol in filename

 Returns status 1 is good (success), 0 is fail.

Arguments: imol (a whole number), filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_coordinates(0, "tutorial-modern.pdb")` | ran, returned `0` |
| Scheme | `(save-coordinates 0 "tutorial-modern.pdb")` | ran, returned `0` |

Python and Scheme gave the same answer.

### save_molecule_number_from_option_menu

Python: `save_molecule_number_from_option_menu()`  
Scheme: `(save-molecule-number-from-option-menu)`

access to graphics_info_t::save_imol for use in callback.c

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_molecule_number_from_option_menu()` | ran, returned `-1` |
| Scheme | `(save-molecule-number-from-option-menu)` | ran, returned `-1` |

Python and Scheme gave the same answer.

### set_save_coordinates_in_original_directory

Python: `set_save_coordinates_in_original_directory(i)`  
Scheme: `(set-save-coordinates-in-original-directory i)`

set save coordinates in the starting directory

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_save_coordinates_in_original_directory(1)` | ran (no return value) |
| Scheme | `(set-save-coordinates-in-original-directory 1)` | ran (no return value) |

### set_save_molecule_number

Python: `set_save_molecule_number(imol)`  
Scheme: `(set-save-molecule-number imol)`

access from callback.c, not to be used in scripting, I suggest.
 Sets the *save* molecule number

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_save_molecule_number(0)` | ran (no return value) |
| Scheme | `(set-save-molecule-number 0)` | ran (no return value) |

