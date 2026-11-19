# Execute Refmac

[Scripting reference](../README.md) > Execute Refmac (43 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_refmac_ncycle_no

Python: `add_refmac_ncycle_no(cycle)`  
Scheme: `(add-refmac-ncycle-no cycle)`

Arguments: cycle (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_refmac_ncycle_no(1)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |
| Scheme | `(add-refmac-ncycle-no 1)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |

### add_refmac_sad_atom

Python: `add_refmac_sad_atom(atom_name, fp, fpp, lambda)`  
Scheme: `(add-refmac-sad-atom atom-name fp fpp lambda)`

Arguments: atom_name (text), fp (a number), fpp (a number), lambda (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_refmac_sad_atom(" CA ", 1.0, 1.0, 1.0)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |
| Scheme | `(add-refmac-sad-atom " CA " 1.0 1.0 1.0)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |

### add_refmac_sad_atom_fp

Python: `add_refmac_sad_atom_fp(atom_name, fp, fpp)`  
Scheme: `(add-refmac-sad-atom-fp atom-name fp fpp)`

Arguments: atom_name (text), fp (a number), fpp (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_refmac_sad_atom_fp(" CA ", 1.0, 1.0)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |
| Scheme | `(add-refmac-sad-atom-fp " CA " 1.0 1.0)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |

### add_refmac_sad_atom_lambda

Python: `add_refmac_sad_atom_lambda(atom_name, lambda)`  
Scheme: `(add-refmac-sad-atom-lambda atom-name lambda)`

Arguments: atom_name (text), lambda (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_refmac_sad_atom_lambda(" CA ", 1.0)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |
| Scheme | `(add-refmac-sad-atom-lambda " CA " 1.0)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |

### add_to_database

Python: `add_to_database(command_strings)`  
Scheme: `(add-to-database command-strings)`

Arguments: command_strings (a list). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_to_database("hello")` | ran (no return value) |
| Scheme | `(add-to-database "hello")` | error: In procedure add-to-database: Wrong type argument in position 1: "hello" |

### add_to_history

Python: `add_to_history(ls)`  
Scheme: `(add-to-history ls)`

Arguments: ls (a list). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_to_history("hello")` | ran (no return value) |
| Scheme | `(add-to-history "hello")` | error: In procedure add-to-history: Wrong type argument in position 1: "hello" |

### add_to_history_simple

Python: `add_to_history_simple(cmd)`  
Scheme: `(add-to-history-simple cmd)`

Arguments: cmd (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_to_history_simple("hello")` | ran (no return value) |
| Scheme | `(add-to-history-simple "hello")` | ran (no return value) |

### add_to_history_typed

Python: `add_to_history_typed(command, args)`  
Scheme: `(add-to-history-typed command args)`

Arguments: command (text), args (a list). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### ccp4_project_directory

Python: `ccp4_project_directory(ccp4_project_name)`  
Scheme: `(ccp4-project-directory ccp4-project-name)`

Arguments: ccp4_project_name (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ccp4_project_directory("my-name")` | ran, returned `''` |
| Scheme | `(ccp4-project-directory "my-name")` | ran, returned `""` |

### clear_refmac_sad_atoms

Python: `clear_refmac_sad_atoms()`  
Scheme: `(clear-refmac-sad-atoms)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_refmac_sad_atoms()` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |
| Scheme | `(clear-refmac-sad-atoms)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |

### compare_mtimes

Python: `compare_mtimes(a, b)`  
Scheme: `(compare-mtimes a b)`

Arguments: a (`coot::str_mtime`), b (`coot::str_mtime`). Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### execute_refmac_real

Python: `execute_refmac_real(pdb_in_filename, pdb_out_filename, mtz_in_filename, mtz_out_filename, cif_lib_filename, fobs_col_name, sigfobs_col_name, r_free_col_name, have_sensible_free_r_flag, make_molecules_flag, refmac_count_string, swap_map_colours_post_refmac_flag, imol_refmac_map, diff_map_flag, phase_combine_flag, phib_string, fom_string, ccp4i_project_dir)`  
Scheme: `(execute-refmac-real pdb-in-filename pdb-out-filename mtz-in-filename mtz-out-filename cif-lib-filename fobs-col-name sigfobs-col-name r-free-col-name have-sensible-free-r-flag make-molecules-flag refmac-count-string swap-map-colours-post-refmac-flag imol-refmac-map diff-map-flag phase-combine-flag phib-string fom-string ccp4i-project-dir)`

Arguments: pdb_in_filename (text), pdb_out_filename (text), mtz_in_filename (text), mtz_out_filename (text), cif_lib_filename (text), fobs_col_name (text), sigfobs_col_name (text), r_free_col_name (text), have_sensible_free_r_flag (a whole number), make_molecules_flag (a whole number), refmac_count_string (text), swap_map_colours_post_refmac_flag (a whole number), imol_refmac_map (a whole number), diff_map_flag (a whole number), phase_combine_flag (a whole number), phib_string (text), fom_string (text), ccp4i_project_dir (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `execute_refmac_real("tutorial-modern.pdb", "tutorial-modern.pdb", "rnasa-1.8-all_refmac1.mtz", "rnasa-1.8-all_refmac1.mtz", "tutorial-modern.pdb", "my-name", "my-name", "my-name", 1, 1, "hello", 1, 1, ...` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |
| Scheme | `(execute-refmac-real "tutorial-modern.pdb" "tutorial-modern.pdb" "rnasa-1.8-all_refmac1.mtz" "rnasa-1.8-all_refmac1.mtz" "tutorial-modern.pdb" "my-name" "my-name" "my-name" 1 1 "hello" 1 1 1 1 "hello" ...` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |

### get_refmac_ncycles

Python: `get_refmac_ncycles()`  
Scheme: `(get-refmac-ncycles)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_refmac_ncycles()` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |
| Scheme | `(get-refmac-ncycles)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |

### get_refmac_phase_input

Python: `get_refmac_phase_input()`  
Scheme: `(get-refmac-phase-input)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_refmac_phase_input()` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |
| Scheme | `(get-refmac-phase-input)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |

### get_refmac_refinement_method

Python: `get_refmac_refinement_method()`  
Scheme: `(get-refmac-refinement-method)`

some methods to get refmac run parameters

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_refmac_refinement_method()` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |
| Scheme | `(get-refmac-refinement-method)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |

### get_refmac_used_mtz_file_state

Python: `get_refmac_used_mtz_file_state()`  
Scheme: `(get-refmac-used-mtz-file-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_refmac_used_mtz_file_state()` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |
| Scheme | `(get-refmac-used-mtz-file-state)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |

### get_saved_refmac_file_filename

Python: `get_saved_refmac_file_filename()`  
Scheme: `(get-saved-refmac-file-filename)`

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_saved_refmac_file_filename()` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |
| Scheme | `(get-saved-refmac-file-filename)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |

### languagize_command

Python: `languagize_command(command_parts)`  
Scheme: `(languagize-command command-parts)`

Arguments: command_parts (a list). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `languagize_command("hello")` | not tried |
| Scheme | `(languagize-command "hello")` | not tried |

### merge_molecules_by_vector

Python: `merge_molecules_by_vector(add_molecules, imol)`  
Scheme: `(merge-molecules-by-vector add-molecules imol)`

return the status and vector of chain-ids of the new chain ids.

Arguments: add_molecules (a list), imol (a whole number). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

### parse_ccp4i_defs

Python: `parse_ccp4i_defs(filename)`  
Scheme: `(parse-ccp4i-defs filename)`

Arguments: filename (text). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `parse_ccp4i_defs("tutorial-modern.pdb")` | not tried |
| Scheme | `(parse-ccp4i-defs "tutorial-modern.pdb")` | not tried |

### pythonize_command_name

Python: `pythonize_command_name(s)`  
Scheme: `(pythonize-command-name s)`

Arguments: s (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `pythonize_command_name("hello")` | not tried |
| Scheme | `(pythonize-command-name "hello")` | not tried |

### refmac_imol_coords

Python: `refmac_imol_coords()`  
Scheme: `(refmac-imol-coords)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refmac_imol_coords()` | not tried |
| Scheme | `(refmac-imol-coords)` | not tried |

### refmac_name

Python: `refmac_name(imol)`  
Scheme: `(refmac-name imol)`

the name for refmac

 Returns a stub name used in the construction of filename for refmac output

Arguments: imol (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refmac_name(0)` | not tried |
| Scheme | `(refmac-name 0)` | not tried |

### refmac_use_intensities_state

Python: `refmac_use_intensities_state()`  
Scheme: `(refmac-use-intensities-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refmac_use_intensities_state()` | not tried |
| Scheme | `(refmac-use-intensities-state)` | not tried |

### refmac_use_ncs_state

Python: `refmac_use_ncs_state()`  
Scheme: `(refmac-use-ncs-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refmac_use_ncs_state()` | not tried |
| Scheme | `(refmac-use-ncs-state)` | not tried |

### refmac_use_sad_state

Python: `refmac_use_sad_state()`  
Scheme: `(refmac-use-sad-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refmac_use_sad_state()` | not tried |
| Scheme | `(refmac-use-sad-state)` | not tried |

### refmac_use_tls_state

Python: `refmac_use_tls_state()`  
Scheme: `(refmac-use-tls-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refmac_use_tls_state()` | not tried |
| Scheme | `(refmac-use-tls-state)` | not tried |

### refmac_use_twin_state

Python: `refmac_use_twin_state()`  
Scheme: `(refmac-use-twin-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refmac_use_twin_state()` | not tried |
| Scheme | `(refmac-use-twin-state)` | not tried |

### save_refmac_params_to_map

Python: `save_refmac_params_to_map(imol_map, mtz_filename, fobs_col, sigfobs_col, r_free_col, r_free_flag_sensible)`  
Scheme: `(save-refmac-params-to-map imol-map mtz-filename fobs-col sigfobs-col r-free-col r-free-flag-sensible)`

Arguments: imol_map (a whole number), mtz_filename (text), fobs_col (text), sigfobs_col (text), r_free_col (text), r_free_flag_sensible (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_refmac_params_to_map(1, "rnasa-1.8-all_refmac1.mtz", "FWT", "hello", "hello", 1)` | not tried |
| Scheme | `(save-refmac-params-to-map 1 "rnasa-1.8-all_refmac1.mtz" "FWT" "hello" "hello" 1)` | not tried |

### save_refmac_phase_params_to_map

Python: `save_refmac_phase_params_to_map(imol_map, phi, fom, hla, hlb, hlc, hld)`  
Scheme: `(save-refmac-phase-params-to-map imol-map phi fom hla hlb hlc hld)`

Arguments: imol_map (a whole number), phi (text), fom (text), hla (text), hlb (text), hlc (text), hld (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_refmac_phase_params_to_map(1, "PHWT", "", "hello", "hello", "hello", "hello")` | not tried |
| Scheme | `(save-refmac-phase-params-to-map 1 "PHWT" "" "hello" "hello" "hello" "hello")` | not tried |

### schemize_command_name

Python: `schemize_command_name(s)`  
Scheme: `(schemize-command-name s)`

Arguments: s (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `schemize_command_name("hello")` | not tried |
| Scheme | `(schemize-command-name "hello")` | not tried |

### set_refmac_molecule

Python: `set_refmac_molecule(imol)`  
Scheme: `(set-refmac-molecule imol)`

this is the option menu callback - does nothing.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_molecule(0)` | not tried |
| Scheme | `(set-refmac-molecule 0)` | not tried |

### set_refmac_ncycles

Python: `set_refmac_ncycles(no_cycles)`  
Scheme: `(set-refmac-ncycles no-cycles)`

Arguments: no_cycles (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_ncycles(1)` | not tried |
| Scheme | `(set-refmac-ncycles 1)` | not tried |

### set_refmac_phase_input

Python: `set_refmac_phase_input(phase_flag)`  
Scheme: `(set-refmac-phase-input phase-flag)`

Arguments: phase_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_phase_input(1)` | not tried |
| Scheme | `(set-refmac-phase-input 1)` | not tried |

### set_refmac_refinement_method

Python: `set_refmac_refinement_method(method)`  
Scheme: `(set-refmac-refinement-method method)`

Arguments: method (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_refinement_method(1)` | not tried |
| Scheme | `(set-refmac-refinement-method 1)` | not tried |

### set_refmac_use_intensities

Python: `set_refmac_use_intensities(state)`  
Scheme: `(set-refmac-use-intensities state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_use_intensities(1)` | not tried |
| Scheme | `(set-refmac-use-intensities 1)` | not tried |

### set_refmac_use_ncs

Python: `set_refmac_use_ncs(state)`  
Scheme: `(set-refmac-use-ncs state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_use_ncs(1)` | not tried |
| Scheme | `(set-refmac-use-ncs 1)` | not tried |

### set_refmac_use_sad

Python: `set_refmac_use_sad(state)`  
Scheme: `(set-refmac-use-sad state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_use_sad(1)` | not tried |
| Scheme | `(set-refmac-use-sad 1)` | not tried |

### set_refmac_use_tls

Python: `set_refmac_use_tls(state)`  
Scheme: `(set-refmac-use-tls state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_use_tls(1)` | not tried |
| Scheme | `(set-refmac-use-tls 1)` | not tried |

### set_refmac_use_twin

Python: `set_refmac_use_twin(state)`  
Scheme: `(set-refmac-use-twin state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_use_twin(1)` | not tried |
| Scheme | `(set-refmac-use-twin 1)` | not tried |

### set_refmac_used_mtz_file

Python: `set_refmac_used_mtz_file(state)`  
Scheme: `(set-refmac-used-mtz-file state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_used_mtz_file(1)` | not tried |
| Scheme | `(set-refmac-used-mtz-file 1)` | not tried |

### set_stored_refmac_file_mtz_filename

Python: `set_stored_refmac_file_mtz_filename(imol, mtz_filename)`  
Scheme: `(set-stored-refmac-file-mtz-filename imol mtz-filename)`

Arguments: imol (a whole number), mtz_filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_stored_refmac_file_mtz_filename(0, "rnasa-1.8-all_refmac1.mtz")` | not tried |
| Scheme | `(set-stored-refmac-file-mtz-filename 0 "rnasa-1.8-all_refmac1.mtz")` | not tried |

### single_quote

Python: `single_quote(s)`  
Scheme: `(single-quote s)`

Arguments: s (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `single_quote("hello")` | not tried |
| Scheme | `(single-quote "hello")` | not tried |

