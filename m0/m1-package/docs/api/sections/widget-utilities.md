# Widget Utilities

[Scripting reference](../README.md) > Widget Utilities (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### set_main_window_title

Python: `set_main_window_title(s)`  
Scheme: `(set-main-window-title s)`

set the main window title.

function added for Lothar Esser

Arguments: s (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_main_window_title("hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(set-main-window-title "hello")` | ran (no return value, nothing visible changed) |

### set_show_modelling_toolbar

Python: `set_show_modelling_toolbar(state)`  
Scheme: `(set-show-modelling-toolbar state)`

function to show or hide the vertical modelling toolbar

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_modelling_toolbar(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-show-modelling-toolbar 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back; NOT all read back): Python: not checked: the getter returned None; Scheme: not checked: the getter returned ''.

