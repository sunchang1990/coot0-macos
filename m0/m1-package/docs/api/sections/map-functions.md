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
| Python | first `imap2 = map_from_mtz_by_calc_phases("rnasa-1.8-all_refmac1.mtz", "FGMP18", "SIGFGMP18", 0)`, then `average_map([[1, 1.0], [imap2, 1.0]])` | ran, returned `4`; changed: new molecule 4 (map, averaged-map); graphics_n_molecules(): 4 -> 5 |
| Scheme | first `(define imap2 (map-from-mtz-by-calc-phases "rnasa-1.8-all_refmac1.mtz" "FGMP18" "SIGFGMP18" 0))`, then `(average-map (list (list 1 1.0) (list imap2 1.0)))` | ran, returned `4`; changed: new molecule 4 (map, averaged-map); graphics_n_molecules(): 4 -> 5 |

Example written and checked by hand on the test data. Expected: returns a new map that is the scaled average of the listed [map, scale] pairs (on the first map's grid).

Python and Scheme gave the same answer.

### calc_phases_generic

Python: `calc_phases_generic(mtz_file_name)`  
Scheme: `(calc-phases-generic mtz-file-name)`

fire up a GUI, which asks us which model molecule we want
 to calc phases from. On "OK" button there, we call
 map_from_mtz_by_refmac_calc_phases()

Arguments: mtz_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `calc_phases_generic("rnasa-1.8-all_refmac1.mtz")` | ran (no return value, nothing visible changed) |
| Scheme | `(calc-phases-generic "rnasa-1.8-all_refmac1.mtz")` | ran (no return value, nothing visible changed) |

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
| Python | `data_resolution(1)` | ran, returned `1.8460990190505981` |
| Scheme | `(data-resolution 1)` | ran, returned `1.8460990190505981` |

Example written and checked by hand on the test data. Expected: returns the resolution (A) of the data behind map 1; negative on error.

Python and Scheme gave the same answer.

### difference_map

Python: `difference_map(imol1, imol2, map_scale)`  
Scheme: `(difference-map imol1 imol2 map-scale)`

make a difference map, taking map_scale * imap2 from imap1,
 on the grid of imap1. Return the new molecule number.
 Return -1 on failure.

Arguments: imol1 (a whole number), imol2 (a whole number), map_scale (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `imap2 = map_from_mtz_by_calc_phases("rnasa-1.8-all_refmac1.mtz", "FGMP18", "SIGFGMP18", 0)`, then `difference_map(1, imap2, 1.0)` | ran, returned `4`; changed: new molecule 4 (map, difference-map); graphics_n_molecules(): 4 -> 5 |
| Scheme | first `(define imap2 (map-from-mtz-by-calc-phases "rnasa-1.8-all_refmac1.mtz" "FGMP18" "SIGFGMP18" 0))`, then `(difference-map 1 imap2 1.0)` | ran, returned `4`; changed: new molecule 4 (map, difference-map); graphics_n_molecules(): 4 -> 5 |

Example written and checked by hand on the test data. Expected: returns the new map molecule (map1 - scale*map2 on map1's grid), marked as a difference map; -1 if either is not a map.

Python and Scheme gave the same answer.

### export_map

Python: `export_map(imol, filename)`  
Scheme: `(export-map imol filename)`

export (write to disk) the map of molecule number imol to
 filename.

 Return 0 on failure, 1 on success.

Arguments: imol (a whole number), filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `export_map(1, "map1.map")` | ran, returned `1` |
| Scheme | `(export-map 1 "map1.map")` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 and writes the whole map as a CCP4 map file; 0 on failure.

Python and Scheme gave the same answer.

### export_map_fragment

Python: `export_map_fragment(imol, x, y, z, radius, filename)`  
Scheme: `(export-map-fragment imol x y z radius filename)`

export a fragment of the map about (x,y,z)

Arguments: imol (a whole number), x (a number), y (a number), z (a number), radius (a number), filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `export_map_fragment(1, 47.1, 10.6, 17.4, 8.0, "frag.map")` | ran, returned `1` |
| Scheme | `(export-map-fragment 1 47.1 10.6 17.4 8.0 "frag.map")` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 and writes a CCP4 map of the density within the radius of (x, y, z).

Python and Scheme gave the same answer.

### export_map_fragment_to_plain_file

Python: `export_map_fragment_to_plain_file(imol, x, y, z, radius, filename)`  
Scheme: `(export-map-fragment-to-plain-file imol x y z radius filename)`

tmp interface for Hamish

Arguments: imol (a whole number), x (a number), y (a number), z (a number), radius (a number), filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `export_map_fragment_to_plain_file(1, 47.1, 10.6, 17.4, 4.0, "frag.txt")` | ran, returned `1` |
| Scheme | `(export-map-fragment-to-plain-file 1 47.1 10.6 17.4 4.0 "frag.txt")` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 and writes the density values around the point to a plain text file.

Python and Scheme gave the same answer.

### export_map_fragment_with_origin_shift

Python: `export_map_fragment_with_origin_shift(imol, x, y, z, radius, filename)`  
Scheme: `(export-map-fragment-with-origin-shift imol x y z radius filename)`

export a fragment of the map about (x,y,z)

Arguments: imol (a whole number), x (a number), y (a number), z (a number), radius (a number), filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `export_map_fragment_with_origin_shift(1, 47.1, 10.6, 17.4, 8.0, "frag-shift.map")` | ran, returned `1` |
| Scheme | `(export-map-fragment-with-origin-shift 1 47.1 10.6 17.4 8.0 "frag-shift.map")` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 and writes a CCP4 map fragment whose origin is moved to the fragment.

Python and Scheme gave the same answer.

### export_map_fragment_with_text_radius

Python: `export_map_fragment_with_text_radius(imol, radius_text, filename)`  
Scheme: `(export-map-fragment-with-text-radius imol radius-text filename)`

convenience function, called from callbacks.c

Arguments: imol (a whole number), radius_text (text), filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `set_rotation_centre(47.1, 10.6, 17.4)`, then `export_map_fragment_with_text_radius(1, "10", "frag-text.map")` | ran (no return value, nothing visible changed) |
| Scheme | first `(set-rotation-centre 47.1 10.6 17.4)`, then `(export-map-fragment-with-text-radius 1 "10" "frag-text.map")` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: writes a map fragment of the given radius (as text, an integer) around the rotation centre.

Note: The radius text is parsed as an integer; the earlier automatic example with a non-number string stopped Coot (uncaught exception).

### get_active_map_drag_flag

Python: `get_active_map_drag_flag()`  
Scheme: `(get-active-map-drag-flag)`

return the state of the dragged map flag

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_active_map_drag_flag()` | ran, returned `1` |
| Scheme | `(get-active-map-drag-flag)` | ran, returned `1` |

Python and Scheme gave the same answer.

### get_contour_level_absolute

Python: `get_contour_level_absolute(imol)`  
Scheme: `(get-contour-level-absolute imol)`

get the contour level

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_contour_level_absolute(0)` | ran, returned `0.0` |
| Scheme | `(get-contour-level-absolute 0)` | ran, returned `0.0` |

Python and Scheme gave the same answer.

### get_contour_level_in_sigma

Python: `get_contour_level_in_sigma(imol)`  
Scheme: `(get-contour-level-in-sigma imol)`

get the contour level in rmd above 0.

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_contour_level_in_sigma(0)` | ran, returned `0.0` |
| Scheme | `(get-contour-level-in-sigma 0)` | ran, returned `0.0` |

Python and Scheme gave the same answer.

### get_map_colour

Python: `get_map_colour(imol)`  
Scheme: `(get-map-colour imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_map_colour(1)` | ran, returned `[0.19999998807907104, 0.38333338499069214, 0.699999988079071]` |
| Scheme | `(get-map-colour 1)` | ran, returned `(0.19999998807907104 0.38333338499069214 0.699999988079071)` |

Example written and checked by hand on the test data. Expected: returns the map's RGB colour (0-1 each); False if not a map.

Python and Scheme gave the same answer.

### map_from_mtz_by_calc_phases

Python: `map_from_mtz_by_calc_phases(mtz_file_name, f_col, sigf_col, imol_coords)`  
Scheme: `(map-from-mtz-by-calc-phases mtz-file-name f-col sigf-col imol-coords)`

Calculate SFs from an MTZ file and generate a map.
 Returns the new molecule number.

Arguments: mtz_file_name (text), f_col (text), sigf_col (text), imol_coords (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_from_mtz_by_calc_phases("rnasa-1.8-all_refmac1.mtz", "FGMP18", "SIGFGMP18", 0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(map-from-mtz-by-calc-phases "rnasa-1.8-all_refmac1.mtz" "FGMP18" "SIGFGMP18" 0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz); graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the new map molecule made from Fobs and phases calculated from the model; -1 on failure.

Note: With column names that are not in the file ("FP", "SIGFP") Coot aborts (Abort trap: uncaught exception) instead of returning -1.

Python and Scheme gave the same answer.

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
| Python | `map_from_mtz_by_refmac_calc_phases("rnasa-1.8-all_refmac1.mtz", "FGMP18", "SIGFGMP18", 0)` | not run: runs refmac |
| Scheme | `(map-from-mtz-by-refmac-calc-phases "rnasa-1.8-all_refmac1.mtz" "FGMP18" "SIGFGMP18" 0)` | not run: runs refmac |

Example written and checked by hand on the test data. Expected: returns a new map molecule calculated with refmac phases from the model (see map_from_mtz_by_calc_phases for the internal version).

### model_resolution

Python: `model_resolution(imol)`  
Scheme: `(model-resolution imol)`

return the resolution set in the header of the
 model/coordinates file. If this number is not available, return a
 number less than 0.

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `model_resolution(0)` | ran, returned `-1.0` |
| Scheme | `(model-resolution 0)` | ran, returned `-1.0` |

Example written and checked by hand on the test data. Expected: returns the resolution from the coordinate file header; -1 when the header has none (correct for tutorial-modern.pdb, whose REMARK 3 gives no parsed resolution).

Python and Scheme gave the same answer.

### reinterp_map

Python: `reinterp_map(map_no, reference_map_no)`  
Scheme: `(reinterp-map map-no reference-map-no)`

make a new map (a copy of map_no) that is in the cell,
 spacegroup and gridding of the map in reference_map_no.

Return the new map molecule number - return -1 on failure

Arguments: map_no (a whole number), reference_map_no (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `reinterp_map(1, 1)` | ran, returned `3`; changed: new molecule 3 (map, map 1 re-interprolated to match 1); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(reinterp-map 1 1)` | ran, returned `3`; changed: new molecule 3 (map, map 1 re-interprolated to match 1); graphics_n_molecules(): 3 -> 4 |

Python and Scheme gave the same answer.

### restore_previous_map_colour

Python: `restore_previous_map_colour(imol)`  
Scheme: `(restore-previous-map-colour imol)`

restore previous colour map for molecule number imol

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `restore_previous_map_colour(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(restore-previous-map-colour 0)` | ran (no return value, nothing visible changed) |

### save_previous_map_colour

Python: `save_previous_map_colour(imol)`  
Scheme: `(save-previous-map-colour imol)`

save previous colour map for molecule number imol

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_previous_map_colour(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(save-previous-map-colour 0)` | ran (no return value, nothing visible changed) |

### scroll_wheel_map

Python: `scroll_wheel_map()`  
Scheme: `(scroll-wheel-map)`

the contouring of which map is altered when the scroll wheel changes?

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `scroll_wheel_map()` | ran, returned `-1` |
| Scheme | `(scroll-wheel-map)` | ran, returned `-1` |

Python and Scheme gave the same answer.

### set_active_map_drag_flag

Python: `set_active_map_drag_flag(t)`  
Scheme: `(set-active-map-drag-flag t)`

set the state of immediate map upate on map drag.

By default, it is on (t=1). On slower computers it might be better to
set t=0.

Arguments: t (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_active_map_drag_flag(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-active-map-drag-flag 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_active_map_drag_flag was 1, set to 0, read back 0; Scheme: get-active-map-drag-flag was 1, set to 0, read back 0.

### set_auto_updating_sfcalc_genmap

Python: `set_auto_updating_sfcalc_genmap(imol_model, imol_map_with_data_attached, imol_updating_difference_map)`  
Scheme: `(set-auto-updating-sfcalc-genmap imol-model imol-map-with-data-attached imol-updating-difference-map)`

As above, calculate structure factors from the model and update the given difference
 map accordingly - but difference map gets updated automatically on modification of
 the imol_model molecule

Arguments: imol_model (a whole number), imol_map_with_data_attached (a whole number), imol_updating_difference_map (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_auto_updating_sfcalc_genmap(0, 1, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-auto-updating-sfcalc-genmap 0 1 1)` | ran (no return value, nothing visible changed) |

### set_auto_updating_sfcalc_genmaps

Python: `set_auto_updating_sfcalc_genmaps(imol_model, imol_map_with_data_attached, imol_updating_2fofc_map, imol_updating_difference_map)`  
Scheme: `(set-auto-updating-sfcalc-genmaps imol-model imol-map-with-data-attached imol-updating-2fofc-map imol-updating-difference-map)`

As above, calculate structure factors from the model and update the given difference
 map accordingly - but the 2fofc and difference map get updated automatically on modification of
 the imol_model molecule

Arguments: imol_model (a whole number), imol_map_with_data_attached (a whole number), imol_updating_2fofc_map (a whole number), imol_updating_difference_map (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_auto_updating_sfcalc_genmaps(0, 1, 1, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-auto-updating-sfcalc-genmaps 0 1 1 1)` | ran (no return value, nothing visible changed) |

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
| Python | `set_contour_by_sigma_step_by_mol(1.0, 1, 0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-contour-by-sigma-step-by-mol 1.0 1 0)` | ran (no return value, nothing visible changed) |

### set_contour_level_absolute

Python: `set_contour_level_absolute(imol_map, level)`  
Scheme: `(set-contour-level-absolute imol-map level)`

set the contour level, direct control

Arguments: imol_map (a whole number), level (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_contour_level_absolute(1, 1.5)` | ran (no return value); changed: map 1 contour level: 0.56 -> 1.5; get_contour_level_absolute(1): 0.56 -> 1.5; get_contour_level_in_sigma(1): 1.499 -> 4.016 |
| Scheme | `(set-contour-level-absolute 1 1.5)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_contour_level_absolute was 0.5600000023841858, set to 1.34, read back 1.340000033378601; Scheme: get-contour-level-absolute was 0.5600000023841858, set to 1.34, read back 1.340000033378601.

### set_contour_level_in_sigma

Python: `set_contour_level_in_sigma(imol_map, level)`  
Scheme: `(set-contour-level-in-sigma imol-map level)`

set the contour level, direct control in r.m.s.d. (if you like that sort of thing)

Arguments: imol_map (a whole number), level (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_contour_level_in_sigma(1, 1.5)` | ran (no return value); changed: map 1 contour level: 1.5 -> 0.5602; get_contour_level_absolute(1): 1.5 -> 0.5602; get_contour_level_in_sigma(1): 4.016 -> 1.5 |
| Scheme | `(set-contour-level-in-sigma 1 1.5)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_contour_level_in_sigma was 1.4993457794189453, set to 2.749, read back 2.749000072479248; Scheme: get-contour-level-in-sigma was 1.4993457794189453, set to 2.749, read back 2.749000072479248.

### set_last_map_colour

Python: `set_last_map_colour(f1, f2, f3)`  
Scheme: `(set-last-map-colour f1 f2 f3)`

set the colour of the last (highest molecule number) map

Arguments: f1 (a number), f2 (a number), f3 (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_last_map_colour(1.0, 1.0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-last-map-colour 1.0 1.0 1.0)` | ran (no return value, nothing visible changed) |

### set_last_map_sigma_step

Python: `set_last_map_sigma_step(f)`  
Scheme: `(set-last-map-sigma-step f)`

set the sigma step of the last map to f sigma

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_last_map_sigma_step(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-last-map-sigma-step 1.0)` | ran (no return value, nothing visible changed) |

### set_map_colour

Python: `set_map_colour(imol, red, green, blue)`  
Scheme: `(set-map-colour imol red green blue)`

set the colour of the imolth map

Arguments: imol (a whole number), red (a number), green (a number), blue (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_map_colour(0, 0.5, 0.5, 0.5)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-map-colour 0 0.5 0.5 0.5)` | ran (no return value, nothing visible changed) |

### set_scroll_wheel_map

Python: `set_scroll_wheel_map(imap)`  
Scheme: `(set-scroll-wheel-map imap)`

set the map that is moved by changing the scroll wheel and
 change_contour_level().

Arguments: imap (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_scroll_wheel_map(1)` | ran (no return value); changed: scroll_wheel_map(): -1 -> 1 |
| Scheme | `(set-scroll-wheel-map 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back; NOT all read back): Python: scroll_wheel_map was 1, set to 0, read back 1 (not taken); Scheme: scroll-wheel-map was 1, set to 0, read back 1 (not taken).

### set_scrollable_map

Python: `set_scrollable_map(imol)`  
Scheme: `(set-scrollable-map imol)`

set the map that has its contour level changed by the
 scrolling the mouse wheel to molecule number imol (same as set_scroll_wheel_map()).

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_scrollable_map(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-scrollable-map 0)` | ran (no return value, nothing visible changed) |

### sfcalc_genmap

Python: `sfcalc_genmap(imol_model, imol_map_with_data_attached, imol_updating_difference_map)`  
Scheme: `(sfcalc-genmap imol-model imol-map-with-data-attached imol-updating-difference-map)`

Calculate structure factors from the model and update the given difference
 map accordingly

Arguments: imol_model (a whole number), imol_map_with_data_attached (a whole number), imol_updating_difference_map (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `sfcalc_genmap(0, 1, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(sfcalc-genmap 0 1 1)` | ran (no return value, nothing visible changed) |

### smooth_map

Python: `smooth_map(map_no, sampling_multiplier)`  
Scheme: `(smooth-map map-no sampling-multiplier)`

make a new map (a copy of map_no) that is in the cell,
 spacegroup and a multiple of the sampling of the input map (a
 sampling factor of more than 1 makes the output maps smoother)

Arguments: map_no (a whole number), sampling_multiplier (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `smooth_map(1, 1.0)` | ran, returned `3`; changed: new molecule 3 (map, map 1 re-interprolated by factor 1.00); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(smooth-map 1 1.0)` | ran, returned `3`; changed: new molecule 3 (map, map 1 re-interprolated by factor 1.00); graphics_n_molecules(): 3 -> 4 |

Python and Scheme gave the same answer.

### transform_map_raw

Python: `transform_map_raw(imol, r00, r01, r02, r10, r11, r12, r20, r21, r22, t0, t1, t2, pt0, pt1, pt2, box_half_size, ref_space_group, cell_a, cell_b, cell_c, alpha, beta, gamma)`  
Scheme: `(transform-map-raw imol r00 r01 r02 r10 r11 r12 r20 r21 r22 t0 t1 t2 pt0 pt1 pt2 box-half-size ref-space-group cell-a cell-b cell-c alpha beta gamma)`

return the new molecule number. The cell is given in Angstroms and
 the angles in degrees. The ref_space_group can be a H-M symbol or
 a colon-separated string of symmetry operators.

Arguments: imol (a whole number), r00 (a number), r01 (a number), r02 (a number), r10 (a number), r11 (a number), r12 (a number), r20 (a number), r21 (a number), r22 (a number), t0 (a number), t1 (a number), t2 (a number), pt0 (a number), pt1 (a number), pt2 (a number), box_half_size (a number), ref_space_group (text), cell_a (a number), cell_b (a number), cell_c (a number), alpha (a number), beta (a number), gamma (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `transform_map_raw(1, 1,0,0, 0,1,0, 0,0,1, 0,0,0, 47.1,10.6,17.4, 10.0, "P 21 21 21", 64.897, 78.323, 38.792, 90, 90, 90)` | ran, returned `3`; changed: new molecule 3 (map, Transformed map); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(transform-map-raw 1 1 0 0 0 1 0 0 0 1 0 0 0 47.1 10.6 17.4 10.0 "P 21 21 21" 64.897 78.323 38.792 90 90 90)` | ran, returned `3`; changed: new molecule 3 (map, Transformed map); graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the number of a new map: a box of the given half-size around the point, transformed by the rotation/translation, in the given cell and space group.

Python and Scheme gave the same answer.

