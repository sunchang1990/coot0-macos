# Execute Refmac

[Scripting reference](../README.md) > Execute Refmac (43 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_refmac_ncycle_no

Python: `add_refmac_ncycle_no(cycle)`  
Scheme: `(add-refmac-ncycle-no cycle)`

Arguments: cycle (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_refmac_ncycle_no(15)` | ran (no return value, nothing visible changed) |
| Scheme | `(add-refmac-ncycle-no 20)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: adds 15 to the list of cycle numbers offered in the Run Refmac dialog.

Note: Only stores a setting for the next Refmac run; does not run Refmac.

### add_refmac_sad_atom

Python: `add_refmac_sad_atom(atom_name, fp, fpp, lambda)`  
Scheme: `(add-refmac-sad-atom atom-name fp fpp lambda)`

Arguments: atom_name (text), fp (a number), fpp (a number), lambda (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_refmac_sad_atom("SE", -8.0, 4.5, 0.9792)` | ran (no return value, nothing visible changed) |
| Scheme | `(add-refmac-sad-atom "SE" -8.0 4.5 0.9792)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: registers Se with f' -8.0, f'' 4.5 at 0.9792 A for a SAD Refmac run.

Note: Only stores a setting for the next Refmac run; does not run Refmac.

### add_refmac_sad_atom_fp

Python: `add_refmac_sad_atom_fp(atom_name, fp, fpp)`  
Scheme: `(add-refmac-sad-atom-fp atom-name fp fpp)`

Arguments: atom_name (text), fp (a number), fpp (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_refmac_sad_atom_fp("S", 0.3, 0.6)` | ran (no return value, nothing visible changed) |
| Scheme | `(add-refmac-sad-atom-fp "S" 0.3 0.6)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: registers S with f' 0.3, f'' 0.6 for a SAD Refmac run.

Note: Only stores a setting for the next Refmac run; does not run Refmac.

### add_refmac_sad_atom_lambda

Python: `add_refmac_sad_atom_lambda(atom_name, lambda)`  
Scheme: `(add-refmac-sad-atom-lambda atom-name lambda)`

Arguments: atom_name (text), lambda (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_refmac_sad_atom_lambda("ZN", 1.2827)` | ran (no return value, nothing visible changed) |
| Scheme | `(add-refmac-sad-atom-lambda "ZN" 1.2827)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: registers Zn at wavelength 1.2827 A (Refmac computes f'/f'') for a SAD run.

Note: Only stores a setting for the next Refmac run; does not run Refmac.

### add_to_database

Python: `add_to_database(command_strings)`  
Scheme: `(add-to-database command-strings)`

Arguments: command_strings (a list). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_to_database("hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(add-to-database "hello")` | error: In procedure add-to-database: Wrong type argument in position 1: "hello" |

### add_to_history

Python: `add_to_history(ls)`  
Scheme: `(add-to-history ls)`

Arguments: ls (a list). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_to_history("hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(add-to-history "hello")` | error: In procedure add-to-history: Wrong type argument in position 1: "hello" |

### add_to_history_simple

Python: `add_to_history_simple(cmd)`  
Scheme: `(add-to-history-simple cmd)`

Arguments: cmd (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_to_history_simple("hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(add-to-history-simple "hello")` | ran (no return value, nothing visible changed) |

### add_to_history_typed

Python: `add_to_history_typed(command, args)`  
Scheme: `(add-to-history-typed command args)`

Arguments: command (text), args (a list). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: C++ helper that records a command in Coot's history.

Note: Exported by SWIG to both languages but unusable from scripts.

### ccp4_project_directory

Python: `ccp4_project_directory(ccp4_project_name)`  
Scheme: `(ccp4-project-directory ccp4-project-name)`

Arguments: ccp4_project_name (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ccp4_project_directory("my-name")` | ran, returned `''` |
| Scheme | `(ccp4-project-directory "my-name")` | ran, returned `""` |

Python and Scheme gave the same answer.

### clear_refmac_sad_atoms

Python: `clear_refmac_sad_atoms()`  
Scheme: `(clear-refmac-sad-atoms)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `add_refmac_sad_atom("SE", -8.0, 4.5, 0.9792)`, then `clear_refmac_sad_atoms()` | ran (no return value, nothing visible changed) |
| Scheme | first `(add-refmac-sad-atom "SE" -8.0 4.5 0.9792)`, then `(clear-refmac-sad-atoms)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: removes all SAD atoms registered with add_refmac_sad_atom*.

Note: Only stores a setting for the next Refmac run; does not run Refmac.

### compare_mtimes

Python: `compare_mtimes(a, b)`  
Scheme: `(compare-mtimes a b)`

Arguments: a (`coot::str_mtime`), b (`coot::str_mtime`). Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: C++ sort helper: True when a is newer than b.

### execute_refmac_real

Python: `execute_refmac_real(pdb_in_filename, pdb_out_filename, mtz_in_filename, mtz_out_filename, cif_lib_filename, fobs_col_name, sigfobs_col_name, r_free_col_name, have_sensible_free_r_flag, make_molecules_flag, refmac_count_string, swap_map_colours_post_refmac_flag, imol_refmac_map, diff_map_flag, phase_combine_flag, phib_string, fom_string, ccp4i_project_dir)`  
Scheme: `(execute-refmac-real pdb-in-filename pdb-out-filename mtz-in-filename mtz-out-filename cif-lib-filename fobs-col-name sigfobs-col-name r-free-col-name have-sensible-free-r-flag make-molecules-flag refmac-count-string swap-map-colours-post-refmac-flag imol-refmac-map diff-map-flag phase-combine-flag phib-string fom-string ccp4i-project-dir)`

Arguments: pdb_in_filename (text), pdb_out_filename (text), mtz_in_filename (text), mtz_out_filename (text), cif_lib_filename (text), fobs_col_name (text), sigfobs_col_name (text), r_free_col_name (text), have_sensible_free_r_flag (a whole number), make_molecules_flag (a whole number), refmac_count_string (text), swap_map_colours_post_refmac_flag (a whole number), imol_refmac_map (a whole number), diff_map_flag (a whole number), phase_combine_flag (a whole number), phib_string (text), fom_string (text), ccp4i_project_dir (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `execute_refmac_real("tutorial-modern.pdb", "tutorial-modern.pdb", "rnasa-1.8-all_refmac1.mtz", "rnasa-1.8-all_refmac1.mtz", "tutorial-modern.pdb", "my-name", "my-name", "my-name", 1, 1, "hello", 1, 1, ...` | not run: runs Refmac (long external program); use run_refmac_by_filename / the Run Refmac dialog |
| Scheme | `(execute-refmac-real "tutorial-modern.pdb" "tutorial-modern.pdb" "rnasa-1.8-all_refmac1.mtz" "rnasa-1.8-all_refmac1.mtz" "tutorial-modern.pdb" "my-name" "my-name" "my-name" 1 1 "hello" 1 1 1 1 "hello" ...` | not run: runs Refmac (long external program); use run_refmac_by_filename / the Run Refmac dialog |

Example written and checked by hand on the test data. Expected: runs Refmac on the given files and reads the results.

### get_refmac_ncycles

Python: `get_refmac_ncycles()`  
Scheme: `(get-refmac-ncycles)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_refmac_ncycles()` | ran, returned `5` |
| Scheme | `(get-refmac-ncycles)` | ran, returned `5` |

Example written and checked by hand on the test data. Expected: returns the number of Refmac cycles (default 5).

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Python and Scheme gave the same answer.

### get_refmac_phase_input

Python: `get_refmac_phase_input()`  
Scheme: `(get-refmac-phase-input)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_refmac_phase_input()` | ran, returned `0` |
| Scheme | `(get-refmac-phase-input)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns the phase input mode: 0 none (default), 1 PHI/FOM, 2 HL, 3 SAD.

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Python and Scheme gave the same answer.

### get_refmac_refinement_method

Python: `get_refmac_refinement_method()`  
Scheme: `(get-refmac-refinement-method)`

some methods to get refmac run parameters

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_refmac_refinement_method()` | ran, returned `0` |
| Scheme | `(get-refmac-refinement-method)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns the refinement method: 0 restrained (default), 1 rigid body, 2 restrained + TLS.

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Python and Scheme gave the same answer.

### get_refmac_used_mtz_file_state

Python: `get_refmac_used_mtz_file_state()`  
Scheme: `(get-refmac-used-mtz-file-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_refmac_used_mtz_file_state()` | ran, returned `1` |
| Scheme | `(get-refmac-used-mtz-file-state)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 when Refmac takes its data from an MTZ file, 0 when from a map's stored parameters.

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Python and Scheme gave the same answer.

### get_saved_refmac_file_filename

Python: `get_saved_refmac_file_filename()`  
Scheme: `(get-saved-refmac-file-filename)`

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_saved_refmac_file_filename()` | ran (no return value, nothing visible changed) |
| Scheme | `(get-saved-refmac-file-filename)` | ran, returned `()` |

Example written and checked by hand on the test data. Expected: returns the MTZ file name chosen for Refmac, nothing when none was chosen.

Note: Only stores a setting for the next Refmac run; does not run Refmac. Python returns None, Scheme returns '() when unset.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### languagize_command

Python: `languagize_command(command_parts)`  
Scheme: `(languagize-command command-parts)`

Arguments: command_parts (a list). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `languagize_command("hello")` | ran, returned `'(h e l l o)'` |
| Scheme | `(languagize-command "hello")` | error: In procedure languagize-command: Wrong type argument in position 1: "hello" |

### merge_molecules_by_vector

Python: `merge_molecules_by_vector(add_molecules, imol)`  
Scheme: `(merge-molecules-by-vector add-molecules imol)`

return the status and vector of chain-ids of the new chain ids.

Arguments: add_molecules (a list), imol (a whole number). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `merge_molecules_by_vector([read_pdb("nag_only.pdb")], 0)` | ran, returned `<Swig Object of type 'std::pair< int,std::vector< merge_molecule_results_info_t,std::allocator< merge_molecule_results_i ...`; changed: molecule 0: added 1 residue(s) (C1); new molecule 3 (model, nag_only.pdb); rotation centre moved 44.4 A to (-0.0, -0.0, -0.0); first_small_coords_imol(): -1 -> 3 ... |
| Scheme | `(merge-molecules-by-vector (list (read-pdb "nag_only.pdb")) 0)` | ran, returned `#<collectable-swig-pointer std::pair< int,std::vector< merge_molecule_results_info_t > > * 92d003b00>`; changed: molecule 0: added 1 residue(s) (C1); new molecule 3 (model, nag_only.pdb); rotation centre moved 44.4 A to (-0.0, -0.0, -0.0); first_small_coords_imol(): -1 -> 3 ... |

Example written and checked by hand on the test data. Expected: merges the listed molecules into molecule 0 (the merge works); the result is a C++ object.

Note: Works, but returns an opaque SWIG pointer; scripts should use merge_molecules(list, imol) which returns a readable result.

### parse_ccp4i_defs

Python: `parse_ccp4i_defs(filename)`  
Scheme: `(parse-ccp4i-defs filename)`

Arguments: filename (text). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `open("directories.def", "w").write("PROJECT_ALIAS,1 _text myproject\nPROJECT_PATH,1 _text /tmp/myproject\n")`, then `parse_ccp4i_defs("directories.def")` | ran, returned `<Swig Object of type 'std::vector< std::pair< std::string,std::string >,std::allocator< std::pair< std::string,std::stri ...` |
| Scheme | first `(call-with-output-file "directories.def" (lambda (p) (display "PROJECT_ALIAS,1 _text myproject\nPROJECT_PATH,1 _text /tmp/myproject\n" p)))`, then `(parse-ccp4i-defs "directories.def")` | ran, returned `#<collectable-swig-pointer std::vector< std::pair< std::string,std::string > > * 97ed8ca60>` |

Example written and checked by hand on the test data. Expected: parses a CCP4i directories.def file into (alias, path) pairs.

Note: Returns an opaque SWIG pointer in both languages (C++ return type not converted); use ccp4i_projects() from scripts.

### pythonize_command_name

Python: `pythonize_command_name(s)`  
Scheme: `(pythonize-command-name s)`

Arguments: s (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `pythonize_command_name("hello")` | ran, returned `'hello'` |
| Scheme | `(pythonize-command-name "hello")` | ran, returned `"hello"` |

Python and Scheme gave the same answer.

### refmac_imol_coords

Python: `refmac_imol_coords()`  
Scheme: `(refmac-imol-coords)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `set_refmac_molecule(0)`, then `refmac_imol_coords()` | ran, returned `0` |
| Scheme | first `(set-refmac-molecule 0)`, then `(refmac-imol-coords)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns the molecule chosen for Refmac (0 = tutorial-modern.pdb here).

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Python and Scheme gave the same answer.

### refmac_name

Python: `refmac_name(imol)`  
Scheme: `(refmac-name imol)`

the name for refmac

 Returns a stub name used in the construction of filename for refmac output

Arguments: imol (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refmac_name(0)` | ran, returned `'tutorial-modern_refmac0-pre.pdb'` |
| Scheme | `(refmac-name 0)` | ran, returned `"tutorial-modern_refmac0-pre.pdb"` |

Example written and checked by hand on the test data. Expected: returns the file name Coot will write molecule 0 to before running Refmac.

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Python and Scheme gave the same answer.

### refmac_use_intensities_state

Python: `refmac_use_intensities_state()`  
Scheme: `(refmac-use-intensities-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refmac_use_intensities_state()` | ran, returned `0` |
| Scheme | `(refmac-use-intensities-state)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns 1 when Refmac uses intensities (default 0, amplitudes).

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Python and Scheme gave the same answer.

### refmac_use_ncs_state

Python: `refmac_use_ncs_state()`  
Scheme: `(refmac-use-ncs-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refmac_use_ncs_state()` | ran, returned `1` |
| Scheme | `(refmac-use-ncs-state)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 when Refmac uses NCS restraints.

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Python and Scheme gave the same answer.

### refmac_use_sad_state

Python: `refmac_use_sad_state()`  
Scheme: `(refmac-use-sad-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refmac_use_sad_state()` | ran, returned `0` |
| Scheme | `(refmac-use-sad-state)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns 1 when Refmac does SAD refinement (default 0).

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Python and Scheme gave the same answer.

### refmac_use_tls_state

Python: `refmac_use_tls_state()`  
Scheme: `(refmac-use-tls-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refmac_use_tls_state()` | ran, returned `1` |
| Scheme | `(refmac-use-tls-state)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 when Refmac uses TLS.

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Python and Scheme gave the same answer.

### refmac_use_twin_state

Python: `refmac_use_twin_state()`  
Scheme: `(refmac-use-twin-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refmac_use_twin_state()` | ran, returned `0` |
| Scheme | `(refmac-use-twin-state)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns 1 when Refmac does twin refinement (default 0).

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Python and Scheme gave the same answer.

### save_refmac_params_to_map

Python: `save_refmac_params_to_map(imol_map, mtz_filename, fobs_col, sigfobs_col, r_free_col, r_free_flag_sensible)`  
Scheme: `(save-refmac-params-to-map imol-map mtz-filename fobs-col sigfobs-col r-free-col r-free-flag-sensible)`

Arguments: imol_map (a whole number), mtz_filename (text), fobs_col (text), sigfobs_col (text), r_free_col (text), r_free_flag_sensible (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_refmac_params_to_map(1, "rnasa-1.8-all_refmac1.mtz", "FGMP18", "SIGFGMP18", "FreeR_flag", 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(save-refmac-params-to-map 1 "rnasa-1.8-all_refmac1.mtz" "FGMP18" "SIGFGMP18" "FreeR_flag" 1)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: stores Fobs/SigF/Rfree columns with map 1 (refmac_parameters(1) shows them).

Note: Only stores a setting for the next Refmac run; does not run Refmac.

### save_refmac_phase_params_to_map

Python: `save_refmac_phase_params_to_map(imol_map, phi, fom, hla, hlb, hlc, hld)`  
Scheme: `(save-refmac-phase-params-to-map imol-map phi fom hla hlb hlc hld)`

Arguments: imol_map (a whole number), phi (text), fom (text), hla (text), hlb (text), hlc (text), hld (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_refmac_phase_params_to_map(1, "PHIC", "FOM", "", "", "", "")` | ran (no return value, nothing visible changed) |
| Scheme | `(save-refmac-phase-params-to-map 1 "PHIC" "FOM" "" "" "" "")` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: stores phase (PHI/FOM or HL) columns with map 1 for a Refmac run with phase input.

Note: Only stores a setting for the next Refmac run; does not run Refmac.

### schemize_command_name

Python: `schemize_command_name(s)`  
Scheme: `(schemize-command-name s)`

Arguments: s (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `schemize_command_name("hello")` | ran, returned `'hello'` |
| Scheme | `(schemize-command-name "hello")` | ran, returned `"hello"` |

Python and Scheme gave the same answer.

### set_refmac_molecule

Python: `set_refmac_molecule(imol)`  
Scheme: `(set-refmac-molecule imol)`

this is the option menu callback - does nothing.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_molecule(0)` | ran, returned `0` |
| Scheme | `(set-refmac-molecule 0)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: chooses molecule 0 for Refmac; returns 0 (option-menu callback).

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Python and Scheme gave the same answer.

### set_refmac_ncycles

Python: `set_refmac_ncycles(no_cycles)`  
Scheme: `(set-refmac-ncycles no-cycles)`

Arguments: no_cycles (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_ncycles(10)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refmac-ncycles 3)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the number of Refmac cycles.

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Setting checked (set to another value and read back, then put back): Python: get_refmac_ncycles was 5, set to 0, read back 0; Scheme: get-refmac-ncycles was 5, set to 0, read back 0.

### set_refmac_phase_input

Python: `set_refmac_phase_input(phase_flag)`  
Scheme: `(set-refmac-phase-input phase-flag)`

Arguments: phase_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_phase_input(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refmac-phase-input 2)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the phase input mode (0 none, 1 PHI/FOM, 2 HL, 3 SAD).

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Setting checked (set to another value and read back, then put back): Python: get_refmac_phase_input was 0, set to 1, read back 1; Scheme: get-refmac-phase-input was 0, set to 1, read back 1.

### set_refmac_refinement_method

Python: `set_refmac_refinement_method(method)`  
Scheme: `(set-refmac-refinement-method method)`

Arguments: method (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_refinement_method(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refmac-refinement-method 2)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the method (0 restrained, 1 rigid body, 2 restrained + TLS).

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Setting checked (set to another value and read back, then put back): Python: get_refmac_refinement_method was 0, set to 1, read back 1; Scheme: get-refmac-refinement-method was 0, set to 1, read back 1.

### set_refmac_use_intensities

Python: `set_refmac_use_intensities(state)`  
Scheme: `(set-refmac-use-intensities state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_use_intensities(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refmac-use-intensities 0)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the Refmac intensities option (read back with refmac_use_intensities_state()).

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Setting checked (set to another value and read back, then put back): Python: refmac_use_intensities_state was 0, set to 1, read back 1; Scheme: refmac-use-intensities-state was 0, set to 1, read back 1.

### set_refmac_use_ncs

Python: `set_refmac_use_ncs(state)`  
Scheme: `(set-refmac-use-ncs state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_use_ncs(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refmac-use-ncs 1)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the Refmac ncs option (read back with refmac_use_ncs_state()).

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Setting checked (set to another value and read back, then put back): Python: refmac_use_ncs_state was 1, set to 0, read back 0; Scheme: refmac-use-ncs-state was 1, set to 0, read back 0.

### set_refmac_use_sad

Python: `set_refmac_use_sad(state)`  
Scheme: `(set-refmac-use-sad state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_use_sad(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refmac-use-sad 0)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the Refmac sad option (read back with refmac_use_sad_state()).

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Setting checked (set to another value and read back, then put back): Python: refmac_use_sad_state was 0, set to 1, read back 1; Scheme: refmac-use-sad-state was 0, set to 1, read back 1.

### set_refmac_use_tls

Python: `set_refmac_use_tls(state)`  
Scheme: `(set-refmac-use-tls state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_use_tls(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refmac-use-tls 1)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the Refmac tls option (read back with refmac_use_tls_state()).

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Setting checked (set to another value and read back, then put back): Python: refmac_use_tls_state was 1, set to 0, read back 0; Scheme: refmac-use-tls-state was 1, set to 0, read back 0.

### set_refmac_use_twin

Python: `set_refmac_use_twin(state)`  
Scheme: `(set-refmac-use-twin state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_use_twin(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refmac-use-twin 0)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the Refmac twin option (read back with refmac_use_twin_state()).

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Setting checked (set to another value and read back, then put back): Python: refmac_use_twin_state was 0, set to 1, read back 1; Scheme: refmac-use-twin-state was 0, set to 1, read back 1.

### set_refmac_used_mtz_file

Python: `set_refmac_used_mtz_file(state)`  
Scheme: `(set-refmac-used-mtz-file state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_used_mtz_file(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refmac-used-mtz-file 0)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: chooses whether Refmac data come from an MTZ file (1) or from a map's stored parameters (0).

Note: Only stores a setting for the next Refmac run; does not run Refmac.

Setting checked (set to another value and read back, then put back): Python: get_refmac_used_mtz_file_state was 1, set to 0, read back 0; Scheme: get-refmac-used-mtz-file-state was 1, set to 0, read back 0.

### set_stored_refmac_file_mtz_filename

Python: `set_stored_refmac_file_mtz_filename(imol, mtz_filename)`  
Scheme: `(set-stored-refmac-file-mtz-filename imol mtz-filename)`

Arguments: imol (a whole number), mtz_filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_stored_refmac_file_mtz_filename(0, "rnasa-1.8-all_refmac1.mtz")` | ran (no return value, nothing visible changed) |
| Scheme | `(set-stored-refmac-file-mtz-filename 0 "rnasa-1.8-all_refmac1.mtz")` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: stores the MTZ file to use with molecule 0 in Refmac runs.

Note: Only stores a setting for the next Refmac run; does not run Refmac.

### single_quote

Python: `single_quote(s)`  
Scheme: `(single-quote s)`

Arguments: s (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `single_quote("hello")` | ran, returned `'"hello"'` |
| Scheme | `(single-quote "hello")` | ran, returned `"\"hello\""` |

Python and Scheme gave the same answer.

