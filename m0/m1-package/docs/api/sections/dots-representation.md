# Dots Representation

[Scripting reference](../README.md) > Dots Representation (6 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### clear_dots

Python: `clear_dots(imol, dots_handle)`  
Scheme: `(clear-dots imol dots-handle)`

clear dots in imol with dots_handle

Arguments: imol (a whole number), dots_handle (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_dots(0, 1)` | ran (no return value) |
| Scheme | `(clear-dots 0 1)` | ran (no return value) |

### clear_dots_by_name

Python: `clear_dots_by_name(imol, dots_object_name)`  
Scheme: `(clear-dots-by-name imol dots-object-name)`

clear the first dots object for imol with given name

Arguments: imol (a whole number), dots_object_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_dots_by_name(0, "my-name")` | ran (no return value) |
| Scheme | `(clear-dots-by-name 0 "my-name")` | ran (no return value) |

### dots

Python: `dots(imol, atom_selection_str, dots_object_name, dot_density, sphere_size_scale)`  
Scheme: `(dots imol atom-selection-str dots-object-name dot-density sphere-size-scale)`

display dotted surface

return a generic objects handle (which can be used to remove later)

Arguments: imol (a whole number), atom_selection_str (text), dots_object_name (text), dot_density (a number), sphere_size_scale (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `dots(0, "//A/41-45", "my-name", 1.0, 1.0)` | ran, returned `0` |
| Scheme | `(dots 0 "//A/41-45" "my-name" 1.0 1.0)` | ran, returned `1` |

### n_dots_sets

Python: `n_dots_sets(imol)`  
Scheme: `(n-dots-sets imol)`

return the number of dots sets for molecule number imol

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `n_dots_sets(0)` | not tried |
| Scheme | `(n-dots-sets 0)` | not tried |

### set_dots_colour

Python: `set_dots_colour(imol, r, g, b)`  
Scheme: `(set-dots-colour imol r g b)`

set the colour of the surface dots of the imol-th molecule
 to be the given single colour

 r,g,b are values between 0.0 and 1.0

Arguments: imol (a whole number), r (a number), g (a number), b (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_dots_colour(0, 0.5, 0.5, 0.5)` | not tried |
| Scheme | `(set-dots-colour 0 0.5 0.5 0.5)` | not tried |

### unset_dots_colour

Python: `unset_dots_colour(imol)`  
Scheme: `(unset-dots-colour imol)`

no longer set the dots of molecule imol to a single colour

i.e. go back to element-based colours.

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `unset_dots_colour(0)` | not tried |
| Scheme | `(unset-dots-colour 0)` | not tried |

