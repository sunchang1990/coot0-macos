# Pointer Atom Functions

[Scripting reference](../README.md) > Pointer Atom Functions (8 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### create_pointer_atom_molecule_maybe

Python: `create_pointer_atom_molecule_maybe()`  
Scheme: `(create-pointer-atom-molecule-maybe)`

Return the current pointer atom molecule, create a pointer
 atom molecule if necessary (i.e. when the user has not set it).

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `create_pointer_atom_molecule_maybe()` | ran, returned `2` |
| Scheme | `(create-pointer-atom-molecule-maybe)` | ran, returned `2` |

### display_where_is_pointer

Python: `display_where_is_pointer()`  
Scheme: `(display-where-is-pointer)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `display_where_is_pointer()` | ran (no return value) |
| Scheme | `(display-where-is-pointer)` | ran (no return value) |

### place_atom_at_pointer

Python: `place_atom_at_pointer()`  
Scheme: `(place-atom-at-pointer)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `place_atom_at_pointer()` | not tried |
| Scheme | `(place-atom-at-pointer)` | not tried |

### place_atom_at_pointer_by_window

Python: `place_atom_at_pointer_by_window()`  
Scheme: `(place-atom-at-pointer-by-window)`

which calls the following gui function (if using non dummies)

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `place_atom_at_pointer_by_window()` | not tried |
| Scheme | `(place-atom-at-pointer-by-window)` | not tried |

### place_typed_atom_at_pointer

Python: `place_typed_atom_at_pointer(type)`  
Scheme: `(place-typed-atom-at-pointer type)`

Arguments: type (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `place_typed_atom_at_pointer("ALA")` | not tried |
| Scheme | `(place-typed-atom-at-pointer "ALA")` | not tried |

### pointer_atom_molecule

Python: `pointer_atom_molecule()`  
Scheme: `(pointer-atom-molecule)`

Return the current pointer atom molecule

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `pointer_atom_molecule()` | not tried |
| Scheme | `(pointer-atom-molecule)` | not tried |

### set_pointer_atom_is_dummy

Python: `set_pointer_atom_is_dummy(i)`  
Scheme: `(set-pointer-atom-is-dummy i)`

! set pointer atom is a water (HOH)

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_pointer_atom_is_dummy(1)` | not tried |
| Scheme | `(set-pointer-atom-is-dummy 1)` | not tried |

### set_pointer_atom_molecule

Python: `set_pointer_atom_molecule(imol)`  
Scheme: `(set-pointer-atom-molecule imol)`

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_pointer_atom_molecule(0)` | not tried |
| Scheme | `(set-pointer-atom-molecule 0)` | not tried |

