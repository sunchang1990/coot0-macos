# check Waters Interface

[Scripting reference](../README.md) > check Waters Interface (10 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### check_waters_by_difference_map

Python: `check_waters_by_difference_map(imol_waters, imol_diff_map, interactive_flag)`  
Scheme: `(check-waters-by-difference-map imol-waters imol-diff-map interactive-flag)`

difference map variance check

Arguments: imol_waters (a whole number), imol_diff_map (a whole number), interactive_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `check_waters_by_difference_map(0, 1, 1)` | ran (no return value) |
| Scheme | `(check-waters-by-difference-map 0 1 1)` | ran (no return value) |

### check_waters_by_difference_map_sigma_level_state

Python: `check_waters_by_difference_map_sigma_level_state()`  
Scheme: `(check-waters-by-difference-map-sigma-level-state)`

Let's give access to the sigma level (default 4)

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `check_waters_by_difference_map_sigma_level_state()` | ran, returned `3.5` |
| Scheme | `(check-waters-by-difference-map-sigma-level-state)` | ran, returned `3.5` |

Python and Scheme gave the same answer.

### delete_checked_waters_baddies

Python: `delete_checked_waters_baddies(imol, b_factor_lim, map_sigma_lim, min_dist, max_dist, part_occ_contact_flag, zero_occ_flag, logical_operator_and_or_flag)`  
Scheme: `(delete-checked-waters-baddies imol b-factor-lim map-sigma-lim min-dist max-dist part-occ-contact-flag zero-occ-flag logical-operator-and-or-flag)`

Delete waters that are fail to meet the given criteria.

Arguments: imol (a whole number), b_factor_lim (a number), map_sigma_lim (a number), min_dist (a number), max_dist (a number), part_occ_contact_flag (a whole number), zero_occ_flag (a whole number), logical_operator_and_or_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_checked_waters_baddies(0, 20.0, 1.5, 1.0, 1.0, 1, 1, 1)` | ran (no return value) |
| Scheme | `(delete-checked-waters-baddies 0 20.0 1.5 1.0 1.0 1 1 1)` | ran (no return value) |

### highly_coordinated_waters

Python: `highly_coordinated_waters(imol, coordination_number, dist_max)`  
Scheme: `(highly-coordinated-waters imol coordination-number dist-max)`

return a list first of waters, second metals that are
 coordinated with at least coordination_number of other atoms at
 distances less than or equal to dist_max. Return Python false on
 not able to make a list, otherwise a list of atoms and neighours.
 can return Python False if imol is not a valid molecule.

Arguments: imol (a whole number), coordination_number (a whole number), dist_max (a number). Returns: a value (see the result of the example).
Also available in Python as `highly_coordinated_waters_py`.
Also available in Scheme as `highly-coordinated-waters-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `highly_coordinated_waters(0, 1, 1.0)` | ran, returned `[[], []]` |
| Scheme | `(highly-coordinated-waters 0 1 1.0)` | ran, returned `(())` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### metal_coordination

Python: `metal_coordination(imol, dist_max)`  
Scheme: `(metal-coordination-scm imol dist-max)`

Arguments: imol (a whole number), dist_max (a number). Returns: a value (see the result of the example).
Also available in Python as `metal_coordination_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `metal_coordination(0, 1.0)` | ran, returned `False` |
| Scheme | `(metal-coordination-scm 0 1.0)` | ran, returned `#f` |

Python and Scheme gave the same answer.

### set_check_waters_b_factor_limit

Python: `set_check_waters_b_factor_limit(f)`  
Scheme: `(set-check-waters-b-factor-limit f)`

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_check_waters_b_factor_limit(1.0)` | ran (no return value) |
| Scheme | `(set-check-waters-b-factor-limit 1.0)` | ran (no return value) |

### set_check_waters_by_difference_map_sigma_level

Python: `set_check_waters_by_difference_map_sigma_level(f)`  
Scheme: `(set-check-waters-by-difference-map-sigma-level f)`

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_check_waters_by_difference_map_sigma_level(1.0)` | ran (no return value) |
| Scheme | `(set-check-waters-by-difference-map-sigma-level 1.0)` | ran (no return value) |

### set_check_waters_map_sigma_limit

Python: `set_check_waters_map_sigma_limit(f)`  
Scheme: `(set-check-waters-map-sigma-limit f)`

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_check_waters_map_sigma_limit(1.0)` | ran (no return value) |
| Scheme | `(set-check-waters-map-sigma-limit 1.0)` | ran (no return value) |

### set_check_waters_max_dist_limit

Python: `set_check_waters_max_dist_limit(f)`  
Scheme: `(set-check-waters-max-dist-limit f)`

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_check_waters_max_dist_limit(1.0)` | ran (no return value) |
| Scheme | `(set-check-waters-max-dist-limit 1.0)` | ran (no return value) |

### set_check_waters_min_dist_limit

Python: `set_check_waters_min_dist_limit(f)`  
Scheme: `(set-check-waters-min-dist-limit f)`

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_check_waters_min_dist_limit(1.0)` | ran (no return value) |
| Scheme | `(set-check-waters-min-dist-limit 1.0)` | ran (no return value) |

