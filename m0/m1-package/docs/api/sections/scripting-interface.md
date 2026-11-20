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
| Python | `post_python_scripting_window()` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(post-python-scripting-window)` | stopped Coot when tried without a window (not checked with a window) |

### post_scheme_scripting_window

Python: `post_scheme_scripting_window()`  
Scheme: `(post-scheme-scripting-window)`

pop-up a scripting window for scheming

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `post_scheme_scripting_window()` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(post-scheme-scripting-window)` | stopped Coot when tried without a window (not checked with a window) |

### post_scripting_window

Python: `post_scripting_window()`  
Scheme: `(post-scripting-window)`

do nothing - compatibility function

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `post_scripting_window()` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(post-scripting-window)` | stopped Coot when tried without a window (not checked with a window) |

### probe_available_p

Python: `probe_available_p()`  
Scheme: `(probe-available-p)`

Can we run probe (was the executable variable set
 properly?) (predicate).

Returns 1 for yes, 2 for no

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `probe_available_p()` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |
| Scheme | `(probe-available-p)` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |

### run_command_line_scripts

Python: `run_command_line_scripts()`  
Scheme: `(run-command-line-scripts)`

called from c-inner-main

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_command_line_scripts()` | not run: not run automatically (run: exits, uses the network, an external program, files or a screen) |
| Scheme | `(run-command-line-scripts)` | not run: not run automatically (run: exits, uses the network, an external program, files or a screen) |

### set_found_coot_gui

Python: `set_found_coot_gui()`  
Scheme: `(set-found-coot-gui)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_found_coot_gui()` | ran (no return value) |
| Scheme | `(set-found-coot-gui)` | ran (no return value) |

### set_found_coot_python_gui

Python: `set_found_coot_python_gui()`  
Scheme: `(set-found-coot-python-gui)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_found_coot_python_gui()` | ran (no return value) |
| Scheme | `(set-found-coot-python-gui)` | ran (no return value) |

### set_guile_gui_loaded_flag

Python: `set_guile_gui_loaded_flag()`  
Scheme: `(set-guile-gui-loaded-flag)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_guile_gui_loaded_flag()` | ran (no return value) |
| Scheme | `(set-guile-gui-loaded-flag)` | ran (no return value) |

### set_python_gui_loaded_flag

Python: `set_python_gui_loaded_flag()`  
Scheme: `(set-python-gui-loaded-flag)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_python_gui_loaded_flag()` | ran (no return value) |
| Scheme | `(set-python-gui-loaded-flag)` | ran (no return value) |

