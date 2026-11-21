# Interface Preferences

[Scripting reference](../README.md) > Interface Preferences (62 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### accept_reject_dialog_docked_show_state

Python: `accept_reject_dialog_docked_show_state()`  
Scheme: `(accept-reject-dialog-docked-show-state)`

what is the accept/reject dialog docked show state?

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `accept_reject_dialog_docked_show_state()` | ran, returned `1` |
| Scheme | `(accept-reject-dialog-docked-show-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### accept_reject_dialog_docked_state

Python: `accept_reject_dialog_docked_state()`  
Scheme: `(accept-reject-dialog-docked-state)`

the accept/reject dialog docked state

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `accept_reject_dialog_docked_state()` | ran, returned `0` |
| Scheme | `(accept-reject-dialog-docked-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### add_status_bar_text

Python: `add_status_bar_text(s)`  
Scheme: `(add-status-bar-text s)`

Put text s into the status bar.

 use this to put info for the user in the statusbar (less intrusive
 than popup).

Arguments: s (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_status_bar_text("hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(add-status-bar-text "hello")` | ran (no return value, nothing visible changed) |

### apply_ncs_to_view_orientation

Python: `apply_ncs_to_view_orientation(imol, current_chain, next_ncs_chain)`  
Scheme: `(apply-ncs-to-view-orientation imol current-chain next-ncs-chain)`

Given that we are in chain current_chain, apply the NCS
 operator that maps current_chain on to next_ncs_chain, so that the
 relative view is preserved. For NCS skipping.

Arguments: imol (a whole number), current_chain (text), next_ncs_chain (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `apply_ncs_to_view_orientation(0, "A", "A")` | ran (no return value, nothing visible changed) |
| Scheme | `(apply-ncs-to-view-orientation 0 "A" "A")` | ran (no return value, nothing visible changed) |

### apply_ncs_to_view_orientation_and_screen_centre

Python: `apply_ncs_to_view_orientation_and_screen_centre(imol, current_chain, next_ncs_chain, forward_flag)`  
Scheme: `(apply-ncs-to-view-orientation-and-screen-centre imol current-chain next-ncs-chain forward-flag)`

as above, but shift the screen centre also.

Arguments: imol (a whole number), current_chain (text), next_ncs_chain (text), forward_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `apply_ncs_to_view_orientation_and_screen_centre(0, "A", "A", 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(apply-ncs-to-view-orientation-and-screen-centre 0 "A" "A" 1)` | ran (no return value, nothing visible changed) |

### clear_preferences

Python: `clear_preferences()`  
Scheme: `(clear-preferences)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_preferences()` | ran (no return value, nothing visible changed) |
| Scheme | `(clear-preferences)` | ran (no return value, nothing visible changed) |

### fill_preferences_main_toolbar_icons

Python: `fill_preferences_main_toolbar_icons(preferences, scrolled_window)`  
Scheme: `(fill-preferences-main-toolbar-icons preferences scrolled-window)`

Arguments: preferences (`GtkWidget *`), scrolled_window (`GtkWidget *`). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: fills the toolbar-icon list of the Preferences dialog (internal GUI helper).

### fill_preferences_model_toolbar_icons

Python: `fill_preferences_model_toolbar_icons(preferences, scrolled_window)`  
Scheme: `(fill-preferences-model-toolbar-icons preferences scrolled-window)`

Arguments: preferences (`GtkWidget *`), scrolled_window (`GtkWidget *`). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: fills the modelling-toolbar icon list of the Preferences dialog (internal GUI helper).

### get_auto_recontour_map

Python: `get_auto_recontour_map()`  
Scheme: `(get-auto-recontour-map)`

return the auto-recontour state

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_auto_recontour_map()` | ran, returned `1` |
| Scheme | `(get-auto-recontour-map)` | ran, returned `1` |

Python and Scheme gave the same answer.

### get_fps_flag

Python: `get_fps_flag()`  
Scheme: `(get-fps-flag)`

set the state of show frames-per-second flag

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `set_fps_flag(1)`, then `get_fps_flag()` | ran, returned `1` |
| Scheme | first `(set-fps-flag 1)`, then `(get-fps-flag)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns the show-frames-per-second flag: 0 by default, 1 after set_fps_flag(1).

Python and Scheme gave the same answer.

### get_view_matrix_element

Python: `get_view_matrix_element(row, col)`  
Scheme: `(get-view-matrix-element row col)`

print the view matrix

Arguments: row (a whole number), col (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_view_matrix_element(1, 1)` | ran, returned `1.0` |
| Scheme | `(get-view-matrix-element 1 1)` | ran, returned `1.0` |

Python and Scheme gave the same answer.

### get_view_quaternion_internal

Python: `get_view_quaternion_internal(element)`  
Scheme: `(get-view-quaternion-internal element)`

internal function to get an element of the view quaternion.
 The whole quaternion is returned by the scheme function
 view-quaternion

Arguments: element (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_view_quaternion_internal(1)` | ran, returned `0.0` |
| Scheme | `(get-view-quaternion-internal 1)` | ran, returned `0.0` |

Python and Scheme gave the same answer.

### hide_main_toolbar

Python: `hide_main_toolbar()`  
Scheme: `(hide-main-toolbar)`

hide the horizontal main toolbar in the GTK2 version

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `hide_main_toolbar()` | ran (no return value, nothing visible changed) |
| Scheme | `(hide-main-toolbar)` | ran (no return value, nothing visible changed) |

### hide_main_toolbar_icon

Python: `hide_main_toolbar_icon(pos)`  
Scheme: `(hide-main-toolbar-icon pos)`

Arguments: pos (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `hide_main_toolbar_icon(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(hide-main-toolbar-icon 1)` | ran (no return value, nothing visible changed) |

### hide_model_toolbar_icon

Python: `hide_model_toolbar_icon(pos)`  
Scheme: `(hide-model-toolbar-icon pos)`

Arguments: pos (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `hide_model_toolbar_icon(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(hide-model-toolbar-icon 1)` | ran (no return value, nothing visible changed) |

### hide_modelling_toolbar

Python: `hide_modelling_toolbar()`  
Scheme: `(hide-modelling-toolbar)`

hide the vertical modelling toolbar in the GTK2 version

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `hide_modelling_toolbar()` | ran (no return value, nothing visible changed) |
| Scheme | `(hide-modelling-toolbar)` | ran (no return value, nothing visible changed) |

### main_toolbar_style_state

Python: `main_toolbar_style_state()`  
Scheme: `(main-toolbar-style-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `main_toolbar_style_state()` | ran, returned `2` |
| Scheme | `(main-toolbar-style-state)` | ran, returned `2` |

Python and Scheme gave the same answer.

### make_preferences_internal

Python: `make_preferences_internal()`  
Scheme: `(make-preferences-internal)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_preferences_internal()` | ran (no return value, nothing visible changed) |
| Scheme | `(make-preferences-internal)` | ran (no return value, nothing visible changed) |

### make_preferences_internal_default

Python: `make_preferences_internal_default()`  
Scheme: `(make-preferences-internal-default)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_preferences_internal_default()` | ran (no return value, nothing visible changed) |
| Scheme | `(make-preferences-internal-default)` | ran (no return value, nothing visible changed) |

### model_fit_refine_dialog_stays_on_top_state

Python: `model_fit_refine_dialog_stays_on_top_state()`  
Scheme: `(model-fit-refine-dialog-stays-on-top-state)`

return the state model-fit-refine dialog stays on top

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `model_fit_refine_dialog_stays_on_top_state()` | ran, returned `1` |
| Scheme | `(model-fit-refine-dialog-stays-on-top-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### model_toolbar_style_state

Python: `model_toolbar_style_state()`  
Scheme: `(model-toolbar-style-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `model_toolbar_style_state()` | ran, returned `1` |
| Scheme | `(model-toolbar-style-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### preferences

Python: `preferences()`  
Scheme: `(preferences)`

section Preferences

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `preferences()` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(preferences)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens the Preferences dialog.

### preferences_internal_change_value_float

Python: `preferences_internal_change_value_float(preference_type, fvalue)`  
Scheme: `(preferences-internal-change-value-float preference-type fvalue)`

Arguments: preference_type (a whole number), fvalue (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `preferences_internal_change_value_float(1, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(preferences-internal-change-value-float 1 1.0)` | ran (no return value, nothing visible changed) |

### preferences_internal_change_value_float3

Python: `preferences_internal_change_value_float3(preference_type, fvalue1, fvalue2, fvalue3)`  
Scheme: `(preferences-internal-change-value-float3 preference-type fvalue1 fvalue2 fvalue3)`

Arguments: preference_type (a whole number), fvalue1 (a number), fvalue2 (a number), fvalue3 (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `preferences_internal_change_value_float3(1, 1.0, 1.0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(preferences-internal-change-value-float3 1 1.0 1.0 1.0)` | ran (no return value, nothing visible changed) |

### preferences_internal_change_value_int

Python: `preferences_internal_change_value_int(preference_type, ivalue)`  
Scheme: `(preferences-internal-change-value-int preference-type ivalue)`

Arguments: preference_type (a whole number), ivalue (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `preferences_internal_change_value_int(1, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(preferences-internal-change-value-int 1 1)` | ran (no return value, nothing visible changed) |

### preferences_internal_change_value_int2

Python: `preferences_internal_change_value_int2(preference_type, ivalue1, ivalue2)`  
Scheme: `(preferences-internal-change-value-int2 preference-type ivalue1 ivalue2)`

Arguments: preference_type (a whole number), ivalue1 (a whole number), ivalue2 (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `preferences_internal_change_value_int2(1, 1, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(preferences-internal-change-value-int2 1 1 1)` | ran (no return value, nothing visible changed) |

### preferences_internal_font_own_colour_flag

Python: `preferences_internal_font_own_colour_flag()`  
Scheme: `(preferences-internal-font-own-colour-flag)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `preferences_internal_font_own_colour_flag()` | ran, returned `-1` |
| Scheme | `(preferences-internal-font-own-colour-flag)` | ran, returned `-1` |

Example written and checked by hand on the test data. Expected: returns the font-own-colour preference; -1 when the preferences table has no such entry (as here: the Preferences dialog has not been made).

Python and Scheme gave the same answer.

### print_view_matrix

Python: `print_view_matrix()`  
Scheme: `(print-view-matrix)`

print the view matrix to the console, useful for molscript,
 perhaps

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `print_view_matrix()` | ran (no return value, nothing visible changed) |
| Scheme | `(print-view-matrix)` | ran (no return value, nothing visible changed) |

### reattach_modelling_toolbar

Python: `reattach_modelling_toolbar()`  
Scheme: `(reattach-modelling-toolbar)`

reattach the modelling toolbar to the last attached position

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `reattach_modelling_toolbar()` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(reattach-modelling-toolbar)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: puts the detached modelling toolbar back in its last place in the main window.

### reset_preferences

Python: `reset_preferences()`  
Scheme: `(reset-preferences)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `reset_preferences()` | ran (no return value, nothing visible changed) |
| Scheme | `(reset-preferences)` | ran (no return value, nothing visible changed) |

### save_preferences

Python: `save_preferences()`  
Scheme: `(save-preferences)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_preferences()` | ran (no return value, nothing visible changed) |
| Scheme | `(save-preferences)` | ran (no return value, nothing visible changed) |

### scroll_by_wheel_mouse_state

Python: `scroll_by_wheel_mouse_state()`  
Scheme: `(scroll-by-wheel-mouse-state)`

return the internal state of the scroll-wheel map contouring

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `scroll_by_wheel_mouse_state()` | ran, returned `1` |
| Scheme | `(scroll-by-wheel-mouse-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### set_accept_reject_dialog_docked

Python: `set_accept_reject_dialog_docked(state)`  
Scheme: `(set-accept-reject-dialog-docked state)`

functions to dock the accept/reject dialog to the toolbar

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_accept_reject_dialog_docked(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-accept-reject-dialog-docked 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back; NOT all read back): Python: accept_reject_dialog_docked_state was 0, set to 1, read back 0 (not taken); Scheme: accept-reject-dialog-docked-state was 0, set to 1, read back 0 (not taken).

### set_accept_reject_dialog_docked_show

Python: `set_accept_reject_dialog_docked_show(state)`  
Scheme: `(set-accept-reject-dialog-docked-show state)`

set the accept/reject dialog docked show state

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_accept_reject_dialog_docked_show(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-accept-reject-dialog-docked-show 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back; NOT all read back): Python: accept_reject_dialog_docked_show_state was 1, set to 0, read back 1 (not taken); Scheme: accept-reject-dialog-docked-show-state was 1, set to 0, read back 1 (not taken).

### set_auto_recontour_map

Python: `set_auto_recontour_map(state)`  
Scheme: `(set-auto-recontour-map state)`

turn off (0) or on (1) auto recontouring (on screen centre change) (default it on)

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_auto_recontour_map(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-auto-recontour-map 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_auto_recontour_map was 1, set to 0, read back 0; Scheme: get-auto-recontour-map was 1, set to 0, read back 0.

### set_default_initial_contour_level_for_difference_map

Python: `set_default_initial_contour_level_for_difference_map(n_sigma)`  
Scheme: `(set-default-initial-contour-level-for-difference-map n-sigma)`

set the default inital contour for FoFc-style map

in sigma

Arguments: n_sigma (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_default_initial_contour_level_for_difference_map(1.5)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-default-initial-contour-level-for-difference-map 1.5)` | ran (no return value, nothing visible changed) |

### set_default_initial_contour_level_for_map

Python: `set_default_initial_contour_level_for_map(n_sigma)`  
Scheme: `(set-default-initial-contour-level-for-map n-sigma)`

set the default inital contour for 2FoFc-style map

in sigma

Arguments: n_sigma (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_default_initial_contour_level_for_map(1.5)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-default-initial-contour-level-for-map 1.5)` | ran (no return value, nothing visible changed) |

### set_fps_flag

Python: `set_fps_flag(t)`  
Scheme: `(set-fps-flag t)`

set show frame-per-second flag

Arguments: t (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_fps_flag(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-fps-flag 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_fps_flag was 0, set to 1, read back 1; Scheme: get-fps-flag was 0, set to 1, read back 1.

### set_main_toolbar_style

Python: `set_main_toolbar_style(state)`  
Scheme: `(set-main-toolbar-style state)`

functions for the main toolbar style

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_main_toolbar_style(1)` | ran (no return value); changed: main_toolbar_style_state(): 2 -> 1 |
| Scheme | `(set-main-toolbar-style 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: main_toolbar_style_state was 2, set to 0, read back 0; Scheme: main-toolbar-style-state was 2, set to 0, read back 0.

### set_mark_cis_peptides_as_bad

Python: `set_mark_cis_peptides_as_bad(istate)`  
Scheme: `(set-mark-cis-peptides-as-bad istate)`

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_mark_cis_peptides_as_bad(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-mark-cis-peptides-as-bad 1)` | ran (no return value, nothing visible changed) |

### set_model_fit_refine_dialog_stays_on_top

Python: `set_model_fit_refine_dialog_stays_on_top(istate)`  
Scheme: `(set-model-fit-refine-dialog-stays-on-top istate)`

model-fit-refine dialog stays on top

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_model_fit_refine_dialog_stays_on_top(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-model-fit-refine-dialog-stays-on-top 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: model_fit_refine_dialog_stays_on_top_state was 1, set to 0, read back 0; Scheme: model-fit-refine-dialog-stays-on-top-state was 1, set to 0, read back 0.

### set_model_toolbar_docked_position

Python: `set_model_toolbar_docked_position(state)`  
Scheme: `(set-model-toolbar-docked-position state)`

to swap sides of the Model/Fit/Refine toolbar
 0 (default) is right, 1 is left, 2 is top, 3 is bottom

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_model_toolbar_docked_position(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-model-toolbar-docked-position 1)` | ran (no return value, nothing visible changed) |

### set_model_toolbar_style

Python: `set_model_toolbar_style(state)`  
Scheme: `(set-model-toolbar-style state)`

functions for the refinement toolbar style

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_model_toolbar_style(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-model-toolbar-style 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: model_toolbar_style_state was 1, set to 0, read back 0; Scheme: model-toolbar-style-state was 1, set to 0, read back 0.

### set_scroll_by_wheel_mouse

Python: `set_scroll_by_wheel_mouse(istate)`  
Scheme: `(set-scroll-by-wheel-mouse istate)`

Some people (like Phil Evans) don't want to scroll their
 map with the mouse-wheel.

 To turn off mouse wheel recontouring call this with istate value of 0

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_scroll_by_wheel_mouse(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-scroll-by-wheel-mouse 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: scroll_by_wheel_mouse_state was 1, set to 0, read back 0; Scheme: scroll-by-wheel-mouse-state was 1, set to 0, read back 0.

### set_show_origin_marker

Python: `set_show_origin_marker(istate)`  
Scheme: `(set-show-origin-marker istate)`

set a flag: is the origin marker to be shown? 1 for yes, 0
 for no.

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_origin_marker(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-show-origin-marker 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: show_origin_marker_state was 1, set to 0, read back 0; Scheme: show-origin-marker-state was 1, set to 0, read back 0.

### set_view_quaternion

Python: `set_view_quaternion(i, j, k, l)`  
Scheme: `(set-view-quaternion i j k l)`

Set the view quaternion

Arguments: i (a number), j (a number), k (a number), l (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_view_quaternion(1.0, 1.0, 1.0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-view-quaternion 1.0 1.0 1.0 1.0)` | ran (no return value, nothing visible changed) |

### show_hide_preferences_tabs

Python: `show_hide_preferences_tabs(toggletoolbutton, preference_type)`  
Scheme: `(show-hide-preferences-tabs toggletoolbutton preference-type)`

Arguments: toggletoolbutton (`GtkToggleToolButton *`), preference_type (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: switches the Preferences dialog tab (toggle-button callback).

### show_main_toolbar

Python: `show_main_toolbar()`  
Scheme: `(show-main-toolbar)`

show the horizontal main toolbar in the GTK2 version
 (the toolbar is shown by default)

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_main_toolbar()` | ran (no return value, nothing visible changed) |
| Scheme | `(show-main-toolbar)` | ran (no return value, nothing visible changed) |

### show_main_toolbar_icon

Python: `show_main_toolbar_icon(pos)`  
Scheme: `(show-main-toolbar-icon pos)`

Arguments: pos (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_main_toolbar_icon(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(show-main-toolbar-icon 1)` | ran (no return value, nothing visible changed) |

### show_mark_cis_peptides_as_bad_state

Python: `show_mark_cis_peptides_as_bad_state()`  
Scheme: `(show-mark-cis-peptides-as-bad-state)`

in geometry graph

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_mark_cis_peptides_as_bad_state()` | ran, returned `1` |
| Scheme | `(show-mark-cis-peptides-as-bad-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### show_model_toolbar_all_icons

Python: `show_model_toolbar_all_icons()`  
Scheme: `(show-model-toolbar-all-icons)`

show all available icons in the modelling toolbar (same as MFR dialog)

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_model_toolbar_all_icons()` | ran (no return value, nothing visible changed) |
| Scheme | `(show-model-toolbar-all-icons)` | ran (no return value, nothing visible changed) |

### show_model_toolbar_icon

Python: `show_model_toolbar_icon(pos)`  
Scheme: `(show-model-toolbar-icon pos)`

Arguments: pos (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_model_toolbar_icon(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(show-model-toolbar-icon 1)` | ran (no return value, nothing visible changed) |

### show_model_toolbar_main_icons

Python: `show_model_toolbar_main_icons()`  
Scheme: `(show-model-toolbar-main-icons)`

show only a selection of icons in the modelling toolbar

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_model_toolbar_main_icons()` | ran (no return value, nothing visible changed) |
| Scheme | `(show-model-toolbar-main-icons)` | ran (no return value, nothing visible changed) |

### show_modelling_toolbar

Python: `show_modelling_toolbar()`  
Scheme: `(show-modelling-toolbar)`

show the vertical modelling toolbar in the GTK2 version
 (the toolbar is shown by default)

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_modelling_toolbar()` | ran (no return value, nothing visible changed) |
| Scheme | `(show-modelling-toolbar)` | ran (no return value, nothing visible changed) |

### show_origin_marker_state

Python: `show_origin_marker_state()`  
Scheme: `(show-origin-marker-state)`

return the origin marker shown? state

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_origin_marker_state()` | ran, returned `1` |
| Scheme | `(show-origin-marker-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### show_preferences

Python: `show_preferences()`  
Scheme: `(show-preferences)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_preferences()` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(show-preferences)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens the Preferences dialog.

### suck_model_fit_dialog

Python: `suck_model_fit_dialog()`  
Scheme: `(suck-model-fit-dialog)`

reparent the Model/Fit/Refine dialog so that it becomes
 part of the main window, next to the GL graphics context

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `suck_model_fit_dialog()` | not run: needs the graphics window (moves the Model/Fit/Refine dialog into the main window); headless it does nothing |
| Scheme | `(suck-model-fit-dialog)` | not run: needs the graphics window (moves the Model/Fit/Refine dialog into the main window); headless it does nothing |

Example written and checked by hand on the test data. Expected: reparents the Model/Fit/Refine dialog into the main window; always returns 0.

### suck_model_fit_dialog_bl

Python: `suck_model_fit_dialog_bl()`  
Scheme: `(suck-model-fit-dialog-bl)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `suck_model_fit_dialog_bl()` | not run: needs the graphics window; headless it does nothing |
| Scheme | `(suck-model-fit-dialog-bl)` | not run: needs the graphics window; headless it does nothing |

Example written and checked by hand on the test data. Expected: as suck_model_fit_dialog, in a detachable handle box; always returns 0.

### update_main_toolbar_icons_menu

Python: `update_main_toolbar_icons_menu()`  
Scheme: `(update-main-toolbar-icons-menu)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_main_toolbar_icons_menu()` | ran (no return value, nothing visible changed) |
| Scheme | `(update-main-toolbar-icons-menu)` | ran (no return value, nothing visible changed) |

### update_model_toolbar_icons_menu

Python: `update_model_toolbar_icons_menu()`  
Scheme: `(update-model-toolbar-icons-menu)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_model_toolbar_icons_menu()` | ran (no return value, nothing visible changed) |
| Scheme | `(update-model-toolbar-icons-menu)` | ran (no return value, nothing visible changed) |

### update_preference_gui

Python: `update_preference_gui()`  
Scheme: `(update-preference-gui)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_preference_gui()` | ran (no return value, nothing visible changed) |
| Scheme | `(update-preference-gui)` | ran (no return value, nothing visible changed) |

### update_toolbar_icons_menu

Python: `update_toolbar_icons_menu(toolbar_index)`  
Scheme: `(update-toolbar-icons-menu toolbar-index)`

Arguments: toolbar_index (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_toolbar_icons_menu(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(update-toolbar-icons-menu 1)` | ran (no return value, nothing visible changed) |

