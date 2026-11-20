# FFFearing

[Scripting reference](../README.md) > FFFearing (3 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### fffear_angular_resolution

Python: `fffear_angular_resolution()`  
Scheme: `(fffear-angular-resolution)`

return the fffear angular resolution in degrees

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fffear_angular_resolution()` | ran, returned `15.0` |
| Scheme | `(fffear-angular-resolution)` | ran, returned `15.0` |

Python and Scheme gave the same answer.

### fffear_search

Python: `fffear_search(imol_model, imol_map)`  
Scheme: `(fffear-search imol-model imol-map)`

fffear search model in molecule number imol_model in map
 number imol_map

Arguments: imol_model (a whole number), imol_map (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fffear_search(0, 1)` | no answer within 60 s (slow, or waits for something) |
| Scheme | `(fffear-search 0 1)` | no answer within 60 s (slow, or waits for something) |

### set_fffear_angular_resolution

Python: `set_fffear_angular_resolution(f)`  
Scheme: `(set-fffear-angular-resolution f)`

set and return the fffear angular resolution in degrees

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_fffear_angular_resolution(1.0)` | ran (no return value) |
| Scheme | `(set-fffear-angular-resolution 1.0)` | ran (no return value) |

