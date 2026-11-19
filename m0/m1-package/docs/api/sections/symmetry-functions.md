# Symmetry Functions

[Scripting reference](../README.md) > Symmetry Functions (27 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_symmetry_on_to_preferences_and_apply

Python: `add_symmetry_on_to_preferences_and_apply()`  
Scheme: `(add-symmetry-on-to-preferences-and-apply)`

a gui function really

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_symmetry_on_to_preferences_and_apply()` | ran (no return value) |
| Scheme | `(add-symmetry-on-to-preferences-and-apply)` | ran (no return value) |

### first_molecule_with_symmetry_displayed

Python: `first_molecule_with_symmetry_displayed()`  
Scheme: `(first-molecule-with-symmetry-displayed)`

return the molecule number.

Returns -1 if there is no molecule with symmetry displayed.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `first_molecule_with_symmetry_displayed()` | ran, returned `0` |
| Scheme | `(first-molecule-with-symmetry-displayed)` | ran, returned `0` |

### get_show_symmetry

Python: `get_show_symmetry()`  
Scheme: `(get-show-symmetry)`

is symmetry master display control on?

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_show_symmetry()` | ran, returned `0` |
| Scheme | `(get-show-symmetry)` | ran, returned `0` |

### get_symmetry_as_calphas_state

Python: `get_symmetry_as_calphas_state(imol)`  
Scheme: `(get-symmetry-as-calphas-state imol)`

what is state of display CAs for molecule number mol_no?

 return state=0 for off, state=1 for on

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_symmetry_as_calphas_state(0)` | ran, returned `0` |
| Scheme | `(get-symmetry-as-calphas-state 0)` | ran, returned `0` |

### get_symmetry_bonds_colour

Python: `get_symmetry_bonds_colour(imol)`  
Scheme: `(get-symmetry-bonds-colour imol)`

Arguments: imol (a whole number). Returns: `double*`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_symmetry_bonds_colour(0)` | ran, returned `<Swig Object of type 'double *' at 0x1086e98c0>` |
| Scheme | `(get-symmetry-bonds-colour 0)` | ran, returned `#<swig-pointer double * 923123f00>` |

### get_text_for_symmetry_size_widget

Python: `get_text_for_symmetry_size_widget()`  
Scheme: `(get-text-for-symmetry-size-widget)`

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_text_for_symmetry_size_widget()` | ran, returned `'13.0 '` |
| Scheme | `(get-text-for-symmetry-size-widget)` | ran, returned `"13.0 "` |

### has_unit_cell_state

Python: `has_unit_cell_state(imol)`  
Scheme: `(has-unit-cell-state imol)`

molecule number imol has a unit cell?

 Returns 1 on "yes, it has a cell", 0 for "no"

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `has_unit_cell_state(0)` | ran, returned `1` |
| Scheme | `(has-unit-cell-state 0)` | ran, returned `1` |

### move_reference_chain_to_symm_chain_position

Python: `move_reference_chain_to_symm_chain_position()`  
Scheme: `(move-reference-chain-to-symm-chain-position)`

This function works by active symm atom.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `move_reference_chain_to_symm_chain_position()` | not tried |
| Scheme | `(move-reference-chain-to-symm-chain-position)` | not tried |

### n_symops

Python: `n_symops(imol)`  
Scheme: `(n-symops imol)`

return the number of symmetry operators for the given molecule

return -1 on no-symmetry for molecule or inappropriate imol number

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `n_symops(0)` | not tried |
| Scheme | `(n-symops 0)` | not tried |

### origin_pre_shift

Python: `origin_pre_shift(imol)`  
Scheme: `(origin-pre-shift imol)`

return the pre-shift (the shift that translates the centre
 of the molecule as close as possible to the origin) as a list of
 ints or Python false on failure

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `origin_pre_shift_py`.
Also available in Scheme as `origin-pre-shift-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `origin_pre_shift(0)` | not tried |
| Scheme | `(origin-pre-shift 0)` | not tried |

### save_symmetry_coords

Python: `save_symmetry_coords(imol, filename, symop_no, shift_a, shift_b, shift_c, pre_shift_to_origin_na, pre_shift_to_origin_nb, pre_shift_to_origin_nc)`  
Scheme: `(save-symmetry-coords imol filename symop-no shift-a shift-b shift-c pre-shift-to-origin-na pre-shift-to-origin-nb pre-shift-to-origin-nc)`

save the symmetry coordinates of molecule number imol to
 filename

Allow a shift of the coordinates to the origin before symmetry
expansion is apllied (this is how symmetry works in Coot
internals).

Arguments: imol (a whole number), filename (text), symop_no (a whole number), shift_a (a whole number), shift_b (a whole number), shift_c (a whole number), pre_shift_to_origin_na (a whole number), pre_shift_to_origin_nb (a whole number), pre_shift_to_origin_nc (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_symmetry_coords(0, "tutorial-modern.pdb", 1, 1, 1, 1, 1, 1, 1)` | not tried |
| Scheme | `(save-symmetry-coords 0 "tutorial-modern.pdb" 1 1 1 1 1 1 1)` | not tried |

### set_show_symmetry_master

Python: `set_show_symmetry_master(state)`  
Scheme: `(set-show-symmetry-master state)`

set display symmetry, master controller

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_symmetry_master(1)` | not tried |
| Scheme | `(set-show-symmetry-master 1)` | not tried |

### set_show_symmetry_molecule

Python: `set_show_symmetry_molecule(mol_no, state)`  
Scheme: `(set-show-symmetry-molecule mol-no state)`

set display symmetry for molecule number mol_no

 pass with state=0 for off, state=1 for on

Arguments: mol_no (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_symmetry_molecule(1, 1)` | not tried |
| Scheme | `(set-show-symmetry-molecule 1 1)` | not tried |

### set_space_group

Python: `set_space_group(imol, spg)`  
Scheme: `(set-space-group imol spg)`

set the space group for a coordinates molecule

 for shelx FA pdb files, there is no space group. So allow the user
 to set it. This can be initted with a HM symbol or a symm list for
 clipper.

This will only work on model molecules.

Returns the success status of the setting (1 good, 0 fail).

Arguments: imol (a whole number), spg (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_space_group(0, "hello")` | not tried |
| Scheme | `(set-space-group 0 "hello")` | not tried |

### set_symmetry_atom_labels_expanded

Python: `set_symmetry_atom_labels_expanded(state)`  
Scheme: `(set-symmetry-atom-labels-expanded state)`

set use expanded symmetry atom labels

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_symmetry_atom_labels_expanded(1)` | not tried |
| Scheme | `(set-symmetry-atom-labels-expanded 1)` | not tried |

### set_symmetry_colour_by_symop

Python: `set_symmetry_colour_by_symop(imol, state)`  
Scheme: `(set-symmetry-colour-by-symop imol state)`

set symmetry colour by symop mode

Arguments: imol (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_symmetry_colour_by_symop(0, 1)` | not tried |
| Scheme | `(set-symmetry-colour-by-symop 0 1)` | not tried |

### set_symmetry_molecule_rotate_colour_map

Python: `set_symmetry_molecule_rotate_colour_map(imol, state)`  
Scheme: `(set-symmetry-molecule-rotate-colour-map imol state)`

set the colour map rotation (i.e. the hue) for the symmetry
 atoms of molecule number imol

Arguments: imol (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_symmetry_molecule_rotate_colour_map(0, 1)` | not tried |
| Scheme | `(set-symmetry-molecule-rotate-colour-map 0 1)` | not tried |

### set_symmetry_shift_search_size

Python: `set_symmetry_shift_search_size(shift)`  
Scheme: `(set-symmetry-shift-search-size shift)`

set the cell shift search size for symmetry searching.

When the coordinates for one (or some) symmetry operator are missing
(which happens sometimes, but rarely), try changing setting this to 2
(default is 1). It slows symmetry searching, which is why it is not
set to 2 by default.

Arguments: shift (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_symmetry_shift_search_size(1)` | not tried |
| Scheme | `(set-symmetry-shift-search-size 1)` | not tried |

### set_symmetry_size

Python: `set_symmetry_size(f)`  
Scheme: `(set-symmetry-size f)`

set the size of the displayed symmetry

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_symmetry_size(1.0)` | not tried |
| Scheme | `(set-symmetry-size 1.0)` | not tried |

### set_symmetry_size_from_widget

Python: `set_symmetry_size_from_widget(text)`  
Scheme: `(set-symmetry-size-from-widget text)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: text (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_symmetry_size_from_widget("hello")` | not tried |
| Scheme | `(set-symmetry-size-from-widget "hello")` | not tried |

### set_symmetry_whole_chain

Python: `set_symmetry_whole_chain(imol, state)`  
Scheme: `(set-symmetry-whole-chain imol state)`

set symmetry colour for the chain

Arguments: imol (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_symmetry_whole_chain(0, 1)` | not tried |
| Scheme | `(set-symmetry-whole-chain 0 1)` | not tried |

### set_unit_cell_and_space_group

Python: `set_unit_cell_and_space_group(imol, a, b, c, alpha, beta, gamma, space_group)`  
Scheme: `(set-unit-cell-and-space-group imol a b c alpha beta gamma space-group)`

set the unit cell for a given model molecule
Angles in degress, cell lengths in Angstroms.
Returns the success status of the setting (1 good, 0 fail).

Arguments: imol (a whole number), a (a number), b (a number), c (a number), alpha (a number), beta (a number), gamma (a number), space_group (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_unit_cell_and_space_group(0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, "hello")` | not tried |
| Scheme | `(set-unit-cell-and-space-group 0 1.0 0.5 1.0 1.0 1.0 1.0 "hello")` | not tried |

### set_unit_cell_and_space_group_using_molecule

Python: `set_unit_cell_and_space_group_using_molecule(imol, imol_from)`  
Scheme: `(set-unit-cell-and-space-group-using-molecule imol imol-from)`

set the unit cell for a given model molecule using the cell of moecule imol_from
This will only work on model molecules.
Returns the success status of the setting (1 good, 0 fail).

Arguments: imol (a whole number), imol_from (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_unit_cell_and_space_group_using_molecule(0, 0)` | not tried |
| Scheme | `(set-unit-cell-and-space-group-using-molecule 0 0)` | not tried |

### setup_save_symmetry_coords

Python: `setup_save_symmetry_coords()`  
Scheme: `(setup-save-symmetry-coords)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_save_symmetry_coords()` | not tried |
| Scheme | `(setup-save-symmetry-coords)` | not tried |

### symmetry_as_calphas

Python: `symmetry_as_calphas(mol_no, state)`  
Scheme: `(symmetry-as-calphas mol-no state)`

display symmetry as CAs?

 pass with state=0 for off, state=1 for on

Arguments: mol_no (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `symmetry_as_calphas(1, 1)` | not tried |
| Scheme | `(symmetry-as-calphas 1 1)` | not tried |

### symmetry_molecule_rotate_colour_map_state

Python: `symmetry_molecule_rotate_colour_map_state(imol)`  
Scheme: `(symmetry-molecule-rotate-colour-map-state imol)`

should there be colour map rotation (i.e. the hue) change
 for the symmetry atoms of molecule number imol?

 return state=0 for off, state=1 for on

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `symmetry_molecule_rotate_colour_map_state(0)` | not tried |
| Scheme | `(symmetry-molecule-rotate-colour-map-state 0)` | not tried |

### undo_symmetry_view

Python: `undo_symmetry_view()`  
Scheme: `(undo-symmetry-view)`

Undo symmetry view. Translate back to main molecule from
 this symmetry position.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `undo_symmetry_view()` | not tried |
| Scheme | `(undo-symmetry-view)` | not tried |

