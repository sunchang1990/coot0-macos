# History Functions

[Scripting reference](../README.md) > History Functions (4 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### print_all_history_in_python

Python: `print_all_history_in_python()`  
Scheme: `(print-all-history-in-python)`

print the history in python format

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `print_all_history_in_python()` | ran (no return value) |
| Scheme | `(print-all-history-in-python)` | ran (no return value) |

### print_all_history_in_scheme

Python: `print_all_history_in_scheme()`  
Scheme: `(print-all-history-in-scheme)`

print the history in scheme format

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `print_all_history_in_scheme()` | ran (no return value) |
| Scheme | `(print-all-history-in-scheme)` | ran (no return value) |

### set_console_display_commands_hilights

Python: `set_console_display_commands_hilights(bold_flag, colour_flag, colour_index)`  
Scheme: `(set-console-display-commands-hilights bold-flag colour-flag colour-index)`

set a flag to show the text command equivalent of gui
 commands in the console as they happen in bold and colours.

 colour_flag: pass 1 for on, 0 for off.

 colour_index 0 to 7 inclusive for various different colourings.

Arguments: bold_flag (a whole number), colour_flag (a whole number), colour_index (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_console_display_commands_hilights(1, 1, 1)` | ran (no return value) |
| Scheme | `(set-console-display-commands-hilights 1 1 1)` | ran (no return value) |

### set_console_display_commands_state

Python: `set_console_display_commands_state(istate)`  
Scheme: `(set-console-display-commands-state istate)`

set a flag to show the text command equivalent of gui
 commands in the console as they happen.

 1 for on, 0 for off.

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_console_display_commands_state(1)` | ran (no return value) |
| Scheme | `(set-console-display-commands-state 1)` | ran (no return value) |

