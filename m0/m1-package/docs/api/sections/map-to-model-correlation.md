# Map to Model Correlation

[Scripting reference](../README.md) > Map to Model Correlation (11 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### density_score_residue

Python: `density_score_residue(imol, residue_spec, imol_map)`  
Scheme: `(density-score-residue imol residue-spec imol-map)`

simple density score for given residue (over-ridden by scripting function)

Arguments: imol (a whole number), residue_spec (a list or value), imol_map (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `density_score_residue(0, ["A", 41, ""], 1)` | ran, returned `4.34853982925415` |
| Scheme | `(density-score-residue 0 (list "A" 41 "") 1)` | ran, returned `4.34853982925415` |

Python and Scheme gave the same answer.

### map_mean

Python: `map_mean(imol)`  
Scheme: `(map-mean-scm imol)`

return sigma for the given map. Return Python False if not
 a valid map molecule number.

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `map_mean_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_mean(1)` | ran, returned `9.449976641917601e-05` |
| Scheme | `(map-mean-scm 1)` | ran, returned `9.449976641917601e-5` |

Example written and checked by hand on the test data. Expected: returns the mean density of map 1 (about 0 for a 2Fo-Fc map); False if not a map.

Python and Scheme gave the same answer.

### map_sigma

Python: `map_sigma(imol)`  
Scheme: `(map-sigma imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `map_sigma_py`.
Also available in Scheme as `map-sigma-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_sigma(1)` | ran, returned `0.37349623441696167` |
| Scheme | `(map-sigma 1)` | ran, returned `0.37349623441696167` |

Example written and checked by hand on the test data. Expected: returns the rms (sigma) of map 1; False if not a map.

Python and Scheme gave the same answer.

### map_statistics

Python: `map_statistics(imol)`  
Scheme: `(map-statistics imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `map_statistics_py`.
Also available in Scheme as `map-statistics-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_statistics(1)` | ran, returned `[1.3091280948174244e-10, 0.3733606442952185, 0.07638043081814125, 6.456661785908296]` |
| Scheme | `(map-statistics 1)` | ran, returned `(1.3091280948174244e-10 0.3733606442952185 0.07638043081814125 6.456661785908296)` |

Example written and checked by hand on the test data. Expected: returns [mean, standard deviation, skew, kurtosis] of the map.

Note: mean here (1.3e-10) differs from map_mean(1) (9.4e-05): different averaging (with/without pseudo-zeros?).

Python and Scheme gave the same answer.

### map_to_model_correlation

Python: `map_to_model_correlation(imol, residue_specs, neighb_residue_specs, atom_mask_mode, imol_map)`  
Scheme: `(map-to-model-correlation imol residue-specs neighb-residue-specs atom-mask-mode imol-map)`

atom-mask-mode is as follows:
0: all-atoms
1: main-chain atoms if is standard amino-acid, else all atoms
2: side-chain atoms if is standard amino-acid, else all atoms
3: side-chain atoms-excluding CB if is standard amino-acid, else all atoms
4: main-chain atoms if is standard amino-acid, else nothing
5: side-chain atoms if is standard amino-acid, else nothing
10: atom radius is dependent atom atom B-factor

Arguments: imol (a whole number), residue_specs (a list or value), neighb_residue_specs (a list or value), atom_mask_mode (a whole number), imol_map (a whole number). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_to_model_correlation(0, [["A", 41, ""], ["A", 42, ""]], [], 0, 1)` | ran, returned `0.534332811832428` |
| Scheme | `(map-to-model-correlation 0 (list (list "A" 41 "") (list "A" 42 "")) (list) 0 1)` | ran, returned `0.534332811832428` |

Example written and checked by hand on the test data. Expected: returns the map-model correlation (a number between -1 and 1) for the residues; nothing changes.

Note: neighb_residue_specs must be a LIST of residue specs (possibly empty); a single spec as in the old example raises SystemError in Python

Python and Scheme gave the same answer.

### map_to_model_correlation_per_residue

Python: `map_to_model_correlation_per_residue(imol, residue_specs, atom_mask_mode, imol_map)`  
Scheme: `(map-to-model-correlation-per-residue imol residue-specs atom-mask-mode imol-map)`

map to model density correlation, reported per residue
 atom-mask-mode is as follows:
0: all-atoms
1: main-chain atoms if is standard amino-acid, else all atoms
2: side-chain atoms if is standard amino-acid, else all atoms
3: side-chain atoms-excluding CB if is standard amino-acid, else all atoms
4: main-chain atoms if is standard amino-acid, else nothing
5: side-chain atoms if is standard amino-acid, else nothing

Arguments: imol (a whole number), residue_specs (a list or value), atom_mask_mode (a whole number), imol_map (a whole number). Returns: a value (see the result of the example).
Also available in Python as `map_to_model_correlation_per_residue_py`.
Also available in Scheme as `map-to-model-correlation-per-residue-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_to_model_correlation_per_residue(0, [["A", 41, ""], ["A", 42, ""]], 1, 1)` | ran, returned `[[[True, 'A', 41, ''], 0.27271050214767456], [[True, 'A', 42, ''], 0.7473998069763184]]` |
| Scheme | `(map-to-model-correlation-per-residue 0 (list (list "A" 41 "") (list "A" 42 "")) 1 1)` | ran, returned `(((#t "A" 41 "") 0.27271050214767456) ((#t "A" 42 "") 0.7473998069763184))` |

Python and Scheme gave the same answer.

### map_to_model_correlation_stats

Python: `map_to_model_correlation_stats(imol, residue_specs, neighb_residue_specs, atom_mask_mode, imol_map)`  
Scheme: `(map-to-model-correlation-stats imol residue-specs neighb-residue-specs atom-mask-mode imol-map)`

map to model density correlation stats
 atom-mask-mode is as follows:
0: all-atoms
1: main-chain atoms if is standard amino-acid, else all atoms
2: side-chain atoms if is standard amino-acid, else all atoms
3: side-chain atoms-excluding CB if is standard amino-acid, else all atoms
4: main-chain atoms if is standard amino-acid, else nothing
5: side-chain atoms if is standard amino-acid, else nothing

Arguments: imol (a whole number), residue_specs (a list or value), neighb_residue_specs (a list or value), atom_mask_mode (a whole number), imol_map (a whole number). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_to_model_correlation_stats(0, [["A", 41, ""], ["A", 42, ""]], [["A", 40, ""]], 0, 1)` | ran, returned `[0.548732629869392, 0.3522034760120561, 0.20996179099783185, 1129.0, 758.1366588845849, 223.62884630216286]` |
| Scheme | `(map-to-model-correlation-stats 0 (list (list "A" 41 "") (list "A" 42 "")) (list (list "A" 40 "")) 0 1)` | ran, returned `(0.548732629869392 0.3522034760120561 0.20996179099783185 1129 758.1366588845849 223.62884630216286 0.16908523276233844  ...` |

Example written and checked by hand on the test data. Expected: returns a list of statistics, first the correlation, then variances, number of grid points and sums.

Note: Python returns 6 values, Scheme returns 12 (Scheme adds more sums/means); same first 6

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### map-to-model-correlation-stats-per-residue-scm

Scheme: `(map-to-model-correlation-stats-per-residue-scm imol residue-specs-scm atom-mask-mode atom-radius-for-masking imol-map)`

map to model stats

Arguments: imol (a whole number), residue-specs-scm (a list or value), atom-mask-mode (a whole number), atom-radius-for-masking (a number), imol-map (a whole number). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | `(map-to-model-correlation-stats-per-residue-scm 0 (list (list "A" 41 "") (list "A" 42 "")) 1 5.0 1)` | ran, returned `(((#t "A" 41 "") (-0.06600063564065085 0.1473731077517851)) ((#t "A" 42 "") (-0.036889933628944244 0.12350242598888322)) ...` |

### map_to_model_correlation_stats_per_residue_range_py

Python: `map_to_model_correlation_stats_per_residue_range_py(imol, chain_id, imol_map, n_residue_per_residue_range, exclude_NOC_flag)`  
Scheme: `(map-to-model-correlation-stats-per-residue-range-scm imol chain-id imol-map n-residue-per-residue-range exclude-NOC-flag)`

map to model density statistics, reported per residue, the middle residue
 of a range of residues
Returns the all-atom stats first and side chains stats second

Arguments: imol (a whole number), chain_id (text), imol_map (a whole number), n_residue_per_residue_range (a whole number), exclude_NOC_flag (a whole number). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_to_model_correlation_stats_per_residue_range_py(0, "A", 1, 1, 1)` | ran, returned `[[[[True, 'A', 1, ''], [1087, 0.7118559265818732]], [[True, 'A', 2, ''], [554, 0.3979060701858177]], [[True, 'A', 3, ''] ...` |
| Scheme | `(map-to-model-correlation-stats-per-residue-range-scm 0 "A" 1 1 1)` | ran, returned `((((#t "A" 1 "") (1087 0.7118559265818732)) ((#t "A" 2 "") (554 0.3979060701858177)) ((#t "A" 3 "") (862 0.8684288459695 ...` |

Python and Scheme gave the same answer.

### qq_plot_map_and_model

Python: `qq_plot_map_and_model(imol, residue_specs_py, neigh_residue_specs_py, atom_mask_mode, imol_map)`  
Scheme: `(qq-plot-map-and-model imol residue-specs-scm neigh-residue-specs-scm atom-mask-mode imol-map)`

Arguments: imol (a whole number), residue_specs_py (a list or value), neigh_residue_specs_py (a list or value), atom_mask_mode (a whole number), imol_map (a whole number). Returns: a value (see the result of the example).
Also available in Python as `qq_plot_map_and_model_py`.
Also available in Scheme as `qq-plot-map-and-model-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `qq_plot_map_and_model(0, [["A", 41, ""], ["A", 42, ""]], [], 0, 1)` | not run: opens a plot window (goograph); needs the graphics window (stops Coot without a screen) |
| Scheme | `(qq-plot-map-and-model 0 (list (list "A" 41 "") (list "A" 42 "")) (list) 0 1)` | not run: opens a plot window (goograph); needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens a Q-Q plot window of map vs model density for the residues.

### set_map_correlation_atom_radius

Python: `set_map_correlation_atom_radius(r)`  
Scheme: `(set-map-correlation-atom-radius r)`

The atom radius is not passed as a parameter to correlation
 functions, let's set it here (default is 1.5A)

Arguments: r (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_map_correlation_atom_radius(0.5)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-map-correlation-atom-radius 0.5)` | ran (no return value, nothing visible changed) |

