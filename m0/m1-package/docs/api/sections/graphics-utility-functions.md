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
| Python | `allow_duplicate_sequence_numbers()` | ran (no return value, nothing visible changed) |
| Scheme | `(allow-duplicate-sequence-numbers)` | ran (no return value, nothing visible changed) |

### assign_hetatms

Python: `assign_hetatms(imol)`  
Scheme: `(assign-hetatms imol)`

some programs produce PDB files with ATOMs where there
 should be HETATMs. This is a function to assign HETATMs as per the
 PDB definition.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `imol_nag = read_pdb("nag_only.pdb")`, then `assign_hetatms(imol_nag)` | ran, returned `30` |
| Scheme | `(assign-hetatms 0)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns the number of atoms changed to HETATM in non-standard residues; 0 for a pure protein.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### check_for_dark_blue_density

Python: `check_for_dark_blue_density()`  
Scheme: `(check-for-dark-blue-density)`

give a warning dialog if density it too dark (blue)

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `check_for_dark_blue_density()` | ran (no return value, nothing visible changed) |
| Scheme | `(check-for-dark-blue-density)` | ran (no return value, nothing visible changed) |

### clear_and_update_model_molecule_from_file

Python: `clear_and_update_model_molecule_from_file(molecule_number, file_name)`  
Scheme: `(clear-and-update-model-molecule-from-file molecule-number file-name)`

replace pdb. Fail if molecule_number is not a valid model molecule.
 Return -1 on failure. Else return molecule_number

Arguments: molecule_number (a whole number), file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `imol2 = read_pdb("tutorial-modern.pdb")`, then `clear_and_update_model_molecule_from_file(imol2, "standard-residues.pdb")` | ran, returned `3`; changed: molecule 3: added 26 residue(s) (A912, A957, A888, A876 ...); molecule 3: deleted 181 residue(s) (A2, A3, A4, A5 ...); molecule 3: atoms of 8 residue(s) (A1, A6, A7, A14 ...); first_small_coords_imol(): -1 -> 3 |
| Scheme | first `(define imol2 (read-pdb "tutorial-modern.pdb"))`, then `(clear-and-update-model-molecule-from-file imol2 "standard-residues.pdb")` | ran, returned `3`; changed: molecule 3: added 26 residue(s) (A912, A957, A888, A876 ...); molecule 3: deleted 181 residue(s) (A2, A3, A4, A5 ...); molecule 3: atoms of 8 residue(s) (A1, A6, A7, A14 ...); first_small_coords_imol(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: replaces the coordinates of the molecule by those in the file, keeping its molecule number; returns that number, -1 on failure.

Python and Scheme gave the same answer.

### copy_residue_range

Python: `copy_residue_range(imol_target, chain_id_target, imol_reference, chain_id_reference, resno_range_start, resno_range_end)`  
Scheme: `(copy-residue-range imol-target chain-id-target imol-reference chain-id-reference resno-range-start resno-range-end)`

copy the given residue range from the reference chain to the target chain

resno_range_start and resno_range_end are inclusive.

Arguments: imol_target (a whole number), chain_id_target (text), imol_reference (a whole number), chain_id_reference (text), resno_range_start (a whole number), resno_range_end (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `imol2 = read_pdb("tutorial-modern.pdb")`, then `copy_residue_range(imol2, "B", 0, "A", 10, 20)` | ran, returned `0`; changed: molecule 3: B-factors of 11 residue(s) (B10, B11, B12, B13 ...); molecule 3: coordinates of 11 residue(s) (B10, B11, B12, B13 ...) |
| Scheme | first `(define imol2 (read-pdb "tutorial-modern.pdb"))`, then `(copy-residue-range imol2 "B" 0 "A" 10 20)` | ran, returned `0`; changed: molecule 3: B-factors of 11 residue(s) (B10, B11, B12, B13 ...); molecule 3: coordinates of 11 residue(s) (B10, B11, B12, B13 ...) |

Example written and checked by hand on the test data. Expected: copies coordinates of the residue range from the reference chain onto the same residues of the target chain (no superposition).

Note: Returns 0 although 11 residues were copied (the old automatic run stopped Coot only because of placeholder arguments). The return status looks unreliable.

Python and Scheme gave the same answer.

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
| Python | `get_idle_function_rock_target_angle()` | ran, returned `-0.05417729701955092` |
| Scheme | `(get-idle-function-rock-target-angle)` | ran, returned `-0.05486917173613091` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### get-input-model-was-cif-state-scm

Scheme: `(get-input-model-was-cif-state-scm imol)`

- get the name state of the input model. Return false if there was an erro with the molecule index

Arguments: imol (a whole number). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | `(get-input-model-was-cif-state-scm 0)` | ran, returned `#f` |

