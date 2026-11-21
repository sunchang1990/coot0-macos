# State Functions

[Scripting reference](../README.md) > State Functions (8 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### run_state_file

Python: `run_state_file()`  
Scheme: `(run-state-file)`

just do it

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_state_file()` | ran (no return value); changed: new molecule 3 (model, tutorial-modern-coot-0.pdb); new molecule 4 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT); rotation centre moved 42.3 A to (41.6, 8.7, 12.9); graphics_n_molecules(): 3 -> 5 ... |
| Scheme | `(run-state-file)` | ran (no return value); changed: new molecule 3 (model, tutorial-modern-coot-0.pdb); new molecule 4 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT); graphics_n_molecules(): 3 -> 5; scroll_wheel_map(): -1 -> 4 |

Example written and checked by hand on the test data. Expected: runs the state file 0-coot.state.py/.scm of the current directory (saved by save_state()); does nothing when there is none.

### run_state_file_maybe

Python: `run_state_file_maybe()`  
Scheme: `(run-state-file-maybe)`

run the state file depending on the state variables

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_state_file_maybe()` | ran (no return value, nothing visible changed) |
| Scheme | `(run-state-file-maybe)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: runs the state file if one exists and the run-state-file status allows it (asks with a dialog when status is 1).

### save_state

Python: `save_state()`  
Scheme: `(save-state)`

save the current state to the default filename

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_state()` | ran (no return value, nothing visible changed) |
| Scheme | `(save-state)` | ran (no return value, nothing visible changed) |

### save_state_file

Python: `save_state_file(filename)`  
Scheme: `(save-state-file filename)`

save the current state to file filename

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_state_file("tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(save-state-file "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

### save_state_file_name

Python: `save_state_file_name()`  
Scheme: `(save-state-file-name-scm)`

the save state file name

 Returns the save state file name

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `save_state_file_name_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_state_file_name()` | ran, returned `'0-coot.state.scm'` |
| Scheme | `(save-state-file-name-scm)` | ran, returned `"0-coot.state.scm"` |

Python and Scheme gave the same answer.

### save_state_file_name_raw

Python: `save_state_file_name_raw()`  
Scheme: `(save-state-file-name-raw)`

only to be used in callbacks.c, don't export

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_state_file_name_raw()` | ran, returned `'0-coot.state.scm'` |
| Scheme | `(save-state-file-name-raw)` | ran, returned `"0-coot.state.scm"` |

Python and Scheme gave the same answer.

### set_run_state_file_status

Python: `set_run_state_file_status(istat)`  
Scheme: `(set-run-state-file-status istat)`

set run state file status

0: never run it
1: ask to run it
2: run it, no questions

Arguments: istat (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_run_state_file_status(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-run-state-file-status 0)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: 0 = never run 0-coot.state.py/.scm at start, 1 = ask, 2 = run without asking; nothing visible changes at once.

### set_save_state_file_name

Python: `set_save_state_file_name(filename)`  
Scheme: `(set-save-state-file-name filename)`

set the filename

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_save_state_file_name("tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(set-save-state-file-name "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

