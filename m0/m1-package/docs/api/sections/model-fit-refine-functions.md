# Model/Fit/Refine Functions

[Scripting reference](../README.md) > Model/Fit/Refine Functions (9 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### post_model_fit_refine_dialog

Python: `post_model_fit_refine_dialog()`  
Scheme: `(post-model-fit-refine-dialog)`

display the Model/Fit/Refine dialog

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `post_model_fit_refine_dialog()` | ran (no return value, nothing visible changed) |
| Scheme | `(post-model-fit-refine-dialog)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens the dialog.

### post_other_modelling_tools_dialog

Python: `post_other_modelling_tools_dialog()`  
Scheme: `(post-other-modelling-tools-dialog)`

display the Other Modelling Tools dialog

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `post_other_modelling_tools_dialog()` | ran (no return value, nothing visible changed) |
| Scheme | `(post-other-modelling-tools-dialog)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens the dialog.

### refinement_move_atoms_with_zero_occupancy_state

Python: `refinement_move_atoms_with_zero_occupancy_state()`  
Scheme: `(refinement-move-atoms-with-zero-occupancy-state)`

return the state of "shall atoms with zero occupancy be moved
 when refining?"

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refinement_move_atoms_with_zero_occupancy_state()` | ran, returned `1` |
| Scheme | `(refinement-move-atoms-with-zero-occupancy-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### set_model_fit_refine_place_atom_at_pointer_label

Python: `set_model_fit_refine_place_atom_at_pointer_label(txt)`  
Scheme: `(set-model-fit-refine-place-atom-at-pointer-label txt)`

Allow the changing of Model/Fit/Refine button label from
 "Place Atom at Pointer"

Arguments: txt (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_model_fit_refine_place_atom_at_pointer_label("hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(set-model-fit-refine-place-atom-at-pointer-label "hello")` | ran (no return value, nothing visible changed) |

### set_model_fit_refine_rotate_translate_zone_label

Python: `set_model_fit_refine_rotate_translate_zone_label(txt)`  
Scheme: `(set-model-fit-refine-rotate-translate-zone-label txt)`

Allow the changing of Model/Fit/Refine button label from
 "Rotate/Translate Zone"

Arguments: txt (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_model_fit_refine_rotate_translate_zone_label("hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(set-model-fit-refine-rotate-translate-zone-label "hello")` | ran (no return value, nothing visible changed) |

### set_refinement_move_atoms_with_zero_occupancy

Python: `set_refinement_move_atoms_with_zero_occupancy(state)`  
Scheme: `(set-refinement-move-atoms-with-zero-occupancy state)`

shall atoms with zero occupancy be moved when refining? (default 1, yes)

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refinement_move_atoms_with_zero_occupancy(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refinement-move-atoms-with-zero-occupancy 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: refinement_move_atoms_with_zero_occupancy_state was 1, set to 0, read back 0; Scheme: refinement-move-atoms-with-zero-occupancy-state was 1, set to 0, read back 0.

### show_select_map_dialog

Python: `show_select_map_dialog()`  
Scheme: `(show-select-map-dialog)`

display the Display Manager dialog

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_select_map_dialog()` | ran (no return value, nothing visible changed) |
| Scheme | `(show-select-map-dialog)` | ran (no return value, nothing visible changed) |

### unset_model_fit_refine_dialog

Python: `unset_model_fit_refine_dialog()`  
Scheme: `(unset-model-fit-refine-dialog)`

unset model/fit/refine dialog

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `unset_model_fit_refine_dialog()` | ran (no return value, nothing visible changed) |
| Scheme | `(unset-model-fit-refine-dialog)` | ran (no return value, nothing visible changed) |

### unset_refine_params_dialog

Python: `unset_refine_params_dialog()`  
Scheme: `(unset-refine-params-dialog)`

unset refine params dialog

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `unset_refine_params_dialog()` | ran (no return value, nothing visible changed) |
| Scheme | `(unset-refine-params-dialog)` | ran (no return value, nothing visible changed) |

