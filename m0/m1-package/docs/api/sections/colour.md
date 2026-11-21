# Colour

[Scripting reference](../README.md) > Colour (13 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### clear_user_defined_atom_colours

Python: `clear_user_defined_atom_colours(imol)`  
Scheme: `(clear-user-defined-atom-colours imol)`

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_user_defined_atom_colours(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(clear-user-defined-atom-colours 0)` | ran (no return value, nothing visible changed) |

### get_colour_map_rotation_on_read_pdb_c_only_flag

Python: `get_colour_map_rotation_on_read_pdb_c_only_flag()`  
Scheme: `(get-colour-map-rotation-on-read-pdb-c-only-flag)`

get the value of graphics_info_t::rotate_colour_map_on_read_pdb_c_only_flag

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_colour_map_rotation_on_read_pdb_c_only_flag()` | ran, returned `1` |
| Scheme | `(get-colour-map-rotation-on-read-pdb-c-only-flag)` | ran, returned `1` |

Python and Scheme gave the same answer.

### set_colour_by_chain

Python: `set_colour_by_chain(imol)`  
Scheme: `(set-colour-by-chain imol)`

colour molecule number imol by chain type

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_colour_by_chain(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-colour-by-chain 0)` | ran (no return value, nothing visible changed) |

### set_colour_by_chain_goodsell_mode

Python: `set_colour_by_chain_goodsell_mode(imol)`  
Scheme: `(set-colour-by-chain-goodsell-mode imol)`

colour molecule number imol by chain type, goodsell-like colour scheme

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_colour_by_chain_goodsell_mode(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-colour-by-chain-goodsell-mode 0)` | ran (no return value, nothing visible changed) |

### set_colour_by_molecule

Python: `set_colour_by_molecule(imol)`  
Scheme: `(set-colour-by-molecule imol)`

colour molecule number imol by molecule

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_colour_by_molecule(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-colour-by-molecule 0)` | ran (no return value, nothing visible changed) |

### set_colour_map_rotation_on_read_pdb

Python: `set_colour_map_rotation_on_read_pdb(f)`  
Scheme: `(set-colour-map-rotation-on-read-pdb f)`

set the hue change step on reading a new molecule

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_colour_map_rotation_on_read_pdb(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-colour-map-rotation-on-read-pdb 1.0)` | ran (no return value, nothing visible changed) |

### set_colour_map_rotation_on_read_pdb_c_only_flag

Python: `set_colour_map_rotation_on_read_pdb_c_only_flag(i)`  
Scheme: `(set-colour-map-rotation-on-read-pdb-c-only-flag i)`

shall the colour map rotation apply only to C atoms?

 @param i 0 for no, 1 for yes

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_colour_map_rotation_on_read_pdb_c_only_flag(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-colour-map-rotation-on-read-pdb-c-only-flag 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_colour_map_rotation_on_read_pdb_c_only_flag was 1, set to 0, read back 0; Scheme: get-colour-map-rotation-on-read-pdb-c-only-flag was 1, set to 0, read back 0.

### set_colour_map_rotation_on_read_pdb_flag

Python: `set_colour_map_rotation_on_read_pdb_flag(i)`  
Scheme: `(set-colour-map-rotation-on-read-pdb-flag i)`

shall the hue change step be used?

 @param i 0 for no, 1 for yes

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_colour_map_rotation_on_read_pdb_flag(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-colour-map-rotation-on-read-pdb-flag 1)` | ran (no return value, nothing visible changed) |

### set_symmetry_colour

Python: `set_symmetry_colour(r, g, b)`  
Scheme: `(set-symmetry-colour r g b)`

set the symmetry colour base

Arguments: r (a number), g (a number), b (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_symmetry_colour(0.5, 0.5, 0.5)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-symmetry-colour 0.5 0.5 0.5)` | ran (no return value, nothing visible changed) |

### set_symmetry_colour_merge

Python: `set_symmetry_colour_merge(v)`  
Scheme: `(set-symmetry-colour-merge v)`

set the colour merge ratio (a fraction 0.0 to 1.0)

Arguments: v (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_symmetry_colour_merge(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-symmetry-colour-merge 1.0)` | ran (no return value, nothing visible changed) |

### set_user_defined_atom_colour_py

Python: `set_user_defined_atom_colour_py(imol, atom_specs_colour_index_tuple_list_py)`  
Scheme: `(set-user-defined-atom-colour-scm imol atom-specs-colour-index-tuple-list-scm)`

for the given molecule imol, pass a list of tuples of items with the first parameter begin the stom spec
 and the second begin the colour index (an int).

Arguments: imol (a whole number), atom_specs_colour_index_tuple_list_py (a list or value). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_user_defined_atom_colour_py(0, ["A", 41, "", " CA ", ""])` | ran (no return value, nothing visible changed) |
| Scheme | `(set-user-defined-atom-colour-scm 0 (list "A" 41 "" " CA " ""))` | ran (no return value, nothing visible changed) |

### set_user_defined_atom_colour_by_residue_py

Python: `set_user_defined_atom_colour_by_residue_py(imol, residue_specs_colour_index_tuple_list_py)`  
Scheme: `(set-user-defined-atom-colour-by-residue-scm imol residue-specs-colour-index-tuple-list-scm)`

for the given molecule imol, pass a list of tuples of items with the first parameter begin the residue spec
 and the second begin the colour index (an int).

Arguments: imol (a whole number), residue_specs_colour_index_tuple_list_py (a list or value). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_user_defined_atom_colour_by_residue_py(0, ["A", 41, ""])` | ran (no return value, nothing visible changed) |
| Scheme | `(set-user-defined-atom-colour-by-residue-scm 0 (list "A" 41 ""))` | ran (no return value, nothing visible changed) |

### set_user_defined_colours_py

Python: `set_user_defined_colours_py(colour_list_py)`

by default user-defined colour indices will use a colour wheel
 but here we can set them ourselves by passing something like: [1, [0.2, 0.3, 0.4]], [2, [0.6, 0.4, 0.2]]]
 i.e. a colour for each colour index. If the colour index goes beyond the limit, or there is a
 missing value, then colour will be [0.5, 0.5, 0.5]

Arguments: colour_list_py (a list or value). Returns: nothing.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_user_defined_colours_py([(30, [1.0, 0.0, 0.0]), (31, [0.0, 0.8, 0.2])])` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: defines user colour indices (index, [r, g, b]) to be used by set_user_defined_atom_colour_by_selection.

Note: Items must be TUPLES (index, [r, g, b]); lists are silently ignored by the C++ (PyTuple_Check).

