# Anisotropic Atoms Interface

[Scripting reference](../README.md) > Anisotropic Atoms Interface (9 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_aniso_probability

Python: `get_aniso_probability()`  
Scheme: `(get-aniso-probability)`

get aniso probability

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_aniso_probability()` | ran, returned `50.0` |
| Scheme | `(get-aniso-probability)` | ran, returned `50.0` |

Python and Scheme gave the same answer.

### get_limit_aniso

Python: `get_limit_aniso()`  
Scheme: `(get-limit-aniso)`

get the aniso radius limit

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_limit_aniso()` | ran, returned `12.0` |
| Scheme | `(get-limit-aniso)` | ran, returned `12.0` |

Python and Scheme gave the same answer.

### get_show_aniso

Python: `get_show_aniso()`  
Scheme: `(get-show-aniso)`

return show-aniso-atoms state

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_show_aniso()` | ran, returned `0` |
| Scheme | `(get-show-aniso)` | ran, returned `0` |

Python and Scheme gave the same answer.

### get_show_limit_aniso

Python: `get_show_limit_aniso()`  
Scheme: `(get-show-limit-aniso)`

get show the aniso limit

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_show_limit_aniso()` | ran, returned `0` |
| Scheme | `(get-show-limit-aniso)` | ran, returned `0` |

Python and Scheme gave the same answer.

### get_text_for_aniso_limit_radius_entry

Python: `get_text_for_aniso_limit_radius_entry()`  
Scheme: `(get-text-for-aniso-limit-radius-entry)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_text_for_aniso_limit_radius_entry()` | ran, returned `'12.0 '` |
| Scheme | `(get-text-for-aniso-limit-radius-entry)` | ran, returned `"12.0 "` |

Python and Scheme gave the same answer.

### set_aniso_limit_size_from_widget

Python: `set_aniso_limit_size_from_widget(text)`  
Scheme: `(set-aniso-limit-size-from-widget text)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: text (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_aniso_limit_size_from_widget("hello")` | ran (no return value) |
| Scheme | `(set-aniso-limit-size-from-widget "hello")` | ran (no return value) |

### set_aniso_probability

Python: `set_aniso_probability(f)`  
Scheme: `(set-aniso-probability f)`

set aniso probability

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_aniso_probability(1.0)` | ran (no return value) |
| Scheme | `(set-aniso-probability 1.0)` | ran (no return value) |

### set_limit_aniso

Python: `set_limit_aniso(state)`  
Scheme: `(set-limit-aniso state)`

set the aniso atom limit

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_limit_aniso(1)` | ran (no return value) |
| Scheme | `(set-limit-aniso 1)` | ran (no return value) |

### set_show_aniso

Python: `set_show_aniso(state)`  
Scheme: `(set-show-aniso state)`

set show aniso atoms

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_aniso(1)` | ran (no return value) |
| Scheme | `(set-show-aniso 1)` | ran (no return value) |

