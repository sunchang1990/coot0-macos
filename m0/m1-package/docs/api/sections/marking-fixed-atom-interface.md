# Marking Fixed Atom Interface

[Scripting reference](../README.md) > Marking Fixed Atom Interface (6 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### clear_all_fixed_atoms

Python: `clear_all_fixed_atoms(imol)`  
Scheme: `(clear-all-fixed-atoms imol)`

clear all fixed atoms

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_all_fixed_atoms(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(clear-all-fixed-atoms 0)` | ran (no return value, nothing visible changed) |

### clear_fixed_atoms_all

Python: `clear_fixed_atoms_all()`  
Scheme: `(clear-fixed-atoms-all)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_fixed_atoms_all()` | ran (no return value, nothing visible changed) |
| Scheme | `(clear-fixed-atoms-all)` | ran (no return value, nothing visible changed) |

### mark_atom_as_fixed

Python: `mark_atom_as_fixed(imol, atom_spec, state)`  
Scheme: `(mark-atom-as-fixed imol atom-spec state)`

Arguments: imol (a whole number), atom_spec (a list or value), state (a whole number). Returns: a value (see the result of the example).
Also available in Python as `mark_atom_as_fixed_py`.
Also available in Scheme as `mark-atom-as-fixed-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mark_atom_as_fixed(0, ["A", 41, "", " CA ", ""], 1)` | ran, returned `True` |
| Scheme | `(mark-atom-as-fixed 0 (list "A" 41 "" " CA " "") 1)` | ran, returned `#f` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### mark_multiple_atoms_as_fixed

Python: `mark_multiple_atoms_as_fixed(imol, atom_spec_list, state)`  
Scheme: `(mark-multiple-atoms-as-fixed-scm imol atom-spec-list state)`

Arguments: imol (a whole number), atom_spec_list (a list or value), state (a whole number). Returns: a whole number.
Also available in Python as `mark_multiple_atoms_as_fixed_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mark_multiple_atoms_as_fixed(0, [["A", 41, "", " CA ", ""], ["A", 41, "", " CB ", ""]], 1)` | ran, returned `2` |
| Scheme | `(mark-multiple-atoms-as-fixed-scm 0 (list (list "A" 41 "" " CA " "") (list "A" 41 "" " CB " "")) 1)` | ran, returned `2` |

Example written and checked by hand on the test data. Expected: returns the number of atoms marked as fixed for refinement (2 here).

Note: atom specs are [chain, resno, ins, atom-name, alt-conf]

Python and Scheme gave the same answer.

### set_debug_atom_picking

Python: `set_debug_atom_picking(istate)`  
Scheme: `(set-debug-atom-picking istate)`

produce debugging output from problematic atom picking

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_debug_atom_picking(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-debug-atom-picking 1)` | ran (no return value, nothing visible changed) |

### setup_fixed_atom_pick

Python: `setup_fixed_atom_pick(ipick, is_unpick)`  
Scheme: `(setup-fixed-atom-pick ipick is-unpick)`

Arguments: ipick (a whole number), is_unpick (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_fixed_atom_pick(1, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(setup-fixed-atom-pick 1 1)` | ran (no return value, nothing visible changed) |

