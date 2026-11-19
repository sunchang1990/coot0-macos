# Validation Functions

[Scripting reference](../README.md) > Validation Functions (24 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### atom_overlap_score

Python: `atom_overlap_score(imol)`  
Scheme: `(atom-overlap-score imol)`

show the pick dialog

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `atom_overlap_score(0)` | ran, returned `218.46453857421875` |
| Scheme | `(atom-overlap-score 0)` | ran, returned `218.46453857421875` |

### c_beta_deviations_py

Python: `c_beta_deviations_py(imol)`  
Scheme: `(c-beta-deviations imol)`

Many more things should go or be moved to here

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Scheme as `c-beta-deviations-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `c_beta_deviations_py(0)` | ran, returned `[[[True, 'A', 2, ''], {'': 0.12761455152709072}], [[True, 'A', 1, ''], {'': 0.16953483228562496}], [[True, 'A', 3, ''],  ...` |
| Scheme | `(c-beta-deviations 0)` | ran, returned `(((#t "B" 96 "") (("" 0.1133771061611323))) ((#t "B" 95 "") (("" 0.04492830156277413))) ((#t "B" 94 "") (("" 0.085321917 ...` |

### clear_diff_map_peaks

Python: `clear_diff_map_peaks()`  
Scheme: `(clear-diff-map-peaks)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_diff_map_peaks()` | ran (no return value) |
| Scheme | `(clear-diff-map-peaks)` | ran (no return value) |

### clear_multi_residue_torsion_mode

Python: `clear_multi_residue_torsion_mode()`  
Scheme: `(clear-multi-residue-torsion-mode)`

These functions are called from callbacks.c

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_multi_residue_torsion_mode()` | ran (no return value) |
| Scheme | `(clear-multi-residue-torsion-mode)` | ran (no return value) |

### deviant_geometry

Python: `deviant_geometry(imol)`  
Scheme: `(deviant-geometry imol)`

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `deviant_geometry(0)` | ran (no return value) |
| Scheme | `(deviant-geometry 0)` | ran (no return value) |

### difference_map_peaks

Python: `difference_map_peaks(imol, imol_coords, level, max_closeness, do_positive_level_flag, do_negative_level_flag, around_model_only_flag)`  
Scheme: `(difference-map-peaks imol imol-coords level max-closeness do-positive-level-flag do-negative-level-flag around-model-only-flag)`

generate a list of difference map peaks

peaks within max_closeness (2.0 A typically) of a larger peak are not
listed.

the flag around_model_only_flag limits the peak list to those only within 4A
of the selected model (useful for maps with molecular symmetry).

Arguments: imol (a whole number), imol_coords (a whole number), level (a number), max_closeness (a number), do_positive_level_flag (a whole number), do_negative_level_flag (a whole number), around_model_only_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `difference_map_peaks(0, 0, 1.5, 1.0, 1, 1, 1)` | ran (no return value) |
| Scheme | `(difference-map-peaks 0 0 1.5 1.0 1 1 1)` | ran (no return value) |

### difference_map_peaks_max_closeness

Python: `difference_map_peaks_max_closeness()`  
Scheme: `(difference-map-peaks-max-closeness)`

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `difference_map_peaks_max_closeness()` | ran, returned `2.0` |
| Scheme | `(difference-map-peaks-max-closeness)` | ran, returned `2.0` |

### get_torsion

Python: `get_torsion(imol, atom_spec_1, atom_spec_2, atom_spec_3, atom_spec_4)`  
Scheme: `(get-torsion imol atom-spec-1 atom-spec-2 atom-spec-3 atom-spec-4)`

Arguments: imol (a whole number), atom_spec_1 (a list or value), atom_spec_2 (a list or value), atom_spec_3 (a list or value), atom_spec_4 (a list or value). Returns: a value (see the result of the example).
Also available in Python as `get_torsion_py`.
Also available in Scheme as `get-torsion-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_torsion(0, ["A", 41, "", " CA ", ""], ["A", 41, "", " CA ", ""], ["A", 41, "", " CA ", ""], ["A", 41, "", " CA ", ""])` | ran, returned `nan` |
| Scheme | `(get-torsion 0 (list "A" 41 "" " CA " "") (list "A" 41 "" " CA " "") (list "A" 41 "" " CA " "") (list "A" 41 "" " CA " ""))` | ran, returned `+nan.0` |

### gln_asn_b_factor_outliers

Python: `gln_asn_b_factor_outliers(imol)`  
Scheme: `(gln-asn-b-factor-outliers imol)`

Make a gui for GLN adn ASN B-factor outiers, compairing the
 O and N temperatur factors difference to the distribution of
 temperature factors from the other atoms.

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `gln_asn_b_factor_outliers(0)` | ran (no return value) |
| Scheme | `(gln-asn-b-factor-outliers 0)` | ran (no return value) |

### is_valid_map_molecule

Python: `is_valid_map_molecule(imol)`  
Scheme: `(is-valid-map-molecule imol)`

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `is_valid_map_molecule(0)` | not tried |
| Scheme | `(is-valid-map-molecule 0)` | not tried |

### is_valid_model_molecule

Python: `is_valid_model_molecule(imol)`  
Scheme: `(is-valid-model-molecule imol)`

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `is_valid_model_molecule(0)` | not tried |
| Scheme | `(is-valid-model-molecule 0)` | not tried |

### map_peaks

Python: `map_peaks(imol_map, n_sigma)`  
Scheme: `(map-peaks imol-map n-sigma)`

return a list of map peaks of molecule number imol_map
 above n_sigma. There will be cluster filtering of the map peaks.
 Return a list of 3d cartestian coordinates or Python False if
 imol_map is not suitable for peak picking.

Arguments: imol_map (a whole number), n_sigma (a number). Returns: a value (see the result of the example).
Also available in Python as `map_peaks_py`.
Also available in Scheme as `map-peaks-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_peaks(1, 1.5)` | not tried |
| Scheme | `(map-peaks 1 1.5)` | not tried |

### map_peaks_around_molecule

Python: `map_peaks_around_molecule(imol_map, sigma, negative_also_flag, imol_coords)`

Arguments: imol_map (a whole number), sigma (a number), negative_also_flag (a whole number), imol_coords (a whole number). Returns: a value (see the result of the example).
Also available in Python as `map_peaks_around_molecule_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_peaks_around_molecule(1, 1.5, 1, 0)` | not tried |

### map_peaks_near_point

Python: `map_peaks_near_point(imol_map, n_sigma, x, y, z, radius)`  
Scheme: `(map-peaks-near-point imol-map n-sigma x y z radius)`

Arguments: imol_map (a whole number), n_sigma (a number), x (a number), y (a number), z (a number), radius (a number). Returns: a value (see the result of the example).
Also available in Python as `map_peaks_near_point_py`.
Also available in Scheme as `map-peaks-near-point-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_peaks_near_point(1, 1.5, 54.5, 9.4, 12.3, 5.0)` | not tried |
| Scheme | `(map-peaks-near-point 1 1.5 54.5 9.4 12.3 5.0)` | not tried |

### map_peaks_near_point_from_list

Python: `map_peaks_near_point_from_list(imol_map, peak_list, x, y, z, radius)`

Arguments: imol_map (a whole number), peak_list (a list or value), x (a number), y (a number), z (a number), radius (a number). Returns: a value (see the result of the example).
Also available in Python as `map_peaks_near_point_from_list_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |

### multi_residue_torsion

Python: `multi_residue_torsion(imol, residues_specs_py)`  
Scheme: `(multi-residue-torsion imol residues-specs-scm)`

create a multi-residue torsion dialog (user manipulation of torsions)

Arguments: imol (a whole number), residues_specs_py (a list or value). Returns: nothing.
Also available in Python as `multi_residue_torsion_py`.
Also available in Scheme as `multi-residue-torsion-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `multi_residue_torsion(0, ["A", 41, ""])` | not tried |
| Scheme | `(multi-residue-torsion 0 (list "A" 41 ""))` | not tried |

### probe_clash_score_as_py

Python: `probe_clash_score_as_py(p)`  
Scheme: `(probe-clash-score-as-scm p)`

Arguments: p (`coot::probe_clash_score_t`). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

### probe_clash_score_from_py

Python: `probe_clash_score_from_py(p)`  
Scheme: `(probe-clash-score-from-scm p)`

Arguments: p (a list or value). Returns: `coot::probe_clash_score_t`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

### screen_vectors

Python: `screen_vectors()`

BL says:: this probably shouldnt be here but cluster with KK code

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `screen_vectors_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `screen_vectors()` | not tried |

### set_difference_map_peaks_max_closeness

Python: `set_difference_map_peaks_max_closeness(m)`  
Scheme: `(set-difference-map-peaks-max-closeness m)`

set the max closeness (i.e. no smaller peaks can be within
 max_closeness of a larger peak)

In the GUI for difference map peaks, there is not a means to set the
max_closeness, so here is a means to set it and query it.

Arguments: m (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_difference_map_peaks_max_closeness(1.0)` | not tried |
| Scheme | `(set-difference-map-peaks-max-closeness 1.0)` | not tried |

### set_multi_residue_torsion_reverse_mode

Python: `set_multi_residue_torsion_reverse_mode(mode)`  
Scheme: `(set-multi-residue-torsion-reverse-mode mode)`

Arguments: mode (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_multi_residue_torsion_reverse_mode(1)` | not tried |
| Scheme | `(set-multi-residue-torsion-reverse-mode 1)` | not tried |

### set_torsion

Python: `set_torsion(imol, chain_id, res_no, insertion_code, alt_conf, atom_name_1, atom_name_2, atom_name_3, atom_name_4, tors)`  
Scheme: `(set-torsion imol chain-id res-no insertion-code alt-conf atom-name-1 atom-name-2 atom-name-3 atom-name-4 tors)`

set the given torsion the given residue. tors is in
 degrees. Return the resulting torsion (also in degrees).

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), insertion_code (text), alt_conf (text), atom_name_1 (text), atom_name_2 (text), atom_name_3 (text), atom_name_4 (text), tors (a number). Returns: a value (see the result of the example).
Also available in Python as `set_torsion_py`.
Also available in Scheme as `set-torsion-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_torsion(0, "A", 41, "", "", " CA ", " CA ", " CA ", " CA ", 1.0)` | not tried |
| Scheme | `(set-torsion 0 "A" 41 "" "" " CA " " CA " " CA " " CA " 1.0)` | not tried |

### setup_multi_residue_torsion

Python: `setup_multi_residue_torsion()`  
Scheme: `(setup-multi-residue-torsion)`

show the rotatable bonds dialog

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_multi_residue_torsion()` | not tried |
| Scheme | `(setup-multi-residue-torsion)` | not tried |

### show_multi_residue_torsion_dialog

Python: `show_multi_residue_torsion_dialog()`  
Scheme: `(show-multi-residue-torsion-dialog)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_multi_residue_torsion_dialog()` | not tried |
| Scheme | `(show-multi-residue-torsion-dialog)` | not tried |

