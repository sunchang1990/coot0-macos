# Map colour

[Scripting reference](../README.md) > Map colour (3 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_molecule_bonds_colour_map_rotation

Python: `get_molecule_bonds_colour_map_rotation(imol)`  
Scheme: `(get-molecule-bonds-colour-map-rotation imol)`

Get the colour map rotation for molecule number imol

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_molecule_bonds_colour_map_rotation(0)` | ran, returned `21.0` |
| Scheme | `(get-molecule-bonds-colour-map-rotation 0)` | ran, returned `21.0` |

### set_colour_map_rotation_for_map

Python: `set_colour_map_rotation_for_map(f)`  
Scheme: `(set-colour-map-rotation-for-map f)`

set the colour map rotation (hue change) for maps

 default: for maps is 14 degrees.

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_colour_map_rotation_for_map(1.0)` | not tried |
| Scheme | `(set-colour-map-rotation-for-map 1.0)` | not tried |

### set_molecule_bonds_colour_map_rotation

Python: `set_molecule_bonds_colour_map_rotation(imol, theta)`  
Scheme: `(set-molecule-bonds-colour-map-rotation imol theta)`

set the colour map rotation for molecule number imol

theta is in degrees

Arguments: imol (a whole number), theta (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_molecule_bonds_colour_map_rotation(0, 10.0)` | not tried |
| Scheme | `(set-molecule-bonds-colour-map-rotation 0 10.0)` | not tried |

