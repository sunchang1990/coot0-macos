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
| Python | `run_state_file()` | not tried |
| Scheme | `(run-state-file)` | not tried |

### run_state_file_maybe

Python: `run_state_file_maybe()`  
Scheme: `(run-state-file-maybe)`

run the state file depending on the state variables

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_state_file_maybe()` | not tried |
| Scheme | `(run-state-file-maybe)` | not tried |

### save_state

Python: `save_state()`  
Scheme: `(save-state)`

save the current state to the default filename

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_state()` | not tried |
| Scheme | `(save-state)` | not tried |

### save_state_file

Python: `save_state_file(filename)`  
Scheme: `(save-state-file filename)`

save the current state to file filename

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_state_file("tutorial-modern.pdb")` | not tried |
| Scheme | `(save-state-file "tutorial-modern.pdb")` | not tried |

### save_state_file_name

Python: `save_state_file_name()`  
Scheme: `(save-state-file-name-scm)`

the save state file name

 Returns the save state file name

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `save_state_file_name_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_state_file_name()` | not tried |
| Scheme | `(save-state-file-name-scm)` | not tried |

### save_state_file_name_raw

Python: `save_state_file_name_raw()`  
Scheme: `(save-state-file-name-raw)`

only to be used in callbacks.c, don't export

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_state_file_name_raw()` | not tried |
| Scheme | `(save-state-file-name-raw)` | not tried |

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
| Python | `set_run_state_file_status(1)` | not tried |
| Scheme | `(set-run-state-file-status 1)` | not tried |

### set_save_state_file_name

Python: `set_save_state_file_name(filename)`  
Scheme: `(set-save-state-file-name filename)`

set the filename

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_save_state_file_name("tutorial-modern.pdb")` | not tried |
| Scheme | `(set-save-state-file-name "tutorial-modern.pdb")` | not tried |

