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
| Python | `get_text_for_phs_cell_chooser(0, "hello")` | ran, returned `<Swig Object of type 'gchar *' at 0x10a26d740>` |
| Scheme | `(get-text-for-phs-cell-chooser 0 "hello")` | ran, returned `#<swig-pointer gchar * 814768050>` |

### graphics_store_phs_filename

Python: `graphics_store_phs_filename(phs_filename)`  
Scheme: `(graphics-store-phs-filename phs-filename)`

spacegroup_from_operators(const char *symm_operators_in_clipper_format);

Arguments: phs_filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_store_phs_filename("tutorial-modern.pdb")` | error: TypeError: in method 'graphics_store_phs_filename', argument 1 of type 'gchar const *' |
| Scheme | `(graphics-store-phs-filename "tutorial-modern.pdb")` | error: In procedure graphics-store-phs-filename: Wrong type argument in position 1: "tutorial-modern.pdb" |

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
| Python | `read_phs_and_coords_and_make_map("tutorial-modern.pdb")` | ran (no return value) |
| Scheme | `(read-phs-and-coords-and-make-map "tutorial-modern.pdb")` | ran (no return value) |

### read_phs_and_make_map_using_cell_symm

Python: `read_phs_and_make_map_using_cell_symm(phs_file_name, hm_spacegroup, a, b, c, alpha, beta, gamma)`  
Scheme: `(read-phs-and-make-map-using-cell-symm phs-file-name hm-spacegroup a b c alpha beta gamma)`

read phs file use coords to use cell and symm to make map

Arguments: phs_file_name (text), hm_spacegroup (text), a (a number), b (a number), c (a number), alpha (a number), beta (a number), gamma (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_phs_and_make_map_using_cell_symm("tutorial-modern.pdb", "hello", 1.0, 0.5, 1.0, 1.0, 1.0, 1.0)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(read-phs-and-make-map-using-cell-symm "tutorial-modern.pdb" "hello" 1.0 0.5 1.0 1.0 1.0 1.0)` | stopped Coot when tried without a window (not checked with a window) |

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
| Python | `read_phs_and_make_map_using_cell_symm_from_mol("tutorial-modern.pdb", 0)` | no answer within 60 s (slow, or waits for something) |
| Scheme | `(read-phs-and-make-map-using-cell-symm-from-mol "tutorial-modern.pdb" 0)` | no answer within 60 s (slow, or waits for something) |

### read_phs_and_make_map_using_cell_symm_from_mol_using_implicit_phs_filename

Python: `read_phs_and_make_map_using_cell_symm_from_mol_using_implicit_phs_filename(imol)`  
Scheme: `(read-phs-and-make-map-using-cell-symm-from-mol-using-implicit-phs-filename imol)`

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_phs_and_make_map_using_cell_symm_from_mol_using_implicit_phs_filename(0)` | ran, returned `2` |
| Scheme | `(read-phs-and-make-map-using-cell-symm-from-mol-using-implicit-phs-filename 0)` | ran, returned `2` |

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
| Python | `read_phs_and_make_map_using_cell_symm_from_previous_mol("tutorial-modern.pdb")` | no answer within 60 s (slow, or waits for something) |
| Scheme | `(read-phs-and-make-map-using-cell-symm-from-previous-mol "tutorial-modern.pdb")` | no answer within 60 s (slow, or waits for something) |

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
| Python | `read_phs_and_make_map_with_reso_limits(0, "tutorial-modern.pdb", 2.0, 2.0)` | ran, returned `2` |
| Scheme | `(read-phs-and-make-map-with-reso-limits 0 "tutorial-modern.pdb" 2.0 2.0)` | ran, returned `2` |

Python and Scheme gave the same answer.

