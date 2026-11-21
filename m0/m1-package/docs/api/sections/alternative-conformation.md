# Alternative Conformation

[Scripting reference](../README.md) > Alternative Conformation (15 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_alt_conf

Python: `add_alt_conf(imol, chain_id, res_no, ins_code, alt_conf, rotamer_number)`  
Scheme: `(add-alt-conf imol chain-id res-no ins-code alt-conf rotamer-number)`

add an alternative conformer to a residue. Add it in
 conformation rotamer number rotamer_number.

Return the new alt_conf chain_id on sucess, python False on fail

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), alt_conf (text), rotamer_number (a whole number). Returns: a value (see the result of the example).
Also available in Python as `add_alt_conf_py`.
Also available in Scheme as `add-alt-conf-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_alt_conf(0, "A", 41, "", "", 0)` | ran, returned `False`; changed: molecule 0: atoms of 1 residue(s) (A41); n_atoms(0): 1465 -> 1474 |
| Scheme | `(add-alt-conf 0 "A" 41 "" "" 0)` | ran, returned `#f`; changed: molecule 0: atoms of 1 residue(s) (A41); n_atoms(0): 1465 -> 1474 |

Example written and checked by hand on the test data. Expected: splits residue A41 into two alternative conformations; documented to return the new alt conf string.

Note: alt_conf must be the EXISTING alt conf of the atoms to split ("" for an ordinary residue). The split works but the return value is False/#f although the source returns the new alt conf on success; likely the bool from split_residue is false after a successful split (suspicious).

Python and Scheme gave the same answer.

### alt_conf_split_type_number

Python: `alt_conf_split_type_number()`  
Scheme: `(alt-conf-split-type-number)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `alt_conf_split_type_number()` | ran, returned `1` |
| Scheme | `(alt-conf-split-type-number)` | ran, returned `1` |

Python and Scheme gave the same answer.

### altconf

Python: `altconf()`  
Scheme: `(altconf)`

turn off pending atom pick

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `altconf()` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(altconf)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: starts the alt-conf pick mode (click an atom in the graphics window).

### fill_occupancy_residue_range

Python: `fill_occupancy_residue_range(imol, chain_id, ires1, ires2)`  
Scheme: `(fill-occupancy-residue-range imol chain-id ires1 ires2)`

Arguments: imol (a whole number), chain_id (text), ires1 (a whole number), ires2 (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fill_occupancy_residue_range(0, "A", 1, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(fill-occupancy-residue-range 0 "A" 1 1)` | ran (no return value, nothing visible changed) |

### get_add_alt_conf_new_atoms_occupancy

Python: `get_add_alt_conf_new_atoms_occupancy()`  
Scheme: `(get-add-alt-conf-new-atoms-occupancy)`

default 0.5

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_add_alt_conf_new_atoms_occupancy()` | ran, returned `0.5` |
| Scheme | `(get-add-alt-conf-new-atoms-occupancy)` | ran, returned `0.5` |

Python and Scheme gave the same answer.

### reset_b_factor_residue_range

Python: `reset_b_factor_residue_range(imol, chain_id, ires1, ires2)`  
Scheme: `(reset-b-factor-residue-range imol chain-id ires1 ires2)`

Arguments: imol (a whole number), chain_id (text), ires1 (a whole number), ires2 (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `reset_b_factor_residue_range(0, "A", 1, 1)` | ran (no return value); changed: molecule 0: B-factors of 1 residue(s) (A1) |
| Scheme | `(reset-b-factor-residue-range 0 "A" 1 1)` | ran (no return value, nothing visible changed) |

### set_add_alt_conf_new_atoms_occupancy

Python: `set_add_alt_conf_new_atoms_occupancy(f)`  
Scheme: `(set-add-alt-conf-new-atoms-occupancy f)`

temporary debugging interface.

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_alt_conf_new_atoms_occupancy(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-add-alt-conf-new-atoms-occupancy 1.0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_add_alt_conf_new_atoms_occupancy was 0.5, set to 1.25, read back 1.25; Scheme: get-add-alt-conf-new-atoms-occupancy was 0.5, set to 1.25, read back 1.25.

### set_add_alt_conf_split_type_number

Python: `set_add_alt_conf_split_type_number(i)`  
Scheme: `(set-add-alt-conf-split-type-number i)`

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_alt_conf_split_type_number(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-add-alt-conf-split-type-number 1)` | ran (no return value, nothing visible changed) |

### set_b_factor_residue_range

Python: `set_b_factor_residue_range(imol, chain_id, ires1, ires2, bval)`  
Scheme: `(set-b-factor-residue-range imol chain-id ires1 ires2 bval)`

Arguments: imol (a whole number), chain_id (text), ires1 (a whole number), ires2 (a whole number), bval (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_b_factor_residue_range(0, "A", 1, 1, 1.0)` | ran (no return value); changed: molecule 0: B-factors of 1 residue(s) (A1) |
| Scheme | `(set-b-factor-residue-range 0 "A" 1 1 1.0)` | ran (no return value, nothing visible changed) |

### set_occupancy_residue_range

Python: `set_occupancy_residue_range(imol, chain_id, ires1, ires2, occ)`  
Scheme: `(set-occupancy-residue-range imol chain-id ires1 ires2 occ)`

Arguments: imol (a whole number), chain_id (text), ires1 (a whole number), ires2 (a whole number), occ (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_occupancy_residue_range(0, "A", 1, 1, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-occupancy-residue-range 0 "A" 1 1 1.0)` | ran (no return value, nothing visible changed) |

### set_show_alt_conf_intermediate_atoms

Python: `set_show_alt_conf_intermediate_atoms(i)`  
Scheme: `(set-show-alt-conf-intermediate-atoms i)`

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_alt_conf_intermediate_atoms(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-show-alt-conf-intermediate-atoms 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: show_alt_conf_intermediate_atoms_state was 0, set to 1, read back 1; Scheme: show-alt-conf-intermediate-atoms-state was 0, set to 1, read back 1.

### show_alt_conf_intermediate_atoms_state

Python: `show_alt_conf_intermediate_atoms_state()`  
Scheme: `(show-alt-conf-intermediate-atoms-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_alt_conf_intermediate_atoms_state()` | ran, returned `0` |
| Scheme | `(show-alt-conf-intermediate-atoms-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### unset_add_alt_conf_define

Python: `unset_add_alt_conf_define()`  
Scheme: `(unset-add-alt-conf-define)`

set the static dialog holder in
 graphics info to NULL

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `unset_add_alt_conf_define()` | ran (no return value, nothing visible changed) |
| Scheme | `(unset-add-alt-conf-define)` | ran (no return value, nothing visible changed) |

### unset_add_alt_conf_dialog

Python: `unset_add_alt_conf_dialog()`  
Scheme: `(unset-add-alt-conf-dialog)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `unset_add_alt_conf_dialog()` | ran (no return value, nothing visible changed) |
| Scheme | `(unset-add-alt-conf-dialog)` | ran (no return value, nothing visible changed) |

### zero_occupancy_residue_range

Python: `zero_occupancy_residue_range(imol, chain_id, ires1, ires2)`  
Scheme: `(zero-occupancy-residue-range imol chain-id ires1 ires2)`

Arguments: imol (a whole number), chain_id (text), ires1 (a whole number), ires2 (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `zero_occupancy_residue_range(0, "A", 1, 1)` | ran (no return value); changed: molecule 0: occupancies of 1 residue(s) (A1) |
| Scheme | `(zero-occupancy-residue-range 0 "A" 1 1)` | ran (no return value, nothing visible changed) |

