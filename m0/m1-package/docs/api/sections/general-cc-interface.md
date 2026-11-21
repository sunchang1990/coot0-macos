# General (cc-interface)

[Scripting reference](../README.md) > General (cc-interface) (21 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### active_atom_spec

Python: `active_atom_spec()`  
Scheme: `(active-atom-spec)`

return a tuple of (Py_Bool (number, atom_spec))

Arguments: none. Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `active_atom_spec()` | ran, returned `(True, (0, [True, 'A', 42, '']))` |
| Scheme | `(active-atom-spec)` | ran, returned `#<collectable-swig-pointer std::pair< bool,std::pair< int,coot::atom_spec_t > > * a24afd4a0>` |

### add_cablam_markup

Python: `add_cablam_markup(imol, cablam_log_file_name)`  
Scheme: `(add-cablam-markup imol cablam-log-file-name)`

CaBLAM

Arguments: imol (a whole number), cablam_log_file_name (text). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_cablam_markup(0, "tutorial-modern.pdb")` | ran, returned `[]` |
| Scheme | `(add-cablam-markup 0 "tutorial-modern.pdb")` | ran, returned `()` |

Python and Scheme gave the same answer.

### add_validation_mol_menu_item

Python: `add_validation_mol_menu_item(imol, name, menu, callback)`  
Scheme: `(add-validation-mol-menu-item imol name menu callback)`

Arguments: imol (a whole number), name (text), menu (`GtkWidget *`), callback (`GtkSignalFunc`). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: adds a molecule item to a validation-graph menu (called by the menus themselves).

### compare_strings

Python: `compare_strings(a, b)`  
Scheme: `(compare-strings a b)`

Arguments: a (text), b (text). Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `compare_strings("apple", "banana")` | ran, returned `True` |
| Scheme | `(compare-strings "banana" "apple")` | ran, returned `#f` |

Example written and checked by hand on the test data. Expected: true when the first string sorts before the second (a < b), false otherwise.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### create_initial_validation_graph_submenu_generic

Python: `create_initial_validation_graph_submenu_generic(window1, menu_name, sub_menu_name)`  
Scheme: `(create-initial-validation-graph-submenu-generic window1 menu-name sub-menu-name)`

Arguments: window1 (`GtkWidget *`), menu_name (text), sub_menu_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: builds a validation-graph sub-menu in the main window (internal GUI function).

### filelist_into_fileselection_clist

Python: `filelist_into_fileselection_clist(fileselection, v)`  
Scheme: `(filelist-into-fileselection-clist fileselection v)`

Arguments: fileselection (`GtkWidget *`), v (a list). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: fills a file selection dialog's list (internal GUI function).

### filtered_by_glob

Python: `filtered_by_glob(pre_directory, data_type)`  
Scheme: `(filtered-by-glob pre-directory data-type)`

Arguments: pre_directory (text), data_type (a whole number). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `filtered_by_glob(".", 1)` | ran, returned `('./1ehz_map.mtz', './ATP.cif', './NAG.cif', './map-coefficients-only.mtz', './rnasa-1.8-all_refmac1.mtz', './rnasa-sf.c ...` |
| Scheme | `(filtered-by-glob "." 1)` | ran, returned `#("./1ehz_map.mtz" "./ATP.cif" "./NAG.cif" "./map-coefficients-only.mtz" "./rnasa-1.8-all_refmac1.mtz" "./rnasa-sf.cif"  ...` |

Python and Scheme gave the same answer.

### float_from_entry

Python: `float_from_entry(entry)`  
Scheme: `(float-from-entry entry)`

Arguments: entry (`GtkWidget *`). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: returns the number typed in a GtkEntry (internal GUI helper).

### get_pisa_interface_bond_info_py

Python: `get_pisa_interface_bond_info_py(bonds_info_py)`  
Scheme: `(get-pisa-interface-bond-info-scm bonds-info-scm)`

Arguments: bonds_info_py (a list or value). Returns: `pisa_interface_bond_info_t`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_pisa_interface_bond_info_py([["h-bonds", 1, 2], ["h-bonds", 3, 4], ["salt-bridges", 5, 6]])` | ran, returned `<coot.pisa_interface_bond_info_t; proxy of <Swig Object of type 'coot::pisa_interface_bond_info_t *' at 0x10b833600> >` |
| Scheme | `(get-pisa-interface-bond-info-scm (list (list 'h-bonds 1 2)))` | ran, returned `#<collectable-swig-pointer coot::pisa_interface_bond_info_t * 94ad7b730>` |

Example written and checked by hand on the test data. Expected: internal PISA helper: counts bond types in a list of [type, atom, atom] and returns a C++ struct (fields n_h_bonds, n_salt_bridges, n_cov_bonds, n_ss_bonds).

Note: Python takes the type as a string, Scheme as a symbol ('h-bonds). Returns a C++ struct, of little use from scripts.

### git_commit

Python: `git_commit()`  
Scheme: `(git-commit)`

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `git_commit()` | ran, returned `'50638a38145722303017be802622d65d83bd7f66'` |
| Scheme | `(git-commit)` | ran, returned `"50638a38145722303017be802622d65d83bd7f66"` |

Python and Scheme gave the same answer.

### goto_next_atom_maybe

Python: `goto_next_atom_maybe(chain_id, resno, ins_code, atom_name)`  
Scheme: `(goto-next-atom-maybe chain-id resno ins-code atom-name)`

Arguments: chain_id (text), resno (a whole number), ins_code (text), atom_name (text). Returns: a value (see the result of the example).
Also available in Python as `goto_next_atom_maybe_py`.
Also available in Scheme as `goto-next-atom-maybe-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `goto_next_atom_maybe("A", 41, "", " CA ")` | ran, returned `['A', 41, '', ' CA ']` |
| Scheme | `(goto-next-atom-maybe "A" 41 "" " CA ")` | ran, returned `("A" 41 "" " CA ")` |

Python and Scheme gave the same answer.

### goto_prev_atom_maybe

Python: `goto_prev_atom_maybe(chain_id, resno, ins_code, atom_name)`  
Scheme: `(goto-prev-atom-maybe chain-id resno ins-code atom-name)`

Arguments: chain_id (text), resno (a whole number), ins_code (text), atom_name (text). Returns: a value (see the result of the example).
Also available in Python as `goto_prev_atom_maybe_py`.
Also available in Scheme as `goto-prev-atom-maybe-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `goto_prev_atom_maybe("A", 41, "", " CA ")` | ran, returned `['A', 40, '', ' CA ']` |
| Scheme | `(goto-prev-atom-maybe "A" 41 "" " CA ")` | ran, returned `("A" 40 "" " CA ")` |

Python and Scheme gave the same answer.

### int_from_entry

Python: `int_from_entry(entry)`  
Scheme: `(int-from-entry entry)`

Arguments: entry (`GtkWidget *`). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: returns the integer typed in a GtkEntry (internal GUI helper).

### menu_item_label

Python: `menu_item_label(menu_item)`  
Scheme: `(menu-item-label menu-item)`

To be used to (typically) get the menu item text label from chain
option menus (rather than the ugly/broken casting of
GtkPositionType data. A wrapper to a static graphics_info_t
function.

Arguments: menu_item (`GtkWidget *`). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: returns the text label of a menu item (internal GUI helper).

### pre_directory_file_selection

Python: `pre_directory_file_selection(sort_button)`  
Scheme: `(pre-directory-file-selection sort-button)`

Arguments: sort_button (`GtkWidget *`). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: sets up the directory part of a file chooser (internal GUI helper).

### probe_dots_short_contact_name_to_expanded_name

Python: `probe_dots_short_contact_name_to_expanded_name(short_name)`  
Scheme: `(probe-dots-short-contact-name-to-expanded-name short-name)`

Arguments: short_name (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `probe_dots_short_contact_name_to_expanded_name("bo")` | ran, returned `'bad overlap'` |
| Scheme | `(probe-dots-short-contact-name-to-expanded-name "bo")` | ran, returned `"bad overlap"` |

Example written and checked by hand on the test data. Expected: returns the long name of a probe contact type (wc, cc, so, bo, hb); 'unknown' otherwise.

Note: Only a string lookup; it does not run probe (old classification was wrong).

Python and Scheme gave the same answer.

### set_go_to_atom_from_atom_spec

Python: `set_go_to_atom_from_atom_spec(residue_spec)`  
Scheme: `(set-go-to-atom-from-atom-spec residue-spec)`

Arguments: residue_spec (a list or value). Returns: a whole number.
Also available in Python as `set_go_to_atom_from_atom_spec_py`.
Also available in Scheme as `set-go-to-atom-from-atom-spec-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_go_to_atom_from_atom_spec(["A", 42, "", " CA ", ""])` | ran, returned `1`; changed: rotation centre moved 3.6 A to (44.4, 10.4, 15.0) |
| Scheme | `(set-go-to-atom-from-atom-spec (list "A" 42 "" " CA " ""))` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 and centres on the atom given as an atom spec [chain, resno, inscode, atom name, altconf].

Python and Scheme gave the same answer.

### set_go_to_atom_from_res_spec

Python: `set_go_to_atom_from_res_spec(residue_spec)`  
Scheme: `(set-go-to-atom-from-res-spec residue-spec)`

Arguments: residue_spec (a list or value). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_go_to_atom_from_res_spec(["A", 41, ""])` | ran, returned `1`; changed: rotation centre moved 3.6 A to (47.1, 10.6, 17.4) |
| Scheme | `(set-go-to-atom-from-res-spec (list "A" 41 ""))` | ran, returned `1` |

Python and Scheme gave the same answer.

### set_go_to_atom_from_spec

Python: `set_go_to_atom_from_spec(atom_spec)`  
Scheme: `(set-go-to-atom-from-spec atom-spec)`

Arguments: atom_spec (`coot::atom_spec_t`). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_go_to_atom_from_spec(["A", 42, "", " CA ", ""])` | not run: takes a C++ coot::atom_spec_t object that cannot be made from Python or Scheme |
| Scheme | `(set-go-to-atom-from-spec (list "A" 42 "" " CA " ""))` | not run: takes a C++ coot::atom_spec_t object that cannot be made from Python or Scheme |

Example written and checked by hand on the test data. Expected: C++-level function taking a coot::atom_spec_t, which scripts cannot build; use set_go_to_atom_from_atom_spec with a list instead.

Note: Exported to both languages but unusable from them; set_go_to_atom_from_atom_spec is the scripting version.

### string_member

Python: `string_member(search, list)`  
Scheme: `(string-member search list)`

Return 1 if search appears in list, 0 if not)

Arguments: search (text), list (a list). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `string_member("b", ["a", "b", "c"])` | ran, returned `1` |
| Scheme | `(string-member "b" (list "a" "b" "c"))` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 when the string is in the list, 0 when not.

Python and Scheme gave the same answer.

### wrapped_nothing_bad_dialog

Python: `wrapped_nothing_bad_dialog(label)`  
Scheme: `(wrapped-nothing-bad-dialog label)`

Arguments: label (text). Returns: `GtkWidget *`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `wrapped_nothing_bad_dialog("hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(wrapped-nothing-bad-dialog "hello")` | ran, returned `()` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

