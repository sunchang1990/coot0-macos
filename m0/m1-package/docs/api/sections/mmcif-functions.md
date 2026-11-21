# mmCIF Functions

[Scripting reference](../README.md) > mmCIF Functions (20 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### auto_read_cif_data_with_phases

Python: `auto_read_cif_data_with_phases(filename)`  
Scheme: `(auto-read-cif-data-with-phases filename)`

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `auto_read_cif_data_with_phases("rnasa-sf.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif SigmaA); new molecule 4 (map, rnasa-sf.cif Difference SigmaA); graphics_n_molecules(): 3 -> 5; scroll_wheel_map(): -1 -> 4 |
| Scheme | `(auto-read-cif-data-with-phases "rnasa-sf.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif SigmaA); new molecule 4 (map, rnasa-sf.cif Difference SigmaA); graphics_n_molecules(): 3 -> 5; scroll_wheel_map(): -1 -> 4 |

Example written and checked by hand on the test data. Expected: returns the SigmaA map molecule number; the difference SigmaA map is made too.

Note: rnasa-sf.cif (in test-data) is a structure-factor mmCIF made from rnasa-1.8-all_refmac1.mtz with gemmi mtz2cif.

Python and Scheme gave the same answer.

### handle_cif_dictionary

Python: `handle_cif_dictionary(filename)`  
Scheme: `(handle-cif-dictionary filename)`

return the number of bonds read (> 0 can be treated as success)

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_cif_dictionary("NAG.cif")` | ran, returned `36` |
| Scheme | `(handle-cif-dictionary "NAG.cif")` | ran, returned `36` |

Example written and checked by hand on the test data. Expected: reads the NAG dictionary; returns its index in the dictionary store (> 0 is success), -1 on failure.

Note: The doc says 'number of bonds read'; the code returns the monomer index of the dictionary (36 here, varies with what was read before).

Python and Scheme gave the same answer.

### handle_cif_dictionary_for_molecule

Python: `handle_cif_dictionary_for_molecule(filename, imol_enc, new_molecule_from_dictionary_cif_checkbutton_state)`  
Scheme: `(handle-cif-dictionary-for-molecule filename imol-enc new-molecule-from-dictionary-cif-checkbutton-state)`

return the number of bonds read (> 0 can be treated as success).
 Apply to the given molecule.

 imol_enc can be the model molecule number or
 IMOL_ENC_ANY = -999999, IMOL_ENC_AUTO = -999998, IMOL_ENC_UNSET = -999997

Arguments: filename (text), imol_enc (a whole number), new_molecule_from_dictionary_cif_checkbutton_state (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_cif_dictionary_for_molecule("NAG.cif", -999999, 1)` | ran, returned `36`; changed: new molecule 3 (model, NAG_from_dict); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | `(handle-cif-dictionary-for-molecule "NAG.cif" -999999 1)` | ran, returned `36`; changed: new molecule 3 (model, NAG_from_dict); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: reads the dictionary for all molecules (-999999 = IMOL_ENC_ANY) and, with the last argument 1, makes a molecule from it; returns the dictionary index. With imol_enc 0 no molecule is made.

Python and Scheme gave the same answer.

### import_all_refmac_cifs

Python: `import_all_refmac_cifs()`  
Scheme: `(import-all-refmac-cifs)`

Use the environment variable COOT_REFMAC_LIB_DIR to find cif files
 in subdirectories and import them all.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `import_all_refmac_cifs()` | ran (no return value, nothing visible changed) |
| Scheme | `(import-all-refmac-cifs)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: reads every .cif dictionary under $COOT_REFMAC_LIB_DIR; does nothing when the variable is not set.

### non_standard_residue_names

Python: `non_standard_residue_names(imol)`  
Scheme: `(non-standard-residue-names imol)`

non-standard residue/monomer names (note HOH is not non-standard).

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `non_standard_residue_names_py`.
Also available in Scheme as `non-standard-residue-names-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `non_standard_residue_names(0)` | ran, returned `[]` |
| Scheme | `(non-standard-residue-names 0)` | ran, returned `()` |

Python and Scheme gave the same answer.

### open_cif_dictionary_file_selector_dialog

Python: `open_cif_dictionary_file_selector_dialog()`  
Scheme: `(open-cif-dictionary-file-selector-dialog)`

open the cif dictionary file selector dialog

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `open_cif_dictionary_file_selector_dialog()` | ran (no return value, nothing visible changed) |
| Scheme | `(open-cif-dictionary-file-selector-dialog)` | ran (no return value, nothing visible changed) |

### read_cif_data

Python: `read_cif_data(filename, imol_coords)`  
Scheme: `(read-cif-data filename imol-coords)`

Arguments: filename (text), imol_coords (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data("rnasa-sf.cif", 0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(read-cif-data "rnasa-sf.cif" 0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif); graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number: a map calculated from F_meas and the phases of model molecule 0.

Note: rnasa-sf.cif (in test-data) is a structure-factor mmCIF made from rnasa-1.8-all_refmac1.mtz with gemmi mtz2cif.

Python and Scheme gave the same answer.

### read_cif_data_2fofc_map

Python: `read_cif_data_2fofc_map(filename, imol_coords)`  
Scheme: `(read-cif-data-2fofc-map filename imol-coords)`

Arguments: filename (text), imol_coords (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_2fofc_map("rnasa-sf.cif", 0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(read-cif-data-2fofc-map "rnasa-sf.cif" 0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif); graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number: a 2Fo-Fc map from the F_meas data and model 0.

Note: rnasa-sf.cif (in test-data) is a structure-factor mmCIF made from rnasa-1.8-all_refmac1.mtz with gemmi mtz2cif.

Python and Scheme gave the same answer.

### read_cif_data_fofc_map

Python: `read_cif_data_fofc_map(filename, imol_coords)`  
Scheme: `(read-cif-data-fofc-map filename imol-coords)`

Arguments: filename (text), imol_coords (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_fofc_map("rnasa-sf.cif", 0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(read-cif-data-fofc-map "rnasa-sf.cif" 0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif); graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number: an Fo-Fc difference map from the F_meas data and model 0.

Note: rnasa-sf.cif (in test-data) is a structure-factor mmCIF made from rnasa-1.8-all_refmac1.mtz with gemmi mtz2cif.

Python and Scheme gave the same answer.

### read_cif_data_with_phases_2fo_fc

Python: `read_cif_data_with_phases_2fo_fc(filename)`  
Scheme: `(read-cif-data-with-phases-2fo-fc filename)`

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_with_phases_2fo_fc("rnasa-sf.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif 2Fo-Fc); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(read-cif-data-with-phases-2fo-fc "rnasa-sf.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif 2Fo-Fc); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number of a 2Fo-Fc map.

Note: rnasa-sf.cif (in test-data) is a structure-factor mmCIF made from rnasa-1.8-all_refmac1.mtz with gemmi mtz2cif.

Python and Scheme gave the same answer.

### read_cif_data_with_phases_diff_sigmaa

Python: `read_cif_data_with_phases_diff_sigmaa(filename)`  
Scheme: `(read-cif-data-with-phases-diff-sigmaa filename)`

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_with_phases_diff_sigmaa("rnasa-sf.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif Difference SigmaA); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(read-cif-data-with-phases-diff-sigmaa "rnasa-sf.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif Difference SigmaA); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number of the difference (mFo-DFc) map from the phases in the file.

Note: rnasa-sf.cif (in test-data) is a structure-factor mmCIF made from rnasa-1.8-all_refmac1.mtz with gemmi mtz2cif.

Python and Scheme gave the same answer.

### read_cif_data_with_phases_fo_alpha_calc

Python: `read_cif_data_with_phases_fo_alpha_calc(filename)`  
Scheme: `(read-cif-data-with-phases-fo-alpha-calc filename)`

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_with_phases_fo_alpha_calc("rnasa-sf.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif Fo ac); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(read-cif-data-with-phases-fo-alpha-calc "rnasa-sf.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif Fo ac); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number of an Fo, alpha-calc map.

Note: rnasa-sf.cif (in test-data) is a structure-factor mmCIF made from rnasa-1.8-all_refmac1.mtz with gemmi mtz2cif.

Python and Scheme gave the same answer.

### read_cif_data_with_phases_fo_fc

Python: `read_cif_data_with_phases_fo_fc(filename)`  
Scheme: `(read-cif-data-with-phases-fo-fc filename)`

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_with_phases_fo_fc("rnasa-sf.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif Fo-Fc); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(read-cif-data-with-phases-fo-fc "rnasa-sf.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif Fo-Fc); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number of an Fo-Fc map.

Note: rnasa-sf.cif (in test-data) is a structure-factor mmCIF made from rnasa-1.8-all_refmac1.mtz with gemmi mtz2cif.

Python and Scheme gave the same answer.

### read_cif_data_with_phases_nfo_fc

Python: `read_cif_data_with_phases_nfo_fc(filename, map_type)`  
Scheme: `(read-cif-data-with-phases-nfo-fc filename map-type)`

Arguments: filename (text), map_type (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_with_phases_nfo_fc("rnasa-sf.cif", 1)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif 2Fo-Fc); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(read-cif-data-with-phases-nfo-fc "rnasa-sf.cif" 1)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif 2Fo-Fc); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: map_type 0 SigmaA, 1 2Fo-Fc, 2 Fo-Fc, 3 Fo alpha-calc, 4 difference SigmaA; returns the new map molecule number.

Note: rnasa-sf.cif (in test-data) is a structure-factor mmCIF made from rnasa-1.8-all_refmac1.mtz with gemmi mtz2cif.

Python and Scheme gave the same answer.

### read_cif_data_with_phases_sigmaa

Python: `read_cif_data_with_phases_sigmaa(filename)`  
Scheme: `(read-cif-data-with-phases-sigmaa filename)`

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_with_phases_sigmaa("rnasa-sf.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif SigmaA); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(read-cif-data-with-phases-sigmaa "rnasa-sf.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sf.cif SigmaA); graphics_n_molecules(): 3 -> 4; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: returns the new map molecule number of the SigmaA (2mFo-DFc) map from the phases in the file.

Note: rnasa-sf.cif (in test-data) is a structure-factor mmCIF made from rnasa-1.8-all_refmac1.mtz with gemmi mtz2cif.

Python and Scheme gave the same answer.

### read_cif_dictionary

Python: `read_cif_dictionary(filename)`  
Scheme: `(read-cif-dictionary filename)`

synonym for above.

return the number of bonds read (> 0 can be treated as success)

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_dictionary("ATP.cif")` | ran, returned `36` |
| Scheme | `(read-cif-dictionary "ATP.cif")` | ran, returned `36` |

Example written and checked by hand on the test data. Expected: same as handle_cif_dictionary: returns the dictionary index (> 0 success), -1 on failure.

Note: Returns the monomer index, not a number of bonds as documented.

Python and Scheme gave the same answer.

### read_small_molecule_cif

Python: `read_small_molecule_cif(file_name)`  
Scheme: `(read-small-molecule-cif file-name)`

Arguments: file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_small_molecule_cif("rnasa-sm.cif")` | ran, returned `3`; changed: new molecule 3 (model, rnasa-sm.cif); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | `(read-small-molecule-cif "rnasa-sm.cif")` | ran, returned `3`; changed: new molecule 3 (model, rnasa-sm.cif); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the new model molecule number made from the atoms (_atom_site_fract_*) of a small-molecule CIF; -1 on failure.

Note: rnasa-sm.cif and rnasa-sm-data.cif (in test-data) are a small-molecule style CIF made from residues A39-41 of the test model and the rnasa reflections, only to show the call.

Python and Scheme gave the same answer.

### read_small_molecule_data_cif

Python: `read_small_molecule_data_cif(file_name)`  
Scheme: `(read-small-molecule-data-cif file-name)`

Arguments: file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_small_molecule_data_cif("rnasa-sm-data.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sm-data.cif SigmaA); new molecule 4 (map, rnasa-sm-data.cif Diff-SigmaA); graphics_n_molecules(): 3 -> 5; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(read-small-molecule-data-cif "rnasa-sm-data.cif")` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sm-data.cif SigmaA); new molecule 4 (map, rnasa-sm-data.cif Diff-SigmaA); graphics_n_molecules(): 3 -> 5; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: returns the molecule number of the SigmaA map made from the reflections (F_meas + F_calc/phase_calc) of a small-molecule data CIF; a difference map is made too.

Note: rnasa-sm.cif and rnasa-sm-data.cif (in test-data) are a small-molecule style CIF made from residues A39-41 of the test model and the rnasa reflections, only to show the call.

Python and Scheme gave the same answer.

### read_small_molecule_data_cif_and_make_map_using_coords

Python: `read_small_molecule_data_cif_and_make_map_using_coords(file_name, imol_coords)`  
Scheme: `(read-small-molecule-data-cif-and-make-map-using-coords file-name imol-coords)`

Arguments: file_name (text), imol_coords (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_small_molecule_data_cif_and_make_map_using_coords("rnasa-sm-data.cif", 0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sm-data.cif SigmaA); new molecule 4 (map, rnasa-sm-data.cif Diff-SigmaA); graphics_n_molecules(): 3 -> 5; scroll_wheel_map(): -1 -> 3 |
| Scheme | `(read-small-molecule-data-cif-and-make-map-using-coords "rnasa-sm-data.cif" 0)` | ran, returned `3`; changed: new molecule 3 (map, rnasa-sm-data.cif SigmaA); new molecule 4 (map, rnasa-sm-data.cif Diff-SigmaA); graphics_n_molecules(): 3 -> 5; scroll_wheel_map(): -1 -> 3 |

Example written and checked by hand on the test data. Expected: returns the new SigmaA map molecule number, phases from the coordinates of model 0; a difference map is made too.

Note: rnasa-sm.cif and rnasa-sm-data.cif (in test-data) are a small-molecule style CIF made from residues A39-41 of the test model and the rnasa reflections, only to show the call.

Python and Scheme gave the same answer.

### write_connectivity

Python: `write_connectivity(monomer_name, filename)`  
Scheme: `(write-connectivity monomer-name filename)`

Arguments: monomer_name (text), filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `handle_cif_dictionary("NAG.cif")`, then `write_connectivity("NAG", "nag-connect.txt")` | ran, returned `1` |
| Scheme | first `(handle-cif-dictionary "NAG.cif")`, then `(write-connectivity "NAG" "nag-connect.txt")` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 and writes a CONECT-style connectivity file for NAG; 0 when the dictionary for that type is not loaded yet (it is not loaded on demand).

Python and Scheme gave the same answer.

