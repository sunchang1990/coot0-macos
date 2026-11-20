# Residue Info

[Scripting reference](../README.md) > Residue Info (13 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### clear_last_simple_distance

Python: `clear_last_simple_distance()`  
Scheme: `(clear-last-simple-distance)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_last_simple_distance()` | ran (no return value) |
| Scheme | `(clear-last-simple-distance)` | ran (no return value) |

### clear_residue_info_edit_list

Python: `clear_residue_info_edit_list()`  
Scheme: `(clear-residue-info-edit-list)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_residue_info_edit_list()` | ran (no return value) |
| Scheme | `(clear-residue-info-edit-list)` | ran (no return value) |

### clear_simple_distances

Python: `clear_simple_distances()`  
Scheme: `(clear-simple-distances)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_simple_distances()` | ran (no return value) |
| Scheme | `(clear-simple-distances)` | ran (no return value) |

### do_angle_define

Python: `do_angle_define()`  
Scheme: `(do-angle-define)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_angle_define()` | ran (no return value) |
| Scheme | `(do-angle-define)` | ran (no return value) |

### do_distance_define

Python: `do_distance_define()`  
Scheme: `(do-distance-define)`

functions that uses mmdb_manager functions/data types moved to graphics_info_t

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_distance_define()` | ran (no return value) |
| Scheme | `(do-distance-define)` | ran (no return value) |

### do_residue_info_dialog

Python: `do_residue_info_dialog()`  
Scheme: `(do-residue-info-dialog)`

Similar to above, we need only one click though.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_residue_info_dialog()` | ran (no return value) |
| Scheme | `(do-residue-info-dialog)` | ran (no return value) |

### do_torsion_define

Python: `do_torsion_define()`  
Scheme: `(do-torsion-define)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_torsion_define()` | ran (no return value) |
| Scheme | `(do-torsion-define)` | ran (no return value) |

### output_residue_info_as_text

Python: `output_residue_info_as_text(atom_index, imol)`  
Scheme: `(output-residue-info-as-text atom-index imol)`

Arguments: atom_index (a whole number), imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `output_residue_info_as_text(0, 0)` | ran (no return value) |
| Scheme | `(output-residue-info-as-text 0 0)` | ran (no return value) |

### output_residue_info_dialog

Python: `output_residue_info_dialog(imol, atom_index)`  
Scheme: `(output-residue-info-dialog imol atom-index)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: imol (a whole number), atom_index (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `output_residue_info_dialog(0, 0)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(output-residue-info-dialog 0 0)` | stopped Coot when tried without a window (not checked with a window) |

### residue_info_apply_all_checkbutton_toggled

Python: `residue_info_apply_all_checkbutton_toggled()`  
Scheme: `(residue-info-apply-all-checkbutton-toggled)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_info_apply_all_checkbutton_toggled()` | ran (no return value) |
| Scheme | `(residue-info-apply-all-checkbutton-toggled)` | ran (no return value) |

### residue_info_dialog

Python: `residue_info_dialog(imol, chain_id, resno, ins_code)`  
Scheme: `(residue-info-dialog imol chain-id resno ins-code)`

show residue info dialog for given residue

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_info_dialog(0, "A", 41, "")` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(residue-info-dialog 0 "A" 41 "")` | stopped Coot when tried without a window (not checked with a window) |

### residue_info_dialog_is_displayed

Python: `residue_info_dialog_is_displayed()`  
Scheme: `(residue-info-dialog-is-displayed)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_info_dialog_is_displayed()` | ran, returned `0` |
| Scheme | `(residue-info-dialog-is-displayed)` | ran, returned `0` |

Python and Scheme gave the same answer.

### unset_residue_info_widget

Python: `unset_residue_info_widget()`  
Scheme: `(unset-residue-info-widget)`

a graphics_info_t function wrapper:

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `unset_residue_info_widget()` | ran (no return value) |
| Scheme | `(unset-residue-info-widget)` | ran (no return value) |

