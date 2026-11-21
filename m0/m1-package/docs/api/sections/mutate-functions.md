# Mutate Functions

[Scripting reference](../README.md) > Mutate Functions (17 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### do_base_mutation

Python: `do_base_mutation(type)`  
Scheme: `(do-base-mutation type)`

an internal function - not useful for scripting:

Arguments: type (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_base_mutation("ALA")` | ran (no return value, nothing visible changed) |
| Scheme | `(do-base-mutation "ALA")` | ran (no return value, nothing visible changed) |

### do_mutation

Python: `do_mutation(type, is_stub_flag)`  
Scheme: `(do-mutation type is-stub-flag)`

Arguments: type (text), is_stub_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_mutation("ALA", 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(do-mutation "ALA" 1)` | ran (no return value, nothing visible changed) |

### handle_residue_type_chooser_entry_chose_type

Python: `handle_residue_type_chooser_entry_chose_type(entry_text, stub_mode)`  
Scheme: `(handle-residue-type-chooser-entry-chose-type entry-text stub-mode)`

Arguments: entry_text (text), stub_mode (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_residue_type_chooser_entry_chose_type("hello", 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(handle-residue-type-chooser-entry-chose-type "hello" 1)` | ran (no return value, nothing visible changed) |

### mutate

Python: `mutate(imol, chain_id, ires, inscode, target_res_type)`  
Scheme: `(mutate imol chain-id ires inscode target-res-type)`

mutate a given residue

target_res_type is a three-letter-code.

Return 1 on a good mutate.

Arguments: imol (a whole number), chain_id (text), ires (a whole number), inscode (text), target_res_type (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mutate(0, "A", 41, "", "ALA")` | ran, returned `1`; changed: molecule 0: atoms of 1 residue(s) (A41); n_atoms(0): 1465 -> 1461 |
| Scheme | `(mutate 0 "A" 41 "" "ALA")` | ran, returned `1`; changed: molecule 0: atoms of 1 residue(s) (A41); n_atoms(0): 1465 -> 1461 |

Python and Scheme gave the same answer.

### mutate_active_residue

Python: `mutate_active_residue()`  
Scheme: `(mutate-active-residue)`

display a dialog that allows the choice of residue type to which to mutate

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mutate_active_residue()` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(mutate-active-residue)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens the residue-type chooser to mutate the active residue (the one at the centre of the screen).

### mutate_auto_fit_do_post_refine_state

Python: `mutate_auto_fit_do_post_refine_state()`  
Scheme: `(mutate-auto-fit-do-post-refine-state)`

what is the value of the previous flag?

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mutate_auto_fit_do_post_refine_state()` | ran, returned `0` |
| Scheme | `(mutate-auto-fit-do-post-refine-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### mutate_base

Python: `mutate_base(imol, chain_id, res_no, ins_code, res_type)`  
Scheme: `(mutate-base imol chain-id res-no ins-code res-type)`

mutate a base. return success status, 1 for a good mutate.

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), res_type (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mutate_base(0, "A", 41, "", "ALA")` | ran, returned `1` |
| Scheme | `(mutate-base 0 "A" 41 "" "ALA")` | ran, returned `1` |

Python and Scheme gave the same answer.

### mutate_single_residue_by_seqno

Python: `mutate_single_residue_by_seqno(ires, inscode, chain_id, imol, target_res_type)`  
Scheme: `(mutate-single-residue-by-seqno ires inscode chain-id imol target-res-type)`

ires is the seqnum of the residue (conventional)

Arguments: ires (a whole number), inscode (text), chain_id (text), imol (a whole number), target_res_type (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mutate_single_residue_by_seqno(41, "", "A", 0, "A")` | ran, returned `1`; changed: molecule 0: atoms of 1 residue(s) (A41); n_atoms(0): 1465 -> 1461 |
| Scheme | `(mutate-single-residue-by-seqno 41 "" "A" 0 #\A)` | ran, returned `1`; changed: molecule 0: atoms of 1 residue(s) (A41); n_atoms(0): 1465 -> 1461 |

Example written and checked by hand on the test data. Expected: returns 1 and mutates residue A41 to the one-letter target type (A = ALA); argument order is resno, inscode, chain, imol, type.

Python and Scheme gave the same answer.

### mutate_single_residue_by_serial_number

Python: `mutate_single_residue_by_serial_number(ires_ser, chain_id, imol, target_res_type)`  
Scheme: `(mutate-single-residue-by-serial-number ires-ser chain-id imol target-res-type)`

an alternate interface to mutation of a singe residue.

 Returns 1 on success, 0 on failure

 ires-ser is the serial number of the residue, not the seqnum
 There 2 functions don't make backups, but mutate() does - CHECKME
 Hence mutate() is for use as a "one-by-one" type and the following
 2 by wrappers that muate either a residue range or a whole chain

 Note that the target_res_type is a char, not a string (or a char *).
 So from the scheme interface you'd use (for example) hash
 backslash A for ALA.

Arguments: ires_ser (a whole number), chain_id (text), imol (a whole number), target_res_type (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mutate_single_residue_by_serial_number(2, "A", 0, "G")` | ran, returned `1`; changed: molecule 0: atoms of 1 residue(s) (A3); n_atoms(0): 1465 -> 1463 |
| Scheme | `(mutate-single-residue-by-serial-number 2 "A" 0 #\G)` | ran, returned `1`; changed: molecule 0: atoms of 1 residue(s) (A3); n_atoms(0): 1465 -> 1463 |

Example written and checked by hand on the test data. Expected: returns 1 and mutates the residue with that serial number (0-based position in the chain, not the residue number) to the one-letter type.

Python and Scheme gave the same answer.

### nudge_residue_sequence

Python: `nudge_residue_sequence(imol, chain_id, res_no_range_start, res_no_range_end, nudge_by, nudge_residue_numbers_also)`  
Scheme: `(nudge-residue-sequence imol chain-id res-no-range-start res-no-range-end nudge-by nudge-residue-numbers-also)`

push the residues along a bit

e.g. if nudge_by is 1, then the sidechain of residue 20 is moved up
onto what is currently residue 21. The mainchain numbering and atoms is not changed.

Returns 0 for failure to nudge (becauese not all the residues were in the range)
 and 1 for success.

Arguments: imol (a whole number), chain_id (text), res_no_range_start (a whole number), res_no_range_end (a whole number), nudge_by (a whole number), nudge_residue_numbers_also (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `nudge_residue_sequence(0, "A", 41, 45, 1, 1)` | ran, returned `1`; changed: molecule 0: deleted 1 residue(s) (A45); molecule 0: atoms of 5 residue(s) (A40, A41, A42, A43 ...); n_atoms(0): 1465 -> 1467 |
| Scheme | `(nudge-residue-sequence 0 "A" 41 45 1 1)` | ran, returned `1`; changed: molecule 0: deleted 1 residue(s) (A45); molecule 0: atoms of 5 residue(s) (A40, A41, A42, A43 ...); n_atoms(0): 1465 -> 1467 |

Python and Scheme gave the same answer.

### progressive_residues_in_chain_check

Python: `progressive_residues_in_chain_check(chain_id, imol)`  
Scheme: `(progressive-residues-in-chain-check chain-id imol)`

auto-mutate stuff

Arguments: chain_id (text), imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `progressive_residues_in_chain_check("A", 0)` | ran, returned `1` |
| Scheme | `(progressive-residues-in-chain-check "A" 0)` | ran, returned `1` |

Python and Scheme gave the same answer.

### rotamer_auto_fit_do_post_refine_state

Python: `rotamer_auto_fit_do_post_refine_state()`  
Scheme: `(rotamer-auto-fit-do-post-refine-state)`

what is the value of the previous flag?

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `rotamer_auto_fit_do_post_refine_state()` | ran, returned `0` |
| Scheme | `(rotamer-auto-fit-do-post-refine-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### set_mutate_auto_fit_do_post_refine

Python: `set_mutate_auto_fit_do_post_refine(istate)`  
Scheme: `(set-mutate-auto-fit-do-post-refine istate)`

Do you want Coot to automatically run a refinement after
 every mutate and autofit?

 1 for yes, 0 for no.

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_mutate_auto_fit_do_post_refine(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-mutate-auto-fit-do-post-refine 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: mutate_auto_fit_do_post_refine_state was 0, set to 1, read back 1; Scheme: mutate-auto-fit-do-post-refine-state was 0, set to 1, read back 1.

### set_residue_type_chooser_stub_state

Python: `set_residue_type_chooser_stub_state(istat)`  
Scheme: `(set-residue-type-chooser-stub-state istat)`

set a flag saying that the residue chosen by mutate or
 auto-fit mutate should only be added as a stub (mainchain + CB)

Arguments: istat (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_residue_type_chooser_stub_state(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-residue-type-chooser-stub-state 1)` | ran (no return value, nothing visible changed) |

### set_rotamer_auto_fit_do_post_refine

Python: `set_rotamer_auto_fit_do_post_refine(istate)`  
Scheme: `(set-rotamer-auto-fit-do-post-refine istate)`

Do you want Coot to automatically run a refinement after
 every rotamer autofit?

 1 for yes, 0 for no.

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_rotamer_auto_fit_do_post_refine(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-rotamer-auto-fit-do-post-refine 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: rotamer_auto_fit_do_post_refine_state was 0, set to 1, read back 1; Scheme: rotamer-auto-fit-do-post-refine-state was 0, set to 1, read back 1.

### setup_mutate

Python: `setup_mutate(state)`  
Scheme: `(setup-mutate state)`

c-interface-build

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_mutate(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(setup-mutate 1)` | ran (no return value, nothing visible changed) |

### setup_mutate_auto_fit

Python: `setup_mutate_auto_fit(state)`  
Scheme: `(setup-mutate-auto-fit state)`

Mutate then fit to map

 that we have a map define is checked first

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_mutate_auto_fit(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(setup-mutate-auto-fit 1)` | ran (no return value, nothing visible changed) |

