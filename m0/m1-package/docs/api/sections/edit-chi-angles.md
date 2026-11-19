# Edit Chi Angles

[Scripting reference](../README.md) > Edit Chi Angles (12 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### edit_chi_angles

Python: `edit_chi_angles(imol, chain_id, resno, ins_code, altconf)`  
Scheme: `(edit-chi-angles imol chain-id resno ins-code altconf)`

display the edit chi angles gui for the given residue

 return a status of 0 if it failed to fined the residue,
 return a value of 1 if it worked.

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), altconf (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `edit_chi_angles(0, "A", 41, "", "")` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(edit-chi-angles 0 "A" 41 "" "")` | stopped Coot when tried without a window (not checked with a window) |

### rotate_chi

Python: `rotate_chi(am)`  
Scheme: `(rotate-chi am)`

Arguments: am (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `rotate_chi(1.0)` | not tried |
| Scheme | `(rotate-chi 1.0)` | not tried |

### set_edit_chi_angles_reverse_fragment_state

Python: `set_edit_chi_angles_reverse_fragment_state(istate)`  
Scheme: `(set-edit-chi-angles-reverse-fragment-state istate)`

a callback from the callbacks.c, setting the state of
 graphics_info_t::edit_chi_angles_reverse_fragment flag

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_edit_chi_angles_reverse_fragment_state(1)` | not tried |
| Scheme | `(set-edit-chi-angles-reverse-fragment-state 1)` | not tried |

### set_find_hydrogen_torsion

Python: `set_find_hydrogen_torsion(state)`  
Scheme: `(set-find-hydrogen-torsions state)`

show torsions that rotate hydrogens in the torsion angle
 manipulation dialog. Note that this may be needed if, in the
 dictionary cif file torsion which have as a 4th atom both a hydrogen
 and a heavier atom bonding to the 3rd atom, but list the 4th atom as
 a hydrogen (not a heavier atom).

Arguments: state (a whole number). Returns: nothing.
Also available in Python as `set_find_hydrogen_torsions`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_find_hydrogen_torsion(1)` | not tried |
| Scheme | `(set-find-hydrogen-torsions 1)` | not tried |

### set_graphics_edit_current_chi

Python: `set_graphics_edit_current_chi(ichi)`  
Scheme: `(set-graphics-edit-current-chi ichi)`

Arguments: ichi (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_graphics_edit_current_chi(1)` | not tried |
| Scheme | `(set-graphics-edit-current-chi 1)` | not tried |

### set_moving_atom_move_chis

Python: `set_moving_atom_move_chis()`  
Scheme: `(set-moving-atom-move-chis)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_moving_atom_move_chis()` | not tried |
| Scheme | `(set-moving-atom-move-chis)` | not tried |

### set_show_chi_angle_bond

Python: `set_show_chi_angle_bond(imode)`  
Scheme: `(set-show-chi-angle-bond imode)`

Arguments: imode (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_chi_angle_bond(1)` | not tried |
| Scheme | `(set-show-chi-angle-bond 1)` | not tried |

### setup_edit_chi_angles

Python: `setup_edit_chi_angles(state)`  
Scheme: `(setup-edit-chi-angles state)`

c-interface-build functions

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_edit_chi_angles(1)` | not tried |
| Scheme | `(setup-edit-chi-angles 1)` | not tried |

### setup_residue_partial_alt_locs

Python: `setup_residue_partial_alt_locs(state)`  
Scheme: `(setup-residue-partial-alt-locs state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_residue_partial_alt_locs(1)` | not tried |
| Scheme | `(setup-residue-partial-alt-locs 1)` | not tried |

### setup_torsion_general

Python: `setup_torsion_general(state)`  
Scheme: `(setup-torsion-general state)`

beloved torsion general at last makes an entrance onto the
 Coot scene...

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_torsion_general(1)` | not tried |
| Scheme | `(setup-torsion-general 1)` | not tried |

### toggle_torsion_general_reverse

Python: `toggle_torsion_general_reverse()`  
Scheme: `(toggle-torsion-general-reverse)`

No need for this to be exported to scripting

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `toggle_torsion_general_reverse()` | not tried |
| Scheme | `(toggle-torsion-general-reverse)` | not tried |

### unset_moving_atom_move_chis

Python: `unset_moving_atom_move_chis()`  
Scheme: `(unset-moving-atom-move-chis)`

button callback

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `unset_moving_atom_move_chis()` | not tried |
| Scheme | `(unset-moving-atom-move-chis)` | not tried |

