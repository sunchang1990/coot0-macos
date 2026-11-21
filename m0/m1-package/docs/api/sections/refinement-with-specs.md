# Refinement with specs

[Scripting reference](../README.md) > Refinement with specs (20 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### accept_moving_atoms

Python: `accept_moving_atoms()`  
Scheme: `(accept-moving-atoms)`

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `accept_moving_atoms_py`.
Also available in Scheme as `accept-moving-atoms-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `(refine_zone(0, "A", 41, 43, ""), accept_moving_atoms())[1]` | ran, returned `['', 0, [['Bonds', 'Bonds:  1.162', 1.1623175144195557], ['Angles', 'Angles: 1.493', 1.4932128190994263], ['Trans_peptid ...`; changed: molecule 0: coordinates of 3 residue(s) (A41, A42, A43) |
| Scheme | `(begin (refine-zone 0 "A" 41 43 "") (accept-moving-atoms))` | ran, returned `("" 0 (("Bonds" "Bonds:  1.162" 1.1620523929595947) ("Angles" "Angles: 1.493" 1.4932188987731934) ("Trans_peptide" "Tran ...`; changed: molecule 0: coordinates of 3 residue(s) (A41, A42, A43) |

Example written and checked by hand on the test data. Expected: accepts the refinement result into the molecule and returns the refinement summary (message, status, per-restraint-type scores); False when there are no moving atoms.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### all_residues_with_serial_numbers

Python: `all_residues_with_serial_numbers(imol)`  
Scheme: `(all-residues-with-serial-numbers imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `all_residues_with_serial_numbers`, `all_residues_with_serial_numbers_py`.
Also available in Scheme as `all-residues-with-serial-numbers-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `all_residues_with_serial_numbers(0)` | ran, returned `[[0, True, 'A', 1, ''], [1, True, 'A', 2, ''], [2, True, 'A', 3, ''], [3, True, 'A', 4, ''], [4, True, 'A', 5, ''], [5,  ...` |
| Scheme | `(all-residues-with-serial-numbers 0)` | ran, returned `((0 #t "A" 1 "") (1 #t "A" 2 "") (2 #t "A" 3 "") (3 #t "A" 4 "") (4 #t "A" 5 "") (5 #t "A" 6 "") (6 #t "A" 7 "") (7 #t " ...` |

Python and Scheme gave the same answer.

### b_factor_distribution_graph

Python: `b_factor_distribution_graph(imol)`  
Scheme: `(b-factor-distribution-graph imol)`

B-factor distribution histogram

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `b_factor_distribution_graph(0)` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(b-factor-distribution-graph 0)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens a histogram window of the B-factors of molecule 0.

### check_waters_baddies

Python: `check_waters_baddies(imol, b_factor_lim, map_sigma_lim, min_dist, max_dist, part_occ_contact_flag, zero_occ_flag, logical_operator_and_or_flag)`  
Scheme: `(check-waters-baddies imol b-factor-lim map-sigma-lim min-dist max-dist part-occ-contact-flag zero-occ-flag logical-operator-and-or-flag)`

Arguments: imol (a whole number), b_factor_lim (a number), map_sigma_lim (a number), min_dist (a number), max_dist (a number), part_occ_contact_flag (a whole number), zero_occ_flag (a whole number), logical_operator_and_or_flag (a whole number). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `check_waters_baddies(0, 20.0, 1.5, 1.0, 1.0, 1, 1, 1)` | ran, returned `()` |
| Scheme | `(check-waters-baddies 0 20.0 1.5 1.0 1.0 1 1 1)` | ran, returned `#()` |

Python and Scheme gave the same answer.

### find_blobs

Python: `find_blobs(imol_model, imol_map, cut_off_density_level)`  
Scheme: `(find-blobs imol-model imol-map cut-off-density-level)`

blobs, returning position and volume

Arguments: imol_model (a whole number), imol_map (a whole number), cut_off_density_level (a number). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `find_blobs(0, 1, 1.5)` | ran, returned `[[[59.897255080580464, 2.932044945000125, -4.155281760924597], 58.12772232083223], [[53.775366015612754, 9.0783475008877 ...` |
| Scheme | `(find-blobs 0 1 1.5)` | ran, returned `((58.12772232083223 59.897255080580464 2.932044945000125 -4.155281760924597) (22.504935971005438 53.775366015612754 9.07 ...` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### get_cryo_em_refinement

Python: `get_cryo_em_refinement()`  
Scheme: `(get-cryo-em-refinement)`

Arguments: none. Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_cryo_em_refinement()` | ran, returned `False` |
| Scheme | `(get-cryo-em-refinement)` | ran, returned `#f` |

Example written and checked by hand on the test data. Expected: returns True when cryo-EM refinement mode is on; False by default.

Python and Scheme gave the same answer.

### get_regenerate_bonds_needs_make_bonds_type_checked_state

Python: `get_regenerate_bonds_needs_make_bonds_type_checked_state()`  
Scheme: `(get-regenerate-bonds-needs-make-bonds-type-checked-state)`

Arguments: none. Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_regenerate_bonds_needs_make_bonds_type_checked_state()` | ran, returned `True` |
| Scheme | `(get-regenerate-bonds-needs-make-bonds-type-checked-state)` | ran, returned `#t` |

Python and Scheme gave the same answer.

### morph_fit_all

Python: `morph_fit_all(imol, transformation_averaging_radius)`  
Scheme: `(morph-fit-all imol transformation-averaging-radius)`

Model morphing (average the atom shift by using shifts of the
atoms within shift_average_radius A of the central residue).
return 0 on fail to move atoms and 1 on fitting happened.

Arguments: imol (a whole number), transformation_averaging_radius (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `morph_fit_all(0, 5.0)` | ran, returned `1`; changed: molecule 0: coordinates of 189 residue(s) (A1, A2, A3, A4 ...) |
| Scheme | `(morph-fit-all 0 5.0)` | ran, returned `1`; changed: molecule 0: coordinates of 189 residue(s) (A1, A2, A3, A4 ...) |

Python and Scheme gave the same answer.

### morph_fit_by_secondary_structure_elements

Python: `morph_fit_by_secondary_structure_elements(imol, chain_id)`  
Scheme: `(morph-fit-by-secondary-structure-elements imol chain-id)`

morph transformation are based primarily on rigid body refinement
of the secondary structure elements.

Arguments: imol (a whole number), chain_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `morph_fit_by_secondary_structure_elements(0, "A")` | ran, returned `0`; changed: molecule 0: coordinates of 93 residue(s) (A1, A2, A3, A4 ...) |
| Scheme | `(morph-fit-by-secondary-structure-elements 0 "A")` | ran, returned `0`; changed: molecule 0: coordinates of 93 residue(s) (A1, A2, A3, A4 ...) |

Example written and checked by hand on the test data. Expected: moves the chain by rigid-body fitting its helices/strands to the refinement map, residues in between follow; returns 0.

Note: returns 0 even though it worked

Python and Scheme gave the same answer.

### morph_fit_chain

Python: `morph_fit_chain(imol, chain_id, transformation_averaging_radius)`  
Scheme: `(morph-fit-chain imol chain-id transformation-averaging-radius)`

Morph the given chain

Arguments: imol (a whole number), chain_id (text), transformation_averaging_radius (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `morph_fit_chain(0, "A", 5.0)` | ran, returned `1`; changed: molecule 0: coordinates of 93 residue(s) (A1, A2, A3, A4 ...) |
| Scheme | `(morph-fit-chain 0 "A" 5.0)` | ran, returned `1`; changed: molecule 0: coordinates of 93 residue(s) (A1, A2, A3, A4 ...) |

Python and Scheme gave the same answer.

### morph_fit_residues

Python: `morph_fit_residues(imol, residue_specs, transformation_averaging_radius)`  
Scheme: `(morph-fit-residues imol residue-specs transformation-averaging-radius)`

morph the given residues.

Arguments: imol (a whole number), residue_specs (a list or value), transformation_averaging_radius (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `morph_fit_residues(0, [["A", 41, ""], ["A", 42, ""]], 5.0)` | ran, returned `1`; changed: molecule 0: coordinates of 91 residue(s) (A1, A2, A3, A4 ...) |
| Scheme | `(morph-fit-residues 0 (list (list "A" 41 "") (list "A" 42 "")) 5.0)` | ran, returned `1`; changed: molecule 0: coordinates of 91 residue(s) (A1, A2, A3, A4 ...) |

Python and Scheme gave the same answer.

### mtz_file_name

Python: `mtz_file_name(imol)`  
Scheme: `(mtz-file-name imol)`

presumes that imol_Refinement_Map has been set

Arguments: imol (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mtz_file_name(0)` | ran, returned `''` |
| Scheme | `(mtz-file-name 0)` | ran, returned `""` |

Python and Scheme gave the same answer.

### refine_zone_with_full_residue_spec

Python: `refine_zone_with_full_residue_spec(imol, chain_id, resno1, inscode_1, resno2, inscode_2, altconf)`  
Scheme: `(refine-zone-with-full-residue-spec imol chain-id resno1 inscode-1 resno2 inscode-2 altconf)`

Arguments: imol (a whole number), chain_id (text), resno1 (a whole number), inscode_1 (text), resno2 (a whole number), inscode_2 (text), altconf (text). Returns: a value (see the result of the example).
Also available in Python as `refine_zone_with_full_residue_spec_py`.
Also available in Scheme as `refine-zone-with-full-residue-spec-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_zone_with_full_residue_spec(0, "A", 41, "", 45, "", "")` | ran, returned `['', -2, False]` |
| Scheme | `(refine-zone-with-full-residue-spec 0 "A" 41 "" 45 "" "")` | ran, returned `("" -2 ())` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### register_post_intermediate_atoms_moved_hook

Python: `register_post_intermediate_atoms_moved_hook(function_name)`

Arguments: function_name (a list or value). Returns: nothing.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `def hook(*args): print("intermediate atoms moved", args)`, then `register_post_intermediate_atoms_moved_hook(hook)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: registers a Python function that Coot calls after the intermediate (moving) atoms move, e.g. while dragging during refinement (Python only).

Note: not seen to run headless (no interactive moving atoms); needs the window to observe

### regularize_residues

Python: `regularize_residues(imol, r)`  
Scheme: `(regularize-residues imol r)`

regularize the given residues

Arguments: imol (a whole number), r (a list or value). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `regularize_residues(0, [["A", 41, ""], ["A", 42, ""]])` | ran, returned `['', -2, False]` |
| Scheme | `(regularize-residues 0 (list (list "A" 41 "") (list "A" 42 "")))` | ran, returned `("" -2 ())` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### rigid_body_fit_with_residue_ranges

Python: `rigid_body_fit_with_residue_ranges(imol, ranges)`  
Scheme: `(rigid-body-fit-with-residue-ranges imol ranges)`

return 0 on fail to refine (no sensible place to put atoms) and 1
on fitting happened.

Arguments: imol (a whole number), ranges (a list). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: rigid-body fits the residue ranges into the refinement map.

### set_cryo_em_refinement

Python: `set_cryo_em_refinement(mode)`  
Scheme: `(set-cryo-em-refinement mode)`

Arguments: mode (true or false). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_cryo_em_refinement(True)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-cryo-em-refinement 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_cryo_em_refinement was False, set to True, read back True; Scheme: get-cryo-em-refinement was False, set to True, read back True.

### set_regenerate_bonds_needs_make_bonds_type_checked

Python: `set_regenerate_bonds_needs_make_bonds_type_checked(state)`  
Scheme: `(set-regenerate-bonds-needs-make-bonds-type-checked state)`

Arguments: state (true or false). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_regenerate_bonds_needs_make_bonds_type_checked(True)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-regenerate-bonds-needs-make-bonds-type-checked 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_regenerate_bonds_needs_make_bonds_type_checked_state was True, set to False, read back False; Scheme: get-regenerate-bonds-needs-make-bonds-type-checked-state was True, set to False, read back False.

### set_show_intermediate_atoms_rama_markup

Python: `set_show_intermediate_atoms_rama_markup(state)`  
Scheme: `(set-show-intermediate-atoms-rama-markup state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_intermediate_atoms_rama_markup(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-show-intermediate-atoms-rama-markup 1)` | ran (no return value, nothing visible changed) |

### set_show_intermediate_atoms_rota_markup

Python: `set_show_intermediate_atoms_rota_markup(state)`  
Scheme: `(set-show-intermediate-atoms-rota-markup state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_intermediate_atoms_rota_markup(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-show-intermediate-atoms-rota-markup 1)` | ran (no return value, nothing visible changed) |

