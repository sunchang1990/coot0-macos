# NCS

[Scripting reference](../README.md) > NCS (29 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_ncs_matrix

Python: `add_ncs_matrix(imol, this_chain_id, target_chain_id, m11, m12, m13, m21, m22, m23, m31, m32, m33, t1, t2, t3)`  
Scheme: `(add-ncs-matrix imol this-chain-id target-chain-id m11 m12 m13 m21 m22 m23 m31 m32 m33 t1 t2 t3)`

Add NCS matrix

Arguments: imol (a whole number), this_chain_id (text), target_chain_id (text), m11 (a number), m12 (a number), m13 (a number), m21 (a number), m22 (a number), m23 (a number), m31 (a number), m32 (a number), m33 (a number), t1 (a number), t2 (a number), t3 (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_ncs_matrix(0, "A", "A", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(add-ncs-matrix 0 "A" "A" 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0)` | ran (no return value, nothing visible changed) |

### add_strict_ncs_from_mtrix_from_self_file

Python: `add_strict_ncs_from_mtrix_from_self_file(imol)`  
Scheme: `(add-strict-ncs-from-mtrix-from-self-file imol)`

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_strict_ncs_from_mtrix_from_self_file(0)` | ran, returned `0` |
| Scheme | `(add-strict-ncs-from-mtrix-from-self-file 0)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: adds strict NCS operators from the MTRIX records of the molecule's own file; always returns 0.

Python and Scheme gave the same answer.

### add_strict_ncs_matrix

Python: `add_strict_ncs_matrix(imol, this_chain_id, target_chain_id, m11, m12, m13, m21, m22, m23, m31, m32, m33, t1, t2, t3)`  
Scheme: `(add-strict-ncs-matrix imol this-chain-id target-chain-id m11 m12 m13 m21 m22 m23 m31 m32 m33 t1 t2 t3)`

add an NCS matrix for strict NCS molecule representation

for CNS strict NCS usage: expand like normal symmetry does

Arguments: imol (a whole number), this_chain_id (text), target_chain_id (text), m11 (a number), m12 (a number), m13 (a number), m21 (a number), m22 (a number), m23 (a number), m31 (a number), m32 (a number), m33 (a number), t1 (a number), t2 (a number), t3 (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_strict_ncs_matrix(0, "A", "A", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)` | ran, returned `1` |
| Scheme | `(add-strict-ncs-matrix 0 "A" "A" 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0)` | ran, returned `1` |

Python and Scheme gave the same answer.

### clear_ncs_ghost_matrices

Python: `clear_ncs_ghost_matrices(imol)`  
Scheme: `(clear-ncs-ghost-matrices imol)`

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_ncs_ghost_matrices(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(clear-ncs-ghost-matrices 0)` | ran (no return value, nothing visible changed) |

### copy_chain

Python: `copy_chain(imol, from_chain, to_chain)`  
Scheme: `(copy-chain imol from-chain to-chain)`

Copy single NCS chain

Arguments: imol (a whole number), from_chain (text), to_chain (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `copy_chain(0, "A", "B")` | ran (no return value); changed: molecule 0: deleted 3 residue(s) (B94, B95, B96); molecule 0: B-factors of 91 residue(s) (B1, B2, B3, B4 ...); molecule 0: atoms of 2 residue(s) (B72, B89); molecule 0: coordinates of 91 residue(s) (B1, B2, B3, B4 ...) ... |
| Scheme | `(copy-chain 0 "A" "B")` | ran (no return value); changed: molecule 0: deleted 3 residue(s) (B94, B95, B96); molecule 0: B-factors of 91 residue(s) (B1, B2, B3, B4 ...); molecule 0: atoms of 2 residue(s) (B72, B89); molecule 0: coordinates of 91 residue(s) (B1, B2, B3, B4 ...) ... |

### copy_from_ncs_master_to_chains

Python: `copy_from_ncs_master_to_chains(imol, master_chain_id, chain_id_list)`  
Scheme: `(copy-from-ncs-master-to-chains imol master-chain-id chain-id-list)`

Arguments: imol (a whole number), master_chain_id (text), chain_id_list (a list or value). Returns: nothing.
Also available in Python as `copy_from_ncs_master_to_chains_py`.
Also available in Scheme as `copy-from-ncs-master-to-chains-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `mutate_single_residue_by_seqno(41, "", "A", 0, "A")`, then `copy_from_ncs_master_to_chains(0, "A", ["B"])` | ran (no return value); changed: molecule 0: deleted 3 residue(s) (B94, B95, B96); molecule 0: B-factors of 90 residue(s) (B1, B2, B3, B4 ...); molecule 0: atoms of 3 residue(s) (B41, B72, B89); molecule 0: coordinates of 90 residue(s) (B1, B2, B3, B4 ...) ... |
| Scheme | first `(mutate-single-residue-by-seqno 41 "" "A" 0 #\A)`, then `(copy-from-ncs-master-to-chains 0 "A" (list "B"))` | ran (no return value); changed: molecule 0: deleted 3 residue(s) (B94, B95, B96); molecule 0: B-factors of 90 residue(s) (B1, B2, B3, B4 ...); molecule 0: atoms of 3 residue(s) (B41, B72, B89); molecule 0: coordinates of 90 residue(s) (B1, B2, B3, B4 ...) ... |

Example written and checked by hand on the test data. Expected: replaces chain B by a superposed copy of master chain A (the A41 mutation appears at B41).

Note: the whole chain is replaced: B residues absent from A (B94-96) are deleted and B72's alt confs are lost

### copy_from_ncs_master_to_others

Python: `copy_from_ncs_master_to_others(imol, chain_id)`  
Scheme: `(copy-from-ncs-master-to-others imol chain-id)`

Copy chain from master to all related NCS chains

Arguments: imol (a whole number), chain_id (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `copy_from_ncs_master_to_others(0, "A")` | ran (no return value); changed: molecule 0: deleted 3 residue(s) (B94, B95, B96); molecule 0: B-factors of 91 residue(s) (B1, B2, B3, B4 ...); molecule 0: atoms of 2 residue(s) (B72, B89); molecule 0: coordinates of 91 residue(s) (B1, B2, B3, B4 ...) ... |
| Scheme | `(copy-from-ncs-master-to-others 0 "A")` | ran (no return value); changed: molecule 0: deleted 3 residue(s) (B94, B95, B96); molecule 0: B-factors of 91 residue(s) (B1, B2, B3, B4 ...); molecule 0: atoms of 2 residue(s) (B72, B89); molecule 0: coordinates of 91 residue(s) (B1, B2, B3, B4 ...) ... |

### copy_from_ncs_master_to_specific_other_chains_py

Python: `copy_from_ncs_master_to_specific_other_chains_py(imol, chain_id, other_chain_id_list_py)`  
Scheme: `(copy-from-ncs-master-to-specific-other-chains-scm imol chain-id other-chain-id-list-scm)`

Copy chain from master to specified other NCS chains

Arguments: imol (a whole number), chain_id (text), other_chain_id_list_py (a list or value). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `mutate_single_residue_by_seqno(41, "", "A", 0, "A")`, then `copy_from_ncs_master_to_specific_other_chains_py(0, "A", ["B"])` | ran (no return value); changed: molecule 0: deleted 3 residue(s) (B94, B95, B96); molecule 0: B-factors of 90 residue(s) (B1, B2, B3, B4 ...); molecule 0: atoms of 3 residue(s) (B41, B72, B89); molecule 0: coordinates of 90 residue(s) (B1, B2, B3, B4 ...) ... |
| Scheme | first `(mutate-single-residue-by-seqno 41 "" "A" 0 #\A)`, then `(copy-from-ncs-master-to-specific-other-chains-scm 0 "A" (list "B"))` | ran (no return value); changed: molecule 0: deleted 3 residue(s) (B94, B95, B96); molecule 0: B-factors of 90 residue(s) (B1, B2, B3, B4 ...); molecule 0: atoms of 3 residue(s) (B41, B72, B89); molecule 0: coordinates of 90 residue(s) (B1, B2, B3, B4 ...) ... |

Example written and checked by hand on the test data. Expected: copies master chain A onto the listed NCS chains (here B), like copy_from_ncs_master_to_chains.

### copy_residue_range_from_ncs_master_to_chains

Python: `copy_residue_range_from_ncs_master_to_chains(imol, master_chain_id, residue_range_start, residue_range_end, chain_id_list)`  
Scheme: `(copy-residue-range-from-ncs-master-to-chains imol master-chain-id residue-range-start residue-range-end chain-id-list)`

Arguments: imol (a whole number), master_chain_id (text), residue_range_start (a whole number), residue_range_end (a whole number), chain_id_list (a list or value). Returns: nothing.
Also available in Python as `copy_residue_range_from_ncs_master_to_chains_py`.
Also available in Scheme as `copy-residue-range-from-ncs-master-to-chains-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `mutate_single_residue_by_seqno(41, "", "A", 0, "A")`, then `copy_residue_range_from_ncs_master_to_chains(0, "A", 40, 45, ["B"])` | ran (no return value); changed: molecule 0: B-factors of 5 residue(s) (B40, B42, B43, B44 ...); molecule 0: atoms of 1 residue(s) (B41); molecule 0: coordinates of 5 residue(s) (B40, B42, B43, B44 ...); n_atoms(0): 1461 -> 1457 |
| Scheme | first `(mutate-single-residue-by-seqno 41 "" "A" 0 #\A)`, then `(copy-residue-range-from-ncs-master-to-chains 0 "A" 40 45 (list "B"))` | ran (no return value); changed: molecule 0: B-factors of 5 residue(s) (B40, B42, B43, B44 ...); molecule 0: atoms of 1 residue(s) (B41); molecule 0: coordinates of 5 residue(s) (B40, B42, B43, B44 ...); n_atoms(0): 1461 -> 1457 |

Example written and checked by hand on the test data. Expected: copies only residues 40-45 of master chain A onto chain B (B41 becomes ALA).

### copy_residue_range_from_ncs_master_to_others

Python: `copy_residue_range_from_ncs_master_to_others(imol, master_chain_id, residue_range_start, residue_range_end)`  
Scheme: `(copy-residue-range-from-ncs-master-to-others imol master-chain-id residue-range-start residue-range-end)`

Copy residue range to all related NCS chains.

 If the
 target residues do not exist in the peer chains, then create
 them.

Arguments: imol (a whole number), master_chain_id (text), residue_range_start (a whole number), residue_range_end (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `copy_residue_range_from_ncs_master_to_others(0, "A", 1, 1)` | ran (no return value); changed: molecule 0: B-factors of 1 residue(s) (B1); molecule 0: coordinates of 1 residue(s) (B1) |
| Scheme | `(copy-residue-range-from-ncs-master-to-others 0 "A" 1 1)` | ran (no return value); changed: molecule 0: coordinates of 1 residue(s) (B1) |

### draw_ncs_ghosts_state

Python: `draw_ncs_ghosts_state(imol)`  
Scheme: `(draw-ncs-ghosts-state imol)`

return the drawing state of NCS ghosts for molecule number
 imol. Return -1 on imol is a bad molecule or no ghosts.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `draw_ncs_ghosts_state(0)` | ran, returned `0` |
| Scheme | `(draw-ncs-ghosts-state 0)` | ran, returned `0` |

Python and Scheme gave the same answer.

### get_ncs_matrix_state

Python: `get_ncs_matrix_state()`  
Scheme: `(get-ncs-matrix-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_ncs_matrix_state()` | ran, returned `1` |
| Scheme | `(get-ncs-matrix-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### make_dynamically_transformed_ncs_maps

Python: `make_dynamically_transformed_ncs_maps(imol_model, imol_map, overwrite_maps_of_same_name_flag)`  
Scheme: `(make-dynamically-transformed-ncs-maps imol-model imol-map overwrite-maps-of-same-name-flag)`

make NCS map

Arguments: imol_model (a whole number), imol_map (a whole number), overwrite_maps_of_same_name_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_dynamically_transformed_ncs_maps(0, 1, 1)` | ran, returned `2`; changed: new molecule 3 (map, Map 1 NCS found from matching Chain B onto Chain A); new molecule 4 (map, Map 1 NCS average of Chain A type molecules); graphics_n_molecules(): 3 -> 5 |
| Scheme | `(make-dynamically-transformed-ncs-maps 0 1 1)` | ran, returned `2`; changed: new molecule 3 (map, Map 1 NCS found from matching Chain B onto Chain A); new molecule 4 (map, Map 1 NCS average of Chain A type molecules); graphics_n_molecules(): 3 -> 5 |

Python and Scheme gave the same answer.

### make_ncs_ghosts_maybe

Python: `make_ncs_ghosts_maybe(imol)`  
Scheme: `(make-ncs-ghosts-maybe imol)`

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_ncs_ghosts_maybe(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(make-ncs-ghosts-maybe 0)` | ran (no return value, nothing visible changed) |

### make_ncs_maps

Python: `make_ncs_maps(imol_model, imol_map)`  
Scheme: `(make-ncs-maps imol-model imol-map)`

Arguments: imol_model (a whole number), imol_map (a whole number). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_ncs_maps(0, 1)` | ran, returned `(3,)`; changed: new molecule 3 (map, Transformed map); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(make-ncs-maps 0 1)` | ran, returned `#(3)`; changed: new molecule 3 (map, Transformed map); graphics_n_molecules(): 3 -> 4 |

Python and Scheme gave the same answer.

### ncs_chain_differences

Python: `ncs_chain_differences(imol, master_chain_id)`  
Scheme: `(ncs-chain-differences imol master-chain-id)`

Return the NCS differences as a list.

 e.g. ["B", "A", [[[1, ""], [1, ""], 0.4], [[2, ""], [2, ""], 0.3]]]
 i.e. ncs_related_chain its_master_chain_id and a list of residue
 info: [residue number matches: [this_resno, this_inscode,
 matching_master_resno, matching_master_inscode,
 rms_atom_position_differences]]

Arguments: imol (a whole number), master_chain_id (text). Returns: a value (see the result of the example).
Also available in Python as `ncs_chain_differences_py`.
Also available in Scheme as `ncs-chain-differences-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ncs_chain_differences(0, "A")` | ran, returned `['B', 'A', [[[1, ''], [1, ''], 0.4996705651283264], [[2, ''], [2, ''], 0.2834187150001526], [[3, ''], [3, ''], 0.3093564 ...` |
| Scheme | `(ncs-chain-differences 0 "A")` | ran, returned `("B" "A" (((1 "") (1 "") 0.4996705651283264) ((2 "") (2 "") 0.2834187150001526) ((3 "") (3 "") 0.3093564510345459) ((4 " ...` |

Python and Scheme gave the same answer.

### ncs_chain_ids

Python: `ncs_chain_ids(imol)`  
Scheme: `(ncs-chain-ids imol)`

Return the ncs chains id for the given molecule.

 return something like: [["A", "B"]] or [["A", "C", "E"], ["B",
 "D", "F"]]. The master chain goes in first.

 If imol does not have NCS ghosts, return python False.

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `ncs_chain_ids_py`.
Also available in Scheme as `ncs-chain-ids-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ncs_chain_ids(0)` | ran, returned `[['A', 'B']]` |
| Scheme | `(ncs-chain-ids 0)` | ran, returned `(("A" "B"))` |

Python and Scheme gave the same answer.

### ncs_control_change_ncs_master_to_chain

Python: `ncs_control_change_ncs_master_to_chain(imol, ichain)`  
Scheme: `(ncs-control-change-ncs-master-to-chain imol ichain)`

change the NCS master chain (by number)

Arguments: imol (a whole number), ichain (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ncs_control_change_ncs_master_to_chain(0, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(ncs-control-change-ncs-master-to-chain 0 1)` | ran (no return value, nothing visible changed) |

### ncs_control_change_ncs_master_to_chain_id

Python: `ncs_control_change_ncs_master_to_chain_id(imol, chain_id)`  
Scheme: `(ncs-control-change-ncs-master-to-chain-id imol chain-id)`

change the NCS master chain (by chain_id)

Arguments: imol (a whole number), chain_id (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ncs_control_change_ncs_master_to_chain_id(0, "A")` | ran (no return value, nothing visible changed) |
| Scheme | `(ncs-control-change-ncs-master-to-chain-id 0 "A")` | ran (no return value, nothing visible changed) |

### ncs_control_display_chain

Python: `ncs_control_display_chain(imol, ichain, state)`  
Scheme: `(ncs-control-display-chain imol ichain state)`

display the NCS master chain

Arguments: imol (a whole number), ichain (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ncs_control_display_chain(0, 1, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(ncs-control-display-chain 0 1 1)` | ran (no return value, nothing visible changed) |

### ncs_ghosts

Python: `ncs_ghosts(imol)`  
Scheme: `(ncs-ghosts imol)`

Get the NCS ghosts description

Returns False on bad imol or a list of ghosts on good imol. Can
 include NCS rtops if they are available, else the rtops are False

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `ncs_ghosts_py`.
Also available in Scheme as `ncs-ghosts-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ncs_ghosts(0)` | ran, returned `[['NCS found from matching Chain B onto Chain A', 'B', 'A', [[0.9704933516651332, -0.046903931449300246, -0.236522040386 ...` |
| Scheme | `(ncs-ghosts 0)` | ran, returned `(("NCS found from matching Chain B onto Chain A" "B" "A" ((0.9704933516651332 -0.046903931449300246 -0.2365220403860403  ...` |

Python and Scheme gave the same answer.

### ncs_master_chains

Python: `ncs_master_chains(imol)`  
Scheme: `(ncs-master-chains imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `ncs_master_chains_py`.
Also available in Scheme as `ncs-master-chains-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ncs_master_chains(0)` | ran, returned `['A']` |
| Scheme | `(ncs-master-chains 0)` | ran, returned `("A")` |

Python and Scheme gave the same answer.

### ncs_update_ghosts

Python: `ncs_update_ghosts(imol)`  
Scheme: `(ncs-update-ghosts imol)`

update ghosts for molecule number imol

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ncs_update_ghosts(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(ncs-update-ghosts 0)` | ran (no return value, nothing visible changed) |

### set_draw_ncs_ghosts

Python: `set_draw_ncs_ghosts(imol, istate)`  
Scheme: `(set-draw-ncs-ghosts imol istate)`

set drawing state of NCS ghosts for molecule number imol

Arguments: imol (a whole number), istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_draw_ncs_ghosts(0, 1)` | ran (no return value); changed: draw_ncs_ghosts_state(0): 0 -> 1 |
| Scheme | `(set-draw-ncs-ghosts 0 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: draw_ncs_ghosts_state was 0, set to 1, read back 1; Scheme: draw-ncs-ghosts-state was 0, set to 1, read back 1.

### set_ncs_ghost_bond_thickness

Python: `set_ncs_ghost_bond_thickness(imol, f)`  
Scheme: `(set-ncs-ghost-bond-thickness imol f)`

set bond thickness of NCS ghosts for molecule number imol

Arguments: imol (a whole number), f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ncs_ghost_bond_thickness(0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-ncs-ghost-bond-thickness 0 1.0)` | ran (no return value, nothing visible changed) |

### set_ncs_homology_level

Python: `set_ncs_homology_level(flev)`  
Scheme: `(set-ncs-homology-level flev)`

At what level of homology should we say that we can't see homology
 for NCS calculation? (default 0.8)

Arguments: flev (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ncs_homology_level(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-ncs-homology-level 1.0)` | ran (no return value, nothing visible changed) |

### set_ncs_matrix_type

Python: `set_ncs_matrix_type(flag)`  
Scheme: `(set-ncs-matrix-type flag)`

Arguments: flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ncs_matrix_type(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-ncs-matrix-type 1)` | ran (no return value, nothing visible changed) |

### set_show_strict_ncs

Python: `set_show_strict_ncs(imol, state)`  
Scheme: `(set-show-strict-ncs imol state)`

set display state of NCS ghost molecules for molecule number imol

Arguments: imol (a whole number), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_strict_ncs(0, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-show-strict-ncs 0 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: show_strict_ncs_state was 1, set to 0, read back 0; Scheme: show-strict-ncs-state was 1, set to 0, read back 0.

### show_strict_ncs_state

Python: `show_strict_ncs_state(imol)`  
Scheme: `(show-strict-ncs-state imol)`

return the state of NCS ghost molecules for molecule number imol

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_strict_ncs_state(0)` | ran, returned `1` |
| Scheme | `(show-strict-ncs-state 0)` | ran, returned `1` |

Python and Scheme gave the same answer.