Example written and checked by hand on the test data. Expected: #f for a model read from PDB format, #t for mmCIF, #f for an invalid molecule.

### get_input_molecule_was_in_mmcif_state

Python: `get_input_molecule_was_in_mmcif_state(imol)`

- get the name state of the input model

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `get_input_molecule_was_in_mmcif_state_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_input_molecule_was_in_mmcif_state(0)` | ran, returned `False` |

Example written and checked by hand on the test data. Expected: False for a molecule read from PDB format, True for one read from mmCIF.

### get_solid_density_surface_opacity

Python: `get_solid_density_surface_opacity(imol)`  
Scheme: `(get-solid-density-surface-opacity imol)`

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_solid_density_surface_opacity(1)` | ran, returned `0.5` |
| Scheme | `(get-solid-density-surface-opacity 1)` | ran, returned `0.5` |

Example written and checked by hand on the test data. Expected: returns the opacity of the map's solid surface (0.5 default).

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
| Python | `graphics_n_molecules()` | ran, returned `3` |
| Scheme | `(graphics-n-molecules)` | ran, returned `3` |

Python and Scheme gave the same answer.

### handle_read_draw_molecule

Python: `handle_read_draw_molecule(filename)`  
Scheme: `(handle-read-draw-molecule filename)`

a synonym for read-pdb. Read the coordinates from
 filename (can be pdb, cif or shelx format)

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_read_draw_molecule("tutorial-modern.pdb")` | ran, returned `3`; changed: new molecule 3 (model, tutorial-modern.pdb); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(handle-read-draw-molecule "tutorial-modern.pdb")` | ran, returned `3`; changed: new molecule 3 (model, tutorial-modern.pdb); graphics_n_molecules(): 3 -> 4 |

Python and Scheme gave the same answer.

### handle_read_draw_molecule_and_move_molecule_here

Python: `handle_read_draw_molecule_and_move_molecule_here(filename)`  
Scheme: `(handle-read-draw-molecule-and-move-molecule-here filename)`

read coordinates from filename and recentre the new
 molecule at the screen rotation centre.

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_read_draw_molecule_and_move_molecule_here("tutorial-modern.pdb")` | ran, returned `3`; changed: new molecule 3 (model, tutorial-modern.pdb); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(handle-read-draw-molecule-and-move-molecule-here "tutorial-modern.pdb")` | ran, returned `3`; changed: new molecule 3 (model, tutorial-modern.pdb); graphics_n_molecules(): 3 -> 4 |

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
| Python | `handle_read_draw_molecule_with_recentre("tutorial-modern.pdb", 1)` | ran, returned `3`; changed: new molecule 3 (model, tutorial-modern.pdb); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(handle-read-draw-molecule-with-recentre "tutorial-modern.pdb" 1)` | ran, returned `3`; changed: new molecule 3 (model, tutorial-modern.pdb); graphics_n_molecules(): 3 -> 4 |

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
| Python | first `imol_nag = read_pdb("nag_only.pdb")`, then `hetify_residue(imol_nag, "A", 1, "")` | ran, returned `1` |
| Scheme | first `(define imol-nag (read-pdb "nag_only.pdb"))`, then `(hetify-residue imol-nag "A" 1 "")` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 when a non-standard residue's atoms are made HETATMs; a standard residue is left alone.

