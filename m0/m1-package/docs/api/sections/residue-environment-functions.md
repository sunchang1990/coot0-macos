# Residue Environment Functions

[Scripting reference](../README.md) > Residue Environment Functions (11 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_atom_geometry_distance

Python: `add_atom_geometry_distance(imol_1, atom_spec_1, imol_2, atom_spec_2)`  
Scheme: `(add-atom-geometry-distance-scm imol-1 atom-spec-1 imol-2 atom-spec-2)`

Arguments: imol_1 (a whole number), atom_spec_1 (a list or value), imol_2 (a whole number), atom_spec_2 (a list or value). Returns: a number.
Also available in Python as `add_atom_geometry_distance_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_atom_geometry_distance(0, ["A", 41, "", " CA ", ""], 0, ["A", 41, "", " CA ", ""])` | ran, returned `0.0` |
| Scheme | `(add-atom-geometry-distance-scm 0 (list "A" 41 "" " CA " "") 0 (list "A" 41 "" " CA " ""))` | ran, returned `0.0` |

Python and Scheme gave the same answer.

### add_geometry_distance

Python: `add_geometry_distance(imol_1, x_1, y_1, z_1, imol_2, x_2, y_2, z_2)`  
Scheme: `(add-geometry-distance imol-1 x-1 y-1 z-1 imol-2 x-2 y-2 z-2)`

Add a geometry distance between points in a given molecule

Returns the distance between the points

Arguments: imol_1 (a whole number), x_1 (a number), y_1 (a number), z_1 (a number), imol_2 (a whole number), x_2 (a number), y_2 (a number), z_2 (a number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_geometry_distance(0, 1.0, 1.0, 1.0, 0, 1.0, 1.0, 1.0)` | ran, returned `0.0` |
| Scheme | `(add-geometry-distance 0 1.0 1.0 1.0 0 1.0 1.0 1.0)` | ran, returned `0.0` |

Python and Scheme gave the same answer.

### label_atoms_in_residue

Python: `label_atoms_in_residue()`  
Scheme: `(label-atoms-in-residue)`

Label the atoms in the central residue

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `label_atoms_in_residue()` | ran (no return value, nothing visible changed) |
| Scheme | `(label-atoms-in-residue)` | ran (no return value, nothing visible changed) |

### label_neighbours

Python: `label_neighbours()`  
Scheme: `(label-neighbours)`

Label the atoms in the residues around the central residue

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `label_neighbours()` | ran (no return value, nothing visible changed) |
| Scheme | `(label-neighbours)` | ran (no return value, nothing visible changed) |

### set_environment_distances_distance_limits

Python: `set_environment_distances_distance_limits(min_dist, max_dist)`  
Scheme: `(set-environment-distances-distance-limits min-dist max-dist)`

min and max distances for the environment distances

Arguments: min_dist (a number), max_dist (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_environment_distances_distance_limits(1.0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-environment-distances-distance-limits 1.0 1.0)` | ran (no return value, nothing visible changed) |

### set_environment_distances_label_atom

Python: `set_environment_distances_label_atom(state)`  
Scheme: `(set-environment-distances-label-atom state)`

Label the atom on Environment Distances start/change

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_environment_distances_label_atom(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-environment-distances-label-atom 1)` | ran (no return value, nothing visible changed) |

### set_show_environment_distances

Python: `set_show_environment_distances(state)`  
Scheme: `(set-show-environment-distances state)`

show environment distances. If state is 0, distances are
 turned off, otherwise distances are turned on.

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_environment_distances(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-show-environment-distances 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: show_environment_distances_state was 1, set to 0, read back 0; Scheme: show-environment-distances-state was 1, set to 0, read back 0.

### set_show_environment_distances_as_solid

Python: `set_show_environment_distances_as_solid(state)`  
Scheme: `(set-show-environment-distances-as-solid state)`

show the environment distances with solid modelling

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_environment_distances_as_solid(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-show-environment-distances-as-solid 1)` | ran (no return value, nothing visible changed) |

### set_show_environment_distances_bumps

Python: `set_show_environment_distances_bumps(state)`  
Scheme: `(set-show-environment-distances-bumps state)`

show bumps environment distances. If state is 0, bump distances are
 turned off, otherwise bump distances are turned on.

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_environment_distances_bumps(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-show-environment-distances-bumps 1)` | ran (no return value, nothing visible changed) |

### set_show_environment_distances_h_bonds

Python: `set_show_environment_distances_h_bonds(state)`  
Scheme: `(set-show-environment-distances-h-bonds state)`

show H-bond environment distances. If state is 0, bump distances are
 turned off, otherwise H-bond distances are turned on.

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_environment_distances_h_bonds(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-show-environment-distances-h-bonds 1)` | ran (no return value, nothing visible changed) |

### show_environment_distances_state

Python: `show_environment_distances_state()`  
Scheme: `(show-environment-distances-state)`

show the state of display of the environment distances

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_environment_distances_state()` | ran, returned `1` |
| Scheme | `(show-environment-distances-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

