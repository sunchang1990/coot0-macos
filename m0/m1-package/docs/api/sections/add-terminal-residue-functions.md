# Add Terminal Residue Functions

[Scripting reference](../README.md) > Add Terminal Residue Functions (15 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_nucleotide

Python: `add_nucleotide(imol, chain_id, res_no)`  
Scheme: `(add-nucleotide imol chain-id res-no)`

Add a terminal nucleotide

No fitting is done

Arguments: imol (a whole number), chain_id (text), res_no (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_nucleotide(0, "A", 41)` | ran, returned `1` |
| Scheme | `(add-nucleotide 0 "A" 41)` | ran, returned `1` |

### add_terminal_residue

Python: `add_terminal_residue(imol, chain_id, residue_number, residue_type, immediate_add)`  
Scheme: `(add-terminal-residue imol chain-id residue-number residue-type immediate-add)`

Add a terminal residue

residue type can be "auto" and immediate_add is recommended to be 1.

Returns 0 on failure, 1 on success

Arguments: imol (a whole number), chain_id (text), residue_number (a whole number), residue_type (text), immediate_add (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_terminal_residue(0, "A", 41, "ALA", 1)` | ran, returned `0` |
| Scheme | `(add-terminal-residue 0 "A" 41 "ALA" 1)` | ran, returned `0` |

### add_terminal_residue_do_post_refine_state

Python: `add_terminal_residue_do_post_refine_state()`  
Scheme: `(add-terminal-residue-do-post-refine-state)`

what is the value of the previous flag?

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_terminal_residue_do_post_refine_state()` | ran, returned `0` |
| Scheme | `(add-terminal-residue-do-post-refine-state)` | ran, returned `0` |

### add_terminal_residue_immediate_addition_state

Python: `add_terminal_residue_immediate_addition_state()`  
Scheme: `(add-terminal-residue-immediate-addition-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_terminal_residue_immediate_addition_state()` | ran, returned `1` |
| Scheme | `(add-terminal-residue-immediate-addition-state)` | ran, returned `1` |

### add_terminal_residue_using_phi_psi

Python: `add_terminal_residue_using_phi_psi(imol, chain_id, res_no, residue_type, phi, psi)`  
Scheme: `(add-terminal-residue-using-phi-psi imol chain-id res-no residue-type phi psi)`

Add a terminal residue using given phi and psi angles

Returns the success status, 0 on failure, 1 on success

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), residue_type (text), phi (a number), psi (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_terminal_residue_using_phi_psi(0, "A", 41, "ALA", 10.0, 10.0)` | ran, returned `0` |
| Scheme | `(add-terminal-residue-using-phi-psi 0 "A" 41 "ALA" 10.0 10.0)` | ran, returned `0` |

### do_add_terminal_residue

Python: `do_add_terminal_residue(state)`  
Scheme: `(do-add-terminal-residue state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_add_terminal_residue(1)` | ran (no return value) |
| Scheme | `(do-add-terminal-residue 1)` | ran (no return value) |

### find_terminal_residue_type

Python: `find_terminal_residue_type(imol, chain_id, resno)`  
Scheme: `(find-terminal-residue-type imol chain-id resno)`

Arguments: imol (a whole number), chain_id (text), resno (a whole number). Returns: a value (see the result of the example).
Also available in Python as `find_terminal_residue_type_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `find_terminal_residue_type(0, "A", 41)` | ran, returned `False` |
| Scheme | `(find-terminal-residue-type 0 "A" 41)` | ran, returned `#f` |

### set_add_terminal_residue_add_other_residue_flag

Python: `set_add_terminal_residue_add_other_residue_flag(i)`  
Scheme: `(set-add-terminal-residue-add-other-residue-flag i)`

Add Terminal Residues actually build 2 residues, this allows us to
 see both residues - default is 0 (off).

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_terminal_residue_add_other_residue_flag(1)` | not tried |
| Scheme | `(set-add-terminal-residue-add-other-residue-flag 1)` | not tried |

### set_add_terminal_residue_debug_trials

Python: `set_add_terminal_residue_debug_trials(debug_state)`  
Scheme: `(set-add-terminal-residue-debug-trials debug-state)`

remove this for 0.9, wraps above

Arguments: debug_state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_terminal_residue_debug_trials(1)` | not tried |
| Scheme | `(set-add-terminal-residue-debug-trials 1)` | not tried |

### set_add_terminal_residue_default_residue_type

Python: `set_add_terminal_residue_default_residue_type(type)`  
Scheme: `(set-add-terminal-residue-default-residue-type type)`

set the residue type of an added terminal residue.

Arguments: type (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_terminal_residue_default_residue_type("ALA")` | not tried |
| Scheme | `(set-add-terminal-residue-default-residue-type "ALA")` | not tried |

### set_add_terminal_residue_do_post_refine

Python: `set_add_terminal_residue_do_post_refine(istat)`  
Scheme: `(set-add-terminal-residue-do-post-refine istat)`

set a flag to run refine zone on terminal residues after an
 addition.

Arguments: istat (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_terminal_residue_do_post_refine(1)` | not tried |
| Scheme | `(set-add-terminal-residue-do-post-refine 1)` | not tried |

### set_add_terminal_residue_do_rigid_body_refine

Python: `set_add_terminal_residue_do_rigid_body_refine(v)`  
Scheme: `(set-add-terminal-residue-do-rigid-body-refine v)`

Arguments: v (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_terminal_residue_do_rigid_body_refine(1)` | not tried |
| Scheme | `(set-add-terminal-residue-do-rigid-body-refine 1)` | not tried |

### set_add_terminal_residue_immediate_addition

Python: `set_add_terminal_residue_immediate_addition(i)`  
Scheme: `(set-add-terminal-residue-immediate-addition i)`

set immediate addition of terminal residue

call with i=1 for immediate addtion

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_terminal_residue_immediate_addition(1)` | not tried |
| Scheme | `(set-add-terminal-residue-immediate-addition 1)` | not tried |

### set_add_terminal_residue_n_phi_psi_trials

Python: `set_add_terminal_residue_n_phi_psi_trials(n)`  
Scheme: `(set-add-terminal-residue-n-phi-psi-trials n)`

mmdb_manager.h)

Arguments: n (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_terminal_residue_n_phi_psi_trials(1)` | not tried |
| Scheme | `(set-add-terminal-residue-n-phi-psi-trials 1)` | not tried |

### set_terminal_residue_do_rigid_body_refine

Python: `set_terminal_residue_do_rigid_body_refine(v)`  
Scheme: `(set-terminal-residue-do-rigid-body-refine v)`

Arguments: v (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_terminal_residue_do_rigid_body_refine(1)` | not tried |
| Scheme | `(set-terminal-residue-do-rigid-body-refine 1)` | not tried |

