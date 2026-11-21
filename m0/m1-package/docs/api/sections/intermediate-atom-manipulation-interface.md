# Intermediate Atom Manipulation Interface

[Scripting reference](../README.md) > Intermediate Atom Manipulation Interface (3 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_target_position_restraint_for_intermediate_atom

Python: `add_target_position_restraint_for_intermediate_atom(atom_spec, position)`

add a target position for an intermediate atom and refine
A function requested by Hamish.
This aplies to intermediate atoms (add_extra_target_position_restraint)
does not. This activates refinement after the restraint is added (add_extra_target_position_restraint
does not).

Arguments: atom_spec (a list or value), position (a list or value). Returns: a value (see the result of the example).
Also available in Python as `add_target_position_restraint_for_intermediate_atom_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_zone(0, "A", 41, 43, ""); print(add_target_position_restraint_for_intermediate_atom(["A", 42, "", " CA ", ""], [45.0, 10.4, 15.0]))` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: during a refinement adds a target-position restraint pulling that atom to the position and refines on.

### add_target_position_restraints_for_intermediate_atoms

Python: `add_target_position_restraints_for_intermediate_atoms(atom_spec_position_list)`

and the multiple-atom version of that (so that they can be applied at the same time)

Arguments: atom_spec_position_list (a list or value). Returns: a value (see the result of the example).
Also available in Python as `add_target_position_restraints_for_intermediate_atoms_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_zone(0, "A", 41, 43, ""); print(add_target_position_restraints_for_intermediate_atoms([[["A", 42, "", " CA ", ""], [45.0, 10.4, 15.0]]]))` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: during a refinement adds target-position restraints for several atoms at once and refines; the return value is always False.

Note: Segmentation fault (Coot stopped, rc 139) with a two-atom list in a headless refinement; one-atom list survived. Possible bug in graphics_info_t::add_target_position_restraints_for_intermediate_atoms (threaded refinement).

### drag_intermediate_atom

Python: `drag_intermediate_atom(atom_spec, position)`  
Scheme: `(drag-intermediate-atom atom-spec position)`

Arguments: atom_spec (a list or value), position (a list or value). Returns: a value (see the result of the example).
Also available in Python as `drag_intermediate_atom_py`.
Also available in Scheme as `drag-intermediate-atom-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_zone(0, "A", 41, 43, ""); print(drag_intermediate_atom(["A", 42, "", " CA ", ""], [45.0, 10.4, 15.0]))` | ran (no return value, nothing visible changed) |
| Scheme | `(begin (refine-zone 0 "A" 41 43 "") (drag-intermediate-atom (list "A" 42 "" " CA " "") (list 45.0 10.4 15.0)))` | ran, returned `#f` |

Example written and checked by hand on the test data. Expected: during a refinement (intermediate atoms present) moves that atom to the position and lets the refinement follow; nothing to drag otherwise.

Python and Scheme gave the same answer.

