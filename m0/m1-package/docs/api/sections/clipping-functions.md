# Clipping Functions

[Scripting reference](../README.md) > Clipping Functions (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### set_clipping_back

Python: `set_clipping_back(v)`  
Scheme: `(set-clipping-back v)`

set clipping plane back

Arguments: v (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_clipping_back(1.0)` | not tried |
| Scheme | `(set-clipping-back 1.0)` | not tried |

### set_clipping_front

Python: `set_clipping_front(v)`  
Scheme: `(set-clipping-front v)`

set clipping plane front

Arguments: v (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_clipping_front(1.0)` | not tried |
| Scheme | `(set-clipping-front 1.0)` | not tried |

