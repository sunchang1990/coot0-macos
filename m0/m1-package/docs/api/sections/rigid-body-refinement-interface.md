# Rigid Body Refinement Interface

[Scripting reference](../README.md) > Rigid Body Refinement Interface (6 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### do_rigid_body_refine

Python: `do_rigid_body_refine(state)`  
Scheme: `(do-rigid-body-refine state)`

a gui-based interface: setup the rigid body refinement.

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_rigid_body_refine(1)` | ran (no return value) |
| Scheme | `(do-rigid-body-refine 1)` | ran (no return value) |

### execute_rigid_body_refine

Python: `execute_rigid_body_refine(auto_range_flag)`  
Scheme: `(execute-rigid-body-refine auto-range-flag)`

Arguments: auto_range_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `execute_rigid_body_refine(1)` | ran (no return value) |
| Scheme | `(execute-rigid-body-refine 1)` | ran (no return value) |

### rigid_body_refine_by_atom_selection

Python: `rigid_body_refine_by_atom_selection(imol, atom_selection_string)`  
Scheme: `(rigid-body-refine-by-atom-selection imol atom-selection-string)`

Arguments: imol (a whole number), atom_selection_string (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `rigid_body_refine_by_atom_selection(0, "//A/41-45")` | not tried |
| Scheme | `(rigid-body-refine-by-atom-selection 0 "//A/41-45")` | not tried |

### rigid_body_refine_by_residue_ranges

Python: `rigid_body_refine_by_residue_ranges(imol, residue_ranges)`  
Scheme: `(rigid-body-refine-by-residue-ranges imol residue-ranges)`

rigid body refine using residue ranges. residue_ranges is
 a list of residue ranges. A residue range is [chain_id,
 resno_start, resno_end].

Arguments: imol (a whole number), residue_ranges (a list or value). Returns: a value (see the result of the example).
Also available in Python as `rigid_body_refine_by_residue_ranges_py`.
Also available in Scheme as `rigid-body-refine-by-residue-ranges-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

### rigid_body_refine_zone

Python: `rigid_body_refine_zone(reso_start, resno_end, chain_id, imol)`  
Scheme: `(rigid-body-refine-zone reso-start resno-end chain-id imol)`

setup rigid body refine zone

 where we set the atom selection
 holders according to the arguments and then call
 execute_rigid_body_refine()

Arguments: reso_start (a whole number), resno_end (a whole number), chain_id (text), imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `rigid_body_refine_zone(1, 45, "A", 0)` | not tried |
| Scheme | `(rigid-body-refine-zone 1 45 "A" 0)` | not tried |

### set_rigid_body_fit_acceptable_fit_fraction

Python: `set_rigid_body_fit_acceptable_fit_fraction(f)`  
Scheme: `(set-rigid-body-fit-acceptable-fit-fraction f)`

set rigid body fraction of atoms in positive density

 @param f in the range 0.0 -> 1.0 (default 0.75)

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_rigid_body_fit_acceptable_fit_fraction(1.0)` | not tried |
| Scheme | `(set-rigid-body-fit-acceptable-fit-fraction 1.0)` | not tried |

