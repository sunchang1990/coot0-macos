# Map Sharpening Interface

[Scripting reference](../README.md) > Map Sharpening Interface (4 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### optimal_B_kurtosis

Python: `optimal_B_kurtosis(imol)`  
Scheme: `(optimal-B-kurtosis imol)`

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `optimal_B_kurtosis(0)` | ran, returned `0.0` |
| Scheme | `(optimal-B-kurtosis 0)` | ran, returned `0.0` |

Python and Scheme gave the same answer.

### set_map_sharpening_scale_limit

Python: `set_map_sharpening_scale_limit(f)`  
Scheme: `(set-map-sharpening-scale-limit f)`

set the limit of the b-factor map sharpening slider (default 30)

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_map_sharpening_scale_limit(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-map-sharpening-scale-limit 1.0)` | ran (no return value, nothing visible changed) |

### sharpen

Python: `sharpen(imol, b_factor)`  
Scheme: `(sharpen imol b-factor)`

Sharpen map imol by b_factor (note (of course) that positive numbers
 blur the map).

Arguments: imol (a whole number), b_factor (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `sharpen(0, 20.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(sharpen 0 20.0)` | ran (no return value, nothing visible changed) |

### sharpen_with_gompertz_scaling

Python: `sharpen_with_gompertz_scaling(imol, b_factor, try_gompertz, gompertz_factor)`  
Scheme: `(sharpen-with-gompertz-scaling imol b-factor try-gompertz gompertz-factor)`

Arguments: imol (a whole number), b_factor (a number), try_gompertz (a whole number), gompertz_factor (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `sharpen_with_gompertz_scaling(0, 20.0, 1, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(sharpen-with-gompertz-scaling 0 20.0 1 1.0)` | ran (no return value, nothing visible changed) |

