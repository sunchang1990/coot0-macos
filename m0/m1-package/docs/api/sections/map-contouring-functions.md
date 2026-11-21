# Map Contouring Functions

[Scripting reference](../README.md) > Map Contouring Functions (6 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### map_contours

Python: `map_contours(imol, contour_level)`

Arguments: imol (a whole number), contour_level (a number). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `set_rotation_centre(47.1, 10.6, 17.4)`, then `len(map_contours(1, 0.3))` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: should return the contour line segments [[x1,y1,z1],[x2,y2,z2]] of map 1 at that level in the box around the rotation centre.

Note: Always returns an empty list here although the map is contoured normally; GenerateSurface_from_Xmap is called with isample/ream arguments (0,1) that may give nothing, or it needs the map to have been drawn. Suspicious.

### set_radial_map_colouring_centre

Python: `set_radial_map_colouring_centre(imol, x, y, z)`  
Scheme: `(set-radial-map-colouring-centre imol x y z)`

radial map colouring centre

Arguments: imol (a whole number), x (a number), y (a number), z (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_radial_map_colouring_centre(0, 54.5, 9.4, 12.3)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-radial-map-colouring-centre 0 54.5 9.4 12.3)` | ran (no return value, nothing visible changed) |

### set_radial_map_colouring_invert

Python: `set_radial_map_colouring_invert(imol, invert_state)`  
Scheme: `(set-radial-map-colouring-invert imol invert-state)`

radial map colouring inverted colour map

Arguments: imol (a whole number), invert_state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_radial_map_colouring_invert(0, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-radial-map-colouring-invert 0 1)` | ran (no return value, nothing visible changed) |

### set_radial_map_colouring_max_radius

Python: `set_radial_map_colouring_max_radius(imol, r)`  
Scheme: `(set-radial-map-colouring-max-radius imol r)`

radial map colouring max

Arguments: imol (a whole number), r (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_radial_map_colouring_max_radius(0, 0.5)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-radial-map-colouring-max-radius 0 0.5)` | ran (no return value, nothing visible changed) |

### set_radial_map_colouring_min_radius

Python: `set_radial_map_colouring_min_radius(imol, r)`  
Scheme: `(set-radial-map-colouring-min-radius imol r)`

radial map colouring min

Arguments: imol (a whole number), r (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_radial_map_colouring_min_radius(0, 0.5)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-radial-map-colouring-min-radius 0 0.5)` | ran (no return value, nothing visible changed) |

### set_radial_map_colouring_saturation

Python: `set_radial_map_colouring_saturation(imol, saturation)`  
Scheme: `(set-radial-map-colouring-saturation imol saturation)`

radial map colouring saturation
saturation is a number between 0 and 1, typically 0.5

Arguments: imol (a whole number), saturation (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_radial_map_colouring_saturation(0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-radial-map-colouring-saturation 0 1.0)` | ran (no return value, nothing visible changed) |

