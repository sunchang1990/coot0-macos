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
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### add_target_position_restraints_for_intermediate_atoms

Python: `add_target_position_restraints_for_intermediate_atoms(atom_spec_position_list)`

and the multiple-atom version of that (so that they can be applied at the same time)

Arguments: atom_spec_position_list (a list or value). Returns: a value (see the result of the example).
Also available in Python as `add_target_position_restraints_for_intermediate_atoms_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_target_position_restraints_for_intermediate_atoms(["A", 41, "", " CA ", ""])` | error: SystemError: <built-in function add_target_position_restraints_for_intermediate_atoms_py> returned a result with an exception set |

### drag_intermediate_atom

Python: `drag_intermediate_atom(atom_spec, position)`  
Scheme: `(drag-intermediate-atom atom-spec position)`

Arguments: atom_spec (a list or value), position (a list or value). Returns: a value (see the result of the example).
Also available in Python as `drag_intermediate_atom_py`.
Also available in Scheme as `drag-intermediate-atom-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

