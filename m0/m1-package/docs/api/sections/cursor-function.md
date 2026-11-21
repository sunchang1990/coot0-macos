# Cursor Function

[Scripting reference](../README.md) > Cursor Function (5 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### fleur_cursor

Python: `fleur_cursor()`  
Scheme: `(fleur-cursor)`

fleur cursor

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fleur_cursor()` | ran (no return value, nothing visible changed) |
| Scheme | `(fleur-cursor)` | ran (no return value, nothing visible changed) |

### normal_cursor

Python: `normal_cursor()`  
Scheme: `(normal-cursor)`

normal cursor

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `normal_cursor()` | ran (no return value, nothing visible changed) |
| Scheme | `(normal-cursor)` | ran (no return value, nothing visible changed) |

### pick_cursor_maybe

Python: `pick_cursor_maybe()`  
Scheme: `(pick-cursor-maybe)`

pick cursor maybe

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `pick_cursor_maybe()` | ran (no return value, nothing visible changed) |
| Scheme | `(pick-cursor-maybe)` | ran (no return value, nothing visible changed) |

### rotate_cursor

Python: `rotate_cursor()`  
Scheme: `(rotate-cursor)`

rotate cursor

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `rotate_cursor()` | ran (no return value, nothing visible changed) |
| Scheme | `(rotate-cursor)` | ran (no return value, nothing visible changed) |

### set_pick_cursor_index

Python: `set_pick_cursor_index(icursor_index)`  
Scheme: `(set-pick-cursor-index icursor-index)`

let the user have a different pick cursor

sometimes (the default) GDK_CROSSHAIR is hard to see, let the user set
their own

Arguments: icursor_index (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_pick_cursor_index(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-pick-cursor-index 1)` | ran (no return value, nothing visible changed) |

