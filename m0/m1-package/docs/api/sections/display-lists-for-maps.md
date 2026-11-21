# Display Lists for Maps

[Scripting reference](../README.md) > Display Lists for Maps (3 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### display_lists_for_maps_state

Python: `display_lists_for_maps_state()`  
Scheme: `(display-lists-for-maps-state)`

return the state of display_lists_for_maps.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `display_lists_for_maps_state()` | ran, returned `0` |
| Scheme | `(display-lists-for-maps-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### set_display_lists_for_maps

Python: `set_display_lists_for_maps(i)`  
Scheme: `(set-display-lists-for-maps i)`

Should display lists be used for maps? It may speed things
 up if these are turned on (or off) - depends on graphics card and
 drivers. Pass 1 for on, 0 for off.

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_display_lists_for_maps(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-display-lists-for-maps 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: display_lists_for_maps_state was 0, set to 1, read back 1; Scheme: display-lists-for-maps-state was 0, set to 1, read back 1.

### update_maps

Python: `update_maps()`  
Scheme: `(update-maps)`

update the maps to the current position - rarely needed

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_maps()` | ran (no return value, nothing visible changed) |
| Scheme | `(update-maps)` | ran (no return value, nothing visible changed) |

