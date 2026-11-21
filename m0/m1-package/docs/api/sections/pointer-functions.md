# Pointer Functions

[Scripting reference](../README.md) > Pointer Functions (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### set_show_pointer_distances

Python: `set_show_pointer_distances(istate)`  
Scheme: `(set-show-pointer-distances istate)`

turn on (or off) the pointer distance by passing 1 (or 0).

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_pointer_distances(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-show-pointer-distances 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: show_pointer_distances_state was 0, set to 1, read back 1; Scheme: show-pointer-distances-state was 0, set to 1, read back 1.

### show_pointer_distances_state

Python: `show_pointer_distances_state()`  
Scheme: `(show-pointer-distances-state)`

show the state of display of the pointer distances

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_pointer_distances_state()` | ran, returned `0` |
| Scheme | `(show-pointer-distances-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

