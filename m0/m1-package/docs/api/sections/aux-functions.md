# Aux functions

[Scripting reference](../README.md) > Aux functions (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### laplacian

Python: `laplacian(imol)`  
Scheme: `(laplacian imol)`

Create the "Laplacian" (-ve second derivative) of the given map.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `laplacian(0)` | ran, returned `-1` |
| Scheme | `(laplacian 0)` | ran, returned `-1` |

Python and Scheme gave the same answer.

