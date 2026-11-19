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

### autobuild_ca_off

Python: `autobuild_ca_off()`  
Scheme: `(autobuild-ca-off)`

void autobuild_ca_on(); - moved to junk

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `autobuild_ca_off()` | ran (no return value) |
| Scheme | `(autobuild-ca-off)` | ran (no return value) |

### do_skeleton_prune

Python: `do_skeleton_prune()`  
Scheme: `(do-skeleton-prune)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_skeleton_prune()` | ran (no return value) |
| Scheme | `(do-skeleton-prune)` | ran (no return value) |

### full_atom_spec_to_atom_index

Python: `full_atom_spec_to_atom_index(imol, chain, resno, inscode, atom_name, altloc)`  
Scheme: `(full-atom-spec-to-atom-index imol chain resno inscode atom-name altloc)`

what is the atom index of the given atom?

Arguments: imol (a whole number), chain (text), resno (a whole number), inscode (text), atom_name (text), altloc (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `full_atom_spec_to_atom_index(0, "A", 41, "", " CA ", "")` | ran, returned `295` |
| Scheme | `(full-atom-spec-to-atom-index 0 "A" 41 "" " CA " "")` | ran, returned `295` |

### glyco_tree

Python: `glyco_tree(imol, active_residue_py)`  
Scheme: `(glyco-tree-scm imol active-residue-scm)`

Arguments: imol (a whole number), active_residue_py (a list or value). Returns: a value (see the result of the example).
Also available in Python as `glyco_tree_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### glyco_tree_compare_trees

Python: `glyco_tree_compare_trees(imol_1, res_spec_1, imol_2, res_spec_2)`  
Scheme: `(glyco-tree-compare-trees-scm imol-1 res-spec-1 imol-2 res-spec-2)`

Arguments: imol_1 (a whole number), res_spec_1 (a list or value), imol_2 (a whole number), res_spec_2 (a list or value). Returns: a value (see the result of the example).
Also available in Python as `glyco_tree_compare_trees_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `glyco_tree_compare_trees(0, ["A", 41, ""], 0, ["A", 41, ""])` | ran, returned `True` |
| Scheme | `(glyco-tree-compare-trees-scm 0 (list "A" 41 "") 0 (list "A" 41 ""))` | ran, returned `#t` |

### glyco_tree_internal_distances_fn_py

Python: `glyco_tree_internal_distances_fn_py(imol, residue_spec, file_name)`  
Scheme: `(glyco-tree-internal-distances-fn-scm imol residue-spec file-name)`

Arguments: imol (a whole number), residue_spec (a list or value), file_name (text). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `glyco_tree_internal_distances_fn_py(0, ["A", 41, ""], "tutorial-modern.pdb")` | ran, returned `False` |
| Scheme | `(glyco-tree-internal-distances-fn-scm 0 (list "A" 41 "") "tutorial-modern.pdb")` | ran, returned `#f` |

### glyco_tree_matched_residue_pairs

Python: `glyco_tree_matched_residue_pairs(imol_1, res_spec_1, imol_2, res_spec_2)`  
Scheme: `(glyco-tree-matched-residue-pairs-scm imol-1 res-spec-1 imol-2 res-spec-2)`

Arguments: imol_1 (a whole number), res_spec_1 (a list or value), imol_2 (a whole number), res_spec_2 (a list or value). Returns: a value (see the result of the example).
Also available in Python as `glyco_tree_matched_residue_pairs_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `glyco_tree_matched_residue_pairs(0, ["A", 41, ""], 0, ["A", 41, ""])` | ran, returned `False` |
| Scheme | `(glyco-tree-matched-residue-pairs-scm 0 (list "A" 41 "") 0 (list "A" 41 ""))` | ran, returned `#f` |

### glyco_tree_residue_id

Python: `glyco_tree_residue_id(imol, residue_spec_py)`  
Scheme: `(glyco-tree-residue-id imol residue-spec-scm)`

Arguments: imol (a whole number), residue_spec_py (a list or value). Returns: a value (see the result of the example).
Also available in Python as `glyco_tree_residue_id_py`.
Also available in Scheme as `glyco-tree-residue-id-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `glyco_tree_residue_id(0, ["A", 41, ""])` | ran, returned `False` |
| Scheme | `(glyco-tree-residue-id 0 (list "A" 41 ""))` | ran, returned `#f` |

### glyco_tree_residues

Python: `glyco_tree_residues(imol, active_residue_py)`  
Scheme: `(glyco-tree-residues imol active-residue-scm)`

Arguments: imol (a whole number), active_residue_py (a list or value). Returns: a value (see the result of the example).
Also available in Python as `glyco_tree_residues_py`.
Also available in Scheme as `glyco-tree-residues-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### glyco_tree_test

Python: `glyco_tree_test()`  
Scheme: `(glyco-tree-test)`

glyco tools test

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `glyco_tree_test()` | ran (no return value) |
| Scheme | `(glyco-tree-test)` | ran (no return value) |

### go_to_atom_alt_conf

Python: `go_to_atom_alt_conf()`  
Scheme: `(go-to-atom-alt-conf)`

the go-to-atom alt conf

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_atom_alt_conf()` | ran, returned `''` |
| Scheme | `(go-to-atom-alt-conf)` | ran, returned `""` |

### go_to_atom_atom_name

Python: `go_to_atom_atom_name()`  
Scheme: `(go-to-atom-atom-name)`

the go-to-atom atom name

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_atom_atom_name()` | ran, returned `'CA'` |
| Scheme | `(go-to-atom-atom-name)` | ran, returned `"CA"` |

### go_to_atom_chain_id

Python: `go_to_atom_chain_id()`  
Scheme: `(go-to-atom-chain-id)`

the go-to-atom chain-id

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_atom_chain_id()` | ran, returned `'A'` |
| Scheme | `(go-to-atom-chain-id)` | ran, returned `"A"` |

### go_to_atom_ins_code

Python: `go_to_atom_ins_code()`  
Scheme: `(go-to-atom-ins-code)`

the go-to-atom insertion code

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_atom_ins_code()` | ran, returned `''` |
| Scheme | `(go-to-atom-ins-code)` | ran, returned `""` |

### go_to_atom_molecule_number

Python: `go_to_atom_molecule_number()`  
Scheme: `(go-to-atom-molecule-number)`

the go-to-atom molecule number

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_atom_molecule_number()` | ran, returned `0` |
| Scheme | `(go-to-atom-molecule-number)` | ran, returned `0` |

### go_to_atom_residue_number

Python: `go_to_atom_residue_number()`  
Scheme: `(go-to-atom-residue-number)`

the go-to-atom residue number

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_atom_residue_number()` | ran, returned `1` |
| Scheme | `(go-to-atom-residue-number)` | ran, returned `1` |

### post_go_to_atom_window

Python: `post_go_to_atom_window()`  
Scheme: `(post-go-to-atom-window)`

Post the Go To Atom Window

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `post_go_to_atom_window()` | not tried |
| Scheme | `(post-go-to-atom-window)` | not tried |

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
| Python | `set_go_to_atom_chain_residue_atom_name("A", 41, " CA ")` | not tried |
| Scheme | `(set-go-to-atom-chain-residue-atom-name "A" 41 " CA ")` | not tried |

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
| Python | `set_go_to_atom_chain_residue_atom_name_full("A", 41, "", " CA ", "")` | not tried |
| Scheme | `(set-go-to-atom-chain-residue-atom-name-full "A" 41 "" " CA " "")` | not tried |

### set_go_to_atom_chain_residue_atom_name_no_redraw

Python: `set_go_to_atom_chain_residue_atom_name_no_redraw(t1, iresno, t3, make_the_move_flag)`  
Scheme: `(set-go-to-atom-chain-residue-atom-name-no-redraw t1 iresno t3 make-the-move-flag)`

set go to atom but don't redraw

Arguments: t1 (text), iresno (a whole number), t3 (text), make_the_move_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_go_to_atom_chain_residue_atom_name_no_redraw("hello", 41, "hello", 1)` | not tried |
| Scheme | `(set-go-to-atom-chain-residue-atom-name-no-redraw "hello" 41 "hello" 1)` | not tried |

### set_go_to_atom_chain_residue_atom_name_strings

Python: `set_go_to_atom_chain_residue_atom_name_strings(t1, t2, txt)`  
Scheme: `(set-go-to-atom-chain-residue-atom-name-strings t1 t2 txt)`

Arguments: t1 (text), t2 (text), txt (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_go_to_atom_chain_residue_atom_name_strings("hello", "hello", "hello")` | not tried |
| Scheme | `(set-go-to-atom-chain-residue-atom-name-strings "hello" "hello" "hello")` | not tried |

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
| Python | `set_go_to_atom_molecule(0)` | not tried |
| Scheme | `(set-go-to-atom-molecule 0)` | not tried |

### test_fragment

Python: `test_fragment()`  
Scheme: `(test-fragment)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `test_fragment()` | not tried |
| Scheme | `(test-fragment)` | not tried |

### test_function

Python: `test_function(i, j)`  
Scheme: `(test-function i j)`

Arguments: i (a list or value), j (a list or value). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

### unset_go_to_atom_widget

Python: `unset_go_to_atom_widget()`  
Scheme: `(unset-go-to-atom-widget)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `unset_go_to_atom_widget()` | not tried |
| Scheme | `(unset-go-to-atom-widget)` | not tried |

### update_go_to_atom_from_current_position

Python: `update_go_to_atom_from_current_position()`  
Scheme: `(update-go-to-atom-from-current-position)`

update the Go To Atom widget entries to atom closest to
 screen centre.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_go_to_atom_from_current_position()` | not tried |
| Scheme | `(update-go-to-atom-from-current-position)` | not tried |

### update_go_to_atom_residue_list

Python: `update_go_to_atom_residue_list(imol)`  
Scheme: `(update-go-to-atom-residue-list imol)`

moving gtk function out of build functions, delete_atom() updates
 the go to atom atom list on deleting an atom

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_go_to_atom_residue_list(0)` | not tried |
| Scheme | `(update-go-to-atom-residue-list 0)` | not tried |

### update_go_to_atom_window_on_changed_mol

Python: `update_go_to_atom_window_on_changed_mol(imol)`  
Scheme: `(update-go-to-atom-window-on-changed-mol imol)`

update the Go To Atom window

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_go_to_atom_window_on_changed_mol(0)` | not tried |
| Scheme | `(update-go-to-atom-window-on-changed-mol 0)` | not tried |

### update_go_to_atom_window_on_new_mol

Python: `update_go_to_atom_window_on_new_mol()`  
Scheme: `(update-go-to-atom-window-on-new-mol)`

update the Go To Atom window. This updates the option menu
 for the molecules.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_go_to_atom_window_on_new_mol()` | not tried |
| Scheme | `(update-go-to-atom-window-on-new-mol)` | not tried |

### update_go_to_atom_window_on_other_molecule_chosen

Python: `update_go_to_atom_window_on_other_molecule_chosen(imol)`  
Scheme: `(update-go-to-atom-window-on-other-molecule-chosen imol)`

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_go_to_atom_window_on_other_molecule_chosen(0)` | not tried |
| Scheme | `(update-go-to-atom-window-on-other-molecule-chosen 0)` | not tried |

