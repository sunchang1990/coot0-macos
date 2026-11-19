# single-model view

[Scripting reference](../README.md) > single-model view (7 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### handle_go_to_residue_keyboarding_mode

Python: `handle_go_to_residue_keyboarding_mode(text)`  
Scheme: `(handle-go-to-residue-keyboarding-mode text)`

Arguments: text (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_go_to_residue_keyboarding_mode("hello")` | error: TypeError: in method 'handle_go_to_residue_keyboarding_mode', argument 1 of type 'gchar const *' |
| Scheme | `(handle-go-to-residue-keyboarding-mode "hello")` | error: In procedure handle-go-to-residue-keyboarding-mode: Wrong type argument in position 1: "hello" |

### run_update_self_maybe

Python: `run_update_self_maybe()`  
Scheme: `(run-update-self-maybe)`

this function is here because it is called by c_inner_main() (ie. need a c interface).

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_update_self_maybe()` | not tried |
| Scheme | `(run-update-self-maybe)` | not tried |

### show_go_to_residue_keyboarding_mode_window

Python: `show_go_to_residue_keyboarding_mode_window()`  
Scheme: `(show-go-to-residue-keyboarding-mode-window)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_go_to_residue_keyboarding_mode_window()` | not tried |
| Scheme | `(show-go-to-residue-keyboarding-mode-window)` | not tried |

### single_model_view_model_number

Python: `single_model_view_model_number(imol, imodel)`  
Scheme: `(single-model-view-model-number imol imodel)`

put molecule number imol to display only model number imodel

Arguments: imol (a whole number), imodel (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `single_model_view_model_number(0, 1)` | not tried |
| Scheme | `(single-model-view-model-number 0 1)` | not tried |

### single_model_view_next_model_number

Python: `single_model_view_next_model_number(imol)`  
Scheme: `(single-model-view-next-model-number imol)`

change the representation to the next model number to be displayed

return 0 on non-multimodel-molecule.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `single_model_view_next_model_number(0)` | not tried |
| Scheme | `(single-model-view-next-model-number 0)` | not tried |

### single_model_view_prev_model_number

Python: `single_model_view_prev_model_number(imol)`  
Scheme: `(single-model-view-prev-model-number imol)`

change the representation to the previous model number to be displayed

return 0 on non-multimodel-molecule.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `single_model_view_prev_model_number(0)` | not tried |
| Scheme | `(single-model-view-prev-model-number 0)` | not tried |

### single_model_view_this_model_number

Python: `single_model_view_this_model_number(imol)`  
Scheme: `(single-model-view-this-model-number imol)`

the current model number being displayed

return 0 on non-multimodel-molecule.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `single_model_view_this_model_number(0)` | not tried |
| Scheme | `(single-model-view-this-model-number 0)` | not tried |

