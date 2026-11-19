# Map Functions

[Scripting reference](../README.md) > Map Functions (35 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### average_map

Python: `average_map(map_number_and_scales)`  
Scheme: `(average-map map-number-and-scales)`

make an average map from the map_number_and_scales (which
 is a list of pairs [map_number, scale_factor] (the scale factors
 are typically 1.0 of course). The output map is in the same
 grid as the first (valid) map. Return -1 on failure to make an
 averaged map, otherwise return the new map molecule number.

Arguments: map_number_and_scales (a list or value). Returns: a whole number.
Also available in Python as `average_map_py`.
Also available in Scheme as `average-map-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### calc_phases_generic

Python: `calc_phases_generic(mtz_file_name)`  
Scheme: `(calc-phases-generic mtz-file-name)`

fire up a GUI, which asks us which model molecule we want
 to calc phases from. On "OK" button there, we call
 map_from_mtz_by_refmac_calc_phases()

Arguments: mtz_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `calc_phases_generic("rnasa-1.8-all_refmac1.mtz")` | ran (no return value) |
| Scheme | `(calc-phases-generic "rnasa-1.8-all_refmac1.mtz")` | ran (no return value) |

### calculate_maps_and_stats_py

Python: `calculate_maps_and_stats_py(imol_model, imol_map_with_data_attached, imol_map_2fofc, imol_map_fofc)`

Calculate structure factors and make a 2FoFC map and a Fo-Fc map updating the given
 molecule numbers for those maps - if thase molecule ids are not valid maps, them generate
 new maps (return the model number information in the returned object)

Arguments: imol_model (a whole number), imol_map_with_data_attached (a whole number), imol_map_2fofc (a whole number), imol_map_fofc (a whole number). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `calculate_maps_and_stats_py(0, 1, 1, 1)` | ran, returned `[-1.0, -1.0, -1.0, -1.0, []]` |

### data_resolution

Python: `data_resolution(imol)`  
Scheme: `(data-resolution imol)`

return the resolution of the data for molecule number imol.
 Return negative number on error, otherwise resolution in A (eg. 2.0)

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `data_resolution(0)` | ran, returned `-1.0` |
| Scheme | `(data-resolution 0)` | ran, returned `-1.0` |

### difference_map

Python: `difference_map(imol1, imol2, map_scale)`  
Scheme: `(difference-map imol1 imol2 map-scale)`

make a difference map, taking map_scale * imap2 from imap1,
 on the grid of imap1. Return the new molecule number.
 Return -1 on failure.

Arguments: imol1 (a whole number), imol2 (a whole number), map_scale (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `difference_map(0, 0, 1.0)` | ran, returned `-1` |
| Scheme | `(difference-map 0 0 1.0)` | ran, returned `-1` |

### export_map

Python: `export_map(imol, filename)`  
Scheme: `(export-map imol filename)`

export (write to disk) the map of molecule number imol to
 filename.

 Return 0 on failure, 1 on success.

Arguments: imol (a whole number), filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `export_map(0, "tutorial-modern.pdb")` | ran, returned `0` |
| Scheme | `(export-map 0 "tutorial-modern.pdb")` | ran, returned `0` |

### export_map_fragment

Python: `export_map_fragment(imol, x, y, z, radius, filename)`  
Scheme: `(export-map-fragment imol x y z radius filename)`

export a fragment of the map about (x,y,z)

Arguments: imol (a whole number), x (a number), y (a number), z (a number), radius (a number), filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `export_map_fragment(0, 54.5, 9.4, 12.3, 5.0, "tutorial-modern.pdb")` | ran, returned `0` |
| Scheme | `(export-map-fragment 0 54.5 9.4 12.3 5.0 "tutorial-modern.pdb")` | ran, returned `0` |

### export_map_fragment_to_plain_file

Python: `export_map_fragment_to_plain_file(imol, x, y, z, radius, filename)`  
Scheme: `(export-map-fragment-to-plain-file imol x y z radius filename)`

tmp interface for Hamish

Arguments: imol (a whole number), x (a number), y (a number), z (a number), radius (a number), filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `export_map_fragment_to_plain_file(0, 54.5, 9.4, 12.3, 5.0, "tutorial-modern.pdb")` | ran, returned `0` |
| Scheme | `(export-map-fragment-to-plain-file 0 54.5 9.4 12.3 5.0 "tutorial-modern.pdb")` | ran, returned `0` |

### export_map_fragment_with_origin_shift

Python: `export_map_fragment_with_origin_shift(imol, x, y, z, radius, filename)`  
Scheme: `(export-map-fragment-with-origin-shift imol x y z radius filename)`

export a fragment of the map about (x,y,z)

Arguments: imol (a whole number), x (a number), y (a number), z (a number), radius (a number), filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `export_map_fragment_with_origin_shift(0, 54.5, 9.4, 12.3, 5.0, "tutorial-modern.pdb")` | ran, returned `0` |
| Scheme | `(export-map-fragment-with-origin-shift 0 54.5 9.4 12.3 5.0 "tutorial-modern.pdb")` | ran, returned `0` |

### export_map_fragment_with_text_radius

Python: `export_map_fragment_with_text_radius(imol, radius_text, filename)`  
Scheme: `(export-map-fragment-with-text-radius imol radius-text filename)`

convenience function, called from callbacks.c

Arguments: imol (a whole number), radius_text (text), filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `export_map_fragment_with_text_radius(0, "hello", "tutorial-modern.pdb")` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(export-map-fragment-with-text-radius 0 "hello" "tutorial-modern.pdb")` | stopped Coot when tried without a window (not checked with a window) |

### get_active_map_drag_flag

Python: `get_active_map_drag_flag()`  
Scheme: `(get-active-map-drag-flag)`

return the state of the dragged map flag

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_active_map_drag_flag()` | ran, returned `1` |
| Scheme | `(get-active-map-drag-flag)` | ran, returned `1` |

### get_contour_level_absolute

Python: `get_contour_level_absolute(imol)`  
Scheme: `(get-contour-level-absolute imol)`

get the contour level

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_contour_level_absolute(0)` | ran, returned `0.0` |
| Scheme | `(get-contour-level-absolute 0)` | ran, returned `0.0` |

### get_contour_level_in_sigma

Python: `get_contour_level_in_sigma(imol)`  
Scheme: `(get-contour-level-in-sigma imol)`

get the contour level in rmd above 0.

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_contour_level_in_sigma(0)` | ran, returned `0.0` |
| Scheme | `(get-contour-level-in-sigma 0)` | ran, returned `0.0` |

### get_map_colour

Python: `get_map_colour(imol)`  
Scheme: `(get-map-colour imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_map_colour(0)` | ran, returned `False` |
| Scheme | `(get-map-colour 0)` | ran, returned `#f` |

### map_from_mtz_by_calc_phases

Python: `map_from_mtz_by_calc_phases(mtz_file_name, f_col, sigf_col, imol_coords)`  
Scheme: `(map-from-mtz-by-calc-phases mtz-file-name f-col sigf-col imol-coords)`

Calculate SFs from an MTZ file and generate a map.
 Returns the new molecule number.

Arguments: mtz_file_name (text), f_col (text), sigf_col (text), imol_coords (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_from_mtz_by_calc_phases("rnasa-1.8-all_refmac1.mtz", "FWT", "hello", 0)` | not tried |
| Scheme | `(map-from-mtz-by-calc-phases "rnasa-1.8-all_refmac1.mtz" "FWT" "hello" 0)` | not tried |

### map_from_mtz_by_refmac_calc_phases

Python: `map_from_mtz_by_refmac_calc_phases(mtz_file_name, f_col, sigf_col, imol_coords)`  
Scheme: `(map-from-mtz-by-refmac-calc-phases mtz-file-name f-col sigf-col imol-coords)`

Calculate SFs (using refmac optionally) from an MTZ file
 and generate a map. Get F and SIGF automatically (first of their
 type) from the mtz file.

Returns the new molecule number, -1 on a problem.

Arguments: mtz_file_name (text), f_col (text), sigf_col (text), imol_coords (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_from_mtz_by_refmac_calc_phases("rnasa-1.8-all_refmac1.mtz", "FWT", "hello", 0)` | not tried |
| Scheme | `(map-from-mtz-by-refmac-calc-phases "rnasa-1.8-all_refmac1.mtz" "FWT" "hello" 0)` | not tried |

### model_resolution

Python: `model_resolution(imol)`  
Scheme: `(model-resolution imol)`

return the resolution set in the header of the
 model/coordinates file. If this number is not available, return a
 number less than 0.

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `model_resolution(0)` | not tried |
| Scheme | `(model-resolution 0)` | not tried |

### reinterp_map

Python: `reinterp_map(map_no, reference_map_no)`  
Scheme: `(reinterp-map map-no reference-map-no)`

make a new map (a copy of map_no) that is in the cell,
 spacegroup and gridding of the map in reference_map_no.

Return the new map molecule number - return -1 on failure

Arguments: map_no (a whole number), reference_map_no (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `reinterp_map(1, 1)` | not tried |
| Scheme | `(reinterp-map 1 1)` | not tried |

### restore_previous_map_colour

Python: `restore_previous_map_colour(imol)`  
Scheme: `(restore-previous-map-colour imol)`

restore previous colour map for molecule number imol

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `restore_previous_map_colour(0)` | not tried |
| Scheme | `(restore-previous-map-colour 0)` | not tried |

### save_previous_map_colour

Python: `save_previous_map_colour(imol)`  
Scheme: `(save-previous-map-colour imol)`

save previous colour map for molecule number imol

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_previous_map_colour(0)` | not tried |
| Scheme | `(save-previous-map-colour 0)` | not tried |

### scroll_wheel_map

Python: `scroll_wheel_map()`  
Scheme: `(scroll-wheel-map)`

the contouring of which map is altered when the scroll wheel changes?

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `scroll_wheel_map()` | not tried |
| Scheme | `(scroll-wheel-map)` | not tried |

### set_active_map_drag_flag

Python: `set_active_map_drag_flag(t)`  
Scheme: `(set-active-map-drag-flag t)`

set the state of immediate map upate on map drag.

By default, it is on (t=1). On slower computers it might be better to
set t=0.

Arguments: t (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_active_map_drag_flag(1)` | not tried |
| Scheme | `(set-active-map-drag-flag 1)` | not tried |

### set_auto_updating_sfcalc_genmap

Python: `set_auto_updating_sfcalc_genmap(imol_model, imol_map_with_data_attached, imol_updating_difference_map)`  
Scheme: `(set-auto-updating-sfcalc-genmap imol-model imol-map-with-data-attached imol-updating-difference-map)`

As above, calculate structure factors from the model and update the given difference
 map accordingly - but difference map gets updated automatically on modification of
 the imol_model molecule

Arguments: imol_model (a whole number), imol_map_with_data_attached (a whole number), imol_updating_difference_map (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_auto_updating_sfcalc_genmap(0, 1, 1)` | not tried |
| Scheme | `(set-auto-updating-sfcalc-genmap 0 1 1)` | not tried |

### set_auto_updating_sfcalc_genmaps

Python: `set_auto_updating_sfcalc_genmaps(imol_model, imol_map_with_data_attached, imol_updating_2fofc_map, imol_updating_difference_map)`  
Scheme: `(set-auto-updating-sfcalc-genmaps imol-model imol-map-with-data-attached imol-updating-2fofc-map imol-updating-difference-map)`

As above, calculate structure factors from the model and update the given difference
 map accordingly - but the 2fofc and difference map get updated automatically on modification of
 the imol_model molecule

Arguments: imol_model (a whole number), imol_map_with_data_attached (a whole number), imol_updating_2fofc_map (a whole number), imol_updating_difference_map (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_auto_updating_sfcalc_genmaps(0, 1, 1, 1)` | not tried |
| Scheme | `(set-auto-updating-sfcalc-genmaps 0 1 1 1)` | not tried |

### set_contour_by_sigma_step_by_mol

Python: `set_contour_by_sigma_step_by_mol(f, state, imol)`  
Scheme: `(set-contour-by-sigma-step-by-mol f state imol)`

set the contour level step

 set the contour level step of molecule number imol to f and
 variable state (setting state to 0 turns off contouring by sigma
 level)

Arguments: f (a number), state (a whole number), imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_contour_by_sigma_step_by_mol(1.0, 1, 0)` | not tried |
| Scheme | `(set-contour-by-sigma-step-by-mol 1.0 1 0)` | not tried |

### set_contour_level_absolute

Python: `set_contour_level_absolute(imol_map, level)`  
Scheme: `(set-contour-level-absolute imol-map level)`

set the contour level, direct control

Arguments: imol_map (a whole number), level (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_contour_level_absolute(1, 1.5)` | not tried |
| Scheme | `(set-contour-level-absolute 1 1.5)` | not tried |

### set_contour_level_in_sigma

Python: `set_contour_level_in_sigma(imol_map, level)`  
Scheme: `(set-contour-level-in-sigma imol-map level)`

set the contour level, direct control in r.m.s.d. (if you like that sort of thing)

Arguments: imol_map (a whole number), level (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_contour_level_in_sigma(1, 1.5)` | not tried |
| Scheme | `(set-contour-level-in-sigma 1 1.5)` | not tried |

### set_last_map_colour

Python: `set_last_map_colour(f1, f2, f3)`  
Scheme: `(set-last-map-colour f1 f2 f3)`

set the colour of the last (highest molecule number) map

Arguments: f1 (a number), f2 (a number), f3 (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_last_map_colour(1.0, 1.0, 1.0)` | not tried |
| Scheme | `(set-last-map-colour 1.0 1.0 1.0)` | not tried |

### set_last_map_sigma_step

Python: `set_last_map_sigma_step(f)`  
Scheme: `(set-last-map-sigma-step f)`

set the sigma step of the last map to f sigma

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_last_map_sigma_step(1.0)` | not tried |
| Scheme | `(set-last-map-sigma-step 1.0)` | not tried |

### set_map_colour

Python: `set_map_colour(imol, red, green, blue)`  
Scheme: `(set-map-colour imol red green blue)`

set the colour of the imolth map

Arguments: imol (a whole number), red (a number), green (a number), blue (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_map_colour(0, 0.5, 0.5, 0.5)` | not tried |
| Scheme | `(set-map-colour 0 0.5 0.5 0.5)` | not tried |

### set_scroll_wheel_map

Python: `set_scroll_wheel_map(imap)`  
Scheme: `(set-scroll-wheel-map imap)`

set the map that is moved by changing the scroll wheel and
 change_contour_level().

Arguments: imap (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_scroll_wheel_map(1)` | not tried |
| Scheme | `(set-scroll-wheel-map 1)` | not tried |

### set_scrollable_map

Python: `set_scrollable_map(imol)`  
Scheme: `(set-scrollable-map imol)`

set the map that has its contour level changed by the
 scrolling the mouse wheel to molecule number imol (same as set_scroll_wheel_map()).

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_scrollable_map(0)` | not tried |
| Scheme | `(set-scrollable-map 0)` | not tried |

### sfcalc_genmap

Python: `sfcalc_genmap(imol_model, imol_map_with_data_attached, imol_updating_difference_map)`  
Scheme: `(sfcalc-genmap imol-model imol-map-with-data-attached imol-updating-difference-map)`

Calculate structure factors from the model and update the given difference
 map accordingly

Arguments: imol_model (a whole number), imol_map_with_data_attached (a whole number), imol_updating_difference_map (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `sfcalc_genmap(0, 1, 1)` | not tried |
| Scheme | `(sfcalc-genmap 0 1 1)` | not tried |

### smooth_map

Python: `smooth_map(map_no, sampling_multiplier)`  
Scheme: `(smooth-map map-no sampling-multiplier)`

make a new map (a copy of map_no) that is in the cell,
 spacegroup and a multiple of the sampling of the input map (a
 sampling factor of more than 1 makes the output maps smoother)

Arguments: map_no (a whole number), sampling_multiplier (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `smooth_map(1, 1.0)` | not tried |
| Scheme | `(smooth-map 1 1.0)` | not tried |

### transform_map_raw

Python: `transform_map_raw(imol, r00, r01, r02, r10, r11, r12, r20, r21, r22, t0, t1, t2, pt0, pt1, pt2, box_half_size, ref_space_group, cell_a, cell_b, cell_c, alpha, beta, gamma)`  
Scheme: `(transform-map-raw imol r00 r01 r02 r10 r11 r12 r20 r21 r22 t0 t1 t2 pt0 pt1 pt2 box-half-size ref-space-group cell-a cell-b cell-c alpha beta gamma)`

return the new molecule number. The cell is given in Angstroms and
 the angles in degrees. The ref_space_group can be a H-M symbol or
 a colon-separated string of symmetry operators.

Arguments: imol (a whole number), r00 (a number), r01 (a number), r02 (a number), r10 (a number), r11 (a number), r12 (a number), r20 (a number), r21 (a number), r22 (a number), t0 (a number), t1 (a number), t2 (a number), pt0 (a number), pt1 (a number), pt2 (a number), box_half_size (a number), ref_space_group (text), cell_a (a number), cell_b (a number), cell_c (a number), alpha (a number), beta (a number), gamma (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `transform_map_raw(0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, "hello", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)` | not tried |
| Scheme | `(transform-map-raw 0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 "hello" 1.0 1.0 1.0 1.0 1.0 1.0)` | not tried |

