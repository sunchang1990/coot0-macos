# Crosshairs Interface

[Scripting reference](../README.md) > Crosshairs Interface (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### draw_crosshairs_state

Python: `draw_crosshairs_state()`  
Scheme: `(draw-crosshairs-state)`

so that we display the crosshairs with the radiobuttons in the
 right state, return draw_crosshairs_flag

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `draw_crosshairs_state()` | ran, returned `0` |
| Scheme | `(draw-crosshairs-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### set_draw_crosshairs

Python: `set_draw_crosshairs(i)`  
Scheme: `(set-draw-crosshairs i)`

draw the distance crosshairs, 0 for off, 1 for on.

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_draw_crosshairs(1)` | ran (no return value); changed: draw_crosshairs_state(): 0 -> 1 |
| Scheme | `(set-draw-crosshairs 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: draw_crosshairs_state was 0, set to 1, read back 1; Scheme: draw-crosshairs-state was 0, set to 1, read back 1.

