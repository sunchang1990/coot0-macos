# Masks

[Scripting reference](../README.md) > Masks (5 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### make_masked_maps_split_by_chain

Python: `make_masked_maps_split_by_chain(imol, imol_map)`  
Scheme: `(make-masked-maps-split-by-chain imol imol-map)`

make chain masked maps

 needs to return a list of values

Arguments: imol (a whole number), imol_map (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_masked_maps_split_by_chain(0, 1)` | ran, returned `0` |
| Scheme | `(make-masked-maps-split-by-chain 0 1)` | ran, returned `0` |

Python and Scheme gave the same answer.

### map_mask_atom_radius

Python: `map_mask_atom_radius()`  
Scheme: `(map-mask-atom-radius)`

get the atom radius for map masking

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `map_mask_atom_radius()` | ran, returned `-99.0` |
| Scheme | `(map-mask-atom-radius)` | ran, returned `-99.0` |

Python and Scheme gave the same answer.

### mask_map_by_atom_selection

Python: `mask_map_by_atom_selection(map_mol_no, coords_mol_no, mmdb_atom_selection, invert_flag)`  
Scheme: `(mask-map-by-atom-selection map-mol-no coords-mol-no mmdb-atom-selection invert-flag)`

mask map by atom selection

Arguments: map_mol_no (a whole number), coords_mol_no (a whole number), mmdb_atom_selection (text), invert_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mask_map_by_atom_selection(1, 1, "//A/41-45", 1)` | ran, returned `-1` |
| Scheme | `(mask-map-by-atom-selection 1 1 "//A/41-45" 1)` | ran, returned `-1` |

Python and Scheme gave the same answer.

### mask_map_by_molecule

Python: `mask_map_by_molecule(map_mol_no, coord_mol_no, invert_flag)`  
Scheme: `(mask-map-by-molecule map-mol-no coord-mol-no invert-flag)`

generate a new map that has been masked by some coordinates

 (mask-map-by-molecule map-no mol-no invert?) creates and
 displays a masked map, cuts down density where the coordinates
 are (invert is 0). If invert? is 1, cut the density down
 where there are no atoms atoms.

Arguments: map_mol_no (a whole number), coord_mol_no (a whole number), invert_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mask_map_by_molecule(1, 1, 1)` | ran, returned `-1` |
| Scheme | `(mask-map-by-molecule 1 1 1)` | ran, returned `-1` |

Python and Scheme gave the same answer.

### set_map_mask_atom_radius

Python: `set_map_mask_atom_radius(rad)`  
Scheme: `(set-map-mask-atom-radius rad)`

set the atom radius for map masking

Arguments: rad (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_map_mask_atom_radius(5.0)` | ran (no return value) |
| Scheme | `(set-map-mask-atom-radius 5.0)` | ran (no return value) |

