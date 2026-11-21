# Variance Map

[Scripting reference](../README.md) > Variance Map (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### make_variance_map

Python: `make_variance_map(map_molecule_number_list)`  
Scheme: `(make-variance-map map-molecule-number-list)`

Arguments: map_molecule_number_list (a list or value). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `imol2 = sharpen_blur_map(1, 30.0)`, then `make_variance_map([1, imol2])` | ran, returned `4`; changed: new molecule 4 (map, variance-map); graphics_n_molecules(): 4 -> 5 |
| Scheme | `(make-variance-map (list 1 (sharpen-blur-map 1 30.0)))` | ran, returned `4`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT Blur 30.00); new molecule 4 (map, variance-map); graphics_n_molecules(): 3 -> 5 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number of the variance map of the given maps.

Note: make_variance_map([1, 1]) (two identical maps) makes a map whose sigma and mean are NaN.

Python and Scheme gave the same answer.

