# Density Increment

[Scripting reference](../README.md) > Density Increment (20 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### change_contour_level

Python: `change_contour_level(is_increment)`  
Scheme: `(change-contour-level is-increment)`

change the contour level of the current map by a step

if is_increment=1 the contour level is increased. If is_increment=0
the map contour level is decreased.

Arguments: is_increment (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `change_contour_level(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(change-contour-level 1)` | ran (no return value, nothing visible changed) |

### get_diff_map_iso_level_increment

Python: `get_diff_map_iso_level_increment()`  
Scheme: `(get-diff-map-iso-level-increment)`

return difference maps iso-map level increment

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_diff_map_iso_level_increment()` | ran, returned `0.004999999888241291` |
| Scheme | `(get-diff-map-iso-level-increment)` | ran, returned `0.004999999888241291` |

Python and Scheme gave the same answer.

### get_iso_level_increment

Python: `get_iso_level_increment()`  
Scheme: `(get-iso-level-increment)`

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_iso_level_increment()` | ran, returned `0.05000000074505806` |
| Scheme | `(get-iso-level-increment)` | ran, returned `0.05000000074505806` |

Python and Scheme gave the same answer.

### get_map_sampling_rate

Python: `get_map_sampling_rate()`  
Scheme: `(get-map-sampling-rate)`

return the map sampling rate

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_map_sampling_rate()` | ran, returned `1.7999999523162842` |
| Scheme | `(get-map-sampling-rate)` | ran, returned `1.7999999523162842` |

Python and Scheme gave the same answer.

### get_text_for_diff_map_iso_level_increment_entry

Python: `get_text_for_diff_map_iso_level_increment_entry(imol)`  
Scheme: `(get-text-for-diff-map-iso-level-increment-entry imol)`

const gchar *text

Arguments: imol (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_text_for_diff_map_iso_level_increment_entry(0)` | ran, returned `'0.0050'` |
| Scheme | `(get-text-for-diff-map-iso-level-increment-entry 0)` | ran, returned `"0.0050"` |

Python and Scheme gave the same answer.

### get_text_for_iso_level_increment_entry

Python: `get_text_for_iso_level_increment_entry(imol)`  
Scheme: `(get-text-for-iso-level-increment-entry imol)`

Arguments: imol (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_text_for_iso_level_increment_entry(0)` | ran, returned `'0.0500'` |
| Scheme | `(get-text-for-iso-level-increment-entry 0)` | ran, returned `"0.0500"` |

Python and Scheme gave the same answer.

### get_text_for_map_sampling_rate_text

Python: `get_text_for_map_sampling_rate_text()`  
Scheme: `(get-text-for-map-sampling-rate-text)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_text_for_map_sampling_rate_text()` | ran, returned `'1.8000'` |
| Scheme | `(get-text-for-map-sampling-rate-text)` | ran, returned `"1.8000"` |

Python and Scheme gave the same answer.

### set_diff_map_iso_level_increment

Python: `set_diff_map_iso_level_increment(val)`  
Scheme: `(set-diff-map-iso-level-increment val)`

set the contour scroll step for difference map (in absolute
 e/A3) to val

The is only activated when scrolling by sigma is turned off

Arguments: val (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_diff_map_iso_level_increment(1.0)` | ran (no return value); changed: get_diff_map_iso_level_increment(): 0.005 -> 1; get_text_for_diff_map_iso_level_increment_entry(0): '0.0050' -> '1.0000'; get_text_for_diff_map_iso_level_increment_entry(1): '0.0050' -> '1.0000' |
| Scheme | `(set-diff-map-iso-level-increment 1.0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_diff_map_iso_level_increment was 0.004999999888241291, set to 0.507, read back 0.5070000290870667; Scheme: get-diff-map-iso-level-increment was 0.004999999888241291, set to 0.507, read back 0.5070000290870667.

### set_diff_map_iso_level_increment_from_text

Python: `set_diff_map_iso_level_increment_from_text(text, imol)`  
Scheme: `(set-diff-map-iso-level-increment-from-text text imol)`

set the difference maps iso-map level increment

Arguments: text (text), imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_diff_map_iso_level_increment_from_text("hello", 0)` | ran (no return value); changed: get_diff_map_iso_level_increment(): 1 -> 0; get_text_for_diff_map_iso_level_increment_entry(0): '1.0000' -> '0.0000'; get_text_for_diff_map_iso_level_increment_entry(1): '1.0000' -> '0.0000' |
| Scheme | `(set-diff-map-iso-level-increment-from-text "hello" 0)` | ran (no return value, nothing visible changed) |

### set_iso_level_increment

Python: `set_iso_level_increment(val)`  
Scheme: `(set-iso-level-increment val)`

set the contour scroll step (in absolute e/A3) for
 2Fo-Fc-style maps to val

The is only activated when scrolling by sigma is turned off

Arguments: val (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_iso_level_increment(1.0)` | ran (no return value); changed: get_iso_level_increment(): 0.05 -> 1; get_text_for_iso_level_increment_entry(0): '0.0500' -> '1.0000'; get_text_for_iso_level_increment_entry(1): '0.0500' -> '1.0000' |
| Scheme | `(set-iso-level-increment 1.0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_iso_level_increment was 0.05000000074505806, set to 0.575, read back 0.574999988079071; Scheme: get-iso-level-increment was 0.05000000074505806, set to 0.575, read back 0.574999988079071.

### set_iso_level_increment_from_text

Python: `set_iso_level_increment_from_text(text, imol)`  
Scheme: `(set-iso-level-increment-from-text text imol)`

Arguments: text (text), imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_iso_level_increment_from_text("hello", 0)` | ran (no return value); changed: get_iso_level_increment(): 1 -> 0; get_text_for_iso_level_increment_entry(0): '1.0000' -> '0.0000'; get_text_for_iso_level_increment_entry(1): '1.0000' -> '0.0000' |
| Scheme | `(set-iso-level-increment-from-text "hello" 0)` | ran (no return value, nothing visible changed) |

### set_last_map_contour_level

Python: `set_last_map_contour_level(level)`  
Scheme: `(set-last-map-contour-level level)`

set the contour level of the map with the highest molecule
 number to level

Arguments: level (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_last_map_contour_level(1.5)` | ran (no return value); changed: map 1 contour level: 0.5602 -> 1.5; get_contour_level_absolute(1): 0.5602 -> 1.5; get_contour_level_in_sigma(1): 1.5 -> 4.016 |
| Scheme | `(set-last-map-contour-level 1.5)` | ran (no return value, nothing visible changed) |

### set_last_map_contour_level_by_sigma

Python: `set_last_map_contour_level_by_sigma(n_sigma)`  
Scheme: `(set-last-map-contour-level-by-sigma n-sigma)`

set the contour level of the map with the highest molecule
 number to n_sigma sigma

Arguments: n_sigma (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_last_map_contour_level_by_sigma(1.5)` | ran (no return value); changed: map 1 contour level: 1.5 -> 0.5602; get_contour_level_absolute(1): 1.5 -> 0.5602; get_contour_level_in_sigma(1): 4.016 -> 1.5 |
| Scheme | `(set-last-map-contour-level-by-sigma 1.5)` | ran (no return value, nothing visible changed) |

### set_map_sampling_rate

Python: `set_map_sampling_rate(r)`  
Scheme: `(set-map-sampling-rate r)`

set the map sampling rate (default 1.5)

Set to something like 2.0 or 2.5 for more finely sampled maps. Useful
for baton-building low resolution maps.

Arguments: r (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_map_sampling_rate(0.5)` | ran (no return value); changed: get_map_sampling_rate(): 1.8 -> 0.5; get_text_for_map_sampling_rate_text(): '1.8000' -> '0.5000' |
| Scheme | `(set-map-sampling-rate 0.5)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_map_sampling_rate was 1.7999999523162842, set to 3.2, read back 3.200000047683716; Scheme: get-map-sampling-rate was 1.7999999523162842, set to 3.2, read back 3.200000047683716.

### set_map_sampling_rate_text

Python: `set_map_sampling_rate_text(text)`  
Scheme: `(set-map-sampling-rate-text text)`

sampling rate

find the molecule for which the single map dialog applies and set
 the contour level and redraw

Arguments: text (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_map_sampling_rate_text("hello")` | ran (no return value); changed: get_map_sampling_rate(): 0.5 -> 1.5; get_text_for_map_sampling_rate_text(): '0.5000' -> '1.5000' |
| Scheme | `(set-map-sampling-rate-text "hello")` | ran (no return value, nothing visible changed) |

### set_residue_density_fit_scale_factor

Python: `set_residue_density_fit_scale_factor(f)`  
Scheme: `(set-residue-density-fit-scale-factor f)`

set the scale factor for the Residue Density fit analysis

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_residue_density_fit_scale_factor(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-residue-density-fit-scale-factor 1.0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: residue_density_fit_scale_factor was 1.0, set to 2.0, read back 2.0; Scheme: residue-density-fit-scale-factor was 1.0, set to 2.0, read back 2.0.

### set_stop_scroll_diff_map

Python: `set_stop_scroll_diff_map(i)`  
Scheme: `(set-stop-scroll-diff-map i)`

create a lower limit to the "Fo-Fc-style" map contour level changing

 (default 1 on)

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_stop_scroll_diff_map(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-stop-scroll-diff-map 1)` | ran (no return value, nothing visible changed) |

### set_stop_scroll_diff_map_level

Python: `set_stop_scroll_diff_map_level(f)`  
Scheme: `(set-stop-scroll-diff-map-level f)`

set the actual difference map level changing limit

 (default 0.0)

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_stop_scroll_diff_map_level(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-stop-scroll-diff-map-level 1.0)` | ran (no return value, nothing visible changed) |

### set_stop_scroll_iso_map

Python: `set_stop_scroll_iso_map(i)`  
Scheme: `(set-stop-scroll-iso-map i)`

create a lower limit to the "2Fo-Fc-style" map contour level changing

 (default 1 on)

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_stop_scroll_iso_map(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-stop-scroll-iso-map 1)` | ran (no return value, nothing visible changed) |

### set_stop_scroll_iso_map_level

Python: `set_stop_scroll_iso_map_level(f)`  
Scheme: `(set-stop-scroll-iso-map-level f)`

set the actual map level changing limit

 (default 0.0)

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_stop_scroll_iso_map_level(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-stop-scroll-iso-map-level 1.0)` | ran (no return value, nothing visible changed) |

