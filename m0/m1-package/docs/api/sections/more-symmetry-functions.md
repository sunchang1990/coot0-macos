# More Symmetry Functions

[Scripting reference](../README.md) > More Symmetry Functions (5 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_molecular_symmetry

Python: `add_molecular_symmetry(imol, r_00, r_01, r_02, r_10, r_11, r_12, r_20, r_21, r_22, about_origin_x, about_origin_y, about_origin_z)`  
Scheme: `(add-molecular-symmetry imol r-00 r-01 r-02 r-10 r-11 r-12 r-20 r-21 r-22 about-origin-x about-origin-y about-origin-z)`

Arguments: imol (a whole number), r_00 (a number), r_01 (a number), r_02 (a number), r_10 (a number), r_11 (a number), r_12 (a number), r_20 (a number), r_21 (a number), r_22 (a number), about_origin_x (a number), about_origin_y (a number), about_origin_z (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_molecular_symmetry(0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)` | ran (no return value) |
| Scheme | `(add-molecular-symmetry 0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0)` | ran (no return value) |

### add_molecular_symmetry_from_mtrix_from_file

Python: `add_molecular_symmetry_from_mtrix_from_file(imol, file_name)`  
Scheme: `(add-molecular-symmetry-from-mtrix-from-file imol file-name)`

Arguments: imol (a whole number), file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_molecular_symmetry_from_mtrix_from_file(0, "tutorial-modern.pdb")` | ran, returned `0` |
| Scheme | `(add-molecular-symmetry-from-mtrix-from-file 0 "tutorial-modern.pdb")` | ran, returned `0` |

### add_molecular_symmetry_from_mtrix_from_self_file

Python: `add_molecular_symmetry_from_mtrix_from_self_file(imol)`  
Scheme: `(add-molecular-symmetry-from-mtrix-from-self-file imol)`

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_molecular_symmetry_from_mtrix_from_self_file(0)` | ran, returned `0` |
| Scheme | `(add-molecular-symmetry-from-mtrix-from-self-file 0)` | ran, returned `0` |

### clashes_with_symmetry

Python: `clashes_with_symmetry(imol, chain_id, res_no, ins_code, clash_dist)`  
Scheme: `(clashes-with-symmetry imol chain-id res-no ins-code clash-dist)`

return 1 if this residue clashes with the symmetry-related
 atoms of the same molecule.
0 means that it did not clash,
-1 means that the residue or molecule could not be found or that there
 was no cell and symmetry.

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), clash_dist (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clashes_with_symmetry(0, "A", 41, "", 1.0)` | ran, returned `0` |
| Scheme | `(clashes-with-symmetry 0 "A" 41 "" 1.0)` | ran, returned `0` |

### get_symmetry

Python: `get_symmetry(imol)`  
Scheme: `(get-symmetry imol)`

return a python object as a list (or some other python container)

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `get_symmetry_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_symmetry(0)` | ran, returned `['x,y,z', '-x+1/2,-y,z+1/2', 'x+1/2,-y+1/2,-z', '-x,y+1/2,-z+1/2']` |
| Scheme | `(get-symmetry 0)` | ran, returned `("x,y,z" "-x+1/2,-y,z+1/2" "x+1/2,-y+1/2,-z" "-x,y+1/2,-z+1/2")` |

