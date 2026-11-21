# Go To Atom Widget Functions

[Scripting reference](../README.md) > Go To Atom Widget Functions (31 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### atom_spec_to_atom_index

Python: `atom_spec_to_atom_index(mol, chain, resno, atom_name)`  
Scheme: `(atom-spec-to-atom-index mol chain resno atom-name)`

what is the atom index of the given atom?

Arguments: mol (a whole number), chain (text), resno (a whole number), atom_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `atom_spec_to_atom_index(0, "A", 41, " CA ")` | ran, returned `295` |
| Scheme | `(atom-spec-to-atom-index 0 "A" 41 " CA ")` | ran, returned `295` |

Python and Scheme gave the same answer.

### autobuild_ca_off

Python: `autobuild_ca_off()`  
Scheme: `(autobuild-ca-off)`

void autobuild_ca_on(); - moved to junk

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `autobuild_ca_off()` | ran (no return value, nothing visible changed) |
| Scheme | `(autobuild-ca-off)` | ran (no return value, nothing visible changed) |

### do_skeleton_prune

Python: `do_skeleton_prune()`  
Scheme: `(do-skeleton-prune)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_skeleton_prune()` | ran (no return value, nothing visible changed) |
| Scheme | `(do-skeleton-prune)` | ran (no return value, nothing visible changed) |

### full_atom_spec_to_atom_index

Python: `full_atom_spec_to_atom_index(imol, chain, resno, inscode, atom_name, altloc)`  
Scheme: `(full-atom-spec-to-atom-index imol chain resno inscode atom-name altloc)`

what is the atom index of the given atom?

Arguments: imol (a whole number), chain (text), resno (a whole number), inscode (text), atom_name (text), altloc (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `full_atom_spec_to_atom_index(0, "A", 41, "", " CA ", "")` | ran, returned `295` |
| Scheme | `(full-atom-spec-to-atom-index 0 "A" 41 "" " CA " "")` | ran, returned `295` |

Python and Scheme gave the same answer.

### glyco_tree

Python: `glyco_tree(imol, active_residue_py)`  
Scheme: `(glyco-tree-scm imol active-residue-scm)`

Arguments: imol (a whole number), active_residue_py (a list or value). Returns: a value (see the result of the example).
Also available in Python as `glyco_tree_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `set_add_linked_residue_do_fit_and_refine(0)`, then `add_linked_residue(0, "A", 39, "", "NAG", "NAG-ASN", 1)`, then `glyco_tree(0, ["A", 39, ""])` | ran, returned `False` |
| Scheme | first `(set-add-linked-residue-do-fit-and-refine 0)`, then `(add-linked-residue 0 "A" 39 "" "NAG" "NAG-ASN" 1)`, then `(glyco-tree-scm 0 (list "A" 39 ""))` | ran, returned `#f` |

Example written and checked by hand on the test data. Expected: unfinished upstream: always returns False (the source says 'incomplete, doesn't work'); use glyco_tree_residues.

Note: Always False even on a real ASN-NAG tree; the C++ body builds the tree but never fills the result.

Python and Scheme gave the same answer.

### glyco_tree_compare_trees

Python: `glyco_tree_compare_trees(imol_1, res_spec_1, imol_2, res_spec_2)`  
Scheme: `(glyco-tree-compare-trees-scm imol-1 res-spec-1 imol-2 res-spec-2)`

Arguments: imol_1 (a whole number), res_spec_1 (a list or value), imol_2 (a whole number), res_spec_2 (a list or value). Returns: a value (see the result of the example).
Also available in Python as `glyco_tree_compare_trees_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `glyco_tree_compare_trees(0, ["A", 41, ""], 0, ["A", 41, ""])` | ran, returned `True` |
| Scheme | `(glyco-tree-compare-trees-scm 0 (list "A" 41 "") 0 (list "A" 41 ""))` | ran, returned `#t` |

Python and Scheme gave the same answer.

### glyco_tree_internal_distances_fn_py

Python: `glyco_tree_internal_distances_fn_py(imol, residue_spec, file_name)`  
Scheme: `(glyco-tree-internal-distances-fn-scm imol residue-spec file-name)`

Arguments: imol (a whole number), residue_spec (a list or value), file_name (text). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `set_add_linked_residue_do_fit_and_refine(0)`, then `add_linked_residue(0, "A", 39, "", "NAG", "NAG-ASN", 1)`, then `glyco_tree_internal_distances_fn_py(0, ["A", 39, ""], "glyco-dist.txt")` | ran, returned `False` |
| Scheme | first `(set-add-linked-residue-do-fit-and-refine 0)`, then `(add-linked-residue 0 "A" 39 "" "NAG" "NAG-ASN" 1)`, then `(glyco-tree-internal-distances-fn-scm 0 (list "A" 39 "") "glyco-dist.txt")` | ran, returned `#f` |

Example written and checked by hand on the test data. Expected: testing function: writes the atom-pair distances inside the glycan tree to the file; the return value is always False.

Python and Scheme gave the same answer.

### glyco_tree_matched_residue_pairs

Python: `glyco_tree_matched_residue_pairs(imol_1, res_spec_1, imol_2, res_spec_2)`  
Scheme: `(glyco-tree-matched-residue-pairs-scm imol-1 res-spec-1 imol-2 res-spec-2)`

Arguments: imol_1 (a whole number), res_spec_1 (a list or value), imol_2 (a whole number), res_spec_2 (a list or value). Returns: a value (see the result of the example).
Also available in Python as `glyco_tree_matched_residue_pairs_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `set_add_linked_residue_do_fit_and_refine(0)`, then `add_linked_residue(0, "A", 39, "", "NAG", "NAG-ASN", 1)`, then `imol2 = read_pdb("tutorial-modern.pdb")`, then `add_linked_residue(imol2, "A", 39, "", "NAG", "NAG-ASN", 1)`, then `glyco_tree_matched_residue_pairs(0, ["A", 39, ""], imol2, ["A", 39, ""])` | ran, returned `[[[True, 'A', 94, ''], [True, 'A', 94, '']], [[True, 'A', 39, ''], [True, 'A', 39, '']]]` |
| Scheme | first `(set-add-linked-residue-do-fit-and-refine 0)`, then `(add-linked-residue 0 "A" 39 "" "NAG" "NAG-ASN" 1)`, then `(define imol2 (read-pdb "tutorial-modern.pdb"))`, then `(add-linked-residue imol2 "A" 39 "" "NAG" "NAG-ASN" 1)`, then `(glyco-tree-matched-residue-pairs-scm 0 (list "A" 39 "") imol2 (list "A" 39 ""))` | ran, returned `(((#t "A" 39 "") (#t "A" 39 "")) ((#t "A" 94 "") (#t "A" 94 "")))` |

Example written and checked by hand on the test data. Expected: returns the pairs of matching residues of two glycan trees.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### glyco_tree_residue_id

Python: `glyco_tree_residue_id(imol, residue_spec_py)`  
Scheme: `(glyco-tree-residue-id imol residue-spec-scm)`

Arguments: imol (a whole number), residue_spec_py (a list or value). Returns: a value (see the result of the example).
Also available in Python as `glyco_tree_residue_id_py`.
Also available in Scheme as `glyco-tree-residue-id-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `set_add_linked_residue_do_fit_and_refine(0)`, then `add_linked_residue(0, "A", 39, "", "NAG", "NAG-ASN", 1)`, then `glyco_tree_residue_id(0, ["A", 94, ""])` | ran, returned `[1, 'unset', 'NAG', 'pyr-ASN', 'ASN', [True, 'A', 39, '']]` |
| Scheme | first `(set-add-linked-residue-do-fit-and-refine 0)`, then `(add-linked-residue 0 "A" 39 "" "NAG" "NAG-ASN" 1)`, then `(glyco-tree-residue-id 0 (list "A" 94 ""))` | ran, returned `(1 unset "NAG" "pyr-ASN" "ASN" (#t "A" 39 ""))` |

Example written and checked by hand on the test data. Expected: returns [level, prime-arm flag, residue type, link type, parent type, parent spec] for a sugar in a glycan tree; False for a residue that is not a sugar in a tree.

Note: Python gives the prime-arm flag as the string 'unset', Scheme as the symbol unset.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### glyco_tree_residues

Python: `glyco_tree_residues(imol, active_residue_py)`  
Scheme: `(glyco-tree-residues imol active-residue-scm)`

Arguments: imol (a whole number), active_residue_py (a list or value). Returns: a value (see the result of the example).
Also available in Python as `glyco_tree_residues_py`.
Also available in Scheme as `glyco-tree-residues-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `set_add_linked_residue_do_fit_and_refine(0)`, then `add_linked_residue(0, "A", 39, "", "NAG", "NAG-ASN", 1)`, then `glyco_tree_residues(0, ["A", 39, ""])` | ran, returned `[[True, 'A', 39, ''], [True, 'A', 94, '']]` |
| Scheme | first `(set-add-linked-residue-do-fit-and-refine 0)`, then `(add-linked-residue 0 "A" 39 "" "NAG" "NAG-ASN" 1)`, then `(glyco-tree-residues 0 (list "A" 39 ""))` | ran, returned `((#t "A" 39 "") (#t "A" 94 ""))` |

Example written and checked by hand on the test data. Expected: returns the residue specs of the glycan tree on that ASN (the ASN itself and the sugars).

Python and Scheme gave the same answer.

### glyco_tree_test

Python: `glyco_tree_test()`  
Scheme: `(glyco-tree-test)`

glyco tools test

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `glyco_tree_test()` | ran (no return value, nothing visible changed) |
| Scheme | `(glyco-tree-test)` | ran (no return value, nothing visible changed) |

### go_to_atom_alt_conf

Python: `go_to_atom_alt_conf()`  
Scheme: `(go-to-atom-alt-conf)`

the go-to-atom alt conf

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_atom_alt_conf()` | ran, returned `''` |
| Scheme | `(go-to-atom-alt-conf)` | ran, returned `""` |

Python and Scheme gave the same answer.

### go_to_atom_atom_name

Python: `go_to_atom_atom_name()`  
Scheme: `(go-to-atom-atom-name)`

the go-to-atom atom name

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_atom_atom_name()` | ran, returned `'CA'` |
| Scheme | `(go-to-atom-atom-name)` | ran, returned `"CA"` |

Python and Scheme gave the same answer.

### go_to_atom_chain_id

Python: `go_to_atom_chain_id()`  
Scheme: `(go-to-atom-chain-id)`

the go-to-atom chain-id

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_atom_chain_id()` | ran, returned `'A'` |
| Scheme | `(go-to-atom-chain-id)` | ran, returned `"A"` |

Python and Scheme gave the same answer.

### go_to_atom_ins_code

Python: `go_to_atom_ins_code()`  
Scheme: `(go-to-atom-ins-code)`

the go-to-atom insertion code

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_atom_ins_code()` | ran, returned `''` |
| Scheme | `(go-to-atom-ins-code)` | ran, returned `""` |

Python and Scheme gave the same answer.

### go_to_atom_molecule_number

Python: `go_to_atom_molecule_number()`  
Scheme: `(go-to-atom-molecule-number)`

the go-to-atom molecule number

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `set_go_to_atom_molecule(0)`, then `go_to_atom_molecule_number()` | ran, returned `0` |
| Scheme | first `(set-go-to-atom-molecule 0)`, then `(go-to-atom-molecule-number)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns the molecule the Go To Atom functions work on (0 here, the model).

Python and Scheme gave the same answer.

### go_to_atom_residue_number

Python: `go_to_atom_residue_number()`  
Scheme: `(go-to-atom-residue-number)`

the go-to-atom residue number

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_atom_residue_number()` | ran, returned `1` |
| Scheme | `(go-to-atom-residue-number)` | ran, returned `1` |

Python and Scheme gave the same answer.

### post_go_to_atom_window

Python: `post_go_to_atom_window()`  
Scheme: `(post-go-to-atom-window)`

Post the Go To Atom Window

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `post_go_to_atom_window()` | ran (no return value, nothing visible changed) |
| Scheme | `(post-go-to-atom-window)` | ran (no return value, nothing visible changed) |

### set_go_to_atom_chain_residue_atom_name

Python: `set_go_to_atom_chain_residue_atom_name(t1_chain_id, iresno, t3_atom_name)`  
Scheme: `(set-go-to-atom-chain-residue-atom-name t1-chain-id iresno t3-atom-name)`

set the go to atom specification

 It seems important for swig that the char * arguments are const
 char *, not const gchar * (or else we get wrong type of argument
 error on (say) "A"

Returns the success status of the go to. 0 for fail, 1 for success.

Arguments: t1_chain_id (text), iresno (a whole number), t3_atom_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_go_to_atom_chain_residue_atom_name("A", 41, " CA ")` | ran, returned `1`; changed: rotation centre moved 7.3 A to (47.1, 10.6, 17.4) |
| Scheme | `(set-go-to-atom-chain-residue-atom-name "A" 41 " CA ")` | ran, returned `1` |

Python and Scheme gave the same answer.

### set_go_to_atom_chain_residue_atom_name_full

Python: `set_go_to_atom_chain_residue_atom_name_full(chain_id, resno, ins_code, atom_name, alt_conf)`  
Scheme: `(set-go-to-atom-chain-residue-atom-name-full chain-id resno ins-code atom-name alt-conf)`

set the go to (full) atom specification

 It seems important for swig that the char * arguments are const
 char *, not const gchar * (or else we get wrong type of argument
 error on (say) "A"

Returns the success status of the go to. 0 for fail, 1 for success.

Arguments: chain_id (text), resno (a whole number), ins_code (text), atom_name (text), alt_conf (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_go_to_atom_chain_residue_atom_name_full("A", 41, "", " CA ", "")` | ran, returned `1` |
| Scheme | `(set-go-to-atom-chain-residue-atom-name-full "A" 41 "" " CA " "")` | ran, returned `1` |

Python and Scheme gave the same answer.

### set_go_to_atom_chain_residue_atom_name_no_redraw

Python: `set_go_to_atom_chain_residue_atom_name_no_redraw(t1, iresno, t3, make_the_move_flag)`  
Scheme: `(set-go-to-atom-chain-residue-atom-name-no-redraw t1 iresno t3 make-the-move-flag)`

set go to atom but don't redraw

Arguments: t1 (text), iresno (a whole number), t3 (text), make_the_move_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_go_to_atom_chain_residue_atom_name_no_redraw("A", 41, " CA ", 1)` | ran, returned `1` |
| Scheme | `(set-go-to-atom-chain-residue-atom-name-no-redraw "A" 41 " CA " 1)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 when the atom is found; with make_the_move_flag 1 the view centres on it.

Python and Scheme gave the same answer.

### set_go_to_atom_chain_residue_atom_name_strings

Python: `set_go_to_atom_chain_residue_atom_name_strings(t1, t2, txt)`  
Scheme: `(set-go-to-atom-chain-residue-atom-name-strings t1 t2 txt)`

Arguments: t1 (text), t2 (text), txt (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_go_to_atom_chain_residue_atom_name_strings("B", "72", " SG ")` | error: TypeError: in method 'set_go_to_atom_chain_residue_atom_name_strings', argument 1 of type 'gchar const *' |
| Scheme | `(set-go-to-atom-chain-residue-atom-name-strings "B" "72" " SG ")` | error: In procedure set-go-to-atom-chain-residue-atom-name-strings: Wrong type argument in position 1: "B" |

Example written and checked by hand on the test data. Expected: should return 1 and centre on SG of Cys B72; use set_go_to_atom_chain_residue_atom_name("B", 72, " SG ") instead.

Note: Not callable from either scripting language: the arguments are declared gchar* and SWIG has no typemap for gchar, so every string is rejected. Likely a wrapper bug (declare const char*).

### set_go_to_atom_molecule

Python: `set_go_to_atom_molecule(imol)`  
Scheme: `(set-go-to-atom-molecule imol)`

set the molecule for the Go To Atom

 For dynarama callback sake. The widget/class knows which
 molecule that it was generated from, so in order to go to the
 molecule from dynarama, we first need to the the molecule - because
 set_go_to_atom_chain_residue_atom_name() does not mention the
 molecule (see "Next/Previous Residue" for reasons for that). This
 function simply calls the graphics_info_t function of the same
 name.

 Also used in scripting, where go-to-atom-chain-residue-atom-name
 does not mention the molecule number.

 20090914-PE set-go-to-atom-molecule can be used in a script and it
 should change the go-to-atom-molecule in the Go To Atom dialog (if
 it is being displayed). This does mean, of course that using the
 ramachandran plot to centre on atoms will change the Go To Atom
 dialog. Maybe that is surprising (maybe not).

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_go_to_atom_molecule(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-go-to-atom-molecule 0)` | ran (no return value, nothing visible changed) |

### test_fragment

Python: `test_fragment()`  
Scheme: `(test-fragment)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `test_fragment()` | ran (no return value, nothing visible changed) |
| Scheme | `(test-fragment)` | ran (no return value, nothing visible changed) |

### test_function

Python: `test_function(i, j)`  
Scheme: `(test-function i j)`

Arguments: i (a list or value), j (a list or value). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `test_function(0, 1)` | ran, returned `False`; changed: graphics_n_molecules(): 3 -> 4 |
| Scheme | `(test-function 0 1)` | ran, returned `#f` |

Example written and checked by hand on the test data. Expected: developer test hook; returns False when its hard-coded test files are absent.

Note: Developer test function: Python version creates an empty molecule as a side effect. Not for users.

Python and Scheme gave the same answer.

### unset_go_to_atom_widget

Python: `unset_go_to_atom_widget()`  
Scheme: `(unset-go-to-atom-widget)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `unset_go_to_atom_widget()` | ran (no return value, nothing visible changed) |
| Scheme | `(unset-go-to-atom-widget)` | ran (no return value, nothing visible changed) |

### update_go_to_atom_from_current_position

Python: `update_go_to_atom_from_current_position()`  
Scheme: `(update-go-to-atom-from-current-position)`

update the Go To Atom widget entries to atom closest to
 screen centre.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_go_to_atom_from_current_position()` | ran (no return value); changed: rotation centre moved 3.8 A to (44.4, 10.4, 15.0) |
| Scheme | `(update-go-to-atom-from-current-position)` | ran (no return value, nothing visible changed) |

### update_go_to_atom_residue_list

Python: `update_go_to_atom_residue_list(imol)`  
Scheme: `(update-go-to-atom-residue-list imol)`

moving gtk function out of build functions, delete_atom() updates
 the go to atom atom list on deleting an atom

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_go_to_atom_residue_list(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(update-go-to-atom-residue-list 0)` | ran (no return value, nothing visible changed) |

### update_go_to_atom_window_on_changed_mol

Python: `update_go_to_atom_window_on_changed_mol(imol)`  
Scheme: `(update-go-to-atom-window-on-changed-mol imol)`

update the Go To Atom window

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_go_to_atom_window_on_changed_mol(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(update-go-to-atom-window-on-changed-mol 0)` | ran (no return value, nothing visible changed) |

### update_go_to_atom_window_on_new_mol

Python: `update_go_to_atom_window_on_new_mol()`  
Scheme: `(update-go-to-atom-window-on-new-mol)`

update the Go To Atom window. This updates the option menu
 for the molecules.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_go_to_atom_window_on_new_mol()` | ran (no return value, nothing visible changed) |
| Scheme | `(update-go-to-atom-window-on-new-mol)` | ran (no return value, nothing visible changed) |

### update_go_to_atom_window_on_other_molecule_chosen

Python: `update_go_to_atom_window_on_other_molecule_chosen(imol)`  
Scheme: `(update-go-to-atom-window-on-other-molecule-chosen imol)`

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_go_to_atom_window_on_other_molecule_chosen(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(update-go-to-atom-window-on-other-molecule-chosen 0)` | ran (no return value, nothing visible changed) |

