# CNS Data Functions

[Scripting reference](../README.md) > CNS Data Functions (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### handle_cns_data_file

Python: `handle_cns_data_file(filename, imol)`  
Scheme: `(handle-cns-data-file filename imol)`

read CNS data (currently only a placeholder)

Arguments: filename (text), imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_cns_data_file("data.hkl", 0)` | not run: needs a CNS reflection file (none in the test data); the earlier attempt stopped Coot without a screen |
| Scheme | `(handle-cns-data-file "data.hkl" 0)` | not run: needs a CNS reflection file (none in the test data); the earlier attempt stopped Coot without a screen |

Example written and checked by hand on the test data. Expected: reads a CNS reflection file and makes a map using the cell of molecule 0.

### handle_cns_data_file_with_cell

Python: `handle_cns_data_file_with_cell(filename, imol, a, b, c, alpha, beta, gamma, spg_info)`  
Scheme: `(handle-cns-data-file-with-cell filename imol a b c alpha beta gamma spg-info)`

read CNS data (currently only a placeholder)

a, b,c are in Angstroems. alpha, beta, gamma are in degrees. spg is
the space group info, either ;-delimited symmetry operators or the
space group name

Arguments: filename (text), imol (a whole number), a (a number), b (a number), c (a number), alpha (a number), beta (a number), gamma (a number), spg_info (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_cns_data_file_with_cell("data.hkl", 0, 64.9, 78.3, 38.8, 90.0, 90.0, 90.0, "P 21 21 21")` | not run: needs a CNS reflection file (none in the test data); the earlier attempt stopped Coot without a screen |
| Scheme | `(handle-cns-data-file-with-cell "data.hkl" 0 64.9 78.3 38.8 90.0 90.0 90.0 "P 21 21 21")` | not run: needs a CNS reflection file (none in the test data); the earlier attempt stopped Coot without a screen |

Example written and checked by hand on the test data. Expected: reads a CNS reflection file with the given cell and space group and makes a map.

