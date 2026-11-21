# single-model view

[Scripting reference](../README.md) > single-model view (7 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### handle_go_to_residue_keyboarding_mode

Python: `handle_go_to_residue_keyboarding_mode(text)`  
Scheme: `(handle-go-to-residue-keyboarding-mode text)`

Arguments: text (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_go_to_residue_keyboarding_mode("A 41")` | not run: not callable from scripting: the gchar* argument type is not wrapped in either language (GUI callback) |
| Scheme | `(handle-go-to-residue-keyboarding-mode "A 41")` | not run: not callable from scripting: the gchar* argument type is not wrapped in either language (GUI callback) |

Example written and checked by hand on the test data. Expected: callback of the keyboarding-mode entry (goes to the typed residue); not usable from scripts: its gchar* argument is not wrapped. Use set_go_to_atom_chain_residue_atom_name("A", 41, " CA ").

### run_update_self_maybe

Python: `run_update_self_maybe()`  
Scheme: `(run-update-self-maybe)`

this function is here because it is called by c_inner_main() (ie. need a c interface).

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_update_self_maybe()` | ran (no return value, nothing visible changed) |
| Scheme | `(run-update-self-maybe)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: does nothing unless Coot was started with --update-self (then it would download a new upstream build over the network: not useful for this port).

Note: Harmless when called; the --update-self path itself needs the network and would replace upstream binaries.

### show_go_to_residue_keyboarding_mode_window

Python: `show_go_to_residue_keyboarding_mode_window()`  
Scheme: `(show-go-to-residue-keyboarding-mode-window)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_go_to_residue_keyboarding_mode_window()` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(show-go-to-residue-keyboarding-mode-window)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens the small 'go to residue' entry window used by keyboard navigation.

### single_model_view_model_number

Python: `single_model_view_model_number(imol, imodel)`  
Scheme: `(single-model-view-model-number imol imodel)`

put molecule number imol to display only model number imodel

Arguments: imol (a whole number), imodel (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `single_model_view_model_number(0, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(single-model-view-model-number 0 1)` | ran (no return value, nothing visible changed) |

### single_model_view_next_model_number

Python: `single_model_view_next_model_number(imol)`  
Scheme: `(single-model-view-next-model-number imol)`

change the representation to the next model number to be displayed

return 0 on non-multimodel-molecule.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `L = [l for l in open("tutorial-modern.pdb") if l.startswith("ATOM")][:60]`, then `open("two-models.pdb", "w").write("MODEL        1\n" + "".join(L) + "ENDMDL\nMODEL        2\n" + "".join(L) + "ENDMDL\nEND\n")`, then `imol_m = read_pdb("two-models.pdb")`, then `single_model_view_next_model_number(imol_m)` | ran, returned `1` |
| Scheme | first `(use-modules (ice-9 rdelim))`, then `(call-with-output-file "two-models.pdb" (lambda (p) (let ((L (call-with-input-file "tutorial-modern.pdb" (lambda (i) (let loop ((acc '())) (let ((l (read-line i ...`, then `(define imol-m (read-pdb "two-models.pdb"))`, then `(single-model-view-next-model-number imol-m)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: shows only the next model and returns its number (1); 0 for a single-model molecule.

Python and Scheme gave the same answer.

### single_model_view_prev_model_number

Python: `single_model_view_prev_model_number(imol)`  
Scheme: `(single-model-view-prev-model-number imol)`

change the representation to the previous model number to be displayed

return 0 on non-multimodel-molecule.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `L = [l for l in open("tutorial-modern.pdb") if l.startswith("ATOM")][:60]`, then `open("two-models.pdb", "w").write("MODEL        1\n" + "".join(L) + "ENDMDL\nMODEL        2\n" + "".join(L) + "ENDMDL\nEND\n")`, then `imol_m = read_pdb("two-models.pdb")`, then `single_model_view_next_model_number(imol_m)`, then `single_model_view_prev_model_number(imol_m)` | ran, returned `2` |
| Scheme | first `(use-modules (ice-9 rdelim))`, then `(call-with-output-file "two-models.pdb" (lambda (p) (let ((L (call-with-input-file "tutorial-modern.pdb" (lambda (i) (let loop ((acc '())) (let ((l (read-line i ...`, then `(define imol-m (read-pdb "two-models.pdb"))`, then `(single-model-view-next-model-number imol-m)`, then `(single-model-view-prev-model-number imol-m)` | ran, returned `2` |

Example written and checked by hand on the test data. Expected: shows only the previous model (wrapping round: 1 -> 2) and returns its number; 0 for a single-model molecule.

Python and Scheme gave the same answer.

### single_model_view_this_model_number

Python: `single_model_view_this_model_number(imol)`  
Scheme: `(single-model-view-this-model-number imol)`

the current model number being displayed

return 0 on non-multimodel-molecule.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `L = [l for l in open("tutorial-modern.pdb") if l.startswith("ATOM")][:60]`, then `open("two-models.pdb", "w").write("MODEL        1\n" + "".join(L) + "ENDMDL\nMODEL        2\n" + "".join(L) + "ENDMDL\nEND\n")`, then `imol_m = read_pdb("two-models.pdb")`, then `single_model_view_next_model_number(imol_m)`, then `single_model_view_this_model_number(imol_m)` | ran, returned `1` |
| Scheme | first `(use-modules (ice-9 rdelim))`, then `(call-with-output-file "two-models.pdb" (lambda (p) (let ((L (call-with-input-file "tutorial-modern.pdb" (lambda (i) (let loop ((acc '())) (let ((l (read-line i ...`, then `(define imol-m (read-pdb "two-models.pdb"))`, then `(single-model-view-next-model-number imol-m)`, then `(single-model-view-this-model-number imol-m)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: the model number shown in single-model view (1 after one 'next'); 0 when all models are shown or the molecule has one model.

Python and Scheme gave the same answer.

