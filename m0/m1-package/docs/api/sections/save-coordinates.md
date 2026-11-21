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
| Python | `save_coordinates(0, "saved-tut.pdb")` | ran, returned `0`; changed: molecule 0 renamed to saved-tut.pdb; molecule_name(0): 'tutorial-modern.pdb' -> 'saved-tut.pdb' |
| Scheme | `(save-coordinates 0 "saved-tut.pdb")` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: writes saved-tut.pdb and the molecule takes that name; returns 0 on success.

Note: The doc says 1 = success, but the code returns the mmdb error code: 0 means success (file written).

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

Example written and checked by hand on the test data. Expected: -1 until a molecule has been chosen in the Save Coordinates dialog (internal state of that dialog).

Python and Scheme gave the same answer.

### set_save_coordinates_in_original_directory

Python: `set_save_coordinates_in_original_directory(i)`  
Scheme: `(set-save-coordinates-in-original-directory i)`

set save coordinates in the starting directory

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_save_coordinates_in_original_directory(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-save-coordinates-in-original-directory 1)` | ran (no return value, nothing visible changed) |

### set_save_molecule_number

Python: `set_save_molecule_number(imol)`  
Scheme: `(set-save-molecule-number imol)`

access from callback.c, not to be used in scripting, I suggest.
 Sets the *save* molecule number

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_save_molecule_number(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-save-molecule-number 0)` | ran (no return value, nothing visible changed) |

