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
| Python | `load_tutorial_model_and_data()` | ran (no return value); changed: new molecule 3 (model, tutorial-modern.pdb); new molecule 4 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT); new molecule 5 (map, rnasa-1.8-all_refmac1.mtz DELFWT PHDELWT); graphics_n_molecules(): 3 -> 6 ... |
| Scheme | `(load-tutorial-model-and-data)` | ran (no return value); changed: new molecule 3 (model, tutorial-modern.pdb); new molecule 4 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT); new molecule 5 (map, rnasa-1.8-all_refmac1.mtz DELFWT PHDELWT); graphics_n_molecules(): 3 -> 6 ... |

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
| Python | first `imol2 = read_pdb("tutorial-modern.pdb")`, then `clear_lsq_matches()`, then `add_lsq_match(10, 30, "A", 10, 30, "B", 1)`, then `apply_lsq_matches_simple(0, imol2)`, then `lsq_improve(0, "//A", imol2, "//B", 4, 2.0)` | ran (no return value); changed: molecule 3: coordinates of 189 residue(s) (A1, A2, A3, A4 ...) |
| Scheme | first `(define imol2 (read-pdb "tutorial-modern.pdb"))`, then `(clear-lsq-matches)`, then `(add-lsq-match 10 30 "A" 10 30 "B" 1)`, then `(apply-lsq-matches-simple 0 imol2)`, then `(lsq-improve 0 "//A" imol2 "//B" 4 2.0)` | ran (no return value); changed: molecule 3: coordinates of 189 residue(s) (A1, A2, A3, A4 ...) |

Example written and checked by hand on the test data. Expected: improves an existing rough superposition of the moving selection onto the reference (Kleywegt & Jones lsq_improve) and moves the molecule.

Note: Not an external program (the old 'not run' classification was wrong). Starting from unsuperposed copies nothing moves; it needs a rough superposition first.

### set_visible_toolbar_multi_refine_cancel_button

Python: `set_visible_toolbar_multi_refine_cancel_button(state)`  
Scheme: `(set-visible-toolbar-multi-refine-cancel-button state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_visible_toolbar_multi_refine_cancel_button(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-visible-toolbar-multi-refine-cancel-button 1)` | ran (no return value, nothing visible changed) |

### set_visible_toolbar_multi_refine_continue_button

Python: `set_visible_toolbar_multi_refine_continue_button(state)`  
Scheme: `(set-visible-toolbar-multi-refine-continue-button state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_visible_toolbar_multi_refine_continue_button(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-visible-toolbar-multi-refine-continue-button 1)` | ran (no return value, nothing visible changed) |

### set_visible_toolbar_multi_refine_stop_button

Python: `set_visible_toolbar_multi_refine_stop_button(state)`  
Scheme: `(set-visible-toolbar-multi-refine-stop-button state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_visible_toolbar_multi_refine_stop_button(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-visible-toolbar-multi-refine-stop-button 1)` | ran (no return value, nothing visible changed) |

### toolbar_multi_refine_button_set_sensitive

Python: `toolbar_multi_refine_button_set_sensitive(button_type, state)`  
Scheme: `(toolbar-multi-refine-button-set-sensitive button-type state)`

button_type is one of "stop", "continue", "cancel"
 state is 1 for on, 0 for off.

Arguments: button_type (text), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `toolbar_multi_refine_button_set_sensitive("hello", 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(toolbar-multi-refine-button-set-sensitive "hello" 1)` | ran (no return value, nothing visible changed) |

### toolbar_multi_refine_cancel

Python: `toolbar_multi_refine_cancel()`  
Scheme: `(toolbar-multi-refine-cancel)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `toolbar_multi_refine_cancel()` | ran (no return value, nothing visible changed) |
| Scheme | `(toolbar-multi-refine-cancel)` | ran (no return value, nothing visible changed) |

### toolbar_multi_refine_continue

Python: `toolbar_multi_refine_continue()`  
Scheme: `(toolbar-multi-refine-continue)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `toolbar_multi_refine_continue()` | ran (no return value, nothing visible changed) |
| Scheme | `(toolbar-multi-refine-continue)` | ran (no return value, nothing visible changed) |

### toolbar_multi_refine_stop

Python: `toolbar_multi_refine_stop()`  
Scheme: `(toolbar-multi-refine-stop)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `toolbar_multi_refine_stop()` | ran (no return value, nothing visible changed) |
| Scheme | `(toolbar-multi-refine-stop)` | ran (no return value, nothing visible changed) |

