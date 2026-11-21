# Using S-expression molecules

[Scripting reference](../README.md) > Using S-expression molecules (10 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### closest_atom_raw

Python: `closest_atom_raw()`  
Scheme: `(closest-atom-raw-scm)`

return the specs of the closest atom to the centre of the screen
Return a list of (list imol chain-id resno ins-code atom-name
alt-conf (list x y z)) for atom that is closest to the screen
for displayed molecules. If there is no atom, return scheme false.
Don't choose the CA of the residue if there is a CA in the residue
of the closest atom

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `closest_atom_raw_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `closest_atom_raw()` | ran, returned `[0, 'A', 42, '', ' OG ', '', 42.08, 9.668, 14.424]` |
| Scheme | `(closest-atom-raw-scm)` | ran, returned `(0 "A" 42 "" " OG " "" 42.08 9.668 14.424)` |

Python and Scheme gave the same answer.

### closest_atom_simple

Python: `closest_atom_simple()`  
Scheme: `(closest-atom-simple-scm)`

return the spec of the closest displayed atom
Return a list of [imol, chain-id, resno, ins-code, atom-name,
alt-conf, [x, y, z]] for atom that is closest to the screen
centre in the given molecule (unlike active-residue, potential CA
substition is not performed). If there is no atom, or if imol is
not a valid model molecule, return False.

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `closest_atom_simple_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `closest_atom_simple()` | ran, returned `[0, 'A', 42, '', ' OG ', '']` |
| Scheme | `(closest-atom-simple-scm)` | ran, returned `(0 "A" 42 "" " OG " "")` |

Python and Scheme gave the same answer.

### get_bonds_representation

Python: `get_bonds_representation(imol)`

return a Python object for the bonds

Arguments: imol (a whole number). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_bonds_representation(0)` | ran, returned `('atom-positions', ((((44.88999938964844, 12.444999694824219, 7.35699987411499), False, [0, 'A', 1, '', ' CA ', ''], 1), ...` |

### get_continue_updating_refinement_atoms_state

Python: `get_continue_updating_refinement_atoms_state()`  
Scheme: `(get-continue-updating-refinement-atoms-state)`

return the continue-updating-refinement-atoms state
0 means off, 1 means on.
Given the current wiring of the refinement, this is always 0, i.e. refine_residues()
will return only after the atoms have finished moving.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_continue_updating_refinement_atoms_state()` | ran, returned `0` |
| Scheme | `(get-continue-updating-refinement-atoms-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### get_dictionary_radii

Python: `get_dictionary_radii()`

return a Python object for the radii of the atoms in the dictionary

Arguments: none. Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_dictionary_radii()` | ran, returned `{'ALA': {' N  ': 1.5499999523162842, ' CA ': 1.7000000476837158, ' C  ': 1.7000000476837158, ' O  ': 1.5199999809265137, ...` |

### get_environment_distances_representation

Python: `get_environment_distances_representation(imol, residue_spec_py)`

return a Python object for the representation of bump and hydrogen bonds of
 the specified residue

Arguments: imol (a whole number), residue_spec_py (a list or value). Returns: a value (see the result of the example).
Also available in Python as `get_environment_distances_representation_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_environment_distances_representation(0, ["A", 41, ""])` | ran, returned `('atom-positions', ((), ()), 'bonds', ((((47.071998596191406, 10.58899974822998, 17.410999298095703), (45.98899841308594 ...` |

### get_intermediate_atoms_bonds_representation

Python: `get_intermediate_atoms_bonds_representation()`

return a Python object for the intermediate atoms bonds

Arguments: none. Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_intermediate_atoms_bonds_representation()` | ran, returned `False` |

Example written and checked by hand on the test data. Expected: False when no refinement is in progress (there are no intermediate atoms); during an interactive refinement it returns the bonds of the moving atoms. (Python only.).

### label_closest_atoms_in_neighbour_residues_py

Python: `label_closest_atoms_in_neighbour_residues_py(imol, residue_spec_py, radius)`  
Scheme: `(label-closest-atoms-in-neighbour-residues-scm imol residue-spec-scm radius)`

label the closest atoms in the residues that neighbour residue_spec

Arguments: imol (a whole number), residue_spec_py (a list or value), radius (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `label_closest_atoms_in_neighbour_residues_py(0, ["A", 41, ""], 5.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(label-closest-atoms-in-neighbour-residues-scm 0 (list "A" 41 "") 5.0)` | ran (no return value, nothing visible changed) |

### residues_near_position

Python: `residues_near_position(imol, pos_in, radius)`  
Scheme: `(residues-near-position imol pos radius)`

Return residue specs for residues that have atoms that are
closer than radius Angstroems to the given position.

Arguments: imol (a whole number), pos_in (a list or value), radius (a number). Returns: a value (see the result of the example).
Also available in Python as `residues_near_position_py`.
Also available in Scheme as `residues-near-position-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residues_near_position(0, [48.3, 7.4, 16.9], 4.0)` | ran, returned `[[True, 'A', 37, ''], [True, 'A', 38, ''], [True, 'A', 39, ''], [True, 'A', 40, ''], [True, 'A', 41, '']]` |
| Scheme | `(residues-near-position 0 (list 48.3 7.4 16.9) 4.0)` | ran, returned `((#t "A" 41 "") (#t "A" 40 "") (#t "A" 39 "") (#t "A" 38 "") (#t "A" 37 ""))` |

Example written and checked by hand on the test data. Expected: the residue specs with an atom within 4 A of the point (the CA of A39): A37-A41. Order differs between the languages.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### residues_near_residues

Python: `residues_near_residues(imol, residues_in, radius)`  
Scheme: `(residues-near-residues imol residues-in radius)`

Return residue specs for residues that have atoms that are
closer than radius Angstroems to any atom in the residues
specified by residues_in.

Arguments: imol (a whole number), residues_in (a list or value), radius (a number). Returns: a value (see the result of the example).
Also available in Python as `residues_near_residues_py`.
Also available in Scheme as `residues-near-residues-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residues_near_residues(0, [["A", 41, ""], ["A", 42, ""]], 5.0)` | ran, returned `[[['A', 42, ''], [['A', 46, ''], ['A', 44, ''], ['A', 43, ''], ['A', 41, ''], ['A', 40, ''], ['A', 39, ''], ['B', 58, '' ...` |
| Scheme | `(residues-near-residues 0 (list (list "A" 41 "") (list "A" 42 "")) 5.0)` | ran, returned `(((#t "A" 41 "") ((#t "B" 61 "") (#t "A" 37 "") (#t "A" 39 "") (#t "A" 40 "") (#t "A" 42 "") (#t "A" 43 "") (#t "A" 44 " ...` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

