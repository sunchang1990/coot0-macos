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
| Python | `map_mean(0)` | ran, returned `False` |
| Scheme | `(map-mean-scm 0)` | ran, returned `#f` |

Python and Scheme gave the same answer.

### map_sigma

Python: `map_sigma(imol)`  
Scheme: `(map-sigma imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `map_sigma_py`.
Also available in Scheme as `map-sigma-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_sigma(0)` | ran, returned `False` |
| Scheme | `(map-sigma 0)` | ran, returned `#f` |

Python and Scheme gave the same answer.

### map_statistics

Python: `map_statistics(imol)`  
Scheme: `(map-statistics imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `map_statistics_py`.
Also available in Scheme as `map-statistics-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_statistics(0)` | ran, returned `False` |
| Scheme | `(map-statistics 0)` | ran, returned `#f` |

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
| Python | `map_to_model_correlation(0, [["A", 41, ""], ["A", 42, ""]], ["A", 41, ""], 1, 1)` | error: SystemError: <built-in function map_to_model_correlation_py> returned a result with an exception set |
| Scheme | `(map-to-model-correlation 0 (list (list "A" 41 "") (list "A" 42 "")) (list "A" 41 "") 1 1)` | error: In procedure length: Wrong type argument in position 1: "A" |

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
| Python | `map_to_model_correlation_stats(0, [["A", 41, ""], ["A", 42, ""]], ["A", 41, ""], 1, 1)` | error: SystemError: <built-in function map_to_model_correlation_stats_py> returned a result with an exception set |
| Scheme | `(map-to-model-correlation-stats 0 (list (list "A" 41 "") (list "A" 42 "")) (list "A" 41 "") 1 1)` | error: In procedure length: Wrong type argument in position 1: "A" |

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
| Python | `qq_plot_map_and_model(0, [["A", 41, ""], ["A", 42, ""]], ["A", 41, ""], 1, 1)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(qq-plot-map-and-model 0 (list (list "A" 41 "") (list "A" 42 "")) (list "A" 41 "") 1 1)` | error: In procedure length: Wrong type argument in position 1: "A" |

### set_map_correlation_atom_radius

Python: `set_map_correlation_atom_radius(r)`  
Scheme: `(set-map-correlation-atom-radius r)`

The atom radius is not passed as a parameter to correlation
 functions, let's set it here (default is 1.5A)

Arguments: r (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_map_correlation_atom_radius(0.5)` | ran (no return value) |
| Scheme | `(set-map-correlation-atom-radius 0.5)` | ran (no return value) |

