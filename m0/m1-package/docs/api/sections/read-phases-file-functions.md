# Read Phases File Functions

[Scripting reference](../README.md) > Read Phases File Functions (9 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_text_for_phs_cell_chooser

Python: `get_text_for_phs_cell_chooser(imol, field)`  
Scheme: `(get-text-for-phs-cell-chooser imol field)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: imol (a whole number), field (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_text_for_phs_cell_chooser(0, "hello")` | ran, returned `<Swig Object of type 'gchar *' at 0x10b833810>` |
| Scheme | `(get-text-for-phs-cell-chooser 0 "hello")` | ran, returned `#<swig-pointer gchar * 94d93d6b0>` |

### graphics_store_phs_filename

Python: `graphics_store_phs_filename(phs_filename)`  
Scheme: `(graphics-store-phs-filename phs-filename)`

spacegroup_from_operators(const char *symm_operators_in_clipper_format);

Arguments: phs_filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_store_phs_filename("tiny.phs")` | not run: not callable from scripts: the gchar* argument has no SWIG conversion (GUI-internal function) |
| Scheme | `(graphics-store-phs-filename "tiny.phs")` | not run: not callable from scripts: the gchar* argument has no SWIG conversion (GUI-internal function) |

Example written and checked by hand on the test data. Expected: internal (file chooser): remembers a .phs file name for the cell/symmetry dialog.

Note: SWIG wraps it but neither language can pass a string to it

### possible_cell_symm_for_phs_file

Python: `possible_cell_symm_for_phs_file()`  
Scheme: `(possible-cell-symm-for-phs-file)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `possible_cell_symm_for_phs_file()` | ran, returned `1` |
| Scheme | `(possible-cell-symm-for-phs-file)` | ran, returned `1` |

Python and Scheme gave the same answer.

### read_phs_and_coords_and_make_map

Python: `read_phs_and_coords_and_make_map(pdb_filename)`  
Scheme: `(read-phs-and-coords-and-make-map pdb-filename)`

read phs file use coords to get cell and symm to make map

uses pending data to make the map.

Arguments: pdb_filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_phs_and_coords_and_make_map("tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(read-phs-and-coords-and-make-map "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

### read_phs_and_make_map_using_cell_symm

Python: `read_phs_and_make_map_using_cell_symm(phs_file_name, hm_spacegroup, a, b, c, alpha, beta, gamma)`  
Scheme: `(read-phs-and-make-map-using-cell-symm phs-file-name hm-spacegroup a b c alpha beta gamma)`

read phs file use coords to use cell and symm to make map

Arguments: phs_file_name (text), hm_spacegroup (text), a (a number), b (a number), c (a number), alpha (a number), beta (a number), gamma (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `open("tiny.phs", "w").write("   1   0   0  100.0  0.9  10.0  2.0\n   0   1   0  150.0  0.8  50.0  2.0\n   0   0   1  80.0  0.7  120.0  2.0\n   1   1   1  60.0   ...`, then `read_phs_and_make_map_using_cell_symm("tiny.phs", "P 21 21 21", 64.897, 78.323, 38.792, 90.0, 90.0, 90.0)` | ran, returned `3`; changed: new molecule 3 (map, tiny.phs); graphics_n_molecules(): 3 -> 4 |
| Scheme | first `(call-with-output-file "tiny.phs" (lambda (port) (display "   1   0   0  100.0  0.9  10.0  2.0\n   0   1   0  150.0  0.8  50.0  2.0\n   0   0   1  80.0  0.7  12 ...`, then `(read-phs-and-make-map-using-cell-symm "tiny.phs" "P 21 21 21" 64.897 78.323 38.792 90.0 90.0 90.0)` | ran, returned `3`; changed: new molecule 3 (map, tiny.phs); graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the new map molecule made from the .phs file with the given space group and cell.

Note: tiny.phs is a 5-reflection hand-made file; when the file does not exist it still returns a molecule number and leaves an empty (non-map) molecule slot instead of -1; with 'hello' as space group Coot stopped

Python and Scheme gave the same answer.

### read_phs_and_make_map_using_cell_symm_from_mol

Python: `read_phs_and_make_map_using_cell_symm_from_mol(phs_filename, imol)`  
Scheme: `(read-phs-and-make-map-using-cell-symm-from-mol phs-filename imol)`

read phs file and use a previously read molecule to provide
 the cell and symmetry information

Returns the new molecule number, return -1 if problem creating the map
(e.g. not phs data, file not found etc).

Arguments: phs_filename (text), imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `open("tiny.phs", "w").write("   1   0   0  100.0  0.9  10.0  2.0\n   0   1   0  150.0  0.8  50.0  2.0\n   0   0   1  80.0  0.7  120.0  2.0\n   1   1   1  60.0   ...`, then `read_phs_and_make_map_using_cell_symm_from_mol("tiny.phs", 0)` | ran, returned `3`; changed: new molecule 3 (map, tiny.phs); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | first `(call-with-output-file "tiny.phs" (lambda (port) (display "   1   0   0  100.0  0.9  10.0  2.0\n   0   1   0  150.0  0.8  50.0  2.0\n   0   0   1  80.0  0.7  12 ...`, then `(read-phs-and-make-map-using-cell-symm-from-mol "tiny.phs" 0)` | ran, returned `3`; changed: new molecule 3 (map, tiny.phs); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: returns the new map molecule made from the .phs file with the cell and space group of molecule 0.

Note: tiny.phs is a 5-reflection hand-made file (h k l F fom phase sigF): the map is meaningless but shows the call; the old run with a PDB file as .phs hung

Python and Scheme gave the same answer.

### read_phs_and_make_map_using_cell_symm_from_mol_using_implicit_phs_filename

Python: `read_phs_and_make_map_using_cell_symm_from_mol_using_implicit_phs_filename(imol)`  
Scheme: `(read-phs-and-make-map-using-cell-symm-from-mol-using-implicit-phs-filename imol)`

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_phs_and_make_map_using_cell_symm_from_mol_using_implicit_phs_filename(0)` | ran, returned `3`; changed: graphics_n_molecules(): 3 -> 4 |
| Scheme | `(read-phs-and-make-map-using-cell-symm-from-mol-using-implicit-phs-filename 0)` | ran, returned `3`; changed: graphics_n_molecules(): 3 -> 4 |

Python and Scheme gave the same answer.

### read_phs_and_make_map_using_cell_symm_from_previous_mol

Python: `read_phs_and_make_map_using_cell_symm_from_previous_mol(phs_filename)`  
Scheme: `(read-phs-and-make-map-using-cell-symm-from-previous-mol phs-filename)`

read a phs file, the cell and symm information is from
 previously read (most recently read) coordinates file

 For use with phs data filename provided on the command line

Arguments: phs_filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `open("tiny.phs", "w").write("   1   0   0  100.0  0.9  10.0  2.0\n   0   1   0  150.0  0.8  50.0  2.0\n   0   0   1  80.0  0.7  120.0  2.0\n   1   1   1  60.0   ...`, then `read_phs_and_make_map_using_cell_symm_from_previous_mol("tiny.phs")` | ran, returned `3`; changed: new molecule 3 (map, tiny.phs); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | first `(call-with-output-file "tiny.phs" (lambda (port) (display "   1   0   0  100.0  0.9  10.0  2.0\n   0   1   0  150.0  0.8  50.0  2.0\n   0   0   1  80.0  0.7  12 ...`, then `(read-phs-and-make-map-using-cell-symm-from-previous-mol "tiny.phs")` | ran, returned `3`; changed: new molecule 3 (map, tiny.phs); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: returns the new map molecule made from the .phs file with the cell/symmetry of the most recently read model.

Note: with a non-existent file it returns a molecule number (not -1) and leaves an empty molecule slot (n_molecules 3 -> 4)

Python and Scheme gave the same answer.

### read_phs_and_make_map_with_reso_limits

Python: `read_phs_and_make_map_with_reso_limits(imol, phs_file_name, reso_lim_low, reso_lim_high)`  
Scheme: `(read-phs-and-make-map-with-reso-limits imol phs-file-name reso-lim-low reso-lim-high)`

read a phs file and use the cell and symm in molecule
 number imol and use the resolution limits reso_lim_high (in Angstroems).

@param imol is the molecule number of the reference (coordinates)
molecule from which the cell and symmetry can be obtained.

@param phs_file_name is the name of the phs data file.

@param reso_lim_high is the high resolution limit in Angstroems.

@param reso_lim_low the low resoluion limit (currently ignored).

Arguments: imol (a whole number), phs_file_name (text), reso_lim_low (a number), reso_lim_high (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_phs_and_make_map_with_reso_limits(0, "tutorial-modern.pdb", 2.0, 2.0)` | ran, returned `3`; changed: new molecule 3 (map, tutorial-modern.pdb); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(read-phs-and-make-map-with-reso-limits 0 "tutorial-modern.pdb" 2.0 2.0)` | ran, returned `3`; changed: new molecule 3 (map, tutorial-modern.pdb); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Python and Scheme gave the same answer.