Note: For a standard residue that exists (GLU A41) it returns -1 although the doc says -1 = residue not found and 0 = no change (the code only sets 1 when atoms changed, else keeps -1).

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
| Python | `make_updating_model_molecule("tutorial-modern.pdb")` | ran, returned `1`; changed: new molecule 3 (model, tutorial-modern.pdb); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(make-updating-model-molecule "tutorial-modern.pdb")` | ran, returned `1`; changed: new molecule 3 (model, tutorial-modern.pdb); graphics_n_molecules(): 3 -> 4 |

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
| Python | first `imol_nag = read_pdb("nag_only.pdb")`, then `molecule_has_hydrogens_raw(imol_nag)` | ran, returned `1` |
| Scheme | first `(define imol-nag (read-pdb "nag_only.pdb"))`, then `(molecule-has-hydrogens-raw imol-nag)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: 1 if the molecule has at least one hydrogen, 0 if not (0 is correct for tutorial-modern.pdb).

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
| Scheme | `(own-molecule-number 1)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns the same number it was given (debug check that a molecule knows its own number).

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

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
| Python | `read_pdb("tutorial-modern.pdb")` | ran, returned `3`; changed: new molecule 3 (model, tutorial-modern.pdb); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(read-pdb "tutorial-modern.pdb")` | ran, returned `3`; changed: new molecule 3 (model, tutorial-modern.pdb); graphics_n_molecules(): 3 -> 4 |

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
| Python | first `imol2 = read_pdb("tutorial-modern.pdb")`, then `delete_residue(imol2, "A", 41, "")`, then `replace_residues_from_mol(imol2, 0, [["A", 41, ""], ["A", 42, ""]])` | ran, returned `1`; changed: molecule 3: added 1 residue(s) (A41) |
| Scheme | first `(define imol2 (read-pdb "tutorial-modern.pdb"))`, then `(delete-residue imol2 "A" 41 "")`, then `(replace-residues-from-mol-scm imol2 0 (list (list "A" 41 "") (list "A" 42 "")))` | ran, returned `1`; changed: molecule 3: added 1 residue(s) (A41) |

Example written and checked by hand on the test data. Expected: replaces (or adds) the listed residues in the target molecule with those of the reference molecule; returns 1 on success.

Python and Scheme gave the same answer.

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
| Python | `reset_view()` | ran, returned `0`; changed: zoom: 100.0 -> 145.85 |
| Scheme | `(reset-view)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: centres on the last-read molecule and resets the zoom (the view does move; see note).

Note: Doc says 'return 1 if we moved', but it returned 0 although the centre moved 3.8 A and the zoom changed.

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
| Python | first `imol_nag = read_pdb("nag_only.pdb")`, then `residue_has_hetatms(imol_nag, "A", 1, "")` | ran, returned `1` |
| Scheme | `(residue-has-hetatms 0 "A" 41 "")` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: 1 if all atoms of the residue are HETATMs, 0 if not, -1 if no such residue.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### screendump_image

Python: `screendump_image(filename)`  
Scheme: `(screendump-image filename)`

dump the current screen image to a file. Format ppm

You can use this, in conjunction with spinning and view moving functions to
make movies

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `screendump_image("view.ppm")` | not run: needs the graphics window (reads the OpenGL frame buffer) |
| Scheme | `(screendump-image "view.ppm")` | not run: needs the graphics window (reads the OpenGL frame buffer) |

Example written and checked by hand on the test data. Expected: writes the current graphics view to the image file.

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
| Python | `set_convert_to_v2_atom_names(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-convert-to-v2-atom-names 1)` | ran (no return value, nothing visible changed) |

### set_do_GL_lighting

Python: `set_do_GL_lighting(state)`  
Scheme: `(set-do-GL-lighting state)`

turn the GL lighting on (state = 1) or off (state = 0)

 slows down the display of simple lines

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_do_GL_lighting(1)` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(set-do-GL-lighting 1)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: turns OpenGL lighting on (1) or off (0) for solid objects.

### set_do_anti_aliasing

Python: `set_do_anti_aliasing(state)`  
Scheme: `(set-do-anti-aliasing state)`

