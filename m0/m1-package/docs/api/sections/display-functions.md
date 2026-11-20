# Display Functions

[Scripting reference](../README.md) > Display Functions (24 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### graphics_draw

Python: `graphics_draw()`  
Scheme: `(graphics-draw)`

draw a frame

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_draw()` | ran (no return value) |
| Scheme | `(graphics-draw)` | ran (no return value) |

### graphics_window_size_and_position_to_preferences

Python: `graphics_window_size_and_position_to_preferences()`  
Scheme: `(graphics-window-size-and-position-to-preferences)`

store the graphics window position and size to zenops-graphics-window-size-and-postion.scm in
 the preferences directory.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_window_size_and_position_to_preferences()` | ran (no return value) |
| Scheme | `(graphics-window-size-and-position-to-preferences)` | ran (no return value) |

### hardware_stereo_angle_factor_state

Python: `hardware_stereo_angle_factor_state()`  
Scheme: `(hardware-stereo-angle-factor-state)`

return the hardware stereo angle factor

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `hardware_stereo_angle_factor_state()` | ran, returned `1.0` |
| Scheme | `(hardware-stereo-angle-factor-state)` | ran, returned `1.0` |

Python and Scheme gave the same answer.

### hardware_stereo_mode

Python: `hardware_stereo_mode()`  
Scheme: `(hardware-stereo-mode)`

try to turn on stereo mode

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `hardware_stereo_mode()` | ran (no return value) |
| Scheme | `(hardware-stereo-mode)` | ran (no return value) |

### mono_mode

Python: `mono_mode()`  
Scheme: `(mono-mode)`

try to turn on mono mode

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mono_mode()` | ran (no return value) |
| Scheme | `(mono-mode)` | ran (no return value) |

### set_accept_reject_dialog_position

Python: `set_accept_reject_dialog_position(x_pos, y_pos)`  
Scheme: `(set-accept-reject-dialog-position x-pos y-pos)`

set position of the Accept/Reject dialog

Arguments: x_pos (a whole number), y_pos (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_accept_reject_dialog_position(1, 1)` | ran (no return value) |
| Scheme | `(set-accept-reject-dialog-position 1 1)` | ran (no return value) |

### set_delete_dialog_position

Python: `set_delete_dialog_position(x_pos, y_pos)`  
Scheme: `(set-delete-dialog-position x-pos y-pos)`

set position of Delete dialog

Arguments: x_pos (a whole number), y_pos (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_delete_dialog_position(1, 1)` | ran (no return value) |
| Scheme | `(set-delete-dialog-position 1 1)` | ran (no return value) |

### set_display_control_dialog_position

Python: `set_display_control_dialog_position(x_pos, y_pos)`  
Scheme: `(set-display-control-dialog-position x-pos y-pos)`

set position of Display Control dialog

Arguments: x_pos (a whole number), y_pos (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_display_control_dialog_position(1, 1)` | ran (no return value) |
| Scheme | `(set-display-control-dialog-position 1 1)` | ran (no return value) |

### set_dti_stereo_mode

Python: `set_dti_stereo_mode(state)`  
Scheme: `(set-dti-stereo-mode state)`

when it works, call it dti_side_by_side_stereo_mode()

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_dti_stereo_mode(1)` | ran (no return value) |
| Scheme | `(set-dti-stereo-mode 1)` | ran (no return value) |

### set_edit_chi_angles_dialog_position

Python: `set_edit_chi_angles_dialog_position(x_pos, y_pos)`  
Scheme: `(set-edit-chi-angles-dialog-position x-pos y-pos)`

set edit chi angles dialog position

Arguments: x_pos (a whole number), y_pos (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_edit_chi_angles_dialog_position(1, 1)` | ran (no return value) |
| Scheme | `(set-edit-chi-angles-dialog-position 1 1)` | ran (no return value) |

### set_go_to_atom_window_position

Python: `set_go_to_atom_window_position(x_pos, y_pos)`  
Scheme: `(set-go-to-atom-window-position x-pos y-pos)`

set position of Go To Atom dialog

Arguments: x_pos (a whole number), y_pos (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_go_to_atom_window_position(1, 1)` | ran (no return value) |
| Scheme | `(set-go-to-atom-window-position 1 1)` | ran (no return value) |

### set_graphics_window_position

Python: `set_graphics_window_position(x_pos, y_pos)`  
Scheme: `(set-graphics-window-position x-pos y-pos)`

set the graphics window position

Arguments: x_pos (a whole number), y_pos (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_graphics_window_position(1, 1)` | ran (no return value) |
| Scheme | `(set-graphics-window-position 1 1)` | ran (no return value) |

### set_graphics_window_size

Python: `set_graphics_window_size(x_size, y_size)`  
Scheme: `(set-graphics-window-size x-size y-size)`

set the window size

Arguments: x_size (a whole number), y_size (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_graphics_window_size(10, 10)` | ran (no return value) |
| Scheme | `(set-graphics-window-size 10 10)` | ran (no return value) |

### set_hardware_stereo_angle_factor

Python: `set_hardware_stereo_angle_factor(f)`  
Scheme: `(set-hardware-stereo-angle-factor f)`

how much should the eyes be separated in stereo mode?

 @param f the angular difference (in multiples of 4.5 degrees)

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_hardware_stereo_angle_factor(1.0)` | ran (no return value) |
| Scheme | `(set-hardware-stereo-angle-factor 1.0)` | ran (no return value) |

### set_model_display_radius

Python: `set_model_display_radius(state, radius)`  
Scheme: `(set-model-display-radius state radius)`

Arguments: state (a whole number), radius (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_model_display_radius(1, 5.0)` | ran (no return value) |
| Scheme | `(set-model-display-radius 1 5.0)` | ran (no return value) |

### set_model_fit_refine_dialog_position

Python: `set_model_fit_refine_dialog_position(x_pos, y_pos)`  
Scheme: `(set-model-fit-refine-dialog-position x-pos y-pos)`

set position of Model/Fit/Refine dialog

Arguments: x_pos (a whole number), y_pos (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_model_fit_refine_dialog_position(1, 1)` | ran (no return value) |
| Scheme | `(set-model-fit-refine-dialog-position 1 1)` | ran (no return value) |

### set_ramachandran_plot_dialog_position

Python: `set_ramachandran_plot_dialog_position(x_pos, y_pos)`  
Scheme: `(set-ramachandran-plot-dialog-position x-pos y-pos)`

set position of the Ramachadran Plot dialog

Arguments: x_pos (a whole number), y_pos (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ramachandran_plot_dialog_position(1, 1)` | ran (no return value) |
| Scheme | `(set-ramachandran-plot-dialog-position 1 1)` | ran (no return value) |

### set_rotamer_selection_dialog_position

Python: `set_rotamer_selection_dialog_position(x_pos, y_pos)`  
Scheme: `(set-rotamer-selection-dialog-position x-pos y-pos)`

set rotamer selection dialog position

Arguments: x_pos (a whole number), y_pos (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_rotamer_selection_dialog_position(1, 1)` | ran (no return value) |
| Scheme | `(set-rotamer-selection-dialog-position 1 1)` | ran (no return value) |

### set_rotate_translate_dialog_position

Python: `set_rotate_translate_dialog_position(x_pos, y_pos)`  
Scheme: `(set-rotate-translate-dialog-position x-pos y-pos)`

set position of the Rotate/Translate Residue Range dialog

Arguments: x_pos (a whole number), y_pos (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_rotate_translate_dialog_position(1, 1)` | ran (no return value) |
| Scheme | `(set-rotate-translate-dialog-position 1 1)` | ran (no return value) |

### set_stereo_style

Python: `set_stereo_style(mode)`  
Scheme: `(set-stereo-style mode)`

set the stereo mode (the relative view of the eyes)

0 is 2010-mode
1 is modern mode

Arguments: mode (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_stereo_style(1)` | ran (no return value) |
| Scheme | `(set-stereo-style 1)` | ran (no return value) |

### side_by_side_stereo_mode

Python: `side_by_side_stereo_mode(use_wall_eye_mode)`  
Scheme: `(side-by-side-stereo-mode use-wall-eye-mode)`

turn on side bye side stereo mode

Arguments: use_wall_eye_mode (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `side_by_side_stereo_mode(1)` | ran (no return value) |
| Scheme | `(side-by-side-stereo-mode 1)` | ran (no return value) |

### stereo_mode_state

Python: `stereo_mode_state()`  
Scheme: `(stereo-mode-state)`

what is the stero state?

 Returns 1 for in hardware stereo, 2 for side by side stereo, else return 0.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `stereo_mode_state()` | ran, returned `0` |
| Scheme | `(stereo-mode-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### store_graphics_window_position

Python: `store_graphics_window_position(x_pos, y_pos)`  
Scheme: `(store-graphics-window-position x-pos y-pos)`

store the graphics window position

Arguments: x_pos (a whole number), y_pos (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `store_graphics_window_position(1, 1)` | ran (no return value) |
| Scheme | `(store-graphics-window-position 1 1)` | ran (no return value) |

### zalman_stereo_mode

Python: `zalman_stereo_mode()`  
Scheme: `(zalman-stereo-mode)`

try to turn on Zalman stereo mode

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `zalman_stereo_mode()` | ran (no return value) |
| Scheme | `(zalman-stereo-mode)` | ran (no return value) |

