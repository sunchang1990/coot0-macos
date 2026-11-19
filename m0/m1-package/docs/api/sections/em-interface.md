# EM interface

[Scripting reference](../README.md) > EM interface (5 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### map_histogram

Python: `map_histogram(imol_map)`  
Scheme: `(map-histogram imol-map)`

make a map histogram

Arguments: imol_map (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_histogram(1)` | not tried |
| Scheme | `(map-histogram 1)` | not tried |

### scale_cell

Python: `scale_cell(imol_map, fac_u, fac_v, fac_w)`  
Scheme: `(scale-cell imol-map fac-u fac-v fac-w)`

Scale the cell, for use with EM maps, where the cell needs
 to be adjusted. Use like: (scale-cell 2 1.012 1.012 1.012). Return error
 status, 1 means it worked, 0 means it did not work.

Arguments: imol_map (a whole number), fac_u (a number), fac_v (a number), fac_w (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `scale_cell(1, 1.0, 1.0, 1.0)` | not tried |
| Scheme | `(scale-cell 1 1.0 1.0 1.0)` | not tried |

### segment_map

Python: `segment_map(imol_map, low_level)`  
Scheme: `(segment-map imol-map low-level)`

create a number of maps by segmenting the given map, above the
 (absolute) low_level. New maps are on the same grid as the input
 map.

Arguments: imol_map (a whole number), low_level (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `segment_map(1, 1.5)` | not tried |
| Scheme | `(segment-map 1 1.5)` | not tried |

### segment_map_multi_scale

Python: `segment_map_multi_scale(imol_map, low_level, b_factor_inc, n_rounds)`  
Scheme: `(segment-map-multi-scale imol-map low-level b-factor-inc n-rounds)`

Arguments: imol_map (a whole number), low_level (a number), b_factor_inc (a number), n_rounds (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `segment_map_multi_scale(1, 1.5, 20.0, 1)` | not tried |
| Scheme | `(segment-map-multi-scale 1 1.5 20.0 1)` | not tried |

### set_ignore_pseudo_zeros_for_map_stats

Python: `set_ignore_pseudo_zeros_for_map_stats(state)`  
Scheme: `(set-ignore-pseudo-zeros-for-map-stats state)`

ignore pseudo-zeros when calculationg maps stats (default 1 = true)

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ignore_pseudo_zeros_for_map_stats(1)` | not tried |
| Scheme | `(set-ignore-pseudo-zeros-for-map-stats 1)` | not tried |

