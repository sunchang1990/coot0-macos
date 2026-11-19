# Simplex Refinement Interface

[Scripting reference](../README.md) > Simplex Refinement Interface (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### fit_residue_range_to_map_by_simplex

Python: `fit_residue_range_to_map_by_simplex(res1, res2, altloc, chain_id, imol, imol_for_map)`  
Scheme: `(fit-residue-range-to-map-by-simplex res1 res2 altloc chain-id imol imol-for-map)`

refine residue range using simplex optimization

Arguments: res1 (a whole number), res2 (a whole number), altloc (text), chain_id (text), imol (a whole number), imol_for_map (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fit_residue_range_to_map_by_simplex(1, 1, "", "A", 0, 1)` | no answer within 60 s (slow, or waits for something) |
| Scheme | `(fit-residue-range-to-map-by-simplex 1 1 "" "A" 0 1)` | no answer within 60 s (slow, or waits for something) |

### score_residue_range_fit_to_map

Python: `score_residue_range_fit_to_map(res1, res2, altloc, chain_id, imol, imol_for_map)`  
Scheme: `(score-residue-range-fit-to-map res1 res2 altloc chain-id imol imol-for-map)`

simply score the residue range fit to map

Arguments: res1 (a whole number), res2 (a whole number), altloc (text), chain_id (text), imol (a whole number), imol_for_map (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `score_residue_range_fit_to_map(1, 1, "", "A", 0, 1)` | not tried |
| Scheme | `(score-residue-range-fit-to-map 1 1 "" "A" 0 1)` | not tried |

