# Dynamic Map

[Scripting reference](../README.md) > Dynamic Map (9 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_dynamic_map_sampling

Python: `get_dynamic_map_sampling()`  
Scheme: `(get-dynamic-map-sampling)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_dynamic_map_sampling()` | ran, returned `0` |
| Scheme | `(get-dynamic-map-sampling)` | ran, returned `0` |

Python and Scheme gave the same answer.

### get_dynamic_map_size_display

Python: `get_dynamic_map_size_display()`  
Scheme: `(get-dynamic-map-size-display)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_dynamic_map_size_display()` | ran, returned `0` |
| Scheme | `(get-dynamic-map-size-display)` | ran, returned `0` |

Python and Scheme gave the same answer.

### set_dynamic_map_sampling_off

Python: `set_dynamic_map_sampling_off()`  
Scheme: `(set-dynamic-map-sampling-off)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_dynamic_map_sampling_off()` | ran (no return value) |
| Scheme | `(set-dynamic-map-sampling-off)` | ran (no return value) |

### set_dynamic_map_sampling_on

Python: `set_dynamic_map_sampling_on()`  
Scheme: `(set-dynamic-map-sampling-on)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_dynamic_map_sampling_on()` | ran (no return value) |
| Scheme | `(set-dynamic-map-sampling-on)` | ran (no return value) |

### set_dynamic_map_size_display_off

Python: `set_dynamic_map_size_display_off()`  
Scheme: `(set-dynamic-map-size-display-off)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_dynamic_map_size_display_off()` | ran (no return value) |
| Scheme | `(set-dynamic-map-size-display-off)` | ran (no return value) |

### set_dynamic_map_size_display_on

Python: `set_dynamic_map_size_display_on()`  
Scheme: `(set-dynamic-map-size-display-on)`

scripting interface:

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_dynamic_map_size_display_on()` | ran (no return value) |
| Scheme | `(set-dynamic-map-size-display-on)` | ran (no return value) |

### set_dynamic_map_zoom_offset

Python: `set_dynamic_map_zoom_offset(i)`  
Scheme: `(set-dynamic-map-zoom-offset i)`

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_dynamic_map_zoom_offset(1)` | ran (no return value) |
| Scheme | `(set-dynamic-map-zoom-offset 1)` | ran (no return value) |

### toggle_dynamic_map_display_size

Python: `toggle_dynamic_map_display_size()`  
Scheme: `(toggle-dynamic-map-display-size)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `toggle_dynamic_map_display_size()` | ran (no return value) |
| Scheme | `(toggle-dynamic-map-display-size)` | ran (no return value) |

### toggle_dynamic_map_sampling

Python: `toggle_dynamic_map_sampling()`  
Scheme: `(toggle-dynamic-map-sampling)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `toggle_dynamic_map_sampling()` | ran (no return value) |
| Scheme | `(toggle-dynamic-map-sampling)` | ran (no return value) |

