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
| Python | `handle_cns_data_file("tutorial-modern.pdb", 0)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(handle-cns-data-file "tutorial-modern.pdb" 0)` | stopped Coot when tried without a window (not checked with a window) |

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
| Python | `handle_cns_data_file_with_cell("tutorial-modern.pdb", 0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, "hello")` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(handle-cns-data-file-with-cell "tutorial-modern.pdb" 0 1.0 0.5 1.0 1.0 1.0 1.0 "hello")` | stopped Coot when tried without a window (not checked with a window) |

