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

Python and Scheme gave the same answer.

### c_beta_deviations_py

Python: `c_beta_deviations_py(imol)`  
Scheme: `(c-beta-deviations imol)`

Many more things should go or be moved to here

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Scheme as `c-beta-deviations-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `c_beta_deviations_py(0)` | ran, returned `[[[True, 'A', 17, ''], {'': 0.13465415823304944}], [[True, 'A', 1, ''], {'': 0.16953483228562496}], [[True, 'A', 2, ''], ...` |
| Scheme | `(c-beta-deviations 0)` | ran, returned `(((#t "A" 25 "") (("" 0.0779894024924761))) ((#t "A" 20 "") (("" 0.07846646398291499))) ((#t "A" 21 "") (("" 0.083184420 ...` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### clear_diff_map_peaks

Python: `clear_diff_map_peaks()`  
Scheme: `(clear-diff-map-peaks)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_diff_map_peaks()` | ran (no return value, nothing visible changed) |
| Scheme | `(clear-diff-map-peaks)` | ran (no return value, nothing visible changed) |

### clear_multi_residue_torsion_mode

Python: `clear_multi_residue_torsion_mode()`  
Scheme: `(clear-multi-residue-torsion-mode)`

These functions are called from callbacks.c

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_multi_residue_torsion_mode()` | ran (no return value, nothing visible changed) |
| Scheme | `(clear-multi-residue-torsion-mode)` | ran (no return value, nothing visible changed) |

### deviant_geometry

Python: `deviant_geometry(imol)`  
Scheme: `(deviant-geometry imol)`

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `deviant_geometry(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(deviant-geometry 0)` | ran (no return value, nothing visible changed) |

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
| Python | `difference_map_peaks(0, 0, 1.5, 1.0, 1, 1, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(difference-map-peaks 0 0 1.5 1.0 1 1 1)` | ran (no return value, nothing visible changed) |

### difference_map_peaks_max_closeness

Python: `difference_map_peaks_max_closeness()`  
Scheme: `(difference-map-peaks-max-closeness)`

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `difference_map_peaks_max_closeness()` | ran, returned `2.0` |
| Scheme | `(difference-map-peaks-max-closeness)` | ran, returned `2.0` |

Python and Scheme gave the same answer.

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

Python and Scheme gave the same answer.

### gln_asn_b_factor_outliers

Python: `gln_asn_b_factor_outliers(imol)`  
Scheme: `(gln-asn-b-factor-outliers imol)`

Make a gui for GLN adn ASN B-factor outiers, compairing the
 O and N temperatur factors difference to the distribution of
 temperature factors from the other atoms.

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `gln_asn_b_factor_outliers(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(gln-asn-b-factor-outliers 0)` | ran (no return value, nothing visible changed) |

### is_valid_map_molecule

Python: `is_valid_map_molecule(imol)`  
Scheme: `(is-valid-map-molecule imol)`

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `is_valid_map_molecule(1)` | ran, returned `1` |
| Scheme | `(is-valid-map-molecule 1)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: 1 for map molecule 1, 0 for the model molecule 0 or an unused number.

Python and Scheme gave the same answer.

### is_valid_model_molecule

Python: `is_valid_model_molecule(imol)`  
Scheme: `(is-valid-model-molecule imol)`

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `is_valid_model_molecule(0)` | ran, returned `1` |
| Scheme | `(is-valid-model-molecule 0)` | ran, returned `1` |

Python and Scheme gave the same answer.

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
| Python | `map_peaks(1, 1.5)` | ran, returned `[[58.71012697972355, 8.723667220957577, 32.92142303206025], [58.09156606964766, 11.74520870289532, 27.625261377819815],  ...` |
| Scheme | `(map-peaks 1 1.5)` | ran, returned `((58.71012697972355 8.723667220957577 32.92142303206025) (58.09156606964766 11.74520870289532 27.625261377819815) (5.139 ...` |

Python and Scheme gave the same answer.

### map_peaks_around_molecule

Python: `map_peaks_around_molecule(imol_map, sigma, negative_also_flag, imol_coords)`

Arguments: imol_map (a whole number), sigma (a number), negative_also_flag (a whole number), imol_coords (a whole number). Returns: a value (see the result of the example).
Also available in Python as `map_peaks_around_molecule_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_peaks_around_molecule(1, 1.5, 1, 0)` | ran, returned `[[3.4549152851104736, [58.71012697972355, 8.723667220957578, -5.8705767848342845]], [3.000621795654297, [25.643064482733 ...` |

### map_peaks_near_point

Python: `map_peaks_near_point(imol_map, n_sigma, x, y, z, radius)`  
Scheme: `(map-peaks-near-point imol-map n-sigma x y z radius)`

Arguments: imol_map (a whole number), n_sigma (a number), x (a number), y (a number), z (a number), radius (a number). Returns: a value (see the result of the example).
Also available in Python as `map_peaks_near_point_py`.
Also available in Scheme as `map-peaks-near-point-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_peaks_near_point(1, 1.5, 54.5, 9.4, 12.3, 5.0)` | ran, returned `[]` |
| Scheme | `(map-peaks-near-point 1 1.5 54.5 9.4 12.3 5.0)` | ran, returned `()` |

Python and Scheme gave the same answer.

### map_peaks_near_point_from_list

Python: `map_peaks_near_point_from_list(imol_map, peak_list, x, y, z, radius)`

Arguments: imol_map (a whole number), peak_list (a list or value), x (a number), y (a number), z (a number), radius (a number). Returns: a value (see the result of the example).
Also available in Python as `map_peaks_near_point_from_list_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_peaks_near_point_from_list(1, [[48.3, 7.4, 16.9], [10.0, 10.0, 10.0]], 48.0, 7.0, 17.0, 5.0)` | ran, returned `[[48.3, 7.4, 16.9]]` |

Example written and checked by hand on the test data. Expected: the peaks of the given list that lie within 5 A of (48, 7, 17): only the first one. (Python only.).

### multi_residue_torsion

Python: `multi_residue_torsion(imol, residues_specs_py)`  
Scheme: `(multi-residue-torsion imol residues-specs-scm)`

create a multi-residue torsion dialog (user manipulation of torsions)

Arguments: imol (a whole number), residues_specs_py (a list or value). Returns: nothing.
Also available in Python as `multi_residue_torsion_py`.
Also available in Scheme as `multi-residue-torsion-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `multi_residue_torsion(0, [[True, "A", 41, ""], [True, "A", 42, ""]])` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(multi-residue-torsion 0 (list (list #t "A" 41 "") (list #t "A" 42 "")))` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens the multi-residue torsion dialog for residues A41-A42 (the torsions can then be dragged).

### probe_clash_score_as_py

Python: `probe_clash_score_as_py(p)`  
Scheme: `(probe-clash-score-as-scm p)`

Arguments: p (`coot::probe_clash_score_t`). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `probe_clash_score_as_py(probe_clash_score_from_py([2, 10, 30, 400, 900]))` | ran, returned `[2, 10, 30, 400, 900]` |
| Scheme | `(probe-clash-score-as-scm (probe-clash-score-from-scm (list 2 10 30 400 900)))` | ran, returned `(2 10 30 400 900)` |

Example written and checked by hand on the test data. Expected: the clash score as a list [bad overlaps, H-bonds, small overlaps, close contacts, wide contacts]; round trip gives the input back.

Note: Fixed in coot0 build 31: Scheme's probe-clash-score-from-scm took the 5th number (wide contacts) from the 4th element, so (2 10 30 400 900) came back as (2 10 30 400 400).

Python and Scheme gave the same answer.

### probe_clash_score_from_py

Python: `probe_clash_score_from_py(p)`  
Scheme: `(probe-clash-score-from-scm p)`

Arguments: p (a list or value). Returns: `coot::probe_clash_score_t`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `probe_clash_score_from_py([2, 10, 30, 400, 900])` | ran, returned `<coot.probe_clash_score_t; proxy of <Swig Object of type 'coot::probe_clash_score_t *' at 0x10bf2f810> >` |
| Scheme | `(probe-clash-score-from-scm (list 2 10 30 400 900))` | ran, returned `#<collectable-swig-pointer coot::probe_clash_score_t * 92ad41a60>` |

Example written and checked by hand on the test data. Expected: a C++ probe clash score object from 5 numbers; prints 'debug::' lines to the terminal.

Note: Fixed in coot0 build 31: the 5th number (wide contacts) was taken from the 4th element in Scheme.

### screen_vectors

Python: `screen_vectors()`

BL says:: this probably shouldnt be here but cluster with KK code

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `screen_vectors_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `screen_vectors()` | ran (no return value, nothing visible changed) |

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
| Python | `set_difference_map_peaks_max_closeness(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-difference-map-peaks-max-closeness 1.0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: difference_map_peaks_max_closeness was 2.0, set to 3.5, read back 3.5; Scheme: difference-map-peaks-max-closeness was 2.0, set to 3.5, read back 3.5.

### set_multi_residue_torsion_reverse_mode

Python: `set_multi_residue_torsion_reverse_mode(mode)`  
Scheme: `(set-multi-residue-torsion-reverse-mode mode)`

Arguments: mode (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_multi_residue_torsion_reverse_mode(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-multi-residue-torsion-reverse-mode 1)` | ran (no return value, nothing visible changed) |

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
| Python | `set_torsion(0, "A", 41, "", "", " CA ", " CA ", " CA ", " CA ", 1.0)` | ran, returned `nan` |
| Scheme | `(set-torsion 0 "A" 41 "" "" " CA " " CA " " CA " " CA " 1.0)` | ran, returned `+nan.0` |

Python and Scheme gave the same answer.

### setup_multi_residue_torsion

Python: `setup_multi_residue_torsion()`  
Scheme: `(setup-multi-residue-torsion)`

show the rotatable bonds dialog

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_multi_residue_torsion()` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(setup-multi-residue-torsion)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: starts the pick mode / dialog for choosing the residues of a multi-residue torsion edit.

### show_multi_residue_torsion_dialog

Python: `show_multi_residue_torsion_dialog()`  
Scheme: `(show-multi-residue-torsion-dialog)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_multi_residue_torsion_dialog()` | ran (no return value, nothing visible changed) |
| Scheme | `(show-multi-residue-torsion-dialog)` | ran (no return value, nothing visible changed) |

