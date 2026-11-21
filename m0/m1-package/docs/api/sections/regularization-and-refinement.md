# Regularization and Refinement

[Scripting reference](../README.md) > Regularization and Refinement (113 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### accept_regularizement

Python: `accept_regularizement()`  
Scheme: `(accept-regularizement)`

a hideous alias for the above

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `accept_regularizement()` | ran (no return value, nothing visible changed) |
| Scheme | `(accept-regularizement)` | ran (no return value, nothing visible changed) |

### add_extra_angle_restraint

Python: `add_extra_angle_restraint(imol, chain_id_1, res_no_1, ins_code_1, atom_name_1, alt_conf_1, chain_id_2, res_no_2, ins_code_2, atom_name_2, alt_conf_2, chain_id_3, res_no_3, ins_code_3, atom_name_3, alt_conf_3, torsion_angle, esd)`  
Scheme: `(add-extra-angle-restraint imol chain-id-1 res-no-1 ins-code-1 atom-name-1 alt-conf-1 chain-id-2 res-no-2 ins-code-2 atom-name-2 alt-conf-2 chain-id-3 res-no-3 ins-code-3 atom-name-3 alt-conf-3 torsion-angle esd)`

Arguments: imol (a whole number), chain_id_1 (text), res_no_1 (a whole number), ins_code_1 (text), atom_name_1 (text), alt_conf_1 (text), chain_id_2 (text), res_no_2 (a whole number), ins_code_2 (text), atom_name_2 (text), alt_conf_2 (text), chain_id_3 (text), res_no_3 (a whole number), ins_code_3 (text), atom_name_3 (text), alt_conf_3 (text), torsion_angle (a number), esd (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_extra_angle_restraint(0, "A", 41, "", " N  ", "", "A", 41, "", " CA ", "", "A", 41, "", " C  ", "", 110.0, 2.0)` | ran, returned `0` |
| Scheme | `(add-extra-angle-restraint 0 "A" 41 "" " N  " "" "A" 41 "" " CA " "" "A" 41 "" " C  " "" 110.0 2.0)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: adds an angle restraint N-CA-C = 110 deg (esd 2) for A41 and returns its index.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### add_extra_bond_restraint

Python: `add_extra_bond_restraint(imol, chain_id_1, res_no_1, ins_code_1, atom_name_1, alt_conf_1, chain_id_2, res_no_2, ins_code_2, atom_name_2, alt_conf_2, bond_dist, esd)`  
Scheme: `(add-extra-bond-restraint imol chain-id-1 res-no-1 ins-code-1 atom-name-1 alt-conf-1 chain-id-2 res-no-2 ins-code-2 atom-name-2 alt-conf-2 bond-dist esd)`

add a user-define bond restraint

 this extra restraint is used when the given atoms are selected in
 refinement or regularization.

 Returns the index of the new restraint.

 Returns -1 when the atoms were not found and no extra bond
 restraint was stored.

Arguments: imol (a whole number), chain_id_1 (text), res_no_1 (a whole number), ins_code_1 (text), atom_name_1 (text), alt_conf_1 (text), chain_id_2 (text), res_no_2 (a whole number), ins_code_2 (text), atom_name_2 (text), alt_conf_2 (text), bond_dist (a number), esd (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_extra_bond_restraint(0, "A", 41, "", " CA ", "", "A", 45, "", " CA ", "", 9.5, 0.05)` | ran, returned `0` |
| Scheme | `(add-extra-bond-restraint 0 "A" 41 "" " CA " "" "A" 45 "" " CA " "" 9.5 0.05)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: adds a user bond restraint of 9.5 A between the two CA atoms and returns its index (-1 on failure).

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### add_extra_bond_restraints

Python: `add_extra_bond_restraints(imol, extra_bond_restraints_py)`  
Scheme: `(add-extra-bond-restraints imol extra-bond-restraints-scm)`

Arguments: imol (a whole number), extra_bond_restraints_py (a list or value). Returns: a whole number.
Also available in Python as `add_extra_bond_restraints_py`.
Also available in Scheme as `add-extra-bond-restraints-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_extra_bond_restraints(0, [["A", 42, "", " CA ", "", "A", 46, "", " CA ", "", 9.0, 0.05]])` | ran, returned `0` |
| Scheme | `(add-extra-bond-restraints 0 (list (list "A" 42 "" " CA " "" "A" 46 "" " CA " "" 9.0 0.05)))` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: adds one bond restraint per list item [chain1 res1 ins1 atom1 alt1 chain2 res2 ins2 atom2 alt2 dist esd]; returns 0.

Python and Scheme gave the same answer.

### add_extra_geman_mcclure_restraint

Python: `add_extra_geman_mcclure_restraint(imol, chain_id_1, res_no_1, ins_code_1, atom_name_1, alt_conf_1, chain_id_2, res_no_2, ins_code_2, atom_name_2, alt_conf_2, bond_dist, esd)`  
Scheme: `(add-extra-geman-mcclure-restraint imol chain-id-1 res-no-1 ins-code-1 atom-name-1 alt-conf-1 chain-id-2 res-no-2 ins-code-2 atom-name-2 alt-conf-2 bond-dist esd)`

add a user-define GM distance restraint

 this extra restraint is used when the given atoms are selected in
 refinement or regularization.

 Returns the index of the new restraint.

 Returns -1 when the atoms were not found and no extra bond
 restraint was stored.

Arguments: imol (a whole number), chain_id_1 (text), res_no_1 (a whole number), ins_code_1 (text), atom_name_1 (text), alt_conf_1 (text), chain_id_2 (text), res_no_2 (a whole number), ins_code_2 (text), atom_name_2 (text), alt_conf_2 (text), bond_dist (a number), esd (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_extra_geman_mcclure_restraint(0, "A", 41, "", " CA ", "", "A", 45, "", " CA ", "", 9.5, 0.05)` | ran, returned `0` |
| Scheme | `(add-extra-geman-mcclure-restraint 0 "A" 41 "" " CA " "" "A" 45 "" " CA " "" 9.5 0.05)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: adds a Geman-McClure distance restraint (robust to outliers) and returns its index.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### add_extra_start_pos_restraint

Python: `add_extra_start_pos_restraint(imol, chain_id_1, res_no_1, ins_code_1, atom_name_1, alt_conf_1, esd)`  
Scheme: `(add-extra-start-pos-restraint imol chain-id-1 res-no-1 ins-code-1 atom-name-1 alt-conf-1 esd)`

Arguments: imol (a whole number), chain_id_1 (text), res_no_1 (a whole number), ins_code_1 (text), atom_name_1 (text), alt_conf_1 (text), esd (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_extra_start_pos_restraint(0, "A", 41, "", " CA ", "", 0.1)` | ran, returned `0` |
| Scheme | `(add-extra-start-pos-restraint 0 "A" 41 "" " CA " "" 0.1)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: restrains A41 CA to its current position (esd 0.1 A); returns 0.

Python and Scheme gave the same answer.

### add_extra_target_position_restraint

Python: `add_extra_target_position_restraint(imol, chain_id, res_no, ins_code, atom_name, alt_conf, x, y, z, weight)`  
Scheme: `(add-extra-target-position-restraint imol chain-id res-no ins-code atom-name alt-conf x y z weight)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), atom_name (text), alt_conf (text), x (a number), y (a number), z (a number), weight (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_extra_target_position_restraint(0, "A", 41, "", " CA ", "", 54.5, 9.4, 12.3, 1.0)` | ran, returned `1` |
| Scheme | `(add-extra-target-position-restraint 0 "A" 41 "" " CA " "" 54.5 9.4 12.3 1.0)` | ran, returned `1` |

Python and Scheme gave the same answer.

### add_extra_torsion_restraint

Python: `add_extra_torsion_restraint(imol, chain_id_1, res_no_1, ins_code_1, atom_name_1, alt_conf_1, chain_id_2, res_no_2, ins_code_2, atom_name_2, alt_conf_2, chain_id_3, res_no_3, ins_code_3, atom_name_3, alt_conf_3, chain_id_4, res_no_4, ins_code_4, atom_name_4, alt_conf_4, torsion_angle, esd, period)`  
Scheme: `(add-extra-torsion-restraint imol chain-id-1 res-no-1 ins-code-1 atom-name-1 alt-conf-1 chain-id-2 res-no-2 ins-code-2 atom-name-2 alt-conf-2 chain-id-3 res-no-3 ins-code-3 atom-name-3 alt-conf-3 chain-id-4 res-no-4 ins-code-4 atom-name-4 alt-conf-4 torsion-angle esd period)`

Arguments: imol (a whole number), chain_id_1 (text), res_no_1 (a whole number), ins_code_1 (text), atom_name_1 (text), alt_conf_1 (text), chain_id_2 (text), res_no_2 (a whole number), ins_code_2 (text), atom_name_2 (text), alt_conf_2 (text), chain_id_3 (text), res_no_3 (a whole number), ins_code_3 (text), atom_name_3 (text), alt_conf_3 (text), chain_id_4 (text), res_no_4 (a whole number), ins_code_4 (text), atom_name_4 (text), alt_conf_4 (text), torsion_angle (a number), esd (a number), period (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_extra_torsion_restraint(0, "A", 41, "", " N  ", "", "A", 41, "", " CA ", "", "A", 41, "", " CB ", "", "A", 41, "", " CG ", "", 180.0, 10.0, 3)` | ran, returned `0` |
| Scheme | `(add-extra-torsion-restraint 0 "A" 41 "" " N  " "" "A" 41 "" " CA " "" "A" 41 "" " CB " "" "A" 41 "" " CG " "" 180.0 10.0 3)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: adds a chi1 torsion restraint (180, esd 10, period 3) on A41 and returns its index.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### add_initial_position_restraints

Python: `add_initial_position_restraints(imol, residue_specs, weight)`  
Scheme: `(add-initial-position-restraints imol residue-specs weight)`

\file
 Coot Scripting Interface - Refinement utilities

Arguments: imol (a whole number), residue_specs (a list), weight (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: adds position restraints for the atoms of the listed residues.

Note: SWIG exposes it but there is no list conversion; use add_extra_start_pos_restraint per atom

### add_omega_torsion_restriants

Python: `add_omega_torsion_restriants()`  
Scheme: `(add-omega-torsion-restriants)`

add restraints on the omega angle of the peptides

 (that is the torsion round the peptide bond). Omega angles that are
 closer to 0 than to 180 will be refined as cis peptides (and of
 course if omega is greater than 90 then the peptide will be refined
 as a trans peptide (this is the normal case).

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_omega_torsion_restriants()` | ran (no return value, nothing visible changed) |
| Scheme | `(add-omega-torsion-restriants)` | ran (no return value, nothing visible changed) |

### add_parallel_plane_restraint

Python: `add_parallel_plane_restraint(imol, chain_id_1, re_no_1, ins_code_1, chain_id_2, re_no_2, ins_code_2)`  
Scheme: `(add-parallel-plane-restraint imol chain-id-1 re-no-1 ins-code-1 chain-id-2 re-no-2 ins-code-2)`

Arguments: imol (a whole number), chain_id_1 (text), re_no_1 (a whole number), ins_code_1 (text), chain_id_2 (text), re_no_2 (a whole number), ins_code_2 (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_parallel_plane_restraint(0, "A", 1, "", "B", 1, "")` | ran (no return value, nothing visible changed) |
| Scheme | `(add-parallel-plane-restraint 0 "A" 1 "" "B" 1 "")` | ran (no return value, nothing visible changed) |

### add_planar_peptide_restraints

Python: `add_planar_peptide_restraints()`  
Scheme: `(add-planar-peptide-restraints)`

add a restraint on peptides to make them planar

 This adds a 5 atom restraint that includes both CA atoms of the
 peptide. Use this rather than editting the mon_lib_list.cif file.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_planar_peptide_restraints()` | ran (no return value, nothing visible changed) |
| Scheme | `(add-planar-peptide-restraints)` | ran (no return value, nothing visible changed) |

### add_refmac_extra_restraints

Python: `add_refmac_extra_restraints(imol, file_name)`  
Scheme: `(add-refmac-extra-restraints imol file-name)`

read in prosmart (typically) extra restraints

Arguments: imol (a whole number), file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `open("extra.txt", "w").write("EXTE DIST FIRST CHAIN A RESI 41 INS . ATOM CA SECOND CHAIN A RESI 45 INS . ATOM CA VALUE 9.5 SIGMA 0.05\n")`, then `add_refmac_extra_restraints(0, "extra.txt")` | ran (no return value, nothing visible changed) |
| Scheme | first `(call-with-output-file "extra.txt" (lambda (port) (display "EXTE DIST FIRST CHAIN A RESI 41 INS . ATOM CA SECOND CHAIN A RESI 45 INS . ATOM CA VALUE 9.5 SIGMA 0 ...`, then `(add-refmac-extra-restraints 0 "extra.txt")` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: reads ProSMART/Refmac 'EXTE DIST ...' lines into extra restraints of molecule 0 (shown by list_extra_restraints).

Note: each line needs the INS fields (24 words); without them nothing is read and no message tells the user

### c_accept_moving_atoms

Python: `c_accept_moving_atoms()`  
Scheme: `(c-accept-moving-atoms)`

accept the new positions of the regularized or refined residues

 If you are scripting refinement and/or regularization, this is the
 function that you need to call after refine-zone or regularize-zone.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `c_accept_moving_atoms()` | ran (no return value, nothing visible changed) |
| Scheme | `(c-accept-moving-atoms)` | ran (no return value, nothing visible changed) |

### check_chiral_volumes

Python: `check_chiral_volumes(imol)`  
Scheme: `(check-chiral-volumes imol)`

query the state of the above option

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `check_chiral_volumes(0)` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(check-chiral-volumes 0)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: checks the chiral centres of molecule 0 and shows the result in a dialog.

### chiral_volume_errors

Python: `chiral_volume_errors(imol)`  
Scheme: `(chiral-volume-errors imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `chiral_volume_errors_py`.
Also available in Scheme as `chiral-volume-errors-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `chiral_volume_errors(0)` | ran, returned `[[-1, 'A', 41, '', ' CA ', '']]` |
| Scheme | `(chiral-volume-errors 0)` | ran, returned `((-1 "A" 41 "" " CA " ""))` |

Python and Scheme gave the same answer.

### clear_all_atom_pull_restraints

Python: `clear_all_atom_pull_restraints()`  
Scheme: `(clear-all-atom-pull-restraints)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_all_atom_pull_restraints()` | ran (no return value, nothing visible changed) |
| Scheme | `(clear-all-atom-pull-restraints)` | ran (no return value, nothing visible changed) |

### clear_moving_atoms_object

Python: `clear_moving_atoms_object()`  
Scheme: `(clear-moving-atoms-object)`

remove the molecule and bonds

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_moving_atoms_object()` | ran (no return value, nothing visible changed) |
| Scheme | `(clear-moving-atoms-object)` | ran (no return value, nothing visible changed) |

### clear_up_moving_atoms

Python: `clear_up_moving_atoms()`  
Scheme: `(clear-up-moving-atoms)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_up_moving_atoms()` | ran (no return value, nothing visible changed) |
| Scheme | `(clear-up-moving-atoms)` | ran (no return value, nothing visible changed) |

### crankshaft_peptide_rotation_optimization_intermediate_atoms

Python: `crankshaft_peptide_rotation_optimization_intermediate_atoms()`  
Scheme: `(crankshaft-peptide-rotation-optimization-intermediate-atoms)`

functions used in callbacks.c

Arguments: none. Returns: `BEGIN_C_DECLS int`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `(refine_zone(0, "A", 41, 43, ""), crankshaft_peptide_rotation_optimization_intermediate_atoms())[1]` | ran, returned `1` |
| Scheme | `(begin (refine-zone 0 "A" 41 43 "") (crankshaft-peptide-rotation-optimization-intermediate-atoms))` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: runs the crankshaft peptide optimisation on the moving atoms; 1 if done, 0 when there are no moving atoms.

Python and Scheme gave the same answer.

### curlew

Python: `curlew()`  
Scheme: `(curlew)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `curlew()` | not run: needs the network and opens a window |
| Scheme | `(curlew)` | not run: needs the network and opens a window |

Example written and checked by hand on the test data. Expected: opens the Curlew extensions browser (downloads the list from the Coot web site).

### decrease_proportional_editing_radius

Python: `decrease_proportional_editing_radius()`  
Scheme: `(decrease-proportional-editing-radius)`

descrease the proportional editing radius

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `decrease_proportional_editing_radius()` | ran (no return value, nothing visible changed) |
| Scheme | `(decrease-proportional-editing-radius)` | ran (no return value, nothing visible changed) |

### delete_all_extra_restraints

Python: `delete_all_extra_restraints(imol)`  
Scheme: `(delete-all-extra-restraints imol)`

clear out all the extra/user-defined restraints for molecule number imol

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_all_extra_restraints(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(delete-all-extra-restraints 0)` | ran (no return value, nothing visible changed) |

### delete_extra_restraint

Python: `delete_extra_restraint(imol, restraint_spec)`  
Scheme: `(delete-extra-restraint imol restraint-spec)`

restraint_spec is something like ['bond', spec_1, spec_2]

 spec_1 and spec_2 do not have to be in the order that the bond was created.

Arguments: imol (a whole number), restraint_spec (a list or value). Returns: nothing.
Also available in Python as `delete_extra_restraint_py`.
Also available in Scheme as `delete-extra-restraint-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_extra_restraint(0, ["A", 41, ""])` | ran (no return value, nothing visible changed) |
| Scheme | `(delete-extra-restraint 0 (list "A" 41 ""))` | ran (no return value, nothing visible changed) |

### delete_extra_restraints_for_residue

Python: `delete_extra_restraints_for_residue(imol, chain_id, res_no, ins_code)`  
Scheme: `(delete-extra-restraints-for-residue imol chain-id res-no ins-code)`

clear out all the extra/user-defined restraints for this residue in molecule number imol

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_extra_restraints_for_residue(0, "A", 41, "")` | ran (no return value, nothing visible changed) |
| Scheme | `(delete-extra-restraints-for-residue 0 "A" 41 "")` | ran (no return value, nothing visible changed) |

### delete_extra_restraints_for_residue_spec

Python: `delete_extra_restraints_for_residue_spec(imol, residue_spec_in_py)`  
Scheme: `(delete-extra-restraints-for-residue-spec imol residue-spec-in)`

Arguments: imol (a whole number), residue_spec_in_py (a list or value). Returns: nothing.
Also available in Python as `delete_extra_restraints_for_residue_spec_py`.
Also available in Scheme as `delete-extra-restraints-for-residue-spec-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_extra_restraints_for_residue_spec(0, ["A", 41, ""])` | ran (no return value, nothing visible changed) |
| Scheme | `(delete-extra-restraints-for-residue-spec 0 (list "A" 41 ""))` | ran (no return value, nothing visible changed) |

### delete_extra_restraints_worse_than

Python: `delete_extra_restraints_worse_than(imol, n_sigma)`  
Scheme: `(delete-extra-restraints-worse-than imol n-sigma)`

Arguments: imol (a whole number), n_sigma (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_extra_restraints_worse_than(0, 1.5)` | ran (no return value, nothing visible changed) |
| Scheme | `(delete-extra-restraints-worse-than 0 1.5)` | ran (no return value, nothing visible changed) |

### delete_restraints

Python: `delete_restraints(comp_id)`  
Scheme: `(delete-restraints comp-id)`

delete the restraints for the given comp_id (i.e. residue name)

Returns success status (0 is failed, 1 is success)

Arguments: comp_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_restraints("ALA")` | ran, returned `1` |
| Scheme | `(delete-restraints "ALA")` | ran, returned `0` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### do_refine

Python: `do_refine(state)`  
Scheme: `(do-refine state)`

pass 0 for off (unclick togglebutton)

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_refine(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(do-refine 1)` | ran (no return value, nothing visible changed) |

### do_regularize

Python: `do_regularize(state)`  
Scheme: `(do-regularize state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_regularize(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(do-regularize 1)` | ran (no return value, nothing visible changed) |

### do_regularize_kill_delete_dialog

Python: `do_regularize_kill_delete_dialog()`  
Scheme: `(do-regularize-kill-delete-dialog)`

and a gui function used by those functions

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_regularize_kill_delete_dialog()` | ran (no return value, nothing visible changed) |
| Scheme | `(do-regularize-kill-delete-dialog)` | ran (no return value, nothing visible changed) |

### does_residue_exist_p

Python: `does_residue_exist_p(imol, chain_id, resno, inscode)`  
Scheme: `(does-residue-exist-p imol chain-id resno inscode)`

Does the residue exist? (Raw function)

 Returns 0 on not-exist, 1 on does exist.

Arguments: imol (a whole number), chain_id (text), resno (a whole number), inscode (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `does_residue_exist_p(0, "A", 41, "")` | ran, returned `1` |
| Scheme | `(does-residue-exist-p 0 "A" 41 "")` | ran, returned `1` |

Python and Scheme gave the same answer.

### dragged_refinement_steps_per_frame

Python: `dragged_refinement_steps_per_frame()`  
Scheme: `(dragged-refinement-steps-per-frame)`

return the number of steps per frame in dragged refinement

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `dragged_refinement_steps_per_frame()` | ran, returned `10` |
| Scheme | `(dragged-refinement-steps-per-frame)` | ran, returned `10` |

Python and Scheme gave the same answer.

### estimate_map_weight

Python: `estimate_map_weight(imol_map)`  
Scheme: `(estimate-map-weight imol-map)`

Arguments: imol_map (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `estimate_map_weight(1)` | ran, returned `40.161048889160156` |
| Scheme | `(estimate-map-weight 1)` | ran, returned `40.161048889160156` |

Python and Scheme gave the same answer.

### extra_restraints_are_shown

Python: `extra_restraints_are_shown(imol)`  
Scheme: `(extra-restraints-are-shown imol)`

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `extra_restraints_are_shown(0)` | ran, returned `1` |
| Scheme | `(extra-restraints-are-shown 0)` | ran, returned `1` |

Python and Scheme gave the same answer.

### generate_local_self_restraints

Python: `generate_local_self_restraints(imol, chain_id, local_dist_max)`  
Scheme: `(generate-local-self-restraints imol chain-id local-dist-max)`

generate external distance local self restraints

Arguments: imol (a whole number), chain_id (text), local_dist_max (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `generate_local_self_restraints(0, "A", 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(generate-local-self-restraints 0 "A" 1.0)` | ran (no return value, nothing visible changed) |

### generate_local_self_restraints_by_residues

Python: `generate_local_self_restraints_by_residues(imol, residue_specs, local_dist_max)`  
Scheme: `(generate-local-self-restraints-by-residues imol residue-specs local-dist-max)`

Arguments: imol (a whole number), residue_specs (a list or value), local_dist_max (a number). Returns: nothing.
Also available in Python as `generate_local_self_restraints_by_residues_py`.
Also available in Scheme as `generate-local-self-restraints-by-residues-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `generate_local_self_restraints_by_residues(0, [["A", 41, ""], ["A", 42, ""]], 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(generate-local-self-restraints-by-residues 0 (list (list "A" 41 "") (list "A" 42 "")) 1.0)` | ran (no return value, nothing visible changed) |

### generate_self_restraints

Python: `generate_self_restraints(imol, local_dist_max)`  
Scheme: `(generate-self-restraints imol local-dist-max)`

generate external distance all-molecule self restraints

Arguments: imol (a whole number), local_dist_max (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `generate_self_restraints(0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(generate-self-restraints 0 1.0)` | ran (no return value, nothing visible changed) |

### get_auto_clear_atom_pull_restraint_state

Python: `get_auto_clear_atom_pull_restraint_state()`  
Scheme: `(get-auto-clear-atom-pull-restraint-state)`

get auto-clear atom pull restraint state

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_auto_clear_atom_pull_restraint_state()` | ran, returned `1` |
| Scheme | `(get-auto-clear-atom-pull-restraint-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### get_map_weight

Python: `get_map_weight()`  
Scheme: `(get-map-weight)`

return the relative weight of the geometric terms to the map terms.

A more sensible name for the matrix_state() function)

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_map_weight()` | ran, returned `60.0` |
| Scheme | `(get-map-weight)` | ran, returned `60.0` |

Python and Scheme gave the same answer.

### imol_refinement_map

Python: `imol_refinement_map()`  
Scheme: `(imol-refinement-map)`

the molecule number of the map used for refinement

 Returns the map number, if it has been set or there is only one
 map, return -1 on no map set (ambiguous) or no maps.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `imol_refinement_map()` | ran, returned `1` |
| Scheme | `(imol-refinement-map)` | ran, returned `1` |

Python and Scheme gave the same answer.

### increase_proportional_editing_radius

Python: `increase_proportional_editing_radius()`  
Scheme: `(increase-proportional-editing-radius)`

iscrease the proportional editing radius

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `increase_proportional_editing_radius()` | ran (no return value, nothing visible changed) |
| Scheme | `(increase-proportional-editing-radius)` | ran (no return value, nothing visible changed) |

### list_extra_restraints

Python: `list_extra_restraints(imol)`  
Scheme: `(list-extra-restraints imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `list_extra_restraints_py`.
Also available in Scheme as `list-extra-restraints-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `add_extra_bond_restraint(0, "A", 41, "", " CA ", "", "A", 45, "", " CA ", "", 9.5, 0.05)`, then `list_extra_restraints(0)` | ran, returned `[['bond', [295, 'A', 41, '', ' CA ', ''], [325, 'A', 45, '', ' CA ', ''], 9.5, 0.05]]` |
| Scheme | first `(add-extra-bond-restraint 0 "A" 41 "" " CA " "" "A" 45 "" " CA " "" 9.5 0.05)`, then `(list-extra-restraints 0)` | ran, returned `((bond (295 "A" 41 "" " CA " "") (325 "A" 45 "" " CA " "") 9.5 0.05) (bond (295 "A" 41 "" " CA " "") (325 "A" 45 "" " CA ...` |

Example written and checked by hand on the test data. Expected: returns the extra restraints of molecule 0 (type, atom specs with atom index, target, esd); False if there are none.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### make_tight_planar_peptide_restraints

Python: `make_tight_planar_peptide_restraints()`  
Scheme: `(make-tight-planar-peptide-restraints)`

make the planar peptide restraints tight

Useful when refining models with cryo-EM maps

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_tight_planar_peptide_restraints()` | ran (no return value, nothing visible changed) |
| Scheme | `(make-tight-planar-peptide-restraints)` | ran (no return value, nothing visible changed) |

### matrix_state

Python: `matrix_state()`  
Scheme: `(matrix-state)`

return the relative weight of the geometric terms to the map terms.

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `matrix_state()` | ran, returned `60.0` |
| Scheme | `(matrix-state)` | ran, returned `60.0` |

Python and Scheme gave the same answer.

### parallel_plane_restraints_are_shown

Python: `parallel_plane_restraints_are_shown(imol)`  
Scheme: `(parallel-plane-restraints-are-shown imol)`

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `parallel_plane_restraints_are_shown(0)` | ran, returned `0` |
| Scheme | `(parallel-plane-restraints-are-shown 0)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns 1 if parallel-plane extra restraints of molecule 0 are drawn, else 0 (default).

Python and Scheme gave the same answer.

### planar_peptide_restraints_state

Python: `planar_peptide_restraints_state()`  
Scheme: `(planar-peptide-restraints-state)`

return 1 if planar peptide restraints are on, 0 if off

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `planar_peptide_restraints_state()` | ran, returned `1` |
| Scheme | `(planar-peptide-restraints-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### refine_auto_range

Python: `refine_auto_range(imol, chain_id, resno1, altconf)`  
Scheme: `(refine-auto-range imol chain-id resno1 altconf)`

refine a zone using auto-range

 presumes that imol_Refinement_Map has been set

Arguments: imol (a whole number), chain_id (text), resno1 (a whole number), altconf (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_auto_range(0, "A", 41, "")` | ran (no return value, nothing visible changed) |
| Scheme | `(refine-auto-range 0 "A" 41 "")` | ran (no return value, nothing visible changed) |

### refine_ramachandran_angles_state

Python: `refine_ramachandran_angles_state()`  
Scheme: `(refine-ramachandran-angles-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_ramachandran_angles_state()` | ran, returned `0` |
| Scheme | `(refine-ramachandran-angles-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### refine_ramachandran_restraints_weight

Python: `refine_ramachandran_restraints_weight()`  
Scheme: `(refine-ramachandran-restraints-weight)`

ramachandran restraints weight

Returns weight as a float

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_ramachandran_restraints_weight()` | ran, returned `40.0` |
| Scheme | `(refine-ramachandran-restraints-weight)` | ran, returned `40.0` |

Python and Scheme gave the same answer.

### refine_residues

Python: `refine_residues(imol, r)`  
Scheme: `(refine-residues imol r)`

refine the residues in the given residue spec list

Returns the refinement summary statistics

Arguments: imol (a whole number), r (a list or value). Returns: a value (see the result of the example).
Also available in Python as `refine_residues_py`.
Also available in Scheme as `refine-residues-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_residues(0, [["A", 41, ""], ["A", 42, ""]])` | ran, returned `['', -2, False]` |
| Scheme | `(refine-residues 0 (list (list "A" 41 "") (list "A" 42 "")))` | ran, returned `("" -2 ())` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### refine_residues_with_alt_conf

Python: `refine_residues_with_alt_conf(imol, r, alt_conf)`  
Scheme: `(refine-residues-with-alt-conf imol r alt-conf)`

Arguments: imol (a whole number), r (a list or value), alt_conf (text). Returns: a value (see the result of the example).
Also available in Python as `refine_residues_with_alt_conf_py`.
Also available in Scheme as `refine-residues-with-alt-conf-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_residues_with_alt_conf(0, [["A", 41, ""], ["A", 42, ""]], "")` | ran, returned `['', -2, False]` |
| Scheme | `(refine-residues-with-alt-conf 0 (list (list "A" 41 "") (list "A" 42 "")) "")` | ran, returned `("" -2 ())` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### refine_residues_with_modes_with_alt_conf

Python: `refine_residues_with_modes_with_alt_conf(imol, r, alt_conf, mode_1, mode_2, mode_3)`  
Scheme: `(refine-residues-with-modes-with-alt-conf-scm imol residues-spec-list-scm alt-conf mode-1 mode-2 mode-3)`

presumes the alt_conf is "".

Arguments: imol (a whole number), r (a list or value), alt_conf (text), mode_1 (a list or value), mode_2 (a list or value), mode_3 (a list or value). Returns: a value (see the result of the example).
Also available in Python as `refine_residues_with_modes_with_alt_conf_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_residues_with_modes_with_alt_conf(0, [["A", 41, ""], ["A", 42, ""]], "", None, None, None)` | ran, returned `['', -2, False]` |
| Scheme | `(refine-residues-with-modes-with-alt-conf-scm 0 (list (list "A" 41 "") (list "A" 42 "")) "" #f #f #f)` | ran, returned `("" -2 ())` |

Example written and checked by hand on the test data. Expected: refines the listed residues (alt conf '') with optional modes; returns the refinement summary [message, status, scores].

Note: status -2 and no movement with mode None/#f: the mode values Coot expects are not documented; treat as unverified

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### refine_with_torsion_restraints_state

Python: `refine_with_torsion_restraints_state()`  
Scheme: `(refine-with-torsion-restraints-state)`

return the state of above

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_with_torsion_restraints_state()` | ran, returned `0` |
| Scheme | `(refine-with-torsion-restraints-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### refine_zone

Python: `refine_zone(imol, chain_id, resno1, resno2, altconf)`  
Scheme: `(refine-zone imol chain-id resno1 resno2 altconf)`

refine a zone

 presumes that imol_Refinement_Map has been set

Arguments: imol (a whole number), chain_id (text), resno1 (a whole number), resno2 (a whole number), altconf (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_zone(0, "A", 41, 45, "")` | ran (no return value, nothing visible changed) |
| Scheme | `(refine-zone 0 "A" 41 45 "")` | ran (no return value, nothing visible changed) |

### refine_zone_atom_index_define

Python: `refine_zone_atom_index_define(imol, ind1, ind2)`  
Scheme: `(refine-zone-atom-index-define imol ind1 ind2)`

refine a zone based on atom indexing

Arguments: imol (a whole number), ind1 (a whole number), ind2 (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_zone_atom_index_define(0, 1, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(refine-zone-atom-index-define 0 1 1)` | ran (no return value, nothing visible changed) |

### refine_zone_with_score

Python: `refine_zone_with_score(imol, chain_id, resno1, resno2, altconf)`  
Scheme: `(refine-zone-with-score imol chain-id resno1 resno2 altconf)`

Arguments: imol (a whole number), chain_id (text), resno1 (a whole number), resno2 (a whole number), altconf (text). Returns: a value (see the result of the example).
Also available in Python as `refine_zone_with_score_py`.
Also available in Scheme as `refine-zone-with-score-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_zone_with_score(0, "A", 41, 45, "")` | ran, returned `['', -2, False]` |
| Scheme | `(refine-zone-with-score 0 "A" 41 45 "")` | ran, returned `("" -2 ())` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### refinement_already_ongoing_p

Python: `refinement_already_ongoing_p()`  
Scheme: `(refinement-already-ongoing-p)`

If there is a refinement on-going already, we don't want to start a new one

The is the means to ask if that is the case. This needs a scheme wrapper to provide refinement-already-ongoing?
The question is translated to "are the intermediate atoms being displayed?" so that might be a more
accurate function name than the current one.

Returns 1 for yes, 0 for no.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refinement_already_ongoing_p()` | ran, returned `0` |
| Scheme | `(refinement-already-ongoing-p)` | ran, returned `0` |

Python and Scheme gave the same answer.

### refinement_immediate_replacement_state

Python: `refinement_immediate_replacement_state()`  
Scheme: `(refinement-immediate-replacement-state)`

query the state of the immediate replacement mode

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refinement_immediate_replacement_state()` | ran, returned `0` |
| Scheme | `(refinement-immediate-replacement-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### refinement_refine_per_frame_state

Python: `refinement_refine_per_frame_state()`  
Scheme: `(refinement-refine-per-frame-state)`

query the state of the above option

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refinement_refine_per_frame_state()` | ran, returned `0` |
| Scheme | `(refinement-refine-per-frame-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### regularize_residues_with_alt_conf

Python: `regularize_residues_with_alt_conf(imol, r, alt_conf)`  
Scheme: `(regularize-residues-with-alt-conf-scm imol r alt-conf)`

presumes the alt_conf is "".

Arguments: imol (a whole number), r (a list or value), alt_conf (text). Returns: a value (see the result of the example).
Also available in Python as `regularize_residues_with_alt_conf_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `regularize_residues_with_alt_conf(0, [["A", 41, ""], ["A", 42, ""]], "")` | ran, returned `['', -2, False]` |
| Scheme | `(regularize-residues-with-alt-conf-scm 0 (list (list "A" 41 "") (list "A" 42 "")) "")` | ran, returned `("" -2 ())` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### regularize_zone

Python: `regularize_zone(imol, chain_id, resno1, resno2, altconf)`  
Scheme: `(regularize-zone imol chain-id resno1 resno2 altconf)`

regularize a zone

Returns a status, whether the regularisation was done or not. 0 for no, 1 for yes.

Arguments: imol (a whole number), chain_id (text), resno1 (a whole number), resno2 (a whole number), altconf (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `regularize_zone(0, "A", 41, 45, "")` | ran, returned `1` |
| Scheme | `(regularize-zone 0 "A" 41 45 "")` | ran, returned `1` |

Python and Scheme gave the same answer.

### regularize_zone_with_score

Python: `regularize_zone_with_score(imol, chain_id, resno1, resno2, altconf)`  
Scheme: `(regularize-zone-with-score imol chain-id resno1 resno2 altconf)`

Arguments: imol (a whole number), chain_id (text), resno1 (a whole number), resno2 (a whole number), altconf (text). Returns: a value (see the result of the example).
Also available in Python as `regularize_zone_with_score_py`.
Also available in Scheme as `regularize-zone-with-score-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `regularize_zone_with_score(0, "A", 41, 45, "")` | ran, returned `['', -2, False]` |
| Scheme | `(regularize-zone-with-score 0 "A" 41 45 "")` | ran, returned `("" -2 ())` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### remove_initial_position_restraints

Python: `remove_initial_position_restraints(imol, residue_specs)`  
Scheme: `(remove-initial-position-restraints imol residue-specs)`

this removed all initial position restraints, not just those listed.

Arguments: imol (a whole number), residue_specs (a list). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: removes all initial-position restraints of the molecule.

### remove_omega_torsion_restriants

Python: `remove_omega_torsion_restriants()`  
Scheme: `(remove-omega-torsion-restriants)`

remove omega restraints on CIS and TRANS linked residues.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_omega_torsion_restriants()` | ran (no return value, nothing visible changed) |
| Scheme | `(remove-omega-torsion-restriants)` | ran (no return value, nothing visible changed) |

### remove_planar_peptide_restraints

Python: `remove_planar_peptide_restraints()`  
Scheme: `(remove-planar-peptide-restraints)`

remove restraints on peptides to make them planar.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_planar_peptide_restraints()` | ran (no return value); changed: planar_peptide_restraints_state(): 1 -> 0 |
| Scheme | `(remove-planar-peptide-restraints)` | ran (no return value, nothing visible changed) |

### repeat_refine_zone

Python: `repeat_refine_zone()`  
Scheme: `(repeat-refine-zone)`

repeat the previous (user-selected) refine zone

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `repeat_refine_zone()` | ran (no return value, nothing visible changed) |
| Scheme | `(repeat-refine-zone)` | ran (no return value, nothing visible changed) |

### secondary_structure_restraints_type

Python: `secondary_structure_restraints_type()`  
Scheme: `(secondary-structure-restraints-type)`

return the secondary structure restraints type

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `secondary_structure_restraints_type()` | ran, returned `0` |
| Scheme | `(secondary-structure-restraints-type)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns the secondary structure restraints type (0 = none, 1 = alpha helix, 2 = beta strand).

Python and Scheme gave the same answer.

### set_auto_clear_atom_pull_restraint

Python: `set_auto_clear_atom_pull_restraint(state)`  
Scheme: `(set-auto-clear-atom-pull-restraint state)`

set auto-clear atom pull restraint

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_auto_clear_atom_pull_restraint(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-auto-clear-atom-pull-restraint 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_auto_clear_atom_pull_restraint_state was 1, set to 0, read back 0; Scheme: get-auto-clear-atom-pull-restraint-state was 1, set to 0, read back 0.

### set_debug_refinement

Python: `set_debug_refinement(state)`  
Scheme: `(set-debug-refinement state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_debug_refinement(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-debug-refinement 1)` | ran (no return value, nothing visible changed) |

### set_dragged_refinement_steps_per_frame

Python: `set_dragged_refinement_steps_per_frame(v)`  
Scheme: `(set-dragged-refinement-steps-per-frame v)`

set the number of refinement steps applied to the
 intermediate atoms each frame of graphics.

 smaller numbers make the movement of the intermediate atoms slower,
 smoother, more elegant.

 Default: 80.

Arguments: v (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_dragged_refinement_steps_per_frame(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-dragged-refinement-steps-per-frame 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: dragged_refinement_steps_per_frame was 10, set to 0, read back 0; Scheme: dragged-refinement-steps-per-frame was 10, set to 0, read back 0.

### set_extra_restraints_prosmart_sigma_limits

Python: `set_extra_restraints_prosmart_sigma_limits(imol, limit_high, limit_low)`  
Scheme: `(set-extra-restraints-prosmart-sigma-limits imol limit-high limit-low)`

often we don't want to see all prosmart restraints, just the (big) violations

Arguments: imol (a whole number), limit_high (a number), limit_low (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_extra_restraints_prosmart_sigma_limits(0, 1.0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-extra-restraints-prosmart-sigma-limits 0 1.0 1.0)` | ran (no return value, nothing visible changed) |

### set_extra_restraints_representation_for_bonds_go_to_CA

Python: `set_extra_restraints_representation_for_bonds_go_to_CA(imol, state)`  
Scheme: `(set-extra-restraints-representation-for-bonds-go-to-CA imol state)`

Arguments: imol (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_extra_restraints_representation_for_bonds_go_to_CA(0, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-extra-restraints-representation-for-bonds-go-to-CA 0 1)` | ran (no return value, nothing visible changed) |

### set_fix_chiral_volumes_before_refinement

Python: `set_fix_chiral_volumes_before_refinement(istate)`  
Scheme: `(set-fix-chiral-volumes-before-refinement istate)`

correct the sign of chiral volumes before commencing refinement?

 Do we want to fix chiral volumes (by moving the chiral atom to the
 other side of the chiral plane if necessary). Default yes
 (1). Note: doesn't work currently.

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_fix_chiral_volumes_before_refinement(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-fix-chiral-volumes-before-refinement 1)` | ran (no return value, nothing visible changed) |

### set_imol_refinement_map

Python: `set_imol_refinement_map(imol)`  
Scheme: `(set-imol-refinement-map imol)`

set the molecule number of the map to be used for
 refinement/fitting.

 Returns imol on success, -1 on failure

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_imol_refinement_map(1)` | ran, returned `1` |
| Scheme | `(set-imol-refinement-map 1)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: sets the map used for refinement; returns the map molecule number, -1 if it is not a map.

Setting checked (set to another value and read back, then put back; NOT all read back): Python: imol_refinement_map was 1, set to 0, read back 1 (not taken); Scheme: imol-refinement-map was 1, set to 0, read back 1 (not taken).

Python and Scheme gave the same answer.

### set_matrix

Python: `set_matrix(f)`  
Scheme: `(set-matrix f)`

set the relative weight of the geometric terms to the map terms

 The default is 60.

 The higher the number the more weight that is given to the map terms
 but the resulting chi squared values are higher). This will be
 needed for maps generated from data not on (or close to) the absolute
 scale or maps that have been scaled (for example so that the sigma
 level has been scaled to 1.0).

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_matrix(1.0)` | ran (no return value); changed: get_map_weight(): 60 -> 1; matrix_state(): 60 -> 1 |
| Scheme | `(set-matrix 1.0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: matrix_state was 60.0, set to 90.5, read back 90.5; Scheme: matrix-state was 60.0, set to 90.5, read back 90.5.

### set_numerical_gradients

Python: `set_numerical_gradients(istate)`  
Scheme: `(set-numerical-gradients istate)`

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_numerical_gradients(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-numerical-gradients 1)` | ran (no return value, nothing visible changed) |

### set_refine_auto_range_step

Python: `set_refine_auto_range_step(i)`  
Scheme: `(set-refine-auto-range-step i)`

change the +/- step for autoranging (default is 1)

Auto-ranging alow you to select a range from one button press, this
allows you to set the number of residues either side of the clicked
residue that becomes the selected zone

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refine_auto_range_step(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refine-auto-range-step 1)` | ran (no return value, nothing visible changed) |

### set_refine_hydrogen_bonds

Python: `set_refine_hydrogen_bonds(state)`  
Scheme: `(set-refine-hydrogen-bonds state)`

add or remove auto H-bond restraints

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refine_hydrogen_bonds(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refine-hydrogen-bonds 1)` | ran (no return value, nothing visible changed) |

### set_refine_max_residues

Python: `set_refine_max_residues(n)`  
Scheme: `(set-refine-max-residues n)`

set the heuristic fencepost for the maximum number of
 residues in the refinement/regularization residue range

 Default is 20

Arguments: n (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refine_max_residues(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refine-max-residues 1)` | ran (no return value, nothing visible changed) |

### set_refine_params_dialog_more_control_frame_is_active

Python: `set_refine_params_dialog_more_control_frame_is_active(state)`  
Scheme: `(set-refine-params-dialog-more-control-frame-is-active state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refine_params_dialog_more_control_frame_is_active(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refine-params-dialog-more-control-frame-is-active 1)` | ran (no return value, nothing visible changed) |

### set_refine_ramachandran_angles

Python: `set_refine_ramachandran_angles(state)`  
Scheme: `(set-refine-ramachandran-angles state)`

name consistent with set_refine_with_torsion_restraints() !?

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refine_ramachandran_angles(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refine-ramachandran-angles 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: refine_ramachandran_angles_state was 0, set to 1, read back 1; Scheme: refine-ramachandran-angles-state was 0, set to 1, read back 1.

### set_refine_ramachandran_restraints_type

Python: `set_refine_ramachandran_restraints_type(type)`  
Scheme: `(set-refine-ramachandran-restraints-type type)`

change the target function type

Arguments: type (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refine_ramachandran_restraints_type(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refine-ramachandran-restraints-type 1)` | ran (no return value, nothing visible changed) |

### set_refine_ramachandran_restraints_weight

Python: `set_refine_ramachandran_restraints_weight(w)`  
Scheme: `(set-refine-ramachandran-restraints-weight w)`

change the target function weight

a big number means bad things

Arguments: w (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refine_ramachandran_restraints_weight(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refine-ramachandran-restraints-weight 1.0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: refine_ramachandran_restraints_weight was 40.0, set to 60.5, read back 60.5; Scheme: refine-ramachandran-restraints-weight was 40.0, set to 60.5, read back 60.5.

### set_refine_ramachandran_torsion_angles

Python: `set_refine_ramachandran_torsion_angles(state)`  
Scheme: `(set-refine-ramachandran-torsion-angles state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refine_ramachandran_torsion_angles(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refine-ramachandran-torsion-angles 1)` | ran (no return value, nothing visible changed) |

### set_refine_rotamers

Python: `set_refine_rotamers(state)`  
Scheme: `(set-refine-rotamers state)`

set the state for using rotamer restraints "drive" mode

1 in on, 0 is off (off by default)

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refine_rotamers(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refine-rotamers 1)` | ran (no return value, nothing visible changed) |

### set_refine_with_torsion_restraints

Python: `set_refine_with_torsion_restraints(istate)`  
Scheme: `(set-refine-with-torsion-restraints istate)`

turn on (or off) torsion restraints

 Pass with istate=1 for on, istate=0 for off.

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refine_with_torsion_restraints(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refine-with-torsion-restraints 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: refine_with_torsion_restraints_state was 0, set to 1, read back 1; Scheme: refine-with-torsion-restraints-state was 0, set to 1, read back 1.

### set_refinement_drag_elasticity

Python: `set_refinement_drag_elasticity(e)`  
Scheme: `(set-refinement-drag-elasticity e)`

- the elasticity of the dragged atom in refinement mode.

Default 0.33

 Bigger numbers mean bigger movement of the other atoms.

Arguments: e (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refinement_drag_elasticity(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refinement-drag-elasticity 1.0)` | ran (no return value, nothing visible changed) |

### set_refinement_geman_mcclure_alpha_from_text

Python: `set_refinement_geman_mcclure_alpha_from_text(combobox_item_idx, t)`  
Scheme: `(set-refinement-geman-mcclure-alpha-from-text combobox-item-idx t)`

Arguments: combobox_item_idx (a whole number), t (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refinement_geman_mcclure_alpha_from_text(2, "0.5")` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refinement-geman-mcclure-alpha-from-text 2 "0.5")` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the Geman-McClure alpha from text (the first argument is the combobox position remembered for the dialog).

### set_refinement_immediate_replacement

Python: `set_refinement_immediate_replacement(istate)`  
Scheme: `(set-refinement-immediate-replacement istate)`

set immediate replacement mode for refinement and
 regularization. You need this (call with istate=1) if you are
 scripting refinement/regularization

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refinement_immediate_replacement(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refinement-immediate-replacement 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: refinement_immediate_replacement_state was 0, set to 1, read back 1; Scheme: refinement-immediate-replacement-state was 0, set to 1, read back 1.

### set_refinement_lennard_jones_epsilon_from_text

Python: `set_refinement_lennard_jones_epsilon_from_text(combobox_item_idx, t)`  
Scheme: `(set-refinement-lennard-jones-epsilon-from-text combobox-item-idx t)`

Arguments: combobox_item_idx (a whole number), t (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refinement_lennard_jones_epsilon_from_text(2, "2.0")` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refinement-lennard-jones-epsilon-from-text 2 "2.0")` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the Lennard-Jones epsilon used in refinement from text (no getter).

### set_refinement_overall_weight_from_text

Python: `set_refinement_overall_weight_from_text(t)`  
Scheme: `(set-refinement-overall-weight-from-text t)`

Arguments: t (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refinement_overall_weight_from_text("30")` | ran (no return value); changed: get_map_weight(): 1 -> 30; matrix_state(): 1 -> 30 |
| Scheme | `(set-refinement-overall-weight-from-text "20")` | ran (no return value); changed: get_map_weight(): 30 -> 20; matrix_state(): 30 -> 20 |

Example written and checked by hand on the test data. Expected: sets the refinement map weight from text; matrix_state() returns the new value.

### set_refinement_ramachandran_restraints_weight_from_text

Python: `set_refinement_ramachandran_restraints_weight_from_text(combobox_item_idx, t)`  
Scheme: `(set-refinement-ramachandran-restraints-weight-from-text combobox-item-idx t)`

Arguments: combobox_item_idx (a whole number), t (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refinement_ramachandran_restraints_weight_from_text(2, "5.0")` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refinement-ramachandran-restraints-weight-from-text 2 "5.0")` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the Ramachandran restraints weight from text; refine_ramachandran_restraints_weight() returns it.

### set_refinement_refine_per_frame

Python: `set_refinement_refine_per_frame(istate)`  
Scheme: `(set-refinement-refine-per-frame istate)`

allow refinement of intermediate atoms after dragging,
 before displaying (default: 0, off).

 An attempt to do something like xfit does, at the request of Frank
 von Delft.

 Pass with istate=1 to enable this option.

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refinement_refine_per_frame(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refinement-refine-per-frame 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: refinement_refine_per_frame_state was 0, set to 1, read back 1; Scheme: refinement-refine-per-frame-state was 0, set to 1, read back 1.

### set_refinement_torsion_weight_from_text

Python: `set_refinement_torsion_weight_from_text(combobox_item_index, t)`  
Scheme: `(set-refinement-torsion-weight-from-text combobox-item-index t)`

Arguments: combobox_item_index (a whole number), t (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refinement_torsion_weight_from_text(2, "5.0")` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refinement-torsion-weight-from-text 2 "5.0")` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the torsion restraints weight used in refinement from text.

### set_refinement_use_soft_mode_nbc_restraints

Python: `set_refinement_use_soft_mode_nbc_restraints(flag)`  
Scheme: `(set-refinement-use-soft-mode-nbc-restraints flag)`

Arguments: flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refinement_use_soft_mode_nbc_restraints(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refinement-use-soft-mode-nbc-restraints 1)` | ran (no return value, nothing visible changed) |

### set_residue_selection_flash_frames_number

Python: `set_residue_selection_flash_frames_number(i)`  
Scheme: `(set-residue-selection-flash-frames-number i)`

set the number of frames for which the selected residue
 range flashes

 On fast computers, this can be set to higher than the default for
 more aesthetic appeal.

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_residue_selection_flash_frames_number(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-residue-selection-flash-frames-number 1)` | ran (no return value, nothing visible changed) |

### set_secondary_structure_restraints_type

Python: `set_secondary_structure_restraints_type(itype)`  
Scheme: `(set-secondary-structure-restraints-type itype)`

set the type of secondary structure restraints

0 no sec str restraints

1 alpha helix restraints

2 beta strand restraints

Arguments: itype (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_secondary_structure_restraints_type(1)` | ran (no return value); changed: secondary_structure_restraints_type(): 0 -> 1 |
| Scheme | `(set-secondary-structure-restraints-type 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: secondary_structure_restraints_type was 0, set to 1, read back 1; Scheme: secondary-structure-restraints-type was 0, set to 1, read back 1.

### set_show_chiral_volume_errors_dialog

Python: `set_show_chiral_volume_errors_dialog(istate)`  
Scheme: `(set-show-chiral-volume-errors-dialog istate)`

For experienced Cooters who don't like Coot nannying about
 chiral volumes during refinement.

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_chiral_volume_errors_dialog(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-show-chiral-volume-errors-dialog 1)` | ran (no return value, nothing visible changed) |

### set_show_extra_restraints

Python: `set_show_extra_restraints(imol, state)`  
Scheme: `(set-show-extra-restraints imol state)`

Arguments: imol (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_extra_restraints(0, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-show-extra-restraints 0 1)` | ran (no return value, nothing visible changed) |

### set_show_parallel_plane_restraints

Python: `set_show_parallel_plane_restraints(imol, state)`  
Scheme: `(set-show-parallel-plane-restraints imol state)`

Arguments: imol (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_parallel_plane_restraints(0, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-show-parallel-plane-restraints 0 1)` | ran (no return value, nothing visible changed) |

### set_torsion_restraints_weight

Python: `set_torsion_restraints_weight(w)`  
Scheme: `(set-torsion-restraints-weight w)`

not ready yet set the weight for torsion restraints (default 1.0)

Arguments: w (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_torsion_restraints_weight(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-torsion-restraints-weight 1.0)` | ran (no return value, nothing visible changed) |

### set_use_only_extra_torsion_restraints_for_torsions

Python: `set_use_only_extra_torsion_restraints_for_torsions(state)`  
Scheme: `(set-use-only-extra-torsion-restraints-for-torsions state)`

set use only extra torsion restraints for torsions

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_use_only_extra_torsion_restraints_for_torsions(1)` | ran (no return value); changed: use_only_extra_torsion_restraints_for_torsions_state(): 0 -> 1 |
| Scheme | `(set-use-only-extra-torsion-restraints-for-torsions 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: use_only_extra_torsion_restraints_for_torsions_state was 0, set to 1, read back 1; Scheme: use-only-extra-torsion-restraints-for-torsions-state was 0, set to 1, read back 1.

### set_use_trans_peptide_restraints

Python: `set_use_trans_peptide_restraints(on_off_state)`  
Scheme: `(set-use-trans-peptide-restraints on-off-state)`

add a restraint on peptides to keep trans peptides trans

i.e. omega in trans-peptides is restraints to 180 degrees.

Arguments: on_off_state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_use_trans_peptide_restraints(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-use-trans-peptide-restraints 1)` | ran (no return value, nothing visible changed) |

### shiftfield_b_factor_refinement

Python: `shiftfield_b_factor_refinement(imol)`  
Scheme: `(shiftfield-b-factor-refinement imol)`

shiftfield B-factor refinement

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `shiftfield_b_factor_refinement(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(shiftfield-b-factor-refinement 0)` | ran (no return value, nothing visible changed) |

### shiftfield_xyz_factor_refinement

Python: `shiftfield_xyz_factor_refinement(imol)`  
Scheme: `(shiftfield-xyz-factor-refinement imol)`

shiftfield xyz refinement

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `shiftfield_xyz_factor_refinement(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(shiftfield-xyz-factor-refinement 0)` | ran (no return value, nothing visible changed) |

### show_restraints_editor

Python: `show_restraints_editor(monomer_type)`  
Scheme: `(show-restraints-editor monomer-type)`

show restraints editor

Arguments: monomer_type (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_restraints_editor("ALA")` | ran (no return value, nothing visible changed) |
| Scheme | `(show-restraints-editor "ALA")` | ran (no return value, nothing visible changed) |

### show_restraints_editor_by_index

Python: `show_restraints_editor_by_index(menu_item_index)`  
Scheme: `(show-restraints-editor-by-index menu-item-index)`

show restraints editor using residue type index

Arguments: menu_item_index (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_restraints_editor_by_index(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(show-restraints-editor-by-index 1)` | ran (no return value, nothing visible changed) |

### stop_refinement_internal

Python: `stop_refinement_internal()`  
Scheme: `(stop-refinement-internal)`

Used by on_accept_reject_refinement_reject_button_clicked()

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `stop_refinement_internal()` | ran (no return value, nothing visible changed) |
| Scheme | `(stop-refinement-internal)` | ran (no return value, nothing visible changed) |

### use_only_extra_torsion_restraints_for_torsions_state

Python: `use_only_extra_torsion_restraints_for_torsions_state()`  
Scheme: `(use-only-extra-torsion-restraints-for-torsions-state)`

return only-use-extra-torsion-restraints-for-torsions state

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `use_only_extra_torsion_restraints_for_torsions_state()` | ran, returned `0` |
| Scheme | `(use-only-extra-torsion-restraints-for-torsions-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### write_interpolated_extra_restraints

Python: `write_interpolated_extra_restraints(imol_1, imol_2, n_steps, file_name_stub)`  
Scheme: `(write-interpolated-extra-restraints imol-1 imol-2 n-steps file-name-stub)`

proSMART interpolated restraints for model morphing

Arguments: imol_1 (a whole number), imol_2 (a whole number), n_steps (a whole number), file_name_stub (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_interpolated_extra_restraints(0, 0, 1, "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(write-interpolated-extra-restraints 0 0 1 "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

### write_interpolated_models_and_extra_restraints

Python: `write_interpolated_models_and_extra_restraints(imol_1, imol_2, n_steps, file_name_stub, interpolation_mode)`  
Scheme: `(write-interpolated-models-and-extra-restraints imol-1 imol-2 n-steps file-name-stub interpolation-mode)`

proSMART interpolated restraints for model morphing and write interpolated model

interpolation_mode is currently dummy - in due course I will addd torion angle interpolation.

Arguments: imol_1 (a whole number), imol_2 (a whole number), n_steps (a whole number), file_name_stub (text), interpolation_mode (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_interpolated_models_and_extra_restraints(0, 0, 1, "tutorial-modern.pdb", 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(write-interpolated-models-and-extra-restraints 0 0 1 "tutorial-modern.pdb" 1)` | ran (no return value, nothing visible changed) |

### write_restraints_cif_dictionary

Python: `write_restraints_cif_dictionary(monomer_type, file_name)`  
Scheme: `(write-restraints-cif-dictionary monomer-type file-name)`

write cif restraints for monomer

Arguments: monomer_type (text), file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_restraints_cif_dictionary("ALA", "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(write-restraints-cif-dictionary "ALA" "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

