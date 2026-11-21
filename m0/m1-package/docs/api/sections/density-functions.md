# Density Functions

[Scripting reference](../README.md) > Density Functions (37 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### another_level

Python: `another_level()`  
Scheme: `(another-level)`

Add another contour level for the last added map.

 Currently, the map must have been generated from an MTZ file.
 Returns the molecule number of the new molecule or -1 on failure

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `another_level()` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(another-level)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Python and Scheme gave the same answer.

### another_level_from_map_molecule_number

Python: `another_level_from_map_molecule_number(imap)`  
Scheme: `(another-level-from-map-molecule-number imap)`

Add another contour level for the given map.

 Currently, the map must have been generated from an MTZ file.
 Returns the molecule number of the new molecule or -1 on failure

Arguments: imap (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `another_level_from_map_molecule_number(1)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(another-level-from-map-molecule-number 1)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Python and Scheme gave the same answer.

### auto_read_do_difference_map_too_state

Python: `auto_read_do_difference_map_too_state()`  
Scheme: `(auto-read-do-difference-map-too-state)`

return the flag to do a difference map (too) on auto-read MTZ

 Returns 0 means no, 1 means yes.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `auto_read_do_difference_map_too_state()` | ran, returned `1` |
| Scheme | `(auto-read-do-difference-map-too-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### cns_file_has_phases_p

Python: `cns_file_has_phases_p(cns_file_name)`  
Scheme: `(cns-file-has-phases-p cns-file-name)`

does the given file have cns phases?

Arguments: cns_file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `cns_file_has_phases_p("tutorial-modern.pdb")` | ran, returned `0` |
| Scheme | `(cns-file-has-phases-p "tutorial-modern.pdb")` | ran, returned `0` |

Python and Scheme gave the same answer.

### density_at_point

Python: `density_at_point(imol_map, x, y, z)`  
Scheme: `(density-at-point imol-map x y z)`

return the density at the given point for the given
 map. Return 0 for bad imol

Arguments: imol_map (a whole number), x (a number), y (a number), z (a number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `density_at_point(1, 54.5, 9.4, 12.3)` | ran, returned `0.19171960651874542` |
| Scheme | `(density-at-point 1 54.5 9.4 12.3)` | ran, returned `0.19171960651874542` |

Python and Scheme gave the same answer.

### esoteric_depth_cue_state

Python: `esoteric_depth_cue_state()`  
Scheme: `(esoteric-depth-cue-state)`

native depth cueing system

 return the state of the esoteric depth cueing flag

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `esoteric_depth_cue_state()` | ran, returned `1` |
| Scheme | `(esoteric-depth-cue-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### get_map_radius

Python: `get_map_radius()`  
Scheme: `(get-map-radius)`

return the extent of the box/radius of electron density contours

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_map_radius()` | ran, returned `16.0` |
| Scheme | `(get-map-radius)` | ran, returned `16.0` |

Python and Scheme gave the same answer.

### get_text_for_density_size_em_widget

Python: `get_text_for_density_size_em_widget()`  
Scheme: `(get-text-for-density-size-em-widget)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_text_for_density_size_em_widget()` | ran, returned `'55.0 '` |
| Scheme | `(get-text-for-density-size-em-widget)` | ran, returned `"55.0 "` |

Python and Scheme gave the same answer.

### get_text_for_density_size_widget

Python: `get_text_for_density_size_widget()`  
Scheme: `(get-text-for-density-size-widget)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_text_for_density_size_widget()` | ran, returned `'16.0 '` |
| Scheme | `(get-text-for-density-size-widget)` | ran, returned `"16.0 "` |

Python and Scheme gave the same answer.

### is_mtz_file_p

Python: `is_mtz_file_p(filename)`  
Scheme: `(is-mtz-file-p filename)`

is the given filename an mtz file?

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `is_mtz_file_p("tutorial-modern.pdb")` | ran, returned `0` |
| Scheme | `(is-mtz-file-p "tutorial-modern.pdb")` | ran, returned `0` |

Python and Scheme gave the same answer.

### make_and_draw_map

Python: `make_and_draw_map(mtz_file_name, f_col, phi_col, weight, use_weights, is_diff_map)`  
Scheme: `(make-and-draw-map mtz-file-name f-col phi-col weight use-weights is-diff-map)`

make a map from an mtz file (simple interface)

 given mtz file mtz_file_name and F column f_col and phases column
 phi_col and optional weight column weight_col (pass use_weights=0 if
 weights are not to be used). Also mark the map as a difference map
 (is_diff_map=1) or not (is_diff_map=0) because they are handled
 differently inside coot.

 Returns -1 on error, else return the new molecule number

Arguments: mtz_file_name (text), f_col (text), phi_col (text), weight (text), use_weights (a whole number), is_diff_map (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "DELFWT", "PHDELWT", "", 0, 1)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz DELFWT PHDELWT); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "DELFWT" "PHDELWT" "" 0 1)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz DELFWT PHDELWT); graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number (-1 on bad columns); a difference map appears.

Note: With weights (weight "FOM", use_weights 1) it returned -1 in both languages, although FOM is a W column (suspicious).

Python and Scheme gave the same answer.

### make_and_draw_map_with_refmac_params

Python: `make_and_draw_map_with_refmac_params(mtz_file_name, a, b, weight, use_weights, is_diff_map, have_refmac_params, fobs_col, sigfobs_col, r_free_col, sensible_f_free_col)`  
Scheme: `(make-and-draw-map-with-refmac-params mtz-file-name a b weight use-weights is-diff-map have-refmac-params fobs-col sigfobs-col r-free-col sensible-f-free-col)`

as the above function, execpt set refmac parameters too

 pass along the refmac column labels for storage (not used in the
 creation of the map)

 Returns -1 on error, else return imol

Arguments: mtz_file_name (text), a (text), b (text), weight (text), use_weights (a whole number), is_diff_map (a whole number), have_refmac_params (a whole number), fobs_col (text), sigfobs_col (text), r_free_col (text), sensible_f_free_col (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_and_draw_map_with_refmac_params("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0, 1, "FGMP18", "SIGFGMP18", "FreeR_flag", 1)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(make-and-draw-map-with-refmac-params "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0 1 "FGMP18" "SIGFGMP18" "FreeR_flag" 1)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: makes the map and stores Fobs/SigF/Rfree columns with it for a later Refmac run; returns the map molecule number.

Python and Scheme gave the same answer.

### make_and_draw_map_with_reso_with_refmac_params

Python: `make_and_draw_map_with_reso_with_refmac_params(mtz_file_name, a, b, weight, use_weights, is_diff_map, have_refmac_params, fobs_col, sigfobs_col, r_free_col, sensible_f_free_col, is_anomalous, use_reso_limits, low_reso_limit, high_reso_lim)`  
Scheme: `(make-and-draw-map-with-reso-with-refmac-params mtz-file-name a b weight use-weights is-diff-map have-refmac-params fobs-col sigfobs-col r-free-col sensible-f-free-col is-anomalous use-reso-limits low-reso-limit high-reso-lim)`

Note to self, we need to save the reso limits in the state file

Arguments: mtz_file_name (text), a (text), b (text), weight (text), use_weights (a whole number), is_diff_map (a whole number), have_refmac_params (a whole number), fobs_col (text), sigfobs_col (text), r_free_col (text), sensible_f_free_col (a whole number), is_anomalous (a whole number), use_reso_limits (a whole number), low_reso_limit (a number), high_reso_lim (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_and_draw_map_with_reso_with_refmac_params("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0, 1, "FGMP18", "SIGFGMP18", "FreeR_flag", 1, 0, 1, 20.0, 3.0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT 20.00 3.00); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(make-and-draw-map-with-reso-with-refmac-params "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0 1 "FGMP18" "SIGFGMP18" "FreeR_flag" 1 0 1 20.0 3.0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT 20.00 3.00); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number; the map is calculated with data between 20 and 3 A only.

Python and Scheme gave the same answer.

### make_updating_map

Python: `make_updating_map(mtz_file_name, f_col, phi_col, weight, use_weights, is_diff_map)`  
Scheme: `(make-updating-map mtz-file-name f-col phi-col weight use-weights is-diff-map)`

make a map molecule from the give file name.

 If the file updates, then the map will be updated.

Arguments: mtz_file_name (text), f_col (text), phi_col (text), weight (text), use_weights (a whole number), is_diff_map (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_updating_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 1, 1)` | ran, returned `1` |
| Scheme | `(make-updating-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 1 1)` | ran, returned `1` |

Python and Scheme gave the same answer.

### map_is_difference_map

Python: `map_is_difference_map(imol)`  
Scheme: `(map-is-difference-map imol)`

map is difference map?

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_is_difference_map(1)` | ran, returned `0` |
| Scheme | `(map-is-difference-map 1)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns 0 for the 2mFo-DFc map 1 (1 for a difference map).

Python and Scheme gave the same answer.

### map_line_width_state

Python: `map_line_width_state()`  
Scheme: `(map-line-width-state)`

return the width in which density contours are drawn

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_line_width_state()` | ran, returned `1` |
| Scheme | `(map-line-width-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### mtz_file_has_phases_p

Python: `mtz_file_has_phases_p(mtz_file_name)`  
Scheme: `(mtz-file-has-phases-p mtz-file-name)`

go down a (new 20060920) different path.

Arguments: mtz_file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mtz_file_has_phases_p("rnasa-1.8-all_refmac1.mtz")` | ran, returned `1` |
| Scheme | `(mtz-file-has-phases-p "rnasa-1.8-all_refmac1.mtz")` | ran, returned `1` |

Python and Scheme gave the same answer.

### read_mtz

Python: `read_mtz(mtz_file_name, f_col, phi_col, weight, use_weights, is_diff_map)`  
Scheme: `(read-mtz mtz-file-name f-col phi-col weight use-weights is-diff-map)`

the function is a synonym of the above function - which now has an archaic-style
 name

Arguments: mtz_file_name (text), f_col (text), phi_col (text), weight (text), use_weights (a whole number), is_diff_map (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_mtz("map-coefficients-only.mtz", "FWT", "PHWT", "", 0, 0)` | ran, returned `3`; changed: new molecule 3 (map, map-coefficients-only.mtz FWT PHWT); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(read-mtz "map-coefficients-only.mtz" "DELFWT" "PHDELWT" "" 0 1)` | ran, returned `3`; changed: new molecule 3 (map, map-coefficients-only.mtz DELFWT PHDELWT); graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number (same as make_and_draw_map).

Python and Scheme gave the same answer.

### refmac_parameters

Python: `refmac_parameters(imol)`  
Scheme: `(refmac-parameters imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `refmac_parameters_py`.
Also available in Scheme as `refmac-parameters-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `imap = make_and_draw_map_with_refmac_params("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0, 1, "FGMP18", "SIGFGMP18", "FreeR_flag", 1)`, then `refmac_parameters(imap)` | ran, returned `['rnasa-1.8-all_refmac1.mtz', 'FWT', 'PHWT', '', 0, 0, 1, 'FGMP18', 'SIGFGMP18', 'FreeR_flag', 1]` |
| Scheme | `(refmac-parameters (make-and-draw-map-with-refmac-params "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0 1 "FGMP18" "SIGFGMP18" "FreeR_flag" 1))` | ran, returned `("rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0 1 "FGMP18" "SIGFGMP18" "FreeR_flag" 1)`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: returns the MTZ file and columns stored with the map; [] for a map made without Refmac parameters.

Note: Does not run Refmac (only reads stored parameters).

Python and Scheme gave the same answer.

### residue_density_fit_scale_factor

Python: `residue_density_fit_scale_factor()`  
Scheme: `(residue-density-fit-scale-factor)`

return the scale factor for the Residue Density fit analysis

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_density_fit_scale_factor()` | ran, returned `1.0` |
| Scheme | `(residue-density-fit-scale-factor)` | ran, returned `1.0` |

Python and Scheme gave the same answer.

### set_auto_read_column_labels

Python: `set_auto_read_column_labels(fwt, phwt, is_for_diff_map_flag)`  
Scheme: `(set-auto-read-column-labels fwt phwt is-for-diff-map-flag)`

set the expected MTZ columns for Auto-reading MTZ file.

 Not every program uses the default refmac labels ("FWT"/"PHWT") for
 its MTZ file. Here we can tell coot to expect other labels so that
 coot can "Auto-open" such MTZ files.

 e.g. (set-auto-read-column-labels "2FOFCWT" "PH2FOFCWT" 0)

Arguments: fwt (text), phwt (text), is_for_diff_map_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_auto_read_column_labels("hello", "hello", 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-auto-read-column-labels "hello" "hello" 1)` | ran (no return value, nothing visible changed) |

### set_auto_read_do_difference_map_too

Python: `set_auto_read_do_difference_map_too(i)`  
Scheme: `(set-auto-read-do-difference-map-too i)`

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_auto_read_do_difference_map_too(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-auto-read-do-difference-map-too 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: auto_read_do_difference_map_too_state was 1, set to 0, read back 0; Scheme: auto-read-do-difference-map-too-state was 1, set to 0, read back 0.

### set_density_size

Python: `set_density_size(f)`  
Scheme: `(set-density-size f)`

another (old) way of setting the radius of the map

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_density_size(1.0)` | ran (no return value); changed: get_map_radius(): 16 -> 1 |
| Scheme | `(set-density-size 1.0)` | ran (no return value, nothing visible changed) |

### set_density_size_em_from_widget

Python: `set_density_size_em_from_widget(text)`  
Scheme: `(set-density-size-em-from-widget text)`

Arguments: text (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_density_size_em_from_widget("hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(set-density-size-em-from-widget "hello")` | ran (no return value, nothing visible changed) |

### set_density_size_from_widget

Python: `set_density_size_from_widget(text)`  
Scheme: `(set-density-size-from-widget text)`

const gchar *text

Arguments: text (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_density_size_from_widget("hello")` | ran (no return value); changed: get_map_radius(): 1 -> 10 |
| Scheme | `(set-density-size-from-widget "hello")` | ran (no return value, nothing visible changed) |

### set_display_intro_string

Python: `set_display_intro_string(str)`  
Scheme: `(set-display-intro-string str)`

Give me this nice message str when I start coot

Arguments: str (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_display_intro_string("hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(set-display-intro-string "hello")` | ran (no return value, nothing visible changed) |

### set_esoteric_depth_cue

Python: `set_esoteric_depth_cue(istate)`  
Scheme: `(set-esoteric-depth-cue istate)`

not everone likes coot's esoteric depth cueing system

 Pass an argument istate=1 to turn it off

 (this function is currently disabled).

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_esoteric_depth_cue(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-esoteric-depth-cue 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: esoteric_depth_cue_state was 1, set to 0, read back 0; Scheme: esoteric-depth-cue-state was 1, set to 0, read back 0.

### set_map_is_difference_map

Python: `set_map_is_difference_map(imol, bool_flag)`  
Scheme: `(set-map-is-difference-map imol bool-flag)`

post-hoc set the map of molecule number imol to be a
 difference map
 Returns success status, 0 -> failure (imol does not have a map)

Arguments: imol (a whole number), bool_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_map_is_difference_map(1, True)` | ran, returned `1`; changed: map 1 contour level: 0.5602 -> 0.56; map 1 colour: [0.2, 0.3833, 0.7] -> [0.2, 0.6, 0.2]; get_contour_level_absolute(1): 0.5602 -> 0.56; get_contour_level_in_sigma(1): 1.5 -> 1.499 ... |
| Scheme | `(set-map-is-difference-map 1 1)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: map 1 is now treated as a difference map (map_is_difference_map(1) -> 1, +/- contours).

Note: Python accepts True; Scheme needs an integer (#t/#f give 'Wrong type (expecting exact integer)').

Setting checked (set to another value and read back, then put back): Python: map_is_difference_map was 0, set to 1, read back 1; Scheme: map-is-difference-map was 0, set to 1, read back 1.

Python and Scheme gave the same answer.

### set_map_line_width

Python: `set_map_line_width(w)`  
Scheme: `(set-map-line-width w)`

draw the lines of the chickenwire density in width w

Arguments: w (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_map_line_width(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-map-line-width 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: map_line_width_state was 1, set to 0, read back 0; Scheme: map-line-width-state was 1, set to 0, read back 0.

### set_map_radius

Python: `set_map_radius(f)`  
Scheme: `(set-map-radius f)`

set the extent of the box/radius of electron density contours for x-ray maps

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_map_radius(1.0)` | ran (no return value); changed: get_map_radius(): 10 -> 1 |
| Scheme | `(set-map-radius 1.0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_map_radius was 16.0, set to 24.5, read back 24.5; Scheme: get-map-radius was 16.0, set to 24.5, read back 24.5.

### set_map_radius_em

Python: `set_map_radius_em(radius)`  
Scheme: `(set-map-radius-em radius)`

set the extent of the box/radius of electron density contours for EM map

Arguments: radius (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_map_radius_em(5.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-map-radius-em 5.0)` | ran (no return value, nothing visible changed) |

### set_map_radius_slider_max

Python: `set_map_radius_slider_max(f)`  
Scheme: `(set-map-radius-slider-max f)`

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_map_radius_slider_max(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-map-radius-slider-max 1.0)` | ran (no return value, nothing visible changed) |

### set_swap_difference_map_colours

Python: `set_swap_difference_map_colours(i)`  
Scheme: `(set-swap-difference-map-colours i)`

not everone likes coot's default difference map colouring.

 Pass an argument i=1 to swap the difference map colouring so that
 red is positive and green is negative.

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_swap_difference_map_colours(1)` | ran (no return value); changed: swap_difference_map_colours_state(): 0 -> 1 |
| Scheme | `(set-swap-difference-map-colours 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: swap_difference_map_colours_state was 0, set to 1, read back 1; Scheme: swap-difference-map-colours-state was 0, set to 1, read back 1.

### stop_updating_molecule

Python: `stop_updating_molecule(imol)`  
Scheme: `(stop-updating-molecule imol)`

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `stop_updating_molecule(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(stop-updating-molecule 0)` | ran (no return value, nothing visible changed) |

### swap_difference_map_colours_state

Python: `swap_difference_map_colours_state()`  
Scheme: `(swap-difference-map-colours-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `swap_difference_map_colours_state()` | ran, returned `0` |
| Scheme | `(swap-difference-map-colours-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### valid_labels

Python: `valid_labels(mtz_file_name, f_col, phi_col, weight_col, use_weights)`  
Scheme: `(valid-labels mtz-file-name f-col phi-col weight-col use-weights)`

does the mtz file have the columms that we want it to have?

Arguments: mtz_file_name (text), f_col (text), phi_col (text), weight_col (text), use_weights (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `valid_labels("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0)` | ran, returned `1` |
| Scheme | `(valid-labels "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 when the F and phase columns exist in the MTZ file, 0 otherwise.

Python and Scheme gave the same answer.

### wrapped_auto_read_make_and_draw_maps

Python: `wrapped_auto_read_make_and_draw_maps(filename)`  
Scheme: `(wrapped-auto-read-make-and-draw-maps filename)`

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `wrapped_auto_read_make_and_draw_maps("tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(wrapped-auto-read-make-and-draw-maps "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

