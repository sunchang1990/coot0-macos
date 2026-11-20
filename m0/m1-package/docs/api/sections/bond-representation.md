# Bond Representation

[Scripting reference](../README.md) > Bond Representation (46 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### additional_representation_by_attributes

Python: `additional_representation_by_attributes(imol, chain_id, resno_start, resno_end, ins_code, representation_type, bonds_box_type, bond_width, draw_hydrogens_flag)`  
Scheme: `(additional-representation-by-attributes imol chain-id resno-start resno-end ins-code representation-type bonds-box-type bond-width draw-hydrogens-flag)`

return the index of the additional representation.
 Returns -1 on error.

Arguments: imol (a whole number), chain_id (text), resno_start (a whole number), resno_end (a whole number), ins_code (text), representation_type (a whole number), bonds_box_type (a whole number), bond_width (a number), draw_hydrogens_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `additional_representation_by_attributes(0, "A", 41, 45, "", 1, 1, 1.0, 1)` | ran, returned `0` |
| Scheme | `(additional-representation-by-attributes 0 "A" 41 45 "" 1 1 1.0 1)` | ran, returned `1` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### additional_representation_by_string

Python: `additional_representation_by_string(imol, atom_selection, representation_type, bonds_box_type, bond_width, draw_hydrogens_flag)`  
Scheme: `(additional-representation-by-string imol atom-selection representation-type bonds-box-type bond-width draw-hydrogens-flag)`

return the index of the additional representation. Return -1 on error

Arguments: imol (a whole number), atom_selection (text), representation_type (a whole number), bonds_box_type (a whole number), bond_width (a number), draw_hydrogens_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `additional_representation_by_string(0, "//A/41-45", 1, 1, 1.0, 1)` | ran, returned `2` |
| Scheme | `(additional-representation-by-string 0 "//A/41-45" 1 1 1.0 1)` | ran, returned `3` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### additional_representation_info

Python: `additional_representation_info(imol)`  
Scheme: `(additional-representation-info imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `additional_representation_info_py`.
Also available in Scheme as `additional-representation-info-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `additional_representation_info(0)` | ran, returned `[[0, 'Sticks: A 41-45', True, 1.0], [1, 'Sticks: A 41-45', True, 1.0], [2, 'Sticks: //A/41-45', True, 1.0], [3, 'Sticks: ...` |
| Scheme | `(additional-representation-info 0)` | ran, returned `((3 "Sticks: //A/41-45" #t 1.0) (2 "Sticks: //A/41-45" #t 1.0) (1 "Sticks: A 41-45" #t 1.0) (0 "Sticks: A 41-45" #t 1.0) ...` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### all_additional_representations_off_except

Python: `all_additional_representations_off_except(imol, representation_number, ball_and_sticks_off_too_flag)`  
Scheme: `(all-additional-representations-off-except imol representation-number ball-and-sticks-off-too-flag)`

undisplay all the additional representations for the given
 molecule, except the given representation number (if it is off, leave it off)

Arguments: imol (a whole number), representation_number (a whole number), ball_and_sticks_off_too_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `all_additional_representations_off_except(0, 1, 1)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(all-additional-representations-off-except 0 1 1)` | ran (no return value) |

### change_model_molecule_representation_mode

Python: `change_model_molecule_representation_mode(up_or_down)`  
Scheme: `(change-model-molecule-representation-mode up-or-down)`

change the representation of the model molecule closest to
 the centre of the screen

Arguments: up_or_down (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `change_model_molecule_representation_mode(1)` | ran (no return value) |
| Scheme | `(change-model-molecule-representation-mode 1)` | ran (no return value) |

### clear_ball_and_stick

Python: `clear_ball_and_stick(imol)`  
Scheme: `(clear-ball-and-stick imol)`

clear ball and stick representation of molecule number imol

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_ball_and_stick(0)` | ran, returned `0` |
| Scheme | `(clear-ball-and-stick 0)` | ran, returned `0` |

Python and Scheme gave the same answer.

### delete_additional_representation

Python: `delete_additional_representation(imol, representation_number)`  
Scheme: `(delete-additional-representation imol representation-number)`

delete a given additional representation

Arguments: imol (a whole number), representation_number (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_additional_representation(0, 1)` | ran (no return value) |
| Scheme | `(delete-additional-representation 0 1)` | ran (no return value) |

### draw_hydrogens_state

Python: `draw_hydrogens_state(imol)`  
Scheme: `(draw-hydrogens-state imol)`

the state of draw hydrogens for molecule number imol.

return -1 on bad imol.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `draw_hydrogens_state(0)` | ran, returned `1` |
| Scheme | `(draw-hydrogens-state 0)` | ran, returned `1` |

Python and Scheme gave the same answer.

### get_bond_colour_rotation_for_molecule

Python: `get_bond_colour_rotation_for_molecule(imol)`  
Scheme: `(get-bond-colour-rotation-for-molecule imol)`

get the bond colour for molecule.

Return -1 on err (bad molecule number)

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_bond_colour_rotation_for_molecule(0)` | ran, returned `21.0` |
| Scheme | `(get-bond-colour-rotation-for-molecule 0)` | ran, returned `21.0` |

Python and Scheme gave the same answer.

### get_default_bond_thickness

Python: `get_default_bond_thickness()`  
Scheme: `(get-default-bond-thickness)`

get the default thickness for bonds

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_default_bond_thickness()` | ran, returned `5` |
| Scheme | `(get-default-bond-thickness)` | ran, returned `5` |

Python and Scheme gave the same answer.

### graphics_molecule_bond_type

Python: `graphics_molecule_bond_type(imol)`  
Scheme: `(graphics-molecule-bond-type imol)`

what is the bond drawing state of molecule number imol

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_molecule_bond_type(0)` | ran, returned `1` |
| Scheme | `(graphics-molecule-bond-type 0)` | ran, returned `1` |

Python and Scheme gave the same answer.

### graphics_to_b_factor_cas_representation

Python: `graphics_to_b_factor_cas_representation(imol)`  
Scheme: `(graphics-to-b-factor-cas-representation imol)`

draw molecule number imol coloured by B-factor, CA + ligands

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_to_b_factor_cas_representation(0)` | ran (no return value) |
| Scheme | `(graphics-to-b-factor-cas-representation 0)` | ran (no return value) |

### graphics_to_b_factor_representation

Python: `graphics_to_b_factor_representation(imol)`  
Scheme: `(graphics-to-b-factor-representation imol)`

draw molecule number imol coloured by B-factor

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_to_b_factor_representation(0)` | ran (no return value) |
| Scheme | `(graphics-to-b-factor-representation 0)` | ran (no return value) |

### graphics_to_bonds_no_waters_representation

Python: `graphics_to_bonds_no_waters_representation(imol)`  
Scheme: `(graphics-to-bonds-no-waters-representation imol)`

draw molecule number imol with no waters

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_to_bonds_no_waters_representation(0)` | ran (no return value) |
| Scheme | `(graphics-to-bonds-no-waters-representation 0)` | ran (no return value) |

### graphics_to_bonds_representation

Python: `graphics_to_bonds_representation(mol)`  
Scheme: `(graphics-to-bonds-representation mol)`

draw molecule number imol with normal bonds

Arguments: mol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_to_bonds_representation(0)` | ran (no return value) |
| Scheme | `(graphics-to-bonds-representation 0)` | ran (no return value) |

### graphics_to_ca_plus_ligands_and_sidechains_representation

Python: `graphics_to_ca_plus_ligands_and_sidechains_representation(imol)`  
Scheme: `(graphics-to-ca-plus-ligands-and-sidechains-representation imol)`

draw molecule number imol as CA + ligands + sidechains

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_to_ca_plus_ligands_and_sidechains_representation(0)` | ran (no return value) |
| Scheme | `(graphics-to-ca-plus-ligands-and-sidechains-representation 0)` | ran (no return value) |

### graphics_to_ca_plus_ligands_representation

Python: `graphics_to_ca_plus_ligands_representation(imol)`  
Scheme: `(graphics-to-ca-plus-ligands-representation imol)`

draw molecule number imol as CA + ligands

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_to_ca_plus_ligands_representation(0)` | ran (no return value) |
| Scheme | `(graphics-to-ca-plus-ligands-representation 0)` | ran (no return value) |

### graphics_to_ca_plus_ligands_sec_struct_representation

Python: `graphics_to_ca_plus_ligands_sec_struct_representation(imol)`  
Scheme: `(graphics-to-ca-plus-ligands-sec-struct-representation imol)`

draw molecule number imol with CA bonds in secondary
 structure representation and ligands

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_to_ca_plus_ligands_sec_struct_representation(0)` | ran (no return value) |
| Scheme | `(graphics-to-ca-plus-ligands-sec-struct-representation 0)` | ran (no return value) |

### graphics_to_ca_representation

Python: `graphics_to_ca_representation(imol)`  
Scheme: `(graphics-to-ca-representation imol)`

draw molecule number imol as CAs

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_to_ca_representation(0)` | ran (no return value) |
| Scheme | `(graphics-to-ca-representation 0)` | ran (no return value) |

### graphics_to_occupancy_representation

Python: `graphics_to_occupancy_representation(imol)`  
Scheme: `(graphics-to-occupancy-representation imol)`

draw molecule number imol coloured by occupancy

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_to_occupancy_representation(0)` | ran (no return value) |
| Scheme | `(graphics-to-occupancy-representation 0)` | ran (no return value) |

### graphics_to_rainbow_representation

Python: `graphics_to_rainbow_representation(imol)`  
Scheme: `(graphics-to-rainbow-representation imol)`

draw molecule number imol in Jones' Rainbow

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_to_rainbow_representation(0)` | ran (no return value) |
| Scheme | `(graphics-to-rainbow-representation 0)` | ran (no return value) |

### graphics_to_sec_struct_bonds_representation

Python: `graphics_to_sec_struct_bonds_representation(imol)`  
Scheme: `(graphics-to-sec-struct-bonds-representation imol)`

draw molecule number imol with bonds in secondary structure
 representation

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_to_sec_struct_bonds_representation(0)` | ran (no return value) |
| Scheme | `(graphics-to-sec-struct-bonds-representation 0)` | ran (no return value) |

### graphics_to_user_defined_atom_colours_all_atoms_representation

Python: `graphics_to_user_defined_atom_colours_all_atoms_representation(imol)`  
Scheme: `(graphics-to-user-defined-atom-colours-all-atoms-representation imol)`

draw molecule number imol all atoms coloured by user-defined atom colours

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_to_user_defined_atom_colours_all_atoms_representation(0)` | ran (no return value) |
| Scheme | `(graphics-to-user-defined-atom-colours-all-atoms-representation 0)` | ran (no return value) |

### graphics_to_user_defined_atom_colours_representation

Python: `graphics_to_user_defined_atom_colours_representation(imol)`  
Scheme: `(graphics-to-user-defined-atom-colours-representation imol)`

draw molecule number imol in CA+Ligands mode coloured by user-defined atom colours

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `graphics_to_user_defined_atom_colours_representation(0)` | ran (no return value) |
| Scheme | `(graphics-to-user-defined-atom-colours-representation 0)` | ran (no return value) |

### make_ball_and_stick

Python: `make_ball_and_stick(imol, atom_selection_str, bond_thickness, sphere_size, do_spheres_flag)`  
Scheme: `(make-ball-and-stick imol atom-selection-str bond-thickness sphere-size do-spheres-flag)`

make a ball and stick representation of imol given atom selection

e.g. (make-ball-and-stick 0 "/1" 0.15 0.25 1)

Arguments: imol (a whole number), atom_selection_str (text), bond_thickness (a number), sphere_size (a number), do_spheres_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_ball_and_stick(0, "//A/41-45", 1.0, 1.0, 1)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(make-ball-and-stick 0 "//A/41-45" 1.0 1.0 1)` | stopped Coot when tried without a window (not checked with a window) |

### set_b_factor_bonds_scale_factor

Python: `set_b_factor_bonds_scale_factor(imol, f)`  
Scheme: `(set-b-factor-bonds-scale-factor imol f)`

scale the colours for colour by b factor representation

Arguments: imol (a whole number), f (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_b_factor_bonds_scale_factor(0, 1.0)` | ran, returned `1` |
| Scheme | `(set-b-factor-bonds-scale-factor 0 1.0)` | ran, returned `1` |

Python and Scheme gave the same answer.

### set_bond_colour_rotation_for_molecule

Python: `set_bond_colour_rotation_for_molecule(imol, f)`  
Scheme: `(set-bond-colour-rotation-for-molecule imol f)`

set bond colour for molecule

Arguments: imol (a whole number), f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_bond_colour_rotation_for_molecule(0, 1.0)` | ran (no return value) |
| Scheme | `(set-bond-colour-rotation-for-molecule 0 1.0)` | ran (no return value) |

### set_bond_thickness

Python: `set_bond_thickness(imol, t)`  
Scheme: `(set-bond-thickness imol t)`

set the thickness of the bonds in molecule number imol to t pixels

Arguments: imol (a whole number), t (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_bond_thickness(0, 1.0)` | ran (no return value) |
| Scheme | `(set-bond-thickness 0 1.0)` | ran (no return value) |

### set_bond_thickness_intermediate_atoms

Python: `set_bond_thickness_intermediate_atoms(t)`  
Scheme: `(set-bond-thickness-intermediate-atoms t)`

set the thickness of the bonds of the intermediate atoms to t pixels

Arguments: t (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_bond_thickness_intermediate_atoms(1.0)` | ran (no return value) |
| Scheme | `(set-bond-thickness-intermediate-atoms 1.0)` | ran (no return value) |

### set_default_bond_thickness

Python: `set_default_bond_thickness(t)`  
Scheme: `(set-default-bond-thickness t)`

set the default thickness for bonds (e.g. in ~/.coot)

Arguments: t (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_default_bond_thickness(1)` | ran (no return value) |
| Scheme | `(set-default-bond-thickness 1)` | ran (no return value) |

### set_default_representation_type

Python: `set_default_representation_type(type)`  
Scheme: `(set-default-representation-type type)`

set the default representation type (default 1).

Arguments: type (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_default_representation_type(1)` | ran (no return value) |
| Scheme | `(set-default-representation-type 1)` | ran (no return value) |

### set_draw_cis_peptide_markups

Python: `set_draw_cis_peptide_markups(status)`  
Scheme: `(set-draw-cis-peptide-markups status)`

set status of drawing cis-peptide markups

 default status is 1.

Arguments: status (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_draw_cis_peptide_markups(1)` | ran (no return value) |
| Scheme | `(set-draw-cis-peptide-markups 1)` | ran (no return value) |

### set_draw_hydrogens

Python: `set_draw_hydrogens(imol, istat)`  
Scheme: `(set-draw-hydrogens imol istat)`

set the hydrogen drawing state. istat = 0 is hydrogens off,
 istat = 1: show hydrogens

Arguments: imol (a whole number), istat (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_draw_hydrogens(0, 1)` | ran (no return value) |
| Scheme | `(set-draw-hydrogens 0 1)` | ran (no return value) |

### set_draw_missing_residues_loops

Python: `set_draw_missing_residues_loops(state)`  
Scheme: `(set-draw-missing-residues-loops state)`

set the state for drawing missing resiude loops

For taking screenshots, we often don't want to see them.

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_draw_missing_residues_loops(1)` | ran (no return value) |
| Scheme | `(set-draw-missing-residues-loops 1)` | ran (no return value) |

### set_draw_moving_atoms_restraints

Python: `set_draw_moving_atoms_restraints(state)`  
Scheme: `(set-draw-moving-atoms-restraints state)`

undocumented feature for development.

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_draw_moving_atoms_restraints(1)` | ran (no return value) |
| Scheme | `(set-draw-moving-atoms-restraints 1)` | ran (no return value) |

### set_draw_stick_mode_atoms

Python: `set_draw_stick_mode_atoms(imol, state)`  
Scheme: `(set-draw-stick-mode-atoms imol state)`

draw little coloured balls on atoms

turn off with state = 0

turn on with state = 1

Arguments: imol (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_draw_stick_mode_atoms(0, 1)` | ran (no return value) |
| Scheme | `(set-draw-stick-mode-atoms 0 1)` | ran (no return value) |

### set_draw_stick_mode_atoms_default

Python: `set_draw_stick_mode_atoms_default(state)`  
Scheme: `(set-draw-stick-mode-atoms-default state)`

set default for the drawing of atoms in stick mode (default is on (1))

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_draw_stick_mode_atoms_default(1)` | ran (no return value) |
| Scheme | `(set-draw-stick-mode-atoms-default 1)` | ran (no return value) |

### set_draw_zero_occ_markers

Python: `set_draw_zero_occ_markers(status)`  
Scheme: `(set-draw-zero-occ-markers status)`

set status of drawing zero occupancy markers.

 default status is 1.

Arguments: status (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_draw_zero_occ_markers(1)` | ran (no return value) |
| Scheme | `(set-draw-zero-occ-markers 1)` | ran (no return value) |

### set_flev_idle_ligand_interactions

Python: `set_flev_idle_ligand_interactions(state)`  
Scheme: `(set-flev-idle-ligand-interactions state)`

Turn on nice animated ligand interaction display.

turn on with arg 1.

turn off with arg 0.

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_flev_idle_ligand_interactions(1)` | ran (no return value) |
| Scheme | `(set-flev-idle-ligand-interactions 1)` | ran (no return value) |

### set_grey_carbon_colour

Python: `set_grey_carbon_colour(imol, r, g, b)`  
Scheme: `(set-grey-carbon-colour imol r g b)`

set the colour for the carbon atoms

can be not grey if you desire, r, g, b in the range 0 to 1.

Arguments: imol (a whole number), r (a number), g (a number), b (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_grey_carbon_colour(0, 0.5, 0.5, 0.5)` | ran (no return value) |
| Scheme | `(set-grey-carbon-colour 0 0.5 0.5 0.5)` | ran (no return value) |

### set_show_additional_representation

Python: `set_show_additional_representation(imol, representation_number, on_off_flag)`  
Scheme: `(set-show-additional-representation imol representation-number on-off-flag)`

display/undisplay the given additional representation

Arguments: imol (a whole number), representation_number (a whole number), on_off_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_additional_representation(0, 1, 1)` | ran (no return value) |
| Scheme | `(set-show-additional-representation 0 1 1)` | ran (no return value) |

### set_show_all_additional_representations

Python: `set_show_all_additional_representations(imol, on_off_flag)`  
Scheme: `(set-show-all-additional-representations imol on-off-flag)`

display/undisplay all the additional representations for the given molecule

Arguments: imol (a whole number), on_off_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_all_additional_representations(0, 1)` | ran (no return value) |
| Scheme | `(set-show-all-additional-representations 0 1)` | ran (no return value) |

### set_unbonded_atom_star_size

Python: `set_unbonded_atom_star_size(f)`  
Scheme: `(set-unbonded-atom-star-size f)`

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_unbonded_atom_star_size(1.0)` | ran (no return value) |
| Scheme | `(set-unbonded-atom-star-size 1.0)` | ran (no return value) |

### set_use_grey_carbons_for_molecule

Python: `set_use_grey_carbons_for_molecule(imol, state)`  
Scheme: `(set-use-grey-carbons-for-molecule imol state)`

make the carbon atoms for molecule imol be grey

Arguments: imol (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_use_grey_carbons_for_molecule(0, 1)` | ran (no return value) |
| Scheme | `(set-use-grey-carbons-for-molecule 0 1)` | ran (no return value) |

### set_use_variable_bond_thickness

Python: `set_use_variable_bond_thickness(state)`  
Scheme: `(set-use-variable-bond-thickness state)`

allow lines that are further away to be thinner

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_use_variable_bond_thickness(1)` | ran (no return value) |
| Scheme | `(set-use-variable-bond-thickness 1)` | ran (no return value) |

### toggle_idle_ligand_interactions

Python: `toggle_idle_ligand_interactions()`  
Scheme: `(toggle-flev-idle-ligand-interactions)`

Toggle for animated ligand interaction display above

Arguments: none. Returns: nothing.
Also available in Python as `toggle_flev_idle_ligand_interactions`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `toggle_idle_ligand_interactions()` | ran (no return value) |
| Scheme | `(toggle-flev-idle-ligand-interactions)` | ran (no return value) |

