# LSQ-improve

[Scripting reference](../README.md) > LSQ-improve (9 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### load_tutorial_model_and_data

Python: `load_tutorial_model_and_data()`  
Scheme: `(load-tutorial-model-and-data)`

load tutorial model and data

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `load_tutorial_model_and_data()` | not tried |
| Scheme | `(load-tutorial-model-and-data)` | not tried |

### lsq_improve

Python: `lsq_improve(imol_ref, ref_selection, imol_moving, moving_selection, n_res, dist_crit)`  
Scheme: `(lsq-improve imol-ref ref-selection imol-moving moving-selection n-res dist-crit)`

an slightly-modified implementation of the "lsq_improve"
 algorithm of Kleywegt and Jones (1997).

 Note that if a residue selection is specified in the residue
 selection(s), then the first residue of the given range must exist
 in the molecule (if not, then mmdb will not select any atoms from
 that molecule).

 Kleywegt and Jones set n_res to 4 and dist_crit to 6.0.

Arguments: imol_ref (a whole number), ref_selection (text), imol_moving (a whole number), moving_selection (text), n_res (a whole number), dist_crit (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `lsq_improve(0, "//A/41-45", 0, "//A/41-45", 1, 1.0)` | not tried |
| Scheme | `(lsq-improve 0 "//A/41-45" 0 "//A/41-45" 1 1.0)` | not tried |

### set_visible_toolbar_multi_refine_cancel_button

Python: `set_visible_toolbar_multi_refine_cancel_button(state)`  
Scheme: `(set-visible-toolbar-multi-refine-cancel-button state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_visible_toolbar_multi_refine_cancel_button(1)` | not tried |
| Scheme | `(set-visible-toolbar-multi-refine-cancel-button 1)` | not tried |

### set_visible_toolbar_multi_refine_continue_button

Python: `set_visible_toolbar_multi_refine_continue_button(state)`  
Scheme: `(set-visible-toolbar-multi-refine-continue-button state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_visible_toolbar_multi_refine_continue_button(1)` | not tried |
| Scheme | `(set-visible-toolbar-multi-refine-continue-button 1)` | not tried |

### set_visible_toolbar_multi_refine_stop_button

Python: `set_visible_toolbar_multi_refine_stop_button(state)`  
Scheme: `(set-visible-toolbar-multi-refine-stop-button state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_visible_toolbar_multi_refine_stop_button(1)` | not tried |
| Scheme | `(set-visible-toolbar-multi-refine-stop-button 1)` | not tried |

### toolbar_multi_refine_button_set_sensitive

Python: `toolbar_multi_refine_button_set_sensitive(button_type, state)`  
Scheme: `(toolbar-multi-refine-button-set-sensitive button-type state)`

button_type is one of "stop", "continue", "cancel"
 state is 1 for on, 0 for off.

Arguments: button_type (text), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `toolbar_multi_refine_button_set_sensitive("hello", 1)` | not tried |
| Scheme | `(toolbar-multi-refine-button-set-sensitive "hello" 1)` | not tried |

### toolbar_multi_refine_cancel

Python: `toolbar_multi_refine_cancel()`  
Scheme: `(toolbar-multi-refine-cancel)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `toolbar_multi_refine_cancel()` | not tried |
| Scheme | `(toolbar-multi-refine-cancel)` | not tried |

### toolbar_multi_refine_continue

Python: `toolbar_multi_refine_continue()`  
Scheme: `(toolbar-multi-refine-continue)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `toolbar_multi_refine_continue()` | not tried |
| Scheme | `(toolbar-multi-refine-continue)` | not tried |

### toolbar_multi_refine_stop

Python: `toolbar_multi_refine_stop()`  
Scheme: `(toolbar-multi-refine-stop)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `toolbar_multi_refine_stop()` | not tried |
| Scheme | `(toolbar-multi-refine-stop)` | not tried |