set the bond lines to be antialiased

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_do_anti_aliasing(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-do-anti-aliasing 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: do_anti_aliasing_state was 0, set to 1, read back 1; Scheme: do-anti-aliasing-state was 0, set to 1, read back 1.

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
| Python | `set_draw_map_standard_lines(0, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-draw-map-standard-lines 0 1)` | ran (no return value, nothing visible changed) |

### set_draw_solid_density_surface

Python: `set_draw_solid_density_surface(imol, state)`  
Scheme: `(set-draw-solid-density-surface imol state)`

sets the density map of the given molecule to be drawn as a
 (transparent) solid surface.

Arguments: imol (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_draw_solid_density_surface(0, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-draw-solid-density-surface 0 1)` | ran (no return value, nothing visible changed) |

### set_flat_shading_for_solid_density_surface

Python: `set_flat_shading_for_solid_density_surface(state)`  
Scheme: `(set-flat-shading-for-solid-density-surface state)`

set the flag to do flat shading rather than smooth shading
 for solid density surface.

Default is 1 (on.

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_flat_shading_for_solid_density_surface(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-flat-shading-for-solid-density-surface 1)` | ran (no return value, nothing visible changed) |

### set_idle_function_rotate_angle

Python: `set_idle_function_rotate_angle(f)`  
Scheme: `(set-idle-function-rotate-angle f)`

how far should we rotate when (auto) spinning? Fast
 computer? set this to 0.1

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_idle_function_rotate_angle(1.0)` | ran (no return value); changed: idle_function_rotate_angle(): 0.15 -> 1 |
| Scheme | `(set-idle-function-rotate-angle 1.0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: idle_function_rotate_angle was 0.15000000596046448, set to 0.725, read back 0.7250000238418579; Scheme: idle-function-rotate-angle was 0.15000000596046448, set to 0.725, read back 0.7250000238418579.

### set_rocking_factors

Python: `set_rocking_factors(width_scale, frequency_scale)`  
Scheme: `(set-rocking-factors width-scale frequency-scale)`

Settings for the inevitable discontents who dislike the
 default rocking rates (defaults 1 and 1)

Arguments: width_scale (a number), frequency_scale (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_rocking_factors(1.0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-rocking-factors 1.0 1.0)` | ran (no return value, nothing visible changed) |

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
| Python | `set_solid_density_surface_opacity(0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-solid-density-surface-opacity 0 1.0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_solid_density_surface_opacity was -1.0, set to -1.0, read back -1.0; Scheme: get-solid-density-surface-opacity was -1.0, set to -1.0, read back -1.0.

### show_calculate_updating_maps_gui

Python: `show_calculate_updating_maps_gui()`  
Scheme: `(show-calculate-updating-maps-gui)`

show the updating maps gui

this function is called from callbacks.c and calls a python gui function

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_calculate_updating_maps_gui()` | ran (no return value, nothing visible changed) |
| Scheme | `(show-calculate-updating-maps-gui)` | ran (no return value, nothing visible changed) |

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
| Python | `start_graphics_interface()` | not run: starts the GTK main loop (blocks; for scripts run with --no-graphics that want the window); no answer in 60 s |
| Scheme | `(start-graphics-interface)` | not run: starts the GTK main loop (blocks; for scripts run with --no-graphics that want the window); no answer in 60 s |

Example written and checked by hand on the test data. Expected: opens the main window when Coot was started without graphics.

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

Example written and checked by hand on the test data. Expected: runs Coot's built-in developer tests; False here because they need the developer's test data (greg-data), which is not shipped.

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
| Python | `toggle_idle_rock_function()` | ran (no return value, nothing visible changed) |
| Scheme | `(toggle-idle-rock-function)` | ran (no return value, nothing visible changed) |

### toggle_idle_spin_function

Python: `toggle_idle_spin_function()`  
Scheme: `(toggle-idle-spin-function)`

Spin spin spin (or not)

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `toggle_idle_spin_function()` | ran (no return value, nothing visible changed) |
| Scheme | `(toggle-idle-spin-function)` | ran (no return value, nothing visible changed) |

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

