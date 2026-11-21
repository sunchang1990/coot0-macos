# Extra Map Functions

[Scripting reference](../README.md) > Extra Map Functions (18 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_map_colour_mol_menu_item

Python: `add_map_colour_mol_menu_item(imol, name, sub_menu, callback)`  
Scheme: `(add-map-colour-mol-menu-item imol name sub-menu callback)`

Arguments: imol (a whole number), name (text), sub_menu (`GtkWidget *`), callback (`GtkSignalFunc`). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: adds a molecule entry to a GTK menu (internal menu building).

### add_map_scroll_wheel_mol_menu_item

Python: `add_map_scroll_wheel_mol_menu_item(imol, name, menu, callback)`  
Scheme: `(add-map-scroll-wheel-mol-menu-item imol name menu callback)`

Actually this function is generic and could be renamed so.

Arguments: imol (a whole number), name (text), menu (`GtkWidget *`), callback (`GtkSignalFunc`). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: adds a molecule entry to a GTK menu (internal menu building).

### amplitude_vs_resolution_py

Python: `amplitude_vs_resolution_py(mol_map)`  
Scheme: `(amplitude-vs-resolution-scm mol-map)`

Arguments: mol_map (a whole number). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `amplitude_vs_resolution_py(1)` | ran, returned `[<NULL>, <NULL>, <NULL>, <NULL>, <NULL>, <NULL>, <NULL>, <NULL>, <NULL>, <NULL>, <NULL>, <NULL>, <NULL>, <NULL>, <NULL>, ...` |
| Scheme | `(amplitude-vs-resolution-scm 1)` | ran, returned `((86091.39604021655 92 0.00424090013636843) (150838.67069283 140 0.01099814952550722) (108113.47222217107 175 0.01797754 ...` |

### analyse_map_point_density_change_py

Python: `analyse_map_point_density_change_py(map_number_list, imol_map_mask)`

test function for analysis of multiple map

Arguments: map_number_list (a list or value), imol_map_mask (a whole number). Returns: a whole number.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `multi_sharpen_blur_map_py(1, [-20.0, 0.0])`, then `analyse_map_point_density_change_py([1, 3, 4], 1)` | ran, returned `5`; changed: new molecule 5 (map, zde); graphics_n_molecules(): 5 -> 6 |

Example written and checked by hand on the test data. Expected: returns a new map of the per-point density change across the listed maps (here map 1 and two blurred copies), masked by map 1.

### auto_read_make_and_draw_maps

Python: `auto_read_make_and_draw_maps(filename)`  
Scheme: `(auto-read-make-and-draw-maps filename)`

read MTZ file filename and from it try to make maps

Useful for reading the output of refmac. The default labels (FWT/PHWT
and DELFWT/PHDELFWT) can be changed using ...[something]

 Returns a list of molecule numbers for the new maps

Arguments: filename (text). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `auto_read_make_and_draw_maps("tutorial-modern.pdb")` | ran, returned `()` |
| Scheme | `(auto-read-make-and-draw-maps "tutorial-modern.pdb")` | ran, returned `#()` |

Python and Scheme gave the same answer.

### auto_read_make_and_draw_maps_from_cns

Python: `auto_read_make_and_draw_maps_from_cns(file_name)`  
Scheme: `(auto-read-make-and-draw-maps-from-cns file-name)`

Arguments: file_name (text). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `auto_read_make_and_draw_maps_from_cns("tutorial-modern.pdb")` | ran, returned `()` |
| Scheme | `(auto-read-make-and-draw-maps-from-cns "tutorial-modern.pdb")` | ran, returned `#()` |

Python and Scheme gave the same answer.

### auto_read_make_and_draw_maps_from_mtz

Python: `auto_read_make_and_draw_maps_from_mtz(file_name)`  
Scheme: `(auto-read-make-and-draw-maps-from-mtz file-name)`

set the flag to do a difference map (too) on auto-read MTZ

Arguments: file_name (text). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `auto_read_make_and_draw_maps_from_mtz("tutorial-modern.pdb")` | ran, returned `()` |
| Scheme | `(auto-read-make-and-draw-maps-from-mtz "tutorial-modern.pdb")` | ran, returned `#()` |

Python and Scheme gave the same answer.

### b_factor_from_map

Python: `b_factor_from_map(imol_map)`  
Scheme: `(b-factor-from-map imol-map)`

b-factor from map
calculate structure factors and use the amplitudes to estimate
the B-factor of the data using a wilson plot using a low resolution
limit of 4.5A.
Returns -1 when given a bad map or there were no data beyond 4.5A

Arguments: imol_map (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `b_factor_from_map(1)` | ran, returned `-1.0` |
| Scheme | `(b-factor-from-map 1)` | ran, returned `-1.0` |

Example written and checked by hand on the test data. Expected: should return the B-factor estimated from map 1's amplitude fall-off.

Note: Always returns -1: the C++ computes b and prints it but returns the unchanged b_factor = -1 (bug in 0.9.8.96).

Python and Scheme gave the same answer.

### flip_hand

Python: `flip_hand(imol_map)`  
Scheme: `(flip-hand imol-map)`

Flip the hand of the map
in case it was accidentally generated on the wrong one.
Returns the molecule number of the flipped map.

Arguments: imol_map (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `flip_hand(1)` | ran, returned `3`; changed: new molecule 3 (map, Map 1 Flipped Hand); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(flip-hand 1)` | ran, returned `3`; changed: new molecule 3 (map, Map 1 Flipped Hand); graphics_n_molecules(): 3 -> 4 |

Python and Scheme gave the same answer.

### go_to_map_molecule_centre

Python: `go_to_map_molecule_centre(imol_map)`  
Scheme: `(go-to-map-molecule-centre imol-map)`

Go to the centre of the molecule - for Cryo-EM Molecules
 and recontour at a sensible value.

Arguments: imol_map (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_map_molecule_centre(1)` | ran (no return value); changed: map 1 contour level: 0.56 -> 0.8904; rotation centre moved 32.3 A to (33.2, 39.3, 18.9); get_contour_level_absolute(1): 0.56 -> 0.8904; get_contour_level_in_sigma(1): 1.499 -> 2.384 |
| Scheme | `(go-to-map-molecule-centre 1)` | ran (no return value, nothing visible changed) |

### handle_read_ccp4_map

Python: `handle_read_ccp4_map(filename, is_diff_map_flag)`  
Scheme: `(handle-read-ccp4-map filename is-diff-map-flag)`

same function as above - old name for the function. Deleted from the API at some stage

Arguments: filename (text), is_diff_map_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_read_ccp4_map("rnasa-map.map", 0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-map.map); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(handle-read-ccp4-map "rnasa-map.map" 0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-map.map); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number; the CCP4 map file is read (second argument 1 = difference map).

Python and Scheme gave the same answer.

### handle_read_emdb_data

Python: `handle_read_emdb_data(dir_name)`  
Scheme: `(handle-read-emdb-data dir-name)`

Arguments: dir_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `import os, shutil; os.makedirs("emd_0001/map", exist_ok=True); shutil.copy("rnasa-map.map", "emd_0001/map/emd_0001.map")`, then `handle_read_emdb_data("emd_0001")` | ran, returned `0`; changed: new molecule 3 (map, emd_0001.map); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | first `(begin (mkdir "emd_0002") (mkdir "emd_0002/map") (copy-file "rnasa-map.map" "emd_0002/map/emd_0002.map"))`, then `(handle-read-emdb-data "emd_0002")` | ran, returned `0`; changed: new molecule 3 (map, emd_0002.map); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: reads every map/*.map and fittedModels/PDB/*.ent of an EMDB entry directory; returns 0.

Note: Return value is always 0 (status never set), also on success.

Python and Scheme gave the same answer.

### map_colour_components

Python: `map_colour_components(imol)`  
Scheme: `(map-colour-components imol)`

return the colour triple of the imolth map
e.g.: [0.4, 0.6, 0.8]. If invalid imol return Py_False.

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `map_colour_components_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_colour_components(1)` | ran, returned `[0.19999998807907104, 0.38333338499069214, 0.699999988079071]` |
| Scheme | `(map-colour-components 1)` | ran, returned `(0.19999998807907104 0.38333338499069214 0.699999988079071)` |

Example written and checked by hand on the test data. Expected: returns the [red, green, blue] colour of map 1.

Python and Scheme gave the same answer.

### multi_sharpen_blur_map_py

Python: `multi_sharpen_blur_map_py(imol_map, b_factors_list)`  
Scheme: `(multi-sharpen-blur-map-scm imol-map b-factors-list)`

make many sharpened or blurred maps
blurred maps are generated by using a positive value of b_factor.

Arguments: imol_map (a whole number), b_factors_list (a list or value). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `multi_sharpen_blur_map_py(1, [-20.0, 0.0, 30.0])` | ran (no return value); changed: new molecule 3 (map, Map Sharpen -20.00); new molecule 4 (map, Map Blur 0.00); new molecule 5 (map, Map Blur 30.00); graphics_n_molecules(): 3 -> 6 |
| Scheme | `(multi-sharpen-blur-map-scm 1 (list -10.0 40.0))` | ran (no return value); changed: new molecule 3 (map, Map Sharpen -10.00); new molecule 4 (map, Map Blur 40.00); graphics_n_molecules(): 3 -> 5 |

Example written and checked by hand on the test data. Expected: one new map per B-factor in the list (negative = sharpen, positive = blur).

### read_ccp4_map

Python: `read_ccp4_map(filename, is_diff_map_flag)`  
Scheme: `(read-ccp4-map filename is-diff-map-flag)`

read a CCP4 map or a CNS map (despite the name).

Arguments: filename (text), is_diff_map_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_ccp4_map("rnasa-map.map", 0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-map.map); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(read-ccp4-map "rnasa-map.map" 0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-map.map); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number.

Python and Scheme gave the same answer.

### res_tracer

Python: `res_tracer(imol_map, pir_file_name)`  
Scheme: `(res-tracer imol-map pir-file-name)`

trace the given map and try to apply the sequence in
the given pir file

Arguments: imol_map (a whole number), pir_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `res_tracer(1, "tutorial-modern.pdb")` | ran (no return value); changed: new molecule 4 (map, Map); graphics_n_molecules(): 3 -> 5 |
| Scheme | `(res-tracer 1 "tutorial-modern.pdb")` | ran (no return value); changed: new molecule 4 (map, Map); graphics_n_molecules(): 3 -> 5 |

### sharpen_blur_map

Python: `sharpen_blur_map(imol_map, b_factor)`  
Scheme: `(sharpen-blur-map imol-map b-factor)`

make a sharpened or blurred map
blurred maps are generated by using a positive value of b_factor.
Returns the index of the map created by applying a b-factor
 to the given map. Return -1 on failure.

Arguments: imol_map (a whole number), b_factor (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `sharpen_blur_map(1, 20.0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT Blur 20.00); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(sharpen-blur-map 1 20.0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT Blur 20.00); graphics_n_molecules(): 3 -> 4 |

Python and Scheme gave the same answer.

### sharpen_blur_map_with_resampling

Python: `sharpen_blur_map_with_resampling(imol_map, b_factor, resample_factor)`  
Scheme: `(sharpen-blur-map-with-resampling imol-map b-factor resample-factor)`

make a sharpened or blurred map with resampling
resampling factor might typically be 1.3
blurred maps are generated by using a positive value of b_factor.
Returns the index of the map created by applying a b-factor
 to the given map. Return -1 on failure.

Arguments: imol_map (a whole number), b_factor (a number), resample_factor (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `sharpen_blur_map_with_resampling(1, 20.0, 1.0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT Blur 20.00); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(sharpen-blur-map-with-resampling 1 20.0 1.0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-1.8-all_refmac1.mtz FWT PHWT Blur 20.00); graphics_n_molecules(): 3 -> 4 |

Python and Scheme gave the same answer.

