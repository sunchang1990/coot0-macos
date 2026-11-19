# Map and Molecule Control

[Scripting reference](../README.md) > Map and Molecule Control (24 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_map_and_mol_display_control_widgets

Python: `add_map_and_mol_display_control_widgets()`  
Scheme: `(add-map-and-mol-display-control-widgets)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_map_and_mol_display_control_widgets()` | ran (no return value) |
| Scheme | `(add-map-and-mol-display-control-widgets)` | ran (no return value) |

### add_map_display_control_widgets

Python: `add_map_display_control_widgets()`  
Scheme: `(add-map-display-control-widgets)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_map_display_control_widgets()` | ran (no return value) |
| Scheme | `(add-map-display-control-widgets)` | ran (no return value) |

### add_mol_display_control_widgets

Python: `add_mol_display_control_widgets()`  
Scheme: `(add-mol-display-control-widgets)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_mol_display_control_widgets()` | ran (no return value) |
| Scheme | `(add-mol-display-control-widgets)` | ran (no return value) |

### close_graphics_display_control_window

Python: `close_graphics_display_control_window()`  
Scheme: `(close-graphics-display-control-window)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `close_graphics_display_control_window()` | ran (no return value) |
| Scheme | `(close-graphics-display-control-window)` | ran (no return value) |

### display_maps

Python: `display_maps(pyo)`  
Scheme: `(display-maps maps-list)`

Arguments: pyo (a list or value). Returns: nothing.
Also available in Python as `display_maps_py`.
Also available in Scheme as `display-maps-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### display_only_active

Python: `display_only_active()`  
Scheme: `(display-only-active)`

display only the active mol and the refinement map

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `display_only_active()` | ran (no return value) |
| Scheme | `(display-only-active)` | ran (no return value) |

### map_is_displayed

Python: `map_is_displayed(imol)`  
Scheme: `(map-is-displayed imol)`

return the display state of molecule number imol
 Returns 1 for on, 0 for off

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_is_displayed(0)` | not tried |
| Scheme | `(map-is-displayed 0)` | not tried |

### merge_molecules

Python: `merge_molecules(add_molecules, imol)`  
Scheme: `(merge-molecules add-molecules imol)`

merge molecules

Returns a pair, the first item of which is a status (1 is good) the second is
a list of merge-infos (one for each of the items in add_molecules). If the
molecule of an add_molecule item is just one residue, return a spec for the
new residue, if it is many residues return a chain id.

the first argument is a list of molecule numbers and the second is the target
 molecule into which the others should be merged

Arguments: add_molecules (a list or value), imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `merge_molecules_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `merge_molecules([0], 0)` | not tried |
| Scheme | `(merge-molecules (list 0) 0)` | not tried |

### mol_is_active

Python: `mol_is_active(imol)`  
Scheme: `(mol-is-active imol)`

return the active state of molecule number imol
 Returns 1 for on, 0 for off

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mol_is_active(0)` | not tried |
| Scheme | `(mol-is-active 0)` | not tried |

### mol_is_displayed

Python: `mol_is_displayed(imol)`  
Scheme: `(mol-is-displayed imol)`

return the display state of molecule number imol

 Returns 1 for on, 0 for off

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mol_is_displayed(0)` | not tried |
| Scheme | `(mol-is-displayed 0)` | not tried |

### post_display_control_window

Python: `post_display_control_window()`  
Scheme: `(post-display-control-window)`

display the Display Constrol window

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `post_display_control_window()` | not tried |
| Scheme | `(post-display-control-window)` | not tried |

### reset_graphics_display_control_window

Python: `reset_graphics_display_control_window()`  
Scheme: `(reset-graphics-display-control-window)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `reset_graphics_display_control_window()` | not tried |
| Scheme | `(reset-graphics-display-control-window)` | not tried |

### set_all_maps_displayed

Python: `set_all_maps_displayed(on_or_off)`  
Scheme: `(set-all-maps-displayed on-or-off)`

if on_or_off is 0 turn off all maps displayed, for other
 values of on_or_off turn on all maps

Arguments: on_or_off (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_all_maps_displayed(1)` | not tried |
| Scheme | `(set-all-maps-displayed 1)` | not tried |

### set_all_models_displayed_and_active

Python: `set_all_models_displayed_and_active(on_or_off)`  
Scheme: `(set-all-models-displayed-and-active on-or-off)`

if on_or_off is 0 turn off all models displayed and active,
 for other values of on_or_off turn on all models.

Arguments: on_or_off (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_all_models_displayed_and_active(1)` | not tried |
| Scheme | `(set-all-models-displayed-and-active 1)` | not tried |

### set_display_only_model_mol

Python: `set_display_only_model_mol(imol)`  
Scheme: `(set-display-only-model-mol imol)`

from all the model molecules, display only imol

This stops flashing/delayed animations with many molecules

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_display_only_model_mol(0)` | not tried |
| Scheme | `(set-display-only-model-mol 0)` | not tried |

### set_map_displayed

Python: `set_map_displayed(imol, state)`  
Scheme: `(set-map-displayed imol state)`

make the map displayed/undisplayed, 0 for off, 1 for on

Arguments: imol (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_map_displayed(0, 1)` | not tried |
| Scheme | `(set-map-displayed 0 1)` | not tried |

### set_merge_molecules_ligand_spec

Python: `set_merge_molecules_ligand_spec(ligand_spec_py)`  
Scheme: `(set-merge-molecules-ligand-spec ligand-spec-scm)`

Arguments: ligand_spec_py (a list or value). Returns: nothing.
Also available in Python as `set_merge_molecules_ligand_spec_py`.
Also available in Scheme as `set-merge-molecules-ligand-spec-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_merge_molecules_ligand_spec(["A", 41, ""])` | not tried |
| Scheme | `(set-merge-molecules-ligand-spec (list "A" 41 ""))` | not tried |

### set_mol_active

Python: `set_mol_active(imol, state)`  
Scheme: `(set-mol-active imol state)`

make the coordinates molecule active/inactve (clickable), 0
 for off, 1 for on

Arguments: imol (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_mol_active(0, 1)` | not tried |
| Scheme | `(set-mol-active 0 1)` | not tried |

### set_mol_displayed

Python: `set_mol_displayed(imol, state)`  
Scheme: `(set-mol-displayed imol state)`

make the coordinates molecule displayed/undisplayed, 0 for off, 1 for on

Arguments: imol (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_mol_displayed(0, 1)` | not tried |
| Scheme | `(set-mol-displayed 0 1)` | not tried |

### set_only_last_model_molecule_displayed

Python: `set_only_last_model_molecule_displayed()`  
Scheme: `(set-only-last-model-molecule-displayed)`

only display the last model molecule

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_only_last_model_molecule_displayed()` | not tried |
| Scheme | `(set-only-last-model-molecule-displayed)` | not tried |

### show_spacegroup

Python: `show_spacegroup(imol)`  
Scheme: `(show-spacegroup imol)`

return the spacegroup of molecule number imol . Deprecated.

Returns "No Spacegroup" when the spacegroup of a molecule has not been
set.

Arguments: imol (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_spacegroup(0)` | not tried |
| Scheme | `(show-spacegroup 0)` | not tried |

### space_group

Python: `space_group(imol)`  
Scheme: `(space-group imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `space_group_py`.
Also available in Scheme as `space-group-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `space_group(0)` | not tried |
| Scheme | `(space-group 0)` | not tried |

### symmetry_operators

Python: `symmetry_operators(imol)`  
Scheme: `(symmetry-operators imol)`

return a list of symmetry operators as strings - or Python False if
 that is not possible.

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `symmetry_operators_py`.
Also available in Scheme as `symmetry-operators-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `symmetry_operators(0)` | not tried |
| Scheme | `(symmetry-operators 0)` | not tried |

### symmetry_operators_to_xHM

Python: `symmetry_operators_to_xHM(symmetry_operators)`  
Scheme: `(symmetry-operators->xHM symmetry-operators)`

take the return value from above and return a xHM symbol (for
 testing currently)

Arguments: symmetry_operators (a list or value). Returns: a value (see the result of the example).
Also available in Python as `symmetry_operators_to_xHM_py`.
Also available in Scheme as `symmetry-operators-to-xHM-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

