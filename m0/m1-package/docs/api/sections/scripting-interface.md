# Scripting Interface

[Scripting reference](../README.md) > Scripting Interface (9 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### post_python_scripting_window

Python: `post_python_scripting_window()`  
Scheme: `(post-python-scripting-window)`

pop-up a scripting window for pythoning

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `post_python_scripting_window()` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(post-python-scripting-window)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens the Python scripting window (Calculate > Scripting > Python...).

### post_scheme_scripting_window

Python: `post_scheme_scripting_window()`  
Scheme: `(post-scheme-scripting-window)`

pop-up a scripting window for scheming

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `post_scheme_scripting_window()` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(post-scheme-scripting-window)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens the Scheme scripting window (Calculate > Scripting > Scheme...).

### post_scripting_window

Python: `post_scripting_window()`  
Scheme: `(post-scripting-window)`

do nothing - compatibility function

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `post_scripting_window()` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(post-scripting-window)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: compatibility name: opens the Scheme scripting window in this build (Guile is built in).

### probe_available_p

Python: `probe_available_p()`  
Scheme: `(probe-available-p)`

Can we run probe (was the executable variable set
 properly?) (predicate).

Returns 1 for yes, 2 for no

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `probe_available_p()` | ran, returned `1` |
| Scheme | `(probe-available-p)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: 1 if the probe program is found (CCP4/Phenix found by run-coot.sh), 0 if not. Only checks; does not run probe.

Python and Scheme gave the same answer.

### run_command_line_scripts

Python: `run_command_line_scripts()`  
Scheme: `(run-command-line-scripts)`

called from c-inner-main

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_command_line_scripts()` | not run: would run the start-up --script files a second time (here the test driver itself); called by Coot at start-up only |
| Scheme | `(run-command-line-scripts)` | not run: would run the start-up --script files a second time (here the test driver itself); called by Coot at start-up only |

Example written and checked by hand on the test data. Expected: runs the --script/--python/--scheme files given on the command line (done once by Coot at start-up).

### set_found_coot_gui

Python: `set_found_coot_gui()`  
Scheme: `(set-found-coot-gui)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_found_coot_gui()` | ran (no return value, nothing visible changed) |
| Scheme | `(set-found-coot-gui)` | ran (no return value, nothing visible changed) |

### set_found_coot_python_gui

Python: `set_found_coot_python_gui()`  
Scheme: `(set-found-coot-python-gui)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_found_coot_python_gui()` | ran (no return value, nothing visible changed) |
| Scheme | `(set-found-coot-python-gui)` | ran (no return value, nothing visible changed) |

### set_guile_gui_loaded_flag

Python: `set_guile_gui_loaded_flag()`  
Scheme: `(set-guile-gui-loaded-flag)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_guile_gui_loaded_flag()` | ran (no return value, nothing visible changed) |
| Scheme | `(set-guile-gui-loaded-flag)` | ran (no return value, nothing visible changed) |

### set_python_gui_loaded_flag

Python: `set_python_gui_loaded_flag()`  
Scheme: `(set-python-gui-loaded-flag)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_python_gui_loaded_flag()` | ran (no return value, nothing visible changed) |
| Scheme | `(set-python-gui-loaded-flag)` | ran (no return value, nothing visible changed) |

