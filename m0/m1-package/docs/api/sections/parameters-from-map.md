# Parameters from map

[Scripting reference](../README.md) > Parameters from map (7 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### cell

Python: `cell(imol)`  
Scheme: `(cell imol)`

return the parameter that made the map,

Returns False or something
 like [45, 46, 47, 90, 90, 120], angles in degress

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `map_cell`, `cell_py`.
Also available in Scheme as `cell-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `cell(0)` | ran, returned `[64.897, 78.323, 38.792, 90.0, 90.0, 90.0]` |
| Scheme | `(cell 0)` | ran, returned `(64.897 78.323 38.792 90.0 90.0 90.0)` |

Python and Scheme gave the same answer.

### map_parameters

Python: `map_parameters(imol)`  
Scheme: `(map-parameters imol)`

return the parameter that made the map,

Returns False or something
 like ["xxx.mtz", "FPH", "PHWT", "", False]

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `map_parameters_py`.
Also available in Scheme as `map-parameters-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_parameters(0)` | ran, returned `False` |
| Scheme | `(map-parameters 0)` | ran, returned `#f` |

Python and Scheme gave the same answer.

### mtz_fp_for_map

Python: `mtz_fp_for_map(imol_map)`  
Scheme: `(mtz-fp-for-map imol-map)`

return the FP column in the file that was use to generate
 the map

 return 0 when there is no mtz file associated with that map (it was
 generated from a CCP4 map file say).

 Caller should dispose of returned pointer.

Arguments: imol_map (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mtz_fp_for_map(1)` | ran, returned `'FWT'` |
| Scheme | `(mtz-fp-for-map 1)` | ran, returned `"FWT"` |

Python and Scheme gave the same answer.

### mtz_hklin_for_map

Python: `mtz_hklin_for_map(imol_map)`  
Scheme: `(mtz-hklin-for-map imol-map)`

return the mtz file that was use to generate the map

 return 0 when there is no mtz file associated with that map (it was
 generated from a CCP4 map file say).

Arguments: imol_map (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mtz_hklin_for_map(1)` | ran, returned `'rnasa-1.8-all_refmac1.mtz'` |
| Scheme | `(mtz-hklin-for-map 1)` | ran, returned `"rnasa-1.8-all_refmac1.mtz"` |

Python and Scheme gave the same answer.

### mtz_phi_for_map

Python: `mtz_phi_for_map(imol_map)`  
Scheme: `(mtz-phi-for-map imol-map)`

return the phases column in mtz file that was use to generate
 the map

 return 0 when there is no mtz file associated with that map (it was
 generated from a CCP4 map file say).
 Caller should dispose of returned pointer.

Arguments: imol_map (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mtz_phi_for_map(1)` | ran, returned `'PHWT'` |
| Scheme | `(mtz-phi-for-map 1)` | ran, returned `"PHWT"` |

Python and Scheme gave the same answer.

### mtz_use_weight_for_map

Python: `mtz_use_weight_for_map(imol_map)`  
Scheme: `(mtz-use-weight-for-map imol-map)`

return flag for whether weights were used that was use to
 generate the map

 return 0 when no weights were used or there is no mtz file
 associated with that map.

Arguments: imol_map (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mtz_use_weight_for_map(1)` | ran, returned `0` |
| Scheme | `(mtz-use-weight-for-map 1)` | ran, returned `0` |

Python and Scheme gave the same answer.

### mtz_weight_for_map

Python: `mtz_weight_for_map(imol_map)`  
Scheme: `(mtz-weight-for-map imol-map)`

return the weight column in the mtz file that was use to
 generate the map

 return 0 when there is no mtz file associated with that map (it was
 generated from a CCP4 map file say) or no weights were used.
 Caller should dispose of returned pointer.

Arguments: imol_map (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mtz_weight_for_map(1)` | ran, returned `''` |
| Scheme | `(mtz-weight-for-map 1)` | ran, returned `""` |

Python and Scheme gave the same answer.

