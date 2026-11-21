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
| Python | `create_pointer_atom_molecule_maybe()` | ran, returned `3`; changed: graphics_n_molecules(): 3 -> 4 |
| Scheme | `(create-pointer-atom-molecule-maybe)` | ran, returned `3`; changed: graphics_n_molecules(): 3 -> 4 |

Python and Scheme gave the same answer.

### display_where_is_pointer

Python: `display_where_is_pointer()`  
Scheme: `(display-where-is-pointer)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `display_where_is_pointer()` | ran (no return value, nothing visible changed) |
| Scheme | `(display-where-is-pointer)` | ran (no return value, nothing visible changed) |

### place_atom_at_pointer

Python: `place_atom_at_pointer()`  
Scheme: `(place-atom-at-pointer)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `place_atom_at_pointer()` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(place-atom-at-pointer)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens the Place Atom at Pointer dialog (choose atom type and molecule).

### place_atom_at_pointer_by_window

Python: `place_atom_at_pointer_by_window()`  
Scheme: `(place-atom-at-pointer-by-window)`

which calls the following gui function (if using non dummies)

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `place_atom_at_pointer_by_window()` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(place-atom-at-pointer-by-window)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens the Place Atom at Pointer dialog.

### place_typed_atom_at_pointer

Python: `place_typed_atom_at_pointer(type)`  
Scheme: `(place-typed-atom-at-pointer type)`

Arguments: type (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `place_typed_atom_at_pointer("ALA")` | ran (no return value); changed: molecule 0: added 1 residue(s) (C1); n_chains(0): 2 -> 3; n_residues(0): 189 -> 190 |
| Scheme | `(place-typed-atom-at-pointer "ALA")` | ran (no return value); changed: molecule 0: added 1 residue(s) (C2); n_residues(0): 190 -> 191 |

### pointer_atom_molecule

Python: `pointer_atom_molecule()`  
Scheme: `(pointer-atom-molecule)`

Return the current pointer atom molecule

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `pointer_atom_molecule()` | ran, returned `-1` |
| Scheme | `(pointer-atom-molecule)` | ran, returned `-1` |

Example written and checked by hand on the test data. Expected: returns the molecule of the pointer atom; -1 when none is placed (fresh Coot).

Python and Scheme gave the same answer.

### set_pointer_atom_is_dummy

Python: `set_pointer_atom_is_dummy(i)`  
Scheme: `(set-pointer-atom-is-dummy i)`

! set pointer atom is a water (HOH)

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_pointer_atom_is_dummy(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-pointer-atom-is-dummy 1)` | ran (no return value, nothing visible changed) |

### set_pointer_atom_molecule

Python: `set_pointer_atom_molecule(imol)`  
Scheme: `(set-pointer-atom-molecule imol)`

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_pointer_atom_molecule(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-pointer-atom-molecule 0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back; NOT all read back): Python: pointer_atom_molecule was -1, set to 0, read back 0; Scheme: pointer-atom-molecule was 0, set to 1, read back 0 (not taken).

