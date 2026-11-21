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

Python and Scheme gave the same answer.

### add_terminal_residue

Python: `add_terminal_residue(imol, chain_id, residue_number, residue_type, immediate_add)`  
Scheme: `(add-terminal-residue imol chain-id residue-number residue-type immediate-add)`

Add a terminal residue

residue type can be "auto" and immediate_add is recommended to be 1.

Returns 0 on failure, 1 on success

Arguments: imol (a whole number), chain_id (text), residue_number (a whole number), residue_type (text), immediate_add (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_terminal_residue(0, "A", 93, "auto", 1)` | ran, returned `1`; changed: molecule 0: added 1 residue(s) (A94); molecule 0: coordinates of 1 residue(s) (A93); n_atoms(0): 1465 -> 1470; n_residues(0): 189 -> 190 |
| Scheme | `(add-terminal-residue 0 "A" 93 "auto" 1)` | ran, returned `1`; changed: molecule 0: added 1 residue(s) (A94); molecule 0: coordinates of 1 residue(s) (A93); n_atoms(0): 1465 -> 1470; n_residues(0): 189 -> 190 |

Example written and checked by hand on the test data. Expected: returns 1 and a new residue appears after the C-terminal residue A93 (fitted to the refinement map).

Python and Scheme gave the same answer.

### add_terminal_residue_do_post_refine_state

Python: `add_terminal_residue_do_post_refine_state()`  
Scheme: `(add-terminal-residue-do-post-refine-state)`

what is the value of the previous flag?

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_terminal_residue_do_post_refine_state()` | ran, returned `0` |
| Scheme | `(add-terminal-residue-do-post-refine-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### add_terminal_residue_immediate_addition_state

Python: `add_terminal_residue_immediate_addition_state()`  
Scheme: `(add-terminal-residue-immediate-addition-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_terminal_residue_immediate_addition_state()` | ran, returned `1` |
| Scheme | `(add-terminal-residue-immediate-addition-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### add_terminal_residue_using_phi_psi

Python: `add_terminal_residue_using_phi_psi(imol, chain_id, res_no, residue_type, phi, psi)`  
Scheme: `(add-terminal-residue-using-phi-psi imol chain-id res-no residue-type phi psi)`

Add a terminal residue using given phi and psi angles

Returns the success status, 0 on failure, 1 on success

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), residue_type (text), phi (a number), psi (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_terminal_residue_using_phi_psi(0, "A", 93, "ALA", -57.0, -47.0)` | ran, returned `1`; changed: molecule 0: added 1 residue(s) (A94); molecule 0: coordinates of 1 residue(s) (A93); n_atoms(0): 1465 -> 1470; n_residues(0): 189 -> 190 |
| Scheme | `(add-terminal-residue-using-phi-psi 0 "A" 93 "GLY" -57.0 -47.0)` | ran, returned `1`; changed: molecule 0: added 1 residue(s) (A94); molecule 0: coordinates of 1 residue(s) (A93); n_atoms(0): 1465 -> 1470; n_residues(0): 189 -> 190 |

Example written and checked by hand on the test data. Expected: returns 1 and adds a residue of the given type after A93 with helical phi/psi.

Python and Scheme gave the same answer.

### do_add_terminal_residue

Python: `do_add_terminal_residue(state)`  
Scheme: `(do-add-terminal-residue state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_add_terminal_residue(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(do-add-terminal-residue 1)` | ran (no return value, nothing visible changed) |

### find_terminal_residue_type

Python: `find_terminal_residue_type(imol, chain_id, resno)`  
Scheme: `(find-terminal-residue-type imol chain-id resno)`

Arguments: imol (a whole number), chain_id (text), resno (a whole number). Returns: a value (see the result of the example).
Also available in Python as `find_terminal_residue_type_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `assign_sequence_from_string(0, "A", "DVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLIDQTC")`, then `find_terminal_residue_type(0, "A", 94)` | ran, returned `'GLN'` |
| Scheme | first `(assign-sequence-from-string 0 "A" "DVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLIDQTC")`, then `(find-terminal-residue-type 0 "A" 94)` | ran, returned `"GLN"` |

Example written and checked by hand on the test data. Expected: returns the residue type the assigned sequence has at the new position A94 (GLN); False/#f when no sequence is assigned to the chain.

Note: resno is the number of the residue to be ADDED (94), not the current terminal residue.

Python and Scheme gave the same answer.

### set_add_terminal_residue_add_other_residue_flag

Python: `set_add_terminal_residue_add_other_residue_flag(i)`  
Scheme: `(set-add-terminal-residue-add-other-residue-flag i)`

Add Terminal Residues actually build 2 residues, this allows us to
 see both residues - default is 0 (off).

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_terminal_residue_add_other_residue_flag(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-add-terminal-residue-add-other-residue-flag 1)` | ran (no return value, nothing visible changed) |

### set_add_terminal_residue_debug_trials

Python: `set_add_terminal_residue_debug_trials(debug_state)`  
Scheme: `(set-add-terminal-residue-debug-trials debug-state)`

remove this for 0.9, wraps above

Arguments: debug_state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_terminal_residue_debug_trials(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-add-terminal-residue-debug-trials 1)` | ran (no return value, nothing visible changed) |

### set_add_terminal_residue_default_residue_type

Python: `set_add_terminal_residue_default_residue_type(type)`  
Scheme: `(set-add-terminal-residue-default-residue-type type)`

set the residue type of an added terminal residue.

Arguments: type (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_terminal_residue_default_residue_type("ALA")` | ran (no return value, nothing visible changed) |
| Scheme | `(set-add-terminal-residue-default-residue-type "ALA")` | ran (no return value, nothing visible changed) |

### set_add_terminal_residue_do_post_refine

Python: `set_add_terminal_residue_do_post_refine(istat)`  
Scheme: `(set-add-terminal-residue-do-post-refine istat)`

set a flag to run refine zone on terminal residues after an
 addition.

Arguments: istat (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_terminal_residue_do_post_refine(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-add-terminal-residue-do-post-refine 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: add_terminal_residue_do_post_refine_state was 0, set to 1, read back 1; Scheme: add-terminal-residue-do-post-refine-state was 0, set to 1, read back 1.

### set_add_terminal_residue_do_rigid_body_refine

Python: `set_add_terminal_residue_do_rigid_body_refine(v)`  
Scheme: `(set-add-terminal-residue-do-rigid-body-refine v)`

Arguments: v (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_terminal_residue_do_rigid_body_refine(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-add-terminal-residue-do-rigid-body-refine 1)` | ran (no return value, nothing visible changed) |

### set_add_terminal_residue_immediate_addition

Python: `set_add_terminal_residue_immediate_addition(i)`  
Scheme: `(set-add-terminal-residue-immediate-addition i)`

set immediate addition of terminal residue

call with i=1 for immediate addtion

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_terminal_residue_immediate_addition(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-add-terminal-residue-immediate-addition 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: add_terminal_residue_immediate_addition_state was 1, set to 0, read back 0; Scheme: add-terminal-residue-immediate-addition-state was 1, set to 0, read back 0.

### set_add_terminal_residue_n_phi_psi_trials

Python: `set_add_terminal_residue_n_phi_psi_trials(n)`  
Scheme: `(set-add-terminal-residue-n-phi-psi-trials n)`

mmdb_manager.h)

Arguments: n (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_terminal_residue_n_phi_psi_trials(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-add-terminal-residue-n-phi-psi-trials 1)` | ran (no return value, nothing visible changed) |

### set_terminal_residue_do_rigid_body_refine

Python: `set_terminal_residue_do_rigid_body_refine(v)`  
Scheme: `(set-terminal-residue-do-rigid-body-refine v)`

Arguments: v (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_terminal_residue_do_rigid_body_refine(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-terminal-residue-do-rigid-body-refine 1)` | ran (no return value, nothing visible changed) |

