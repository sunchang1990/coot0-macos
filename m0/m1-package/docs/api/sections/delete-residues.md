# Delete Residues

[Scripting reference](../README.md) > Delete Residues (46 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### cis_peptides

Python: `cis_peptides(imol)`  
Scheme: `(cis-peptides imol)`

return cis_peptide info for imol.

Return a Python list object of [residue1, residue2, omega]

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `cis_peptides_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `cis_peptides(0)` | ran, returned `[[[True, 'A', 26, ''], [True, 'A', 27, ''], 6.120067119598389], [[True, 'A', 40, ''], [True, 'A', 41, ''], 47.1598320007 ...` |
| Scheme | `(cis-peptides 0)` | ran, returned `(((#t "A" 26 "") (#t "A" 27 "") 6.120067119598389) ((#t "A" 40 "") (#t "A" 41 "") 47.15983200073242) ((#t "B" 26 "") (#t ...` |

Python and Scheme gave the same answer.

### cis_trans_convert

Python: `cis_trans_convert(imol, chain_id, resno, altconf)`  
Scheme: `(cis-trans-convert imol chain-id resno altconf)`

Arguments: imol (a whole number), chain_id (text), resno (a whole number), altconf (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `cis_trans_convert(0, "A", 41, "")` | ran (no return value); changed: molecule 0: coordinates of 2 residue(s) (A41, A42) |
| Scheme | `(cis-trans-convert 0 "A" 41 "")` | ran (no return value); changed: molecule 0: coordinates of 2 residue(s) (A41, A42) |

### cis_trans_convert_intermediate_atoms

Python: `cis_trans_convert_intermediate_atoms()`  
Scheme: `(cis-trans-convert-intermediate-atoms)`

cis-trans convert the active residue of the active atom in the
 inermediate atoms, and continue with the refinement

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `refine_zone(0, "A", 41, 42, "")`, then `cis_trans_convert_intermediate_atoms()` | ran, returned `0` |
| Scheme | first `(refine-zone 0 "A" 41 42 "")`, then `(cis-trans-convert-intermediate-atoms)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: converts the peptide at the active residue of the intermediate atoms; 0 when there is no active intermediate peptide.

Note: Returned 0 headless; probably needs the active (centred) atom from the graphics window.

Python and Scheme gave the same answer.

### clear_delete_item_widget

Python: `clear_delete_item_widget()`  
Scheme: `(clear-delete-item-widget)`

for when we cancel with picking an atom

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_delete_item_widget()` | ran (no return value, nothing visible changed) |
| Scheme | `(clear-delete-item-widget)` | ran (no return value, nothing visible changed) |

### clear_pending_delete_item

Python: `clear_pending_delete_item()`  
Scheme: `(clear-pending-delete-item)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_pending_delete_item()` | ran (no return value, nothing visible changed) |
| Scheme | `(clear-pending-delete-item)` | ran (no return value, nothing visible changed) |

### delete_atom

Python: `delete_atom(imol, chain_id, resno, ins_code, at_name, altloc)`  
Scheme: `(delete-atom imol chain-id resno ins-code at-name altloc)`

delete atom in residue

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), at_name (text), altloc (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_atom(0, "A", 41, "", " CA ", "")` | ran (no return value); changed: molecule 0: atoms of 1 residue(s) (A41); n_atoms(0): 1465 -> 1464 |
| Scheme | `(delete-atom 0 "A" 41 "" " CA " "")` | ran (no return value); changed: molecule 0: atoms of 1 residue(s) (A41); n_atoms(0): 1465 -> 1464 |

### delete_atom_by_atom_index

Python: `delete_atom_by_atom_index(imol, index, do_delete_dialog)`  
Scheme: `(delete-atom-by-atom-index imol index do-delete-dialog)`

Arguments: imol (a whole number), index (a whole number), do_delete_dialog (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_atom_by_atom_index(0, 1, 1)` | ran (no return value); changed: molecule 0: atoms of 1 residue(s) (A1); n_atoms(0): 1465 -> 1464 |
| Scheme | `(delete-atom-by-atom-index 0 1 1)` | ran (no return value); changed: molecule 0: atoms of 1 residue(s) (A1); n_atoms(0): 1465 -> 1464 |

### delete_chain

Python: `delete_chain(imol, chain_id)`  
Scheme: `(delete-chain imol chain-id)`

delete the chain

Arguments: imol (a whole number), chain_id (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_chain(0, "A")` | ran (no return value); changed: molecule 0: deleted 93 residue(s) (A1, A2, A3, A4 ...); n_atoms(0): 1465 -> 745; n_chains(0): 2 -> 1; n_residues(0): 189 -> 96 |
| Scheme | `(delete-chain 0 "A")` | ran (no return value); changed: molecule 0: deleted 93 residue(s) (A1, A2, A3, A4 ...); n_atoms(0): 1465 -> 745; n_chains(0): 2 -> 1; n_residues(0): 189 -> 96 |

### delete_hydrogen_atoms

Python: `delete_hydrogen_atoms(imol)`  
Scheme: `(delete-hydrogen-atoms imol)`

delete all hydrogens in molecule,

 Returns number of hydrogens deleted.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `imol = get_monomer("ALA")`, then `delete_hydrogen_atoms(imol)` | ran, returned `7`; changed: molecule 3: atoms of 1 residue(s) (A1) |
| Scheme | `(delete-hydrogen-atoms (get-monomer "SER"))` | ran, returned `7`; changed: new molecule 3 (model, SER_from_dict); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the number of hydrogen atoms deleted (the dictionary monomer has 7).

Python and Scheme gave the same answer.

### delete_hydrogens

Python: `delete_hydrogens(imol)`  
Scheme: `(delete-hydrogens imol)`

delete all hydrogens in molecule,

 Returns number of hydrogens deleted.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_hydrogens(get_monomer("ALA"))` | ran, returned `7`; changed: new molecule 3 (model, ALA_from_dict); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | `(delete-hydrogens (get-monomer "SER"))` | ran, returned `7`; changed: new molecule 3 (model, SER_from_dict); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the number of hydrogen atoms deleted (same as delete_hydrogen_atoms).

Python and Scheme gave the same answer.

### delete_item_mode_is_atom_p

Python: `delete_item_mode_is_atom_p()`  
Scheme: `(delete-item-mode-is-atom-p)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_item_mode_is_atom_p()` | ran, returned `0` |
| Scheme | `(delete-item-mode-is-atom-p)` | ran, returned `0` |

Python and Scheme gave the same answer.

### delete_item_mode_is_chain_p

Python: `delete_item_mode_is_chain_p()`  
Scheme: `(delete-item-mode-is-chain-p)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_item_mode_is_chain_p()` | ran, returned `0` |
| Scheme | `(delete-item-mode-is-chain-p)` | ran, returned `0` |

Python and Scheme gave the same answer.

### delete_item_mode_is_residue_p

Python: `delete_item_mode_is_residue_p()`  
Scheme: `(delete-item-mode-is-residue-p)`

(predicate) a boolean

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_item_mode_is_residue_p()` | ran, returned `1` |
| Scheme | `(delete-item-mode-is-residue-p)` | ran, returned `1` |

Python and Scheme gave the same answer.

### delete_item_mode_is_sidechain_p

Python: `delete_item_mode_is_sidechain_p()`  
Scheme: `(delete-item-mode-is-sidechain-p)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_item_mode_is_sidechain_p()` | ran, returned `0` |
| Scheme | `(delete-item-mode-is-sidechain-p)` | ran, returned `0` |

Python and Scheme gave the same answer.

### delete_item_mode_is_sidechain_range_p

Python: `delete_item_mode_is_sidechain_range_p()`  
Scheme: `(delete-item-mode-is-sidechain-range-p)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_item_mode_is_sidechain_range_p()` | ran, returned `0` |
| Scheme | `(delete-item-mode-is-sidechain-range-p)` | ran, returned `0` |

Python and Scheme gave the same answer.

### delete_item_mode_is_water_p

Python: `delete_item_mode_is_water_p()`  
Scheme: `(delete-item-mode-is-water-p)`

predicate again

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_item_mode_is_water_p()` | ran, returned `0` |
| Scheme | `(delete-item-mode-is-water-p)` | ran, returned `0` |

Python and Scheme gave the same answer.

### delete_item_widget_is_being_shown

Python: `delete_item_widget_is_being_shown()`  
Scheme: `(delete-item-widget-is-being-shown)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_item_widget_is_being_shown()` | ran, returned `0` |
| Scheme | `(delete-item-widget-is-being-shown)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns 0: the Delete dialog is not open.

Python and Scheme gave the same answer.

### delete_item_widget_keep_active_on

Python: `delete_item_widget_keep_active_on()`  
Scheme: `(delete-item-widget-keep-active-on)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_item_widget_keep_active_on()` | ran, returned `0` |
| Scheme | `(delete-item-widget-keep-active-on)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns 0: the Delete dialog (and its 'keep active' check button) is not open.

Python and Scheme gave the same answer.

### delete_object_handle_delete_dialog

Python: `delete_object_handle_delete_dialog(do_delete_dialog)`  
Scheme: `(delete-object-handle-delete-dialog do-delete-dialog)`

utility function, moving widget work out of c-interface-build.cc

Arguments: do_delete_dialog (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_object_handle_delete_dialog(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(delete-object-handle-delete-dialog 1)` | ran (no return value, nothing visible changed) |

### delete_residue

Python: `delete_residue(imol, chain_id, resno, inscode)`  
Scheme: `(delete-residue imol chain-id resno inscode)`

delete residue

Arguments: imol (a whole number), chain_id (text), resno (a whole number), inscode (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_residue(0, "A", 41, "")` | ran (no return value); changed: molecule 0: deleted 1 residue(s) (A41); n_atoms(0): 1465 -> 1456; n_residues(0): 189 -> 188 |
| Scheme | `(delete-residue 0 "A" 41 "")` | ran (no return value); changed: molecule 0: deleted 1 residue(s) (A41); n_atoms(0): 1465 -> 1456; n_residues(0): 189 -> 188 |

### delete_residue_by_atom_index

Python: `delete_residue_by_atom_index(imol, index, do_delete_dialog)`  
Scheme: `(delete-residue-by-atom-index imol index do-delete-dialog)`

Arguments: imol (a whole number), index (a whole number), do_delete_dialog (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_residue_by_atom_index(0, 1, 1)` | ran (no return value); changed: molecule 0: deleted 1 residue(s) (A1); n_atoms(0): 1465 -> 1457; n_residues(0): 189 -> 188 |
| Scheme | `(delete-residue-by-atom-index 0 1 1)` | ran (no return value); changed: molecule 0: deleted 1 residue(s) (A1); n_atoms(0): 1465 -> 1457; n_residues(0): 189 -> 188 |

### delete_residue_hydrogens

Python: `delete_residue_hydrogens(imol, chain_id, resno, inscode, altloc)`  
Scheme: `(delete-residue-hydrogens imol chain-id resno inscode altloc)`

delete hydrogen atoms in residue

Arguments: imol (a whole number), chain_id (text), resno (a whole number), inscode (text), altloc (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_residue_hydrogens(0, "A", 41, "", "")` | ran (no return value, nothing visible changed) |
| Scheme | `(delete-residue-hydrogens 0 "A" 41 "" "")` | ran (no return value, nothing visible changed) |

### delete_residue_hydrogens_by_atom_index

Python: `delete_residue_hydrogens_by_atom_index(imol, index, do_delete_dialog)`  
Scheme: `(delete-residue-hydrogens-by-atom-index imol index do-delete-dialog)`

Arguments: imol (a whole number), index (a whole number), do_delete_dialog (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_residue_hydrogens_by_atom_index(0, 1, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(delete-residue-hydrogens-by-atom-index 0 1 1)` | ran (no return value, nothing visible changed) |

### delete_residue_range

Python: `delete_residue_range(imol, chain_id, resno_start, end_resno)`  
Scheme: `(delete-residue-range imol chain-id resno-start end-resno)`

delete residue range

Arguments: imol (a whole number), chain_id (text), resno_start (a whole number), end_resno (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_residue_range(0, "A", 41, 45)` | ran (no return value); changed: molecule 0: deleted 5 residue(s) (A41, A42, A43, A44 ...); n_atoms(0): 1465 -> 1428; n_residues(0): 189 -> 184 |
| Scheme | `(delete-residue-range 0 "A" 41 45)` | ran (no return value); changed: molecule 0: deleted 5 residue(s) (A41, A42, A43, A44 ...); n_atoms(0): 1465 -> 1428; n_residues(0): 189 -> 184 |

### delete_residue_sidechain

Python: `delete_residue_sidechain(imol, chain_id, resno, ins_code, do_delete_dialog)`  
Scheme: `(delete-residue-sidechain imol chain-id resno ins-code do-delete-dialog)`

delete all atoms in residue that are not main chain or CB

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), do_delete_dialog (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_residue_sidechain(0, "A", 41, "", 1)` | ran (no return value); changed: molecule 0: atoms of 1 residue(s) (A41); n_atoms(0): 1465 -> 1461 |
| Scheme | `(delete-residue-sidechain 0 "A" 41 "" 1)` | ran (no return value); changed: molecule 0: atoms of 1 residue(s) (A41); n_atoms(0): 1465 -> 1461 |

### delete_residue_with_full_spec

Python: `delete_residue_with_full_spec(imol, imodel, chain_id, resno, inscode, altloc)`  
Scheme: `(delete-residue-with-full-spec imol imodel chain-id resno inscode altloc)`

delete residue with altconf

Arguments: imol (a whole number), imodel (a whole number), chain_id (text), resno (a whole number), inscode (text), altloc (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_residue_with_full_spec(0, 1, "A", 41, "", "")` | ran (no return value); changed: molecule 0: deleted 1 residue(s) (A41); n_atoms(0): 1465 -> 1456; n_residues(0): 189 -> 188 |
| Scheme | `(delete-residue-with-full-spec 0 1 "A" 41 "" "")` | ran (no return value); changed: molecule 0: deleted 1 residue(s) (A41); n_atoms(0): 1465 -> 1456; n_residues(0): 189 -> 188 |

### delete_residues

Python: `delete_residues(imol, residue_specs_py)`  
Scheme: `(delete-residues imol residue-specs-scm)`

delete residues in the residue spec list

Arguments: imol (a whole number), residue_specs_py (a list or value). Returns: nothing.
Also available in Python as `delete_residues_py`.
Also available in Scheme as `delete-residues-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_residues(0, [["A", 41, ""], ["A", 42, ""]])` | ran (no return value); changed: molecule 0: deleted 2 residue(s) (A41, A42); n_atoms(0): 1465 -> 1450; n_residues(0): 189 -> 187 |
| Scheme | `(delete-residues 0 (list (list "A" 41 "") (list "A" 42 "")))` | ran (no return value); changed: molecule 0: deleted 2 residue(s) (A41, A42); n_atoms(0): 1465 -> 1450; n_residues(0): 189 -> 187 |

### delete_sidechains_for_chain

Python: `delete_sidechains_for_chain(imol, chain_id)`  
Scheme: `(delete-sidechains-for-chain imol chain-id)`

delete the side chains in the chain

Arguments: imol (a whole number), chain_id (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_sidechains_for_chain(0, "A")` | ran (no return value); changed: molecule 0: atoms of 78 residue(s) (A1, A2, A3, A5 ...); n_atoms(0): 1465 -> 1201 |
| Scheme | `(delete-sidechains-for-chain 0 "A")` | ran (no return value); changed: molecule 0: atoms of 78 residue(s) (A1, A2, A3, A5 ...); n_atoms(0): 1465 -> 1201 |

### delete_waters

Python: `delete_waters(imol)`  
Scheme: `(delete-waters imol)`

delete all waters in molecule,

 Returns number of waters deleted.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `imol = read_pdb("1ehz.pdb")`, then `delete_waters(imol)` | ran, returned `160`; changed: molecule 3: deleted 160 residue(s) (A101, A102, A103, A104 ...) |
| Scheme | `(delete-waters (read-pdb "1ehz.pdb"))` | ran, returned `160`; changed: new molecule 3 (model, 1ehz.pdb); rotation centre moved 51.0 A to (67.6, 49.7, 28.6); graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the number of waters deleted (tutorial-modern.pdb has none, 1ehz.pdb has 160).

Python and Scheme gave the same answer.

### do_cis_trans_conversion_setup

Python: `do_cis_trans_conversion_setup(istate)`  
Scheme: `(do-cis-trans-conversion-setup istate)`

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_cis_trans_conversion_setup(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(do-cis-trans-conversion-setup 1)` | ran (no return value, nothing visible changed) |

### do_rot_trans_setup

Python: `do_rot_trans_setup(state)`  
Scheme: `(do-rot-trans-setup state)`

sets flag for atom selection clicks

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_rot_trans_setup(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(do-rot-trans-setup 1)` | ran (no return value, nothing visible changed) |

### get_rot_trans_object_type

Python: `get_rot_trans_object_type()`  
Scheme: `(get-rot-trans-object-type)`

zone, chain, mol

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_rot_trans_object_type()` | ran, returned `12` |
| Scheme | `(get-rot-trans-object-type)` | ran, returned `12` |

Python and Scheme gave the same answer.

### post_delete_item_dialog

Python: `post_delete_item_dialog()`  
Scheme: `(post-delete-item-dialog)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `post_delete_item_dialog()` | not run: opens a dialog; needs the graphics window (stops Coot without a screen) |
| Scheme | `(post-delete-item-dialog)` | not run: opens a dialog; needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens the Delete item dialog.

### rot_trans_reset_previous

Python: `rot_trans_reset_previous()`  
Scheme: `(rot-trans-reset-previous)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `rot_trans_reset_previous()` | ran (no return value, nothing visible changed) |
| Scheme | `(rot-trans-reset-previous)` | ran (no return value, nothing visible changed) |

### set_delete_atom_mode

Python: `set_delete_atom_mode()`  
Scheme: `(set-delete-atom-mode)`

toggle callbacks

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_delete_atom_mode()` | ran (no return value, nothing visible changed) |
| Scheme | `(set-delete-atom-mode)` | ran (no return value, nothing visible changed) |

### set_delete_chain_mode

Python: `set_delete_chain_mode()`  
Scheme: `(set-delete-chain-mode)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_delete_chain_mode()` | ran (no return value, nothing visible changed) |
| Scheme | `(set-delete-chain-mode)` | ran (no return value, nothing visible changed) |

### set_delete_residue_hydrogens_mode

Python: `set_delete_residue_hydrogens_mode()`  
Scheme: `(set-delete-residue-hydrogens-mode)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_delete_residue_hydrogens_mode()` | ran (no return value, nothing visible changed) |
| Scheme | `(set-delete-residue-hydrogens-mode)` | ran (no return value, nothing visible changed) |

### set_delete_residue_mode

Python: `set_delete_residue_mode()`  
Scheme: `(set-delete-residue-mode)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_delete_residue_mode()` | ran (no return value, nothing visible changed) |
| Scheme | `(set-delete-residue-mode)` | ran (no return value, nothing visible changed) |

### set_delete_residue_zone_mode

Python: `set_delete_residue_zone_mode()`  
Scheme: `(set-delete-residue-zone-mode)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_delete_residue_zone_mode()` | ran (no return value, nothing visible changed) |
| Scheme | `(set-delete-residue-zone-mode)` | ran (no return value, nothing visible changed) |

### set_delete_sidechain_mode

Python: `set_delete_sidechain_mode()`  
Scheme: `(set-delete-sidechain-mode)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_delete_sidechain_mode()` | ran (no return value, nothing visible changed) |
| Scheme | `(set-delete-sidechain-mode)` | ran (no return value, nothing visible changed) |

### set_delete_sidechain_range_mode

Python: `set_delete_sidechain_range_mode()`  
Scheme: `(set-delete-sidechain-range-mode)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_delete_sidechain_range_mode()` | ran (no return value, nothing visible changed) |
| Scheme | `(set-delete-sidechain-range-mode)` | ran (no return value, nothing visible changed) |

### set_delete_water_mode

Python: `set_delete_water_mode()`  
Scheme: `(set-delete-water-mode)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_delete_water_mode()` | ran (no return value, nothing visible changed) |
| Scheme | `(set-delete-water-mode)` | ran (no return value, nothing visible changed) |

### set_rot_trans_object_type

Python: `set_rot_trans_object_type(rt_type)`  
Scheme: `(set-rot-trans-object-type rt-type)`

Arguments: rt_type (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_rot_trans_object_type(1)` | ran (no return value); changed: get_rot_trans_object_type(): 12 -> 1 |
| Scheme | `(set-rot-trans-object-type 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_rot_trans_object_type was 12, set to 0, read back 0; Scheme: get-rot-trans-object-type was 12, set to 0, read back 0.

### set_rotate_translate_zone_rotates_about_zone_centre

Python: `set_rotate_translate_zone_rotates_about_zone_centre(istate)`  
Scheme: `(set-rotate-translate-zone-rotates-about-zone-centre istate)`

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_rotate_translate_zone_rotates_about_zone_centre(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-rotate-translate-zone-rotates-about-zone-centre 1)` | ran (no return value, nothing visible changed) |

### store_delete_item_widget_position

Python: `store_delete_item_widget_position()`  
Scheme: `(store-delete-item-widget-position)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `store_delete_item_widget_position()` | not run: needs the Delete dialog open (stops Coot without a screen) |
| Scheme | `(store-delete-item-widget-position)` | not run: needs the Delete dialog open (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: remembers the position of the open Delete dialog.

### twisted_trans_peptides

Python: `twisted_trans_peptides(imol)`  
Scheme: `(twisted-trans-peptides imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `twisted_trans_peptides_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `twisted_trans_peptides(0)` | ran, returned `[[[True, 'A', 41, ''], [True, 'A', 42, ''], -134.07498676511048]]` |
| Scheme | `(twisted-trans-peptides 0)` | ran, returned `(((#t "A" 41 "") (#t "A" 42 "") -134.07498676511048))` |

Python and Scheme gave the same answer.

