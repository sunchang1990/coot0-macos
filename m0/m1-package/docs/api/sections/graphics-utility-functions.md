# Graphics Utility Functions

[Scripting reference](../README.md) > Graphics Utility Functions (45 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### allow_duplicate_sequence_numbers

Python: `allow_duplicate_sequence_numbers()`  
Scheme: `(allow-duplicate-sequence-numbers)`

enable reading PDB/pdbx files with duplicate sequence numbers

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `allow_duplicate_sequence_numbers()` | ran (no return value) |
| Scheme | `(allow-duplicate-sequence-numbers)` | ran (no return value) |

### assign_hetatms

Python: `assign_hetatms(imol)`  
Scheme: `(assign-hetatms imol)`

some programs produce PDB files with ATOMs where there
 should be HETATMs. This is a function to assign HETATMs as per the
 PDB definition.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `assign_hetatms(0)` | ran, returned `0` |
| Scheme | `(assign-hetatms 0)` | ran, returned `0` |

Python and Scheme gave the same answer.

### check_for_dark_blue_density

Python: `check_for_dark_blue_density()`  
Scheme: `(check-for-dark-blue-density)`

give a warning dialog if density it too dark (blue)

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `check_for_dark_blue_density()` | ran (no return value) |
| Scheme | `(check-for-dark-blue-density)` | ran (no return value) |

### clear_and_update_model_molecule_from_file

Python: `clear_and_update_model_molecule_from_file(molecule_number, file_name)`  
Scheme: `(clear-and-update-model-molecule-from-file molecule-number file-name)`

replace pdb. Fail if molecule_number is not a valid model molecule.
 Return -1 on failure. Else return molecule_number

Arguments: molecule_number (a whole number), file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_and_update_model_molecule_from_file(0, "tutorial-modern.pdb")` | ran, returned `0` |
| Scheme | `(clear-and-update-model-molecule-from-file 0 "tutorial-modern.pdb")` | ran, returned `0` |

Python and Scheme gave the same answer.

### copy_residue_range

Python: `copy_residue_range(imol_target, chain_id_target, imol_reference, chain_id_reference, resno_range_start, resno_range_end)`  
Scheme: `(copy-residue-range imol-target chain-id-target imol-reference chain-id-reference resno-range-start resno-range-end)`

copy the given residue range from the reference chain to the target chain

resno_range_start and resno_range_end are inclusive.

Arguments: imol_target (a whole number), chain_id_target (text), imol_reference (a whole number), chain_id_reference (text), resno_range_start (a whole number), resno_range_end (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `copy_residue_range(0, "A", 0, "A", 41, 45)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(copy-residue-range 0 "A" 0 "A" 41 45)` | stopped Coot when tried without a window (not checked with a window) |

### do_GL_lighting_state

Python: `do_GL_lighting_state()`  
Scheme: `(do-GL-lighting-state)`

return the flag for GL lighting

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_GL_lighting_state()` | ran, returned `0` |
| Scheme | `(do-GL-lighting-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### do_anti_aliasing_state

Python: `do_anti_aliasing_state()`  
Scheme: `(do-anti-aliasing-state)`

return the flag for antialiasing the bond lines

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_anti_aliasing_state()` | ran, returned `0` |
| Scheme | `(do-anti-aliasing-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### get_idle_function_rock_target_angle

Python: `get_idle_function_rock_target_angle()`  
Scheme: `(get-idle-function-rock-target-angle)`

used by above to set the angle to rotate to (time dependent)

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_idle_function_rock_target_angle()` | ran, returned `0.007305599456073013` |
| Scheme | `(get-idle-function-rock-target-angle)` | ran, returned `0.007117656556372816` |

Python and Scheme gave the same answer.

### get-input-model-was-cif-state-scm

Scheme: `(get-input-model-was-cif-state-scm imol)`

- get the name state of the input model. Return false if there was an erro with the molecule index

Arguments: imol (a whole number). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | `(get-input-model-was-cif-state-scm 0)` | ran, returned `#f` |

### get_input_molecule_was_in_mmcif_state

Python: `get_input_molecule_was_in_mmcif_state(imol)`

- get the name state of the input model

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `get_input_molecule_was_in_mmcif_state_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_input_molecule_was_in_mmcif_state(0)` | ran, returned `False` |

### get_solid_density_surface_opacity

Python: `get_solid_density_surface_opacity(imol)`  
Scheme: `(get-solid-density-surface-opacity imol)`

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_solid_density_surface_opacity(0)` | ran, returned `-1.0` |
| Scheme | `(get-solid-density-surface-opacity 0)` | ran, returned `-1.0` |

Python and Scheme gave the same answer.

### graphics_n_molecules

Python: `graphics_n_molecules()`  
Scheme: `(graphics-n-molecules)`

return the number of molecules (coordinates molecules and
 map molecules combined) that are currently in coot

 Returns the number of molecules (closed molecules are not counted)

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_n_molecules()` | ran, returned `2` |
| Scheme | `(graphics-n-molecules)` | ran, returned `2` |

Python and Scheme gave the same answer.

### handle_read_draw_molecule

Python: `handle_read_draw_molecule(filename)`  
Scheme: `(handle-read-draw-molecule filename)`

a synonym for read-pdb. Read the coordinates from
 filename (can be pdb, cif or shelx format)

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_read_draw_molecule("tutorial-modern.pdb")` | ran, returned `2` |
| Scheme | `(handle-read-draw-molecule "tutorial-modern.pdb")` | ran, returned `2` |

Python and Scheme gave the same answer.

### handle_read_draw_molecule_and_move_molecule_here

Python: `handle_read_draw_molecule_and_move_molecule_here(filename)`  
Scheme: `(handle-read-draw-molecule-and-move-molecule-here filename)`

read coordinates from filename and recentre the new
 molecule at the screen rotation centre.

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_read_draw_molecule_and_move_molecule_here("tutorial-modern.pdb")` | ran, returned `2` |
| Scheme | `(handle-read-draw-molecule-and-move-molecule-here "tutorial-modern.pdb")` | ran, returned `2` |

Python and Scheme gave the same answer.

### handle_read_draw_molecule_with_recentre

Python: `handle_read_draw_molecule_with_recentre(filename, recentre_on_read_pdb_flag)`  
Scheme: `(handle-read-draw-molecule-with-recentre filename recentre-on-read-pdb-flag)`

read coordinates from filename with option to not recentre.

 set recentre_on_read_pdb_flag to 0 if you don't want the view to
 recentre on the new coordinates.

Arguments: filename (text), recentre_on_read_pdb_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_read_draw_molecule_with_recentre("tutorial-modern.pdb", 1)` | ran, returned `2` |
| Scheme | `(handle-read-draw-molecule-with-recentre "tutorial-modern.pdb" 1)` | ran, returned `2` |

Python and Scheme gave the same answer.

### het_group_n_atoms

Python: `het_group_n_atoms(comp_id)`  
Scheme: `(het-group-n-atoms comp-id)`

return the number of non-hydrogen atoms in the given
 het-group (comp-id).

Return -1 on comp-id not found in dictionary.

Arguments: comp_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `het_group_n_atoms("ALA")` | ran, returned `6` |
| Scheme | `(het-group-n-atoms "ALA")` | ran, returned `6` |

Python and Scheme gave the same answer.

### het_group_residues

Python: `het_group_residues(imol)`  
Scheme: `(het-group-residues imol)`

- get the specs for hetgroups - waters are not counted as het-groups.

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `het_group_residues_py`.
Also available in Scheme as `het-group-residues-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `het_group_residues(0)` | ran, returned `[]` |
| Scheme | `(het-group-residues 0)` | ran, returned `()` |

Python and Scheme gave the same answer.

### hetify_residue

Python: `hetify_residue(imol, chain_id, resno, ins_code)`  
Scheme: `(hetify-residue imol chain-id resno ins-code)`

if this is not a standard group, then turn the atoms to HETATMs.

Return 1 on atoms changes, 0 on not. Return -1 if residue not found.

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `hetify_residue(0, "A", 41, "")` | ran, returned `-1` |
| Scheme | `(hetify-residue 0 "A" 41 "")` | ran, returned `-1` |

Python and Scheme gave the same answer.

### idle_function_rotate_angle

Python: `idle_function_rotate_angle()`  
Scheme: `(idle-function-rotate-angle)`

what is the idle function rotation angle?

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `idle_function_rotate_angle()` | ran, returned `0.15000000596046448` |
| Scheme | `(idle-function-rotate-angle)` | ran, returned `0.15000000596046448` |

Python and Scheme gave the same answer.

### make_updating_model_molecule

Python: `make_updating_model_molecule(filename)`  
Scheme: `(make-updating-model-molecule filename)`

make a model molecule from the give file name.
If the file updates, then the model will be updated.

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_updating_model_molecule("tutorial-modern.pdb")` | ran, returned `1` |
| Scheme | `(make-updating-model-molecule "tutorial-modern.pdb")` | ran, returned `1` |

Python and Scheme gave the same answer.

### molecule_has_hydrogens_raw

Python: `molecule_has_hydrogens_raw(imol)`  
Scheme: `(molecule-has-hydrogens-raw imol)`

return either 1 (yes, there is at least one hydrogen) or 0 (no
 hydrogens, or no such molecule). The scripting interface to this
 does not have the _raw suffix and returns a scheme or python
 boolean True or False.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `molecule_has_hydrogens_raw(0)` | ran, returned `0` |
| Scheme | `(molecule-has-hydrogens-raw 0)` | ran, returned `0` |

Python and Scheme gave the same answer.

### own_molecule_number

Python: `own_molecule_number(imol)`  
Scheme: `(own-molecule-number imol)`

a testing/debugging function. Used in a test to make sure that the
 outside number of a molecule (the vector index) is the same as that
 embedded in the molecule description object. Return -1 on
 non-valid passed imol.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `own_molecule_number(0)` | ran, returned `0` |
| Scheme | `(own-molecule-number 0)` | ran, returned `0` |

Python and Scheme gave the same answer.

### python_at_prompt_at_startup_state

Python: `python_at_prompt_at_startup_state()`  
Scheme: `(python-at-prompt-at-startup-state)`

is the python interpreter at the prompt?

Returns 1 for yes, 0 for no.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `python_at_prompt_at_startup_state()` | ran, returned `1` |
| Scheme | `(python-at-prompt-at-startup-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### read_pdb

Python: `read_pdb(filename)`  
Scheme: `(read-pdb filename)`

read coordinates from filename

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_pdb("tutorial-modern.pdb")` | ran, returned `2` |
| Scheme | `(read-pdb "tutorial-modern.pdb")` | ran, returned `2` |

Python and Scheme gave the same answer.

### replace_fragment

Python: `replace_fragment(imol_target, imol_fragment, atom_selection)`  
Scheme: `(replace-fragment imol-target imol-fragment atom-selection)`

replace the parts of molecule number imol that are
 duplicated in molecule number imol_frag

Arguments: imol_target (a whole number), imol_fragment (a whole number), atom_selection (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `replace_fragment(0, 0, "//A/41-45")` | ran, returned `1` |
| Scheme | `(replace-fragment 0 0 "//A/41-45")` | ran, returned `1` |

Python and Scheme gave the same answer.

### replace_residues_from_mol

Python: `replace_residues_from_mol(imol_target, imol_ref, residue_specs_list_ref_py)`  
Scheme: `(replace-residues-from-mol-scm imol-target imol-ref residue-specs-list-ref-scm)`

Arguments: imol_target (a whole number), imol_ref (a whole number), residue_specs_list_ref_py (a list or value). Returns: a whole number.
Also available in Python as `replace_residues_from_mol_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `replace_residues_from_mol(0, 0, ["A", 41, ""])` | error: SystemError: <built-in function replace_residues_from_mol_py> returned a result with an exception set |
| Scheme | `(replace-residues-from-mol-scm 0 0 (list "A" 41 ""))` | error: In procedure length: Wrong type argument in position 1: "A" |

### reset_view

Python: `reset_view()`  
Scheme: `(reset-view)`

"Reset" the view

 return 1 if we moved, else return 0.

 centre on last-read molecule with zoom 100. If we are there, then
 go to the previous molecule, if we are there, then go to the origin.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `reset_view()` | ran, returned `0` |
| Scheme | `(reset-view)` | ran, returned `0` |

Python and Scheme gave the same answer.

### residue_has_hetatms

Python: `residue_has_hetatms(imol, chain_id, resno, ins_code)`  
Scheme: `(residue-has-hetatms imol chain-id resno ins-code)`

residue has HETATMs?

return 1 if all atoms of the specified residue are HETATMs, else,
return 0. If residue not found, return -1.

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_has_hetatms(0, "A", 41, "")` | ran, returned `0` |
| Scheme | `(residue-has-hetatms 0 "A" 41 "")` | ran, returned `0` |

Python and Scheme gave the same answer.

### screendump_image

Python: `screendump_image(filename)`  
Scheme: `(screendump-image filename)`

dump the current screen image to a file. Format ppm

You can use this, in conjunction with spinning and view moving functions to
make movies

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `screendump_image("tutorial-modern.pdb")` | not run: not run automatically (screendump: exits, uses the network, an external program, files or a screen) |
| Scheme | `(screendump-image "tutorial-modern.pdb")` | not run: not run automatically (screendump: exits, uses the network, an external program, files or a screen) |

### set_convert_to_v2_atom_names

Python: `set_convert_to_v2_atom_names(state)`  
Scheme: `(set-convert-to-v2-atom-names state)`

shall we convert nucleotides to match the old dictionary
 names?

Usually (after 2006 or so) we do not want to do this (given current
Coot architecture). Coot should handle the residue synonyms
transparently.

default off (0).

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_convert_to_v2_atom_names(1)` | ran (no return value) |
| Scheme | `(set-convert-to-v2-atom-names 1)` | ran (no return value) |

### set_do_GL_lighting

Python: `set_do_GL_lighting(state)`  
Scheme: `(set-do-GL-lighting state)`

turn the GL lighting on (state = 1) or off (state = 0)

 slows down the display of simple lines

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_do_GL_lighting(1)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(set-do-GL-lighting 1)` | stopped Coot when tried without a window (not checked with a window) |

### set_do_anti_aliasing

Python: `set_do_anti_aliasing(state)`  
Scheme: `(set-do-anti-aliasing state)`

set the bond lines to be antialiased

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_do_anti_aliasing(1)` | ran (no return value) |
| Scheme | `(set-do-anti-aliasing 1)` | ran (no return value) |

### set_draw_map_standard_lines

Python: `set_draw_map_standard_lines(imol, state)`  
Scheme: `(set-draw-map-standard-lines imol state)`

toggle for standard lines representation of map.

 This turns off/on standard lines representation of map. transparent
 surface is another representation type.

 If you want to just turn off a map, don't use this, use
 set_map_displayed().

Arguments: imol (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_draw_map_standard_lines(0, 1)` | ran (no return value) |
| Scheme | `(set-draw-map-standard-lines 0 1)` | ran (no return value) |

### set_draw_solid_density_surface

Python: `set_draw_solid_density_surface(imol, state)`  
Scheme: `(set-draw-solid-density-surface imol state)`

sets the density map of the given molecule to be drawn as a
 (transparent) solid surface.

Arguments: imol (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_draw_solid_density_surface(0, 1)` | ran (no return value) |
| Scheme | `(set-draw-solid-density-surface 0 1)` | ran (no return value) |

### set_flat_shading_for_solid_density_surface

Python: `set_flat_shading_for_solid_density_surface(state)`  
Scheme: `(set-flat-shading-for-solid-density-surface state)`

set the flag to do flat shading rather than smooth shading
 for solid density surface.

Default is 1 (on.

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_flat_shading_for_solid_density_surface(1)` | ran (no return value) |
| Scheme | `(set-flat-shading-for-solid-density-surface 1)` | ran (no return value) |

### set_idle_function_rotate_angle

Python: `set_idle_function_rotate_angle(f)`  
Scheme: `(set-idle-function-rotate-angle f)`

how far should we rotate when (auto) spinning? Fast
 computer? set this to 0.1

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_idle_function_rotate_angle(1.0)` | ran (no return value) |
| Scheme | `(set-idle-function-rotate-angle 1.0)` | ran (no return value) |

### set_rocking_factors

Python: `set_rocking_factors(width_scale, frequency_scale)`  
Scheme: `(set-rocking-factors width-scale frequency-scale)`

Settings for the inevitable discontents who dislike the
 default rocking rates (defaults 1 and 1)

Arguments: width_scale (a number), frequency_scale (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_rocking_factors(1.0, 1.0)` | ran (no return value) |
| Scheme | `(set-rocking-factors 1.0 1.0)` | ran (no return value) |

### set_solid_density_surface_opacity

Python: `set_solid_density_surface_opacity(imol, opacity)`  
Scheme: `(set-solid-density-surface-opacity imol opacity)`

set the opacity of density surface representation of the
 given map.

0.0 is totally transparent, 1.0 is completely opaque and (because the
objects are no longer depth sorted) considerably faster to render.
0.3 is a reasonable number.

Arguments: imol (a whole number), opacity (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_solid_density_surface_opacity(0, 1.0)` | ran (no return value) |
| Scheme | `(set-solid-density-surface-opacity 0 1.0)` | ran (no return value) |

### show_calculate_updating_maps_gui

Python: `show_calculate_updating_maps_gui()`  
Scheme: `(show-calculate-updating-maps-gui)`

show the updating maps gui

this function is called from callbacks.c and calls a python gui function

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_calculate_updating_maps_gui()` | ran (no return value) |
| Scheme | `(show-calculate-updating-maps-gui)` | ran (no return value) |

### start_graphics_interface

Python: `start_graphics_interface()`  
Scheme: `(start-graphics-interface)`

start Gtk (and graphics)

 This function is useful if it was not started already (which can be
 achieved by using the command line argument --no-graphics).

 An interface for Ralf

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `start_graphics_interface()` | no answer within 60 s (slow, or waits for something) |
| Scheme | `(start-graphics-interface)` | no answer within 60 s (slow, or waits for something) |

### test_internal

Python: `test_internal()`  
Scheme: `(test-internal)`

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `test_internal_py`.
Also available in Scheme as `test-internal-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `test_internal()` | ran, returned `False` |
| Scheme | `(test-internal)` | ran, returned `#f` |

Python and Scheme gave the same answer.

### test_internal_single

Python: `test_internal_single()`  
Scheme: `(test-internal-single)`

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `test_internal_single_py`.
Also available in Scheme as `test-internal-single-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `test_internal_single()` | ran, returned `True` |
| Scheme | `(test-internal-single)` | ran, returned `#t` |

Python and Scheme gave the same answer.

### toggle_idle_rock_function

Python: `toggle_idle_rock_function()`  
Scheme: `(toggle-idle-rock-function)`

Rock (not roll) (self-timed)

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `toggle_idle_rock_function()` | ran (no return value) |
| Scheme | `(toggle-idle-rock-function)` | ran (no return value) |

### toggle_idle_spin_function

Python: `toggle_idle_spin_function()`  
Scheme: `(toggle-idle-spin-function)`

Spin spin spin (or not)

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `toggle_idle_spin_function()` | ran (no return value) |
| Scheme | `(toggle-idle-spin-function)` | ran (no return value) |

### use_graphics_interface_state

Python: `use_graphics_interface_state()`  
Scheme: `(use-graphics-interface-state)`

shall we start up the Gtk and the graphics window?

 if passed the command line argument --no-graphics, coot will not start up gtk
 itself.

 An interface function for Ralf.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `use_graphics_interface_state()` | ran, returned `0` |
| Scheme | `(use-graphics-interface-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

