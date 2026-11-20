# mmCIF Functions

[Scripting reference](../README.md) > mmCIF Functions (20 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### auto_read_cif_data_with_phases

Python: `auto_read_cif_data_with_phases(filename)`  
Scheme: `(auto-read-cif-data-with-phases filename)`

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `auto_read_cif_data_with_phases("tutorial-modern.pdb")` | ran, returned `-1` |
| Scheme | `(auto-read-cif-data-with-phases "tutorial-modern.pdb")` | ran, returned `-1` |

Python and Scheme gave the same answer.

### handle_cif_dictionary

Python: `handle_cif_dictionary(filename)`  
Scheme: `(handle-cif-dictionary filename)`

return the number of bonds read (> 0 can be treated as success)

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_cif_dictionary("tutorial-modern.pdb")` | ran, returned `-1` |
| Scheme | `(handle-cif-dictionary "tutorial-modern.pdb")` | ran, returned `-1` |

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
| Python | `handle_cif_dictionary_for_molecule("tutorial-modern.pdb", 0, 1)` | ran, returned `-1` |
| Scheme | `(handle-cif-dictionary-for-molecule "tutorial-modern.pdb" 0 1)` | ran, returned `-1` |

Python and Scheme gave the same answer.

### import_all_refmac_cifs

Python: `import_all_refmac_cifs()`  
Scheme: `(import-all-refmac-cifs)`

Use the environment variable COOT_REFMAC_LIB_DIR to find cif files
 in subdirectories and import them all.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `import_all_refmac_cifs()` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |
| Scheme | `(import-all-refmac-cifs)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |

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
| Python | `open_cif_dictionary_file_selector_dialog()` | ran (no return value) |
| Scheme | `(open-cif-dictionary-file-selector-dialog)` | ran (no return value) |

### read_cif_data

Python: `read_cif_data(filename, imol_coords)`  
Scheme: `(read-cif-data filename imol-coords)`

Arguments: filename (text), imol_coords (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data("tutorial-modern.pdb", 0)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(read-cif-data "tutorial-modern.pdb" 0)` | stopped Coot when tried without a window (not checked with a window) |

### read_cif_data_2fofc_map

Python: `read_cif_data_2fofc_map(filename, imol_coords)`  
Scheme: `(read-cif-data-2fofc-map filename imol-coords)`

Arguments: filename (text), imol_coords (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_2fofc_map("tutorial-modern.pdb", 0)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(read-cif-data-2fofc-map "tutorial-modern.pdb" 0)` | stopped Coot when tried without a window (not checked with a window) |

### read_cif_data_fofc_map

Python: `read_cif_data_fofc_map(filename, imol_coords)`  
Scheme: `(read-cif-data-fofc-map filename imol-coords)`

Arguments: filename (text), imol_coords (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_fofc_map("tutorial-modern.pdb", 0)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(read-cif-data-fofc-map "tutorial-modern.pdb" 0)` | stopped Coot when tried without a window (not checked with a window) |

### read_cif_data_with_phases_2fo_fc

Python: `read_cif_data_with_phases_2fo_fc(filename)`  
Scheme: `(read-cif-data-with-phases-2fo-fc filename)`

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_with_phases_2fo_fc("tutorial-modern.pdb")` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(read-cif-data-with-phases-2fo-fc "tutorial-modern.pdb")` | stopped Coot when tried without a window (not checked with a window) |

### read_cif_data_with_phases_diff_sigmaa

Python: `read_cif_data_with_phases_diff_sigmaa(filename)`  
Scheme: `(read-cif-data-with-phases-diff-sigmaa filename)`

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_with_phases_diff_sigmaa("tutorial-modern.pdb")` | ran, returned `-1` |
| Scheme | `(read-cif-data-with-phases-diff-sigmaa "tutorial-modern.pdb")` | ran, returned `-1` |

Python and Scheme gave the same answer.

### read_cif_data_with_phases_fo_alpha_calc

Python: `read_cif_data_with_phases_fo_alpha_calc(filename)`  
Scheme: `(read-cif-data-with-phases-fo-alpha-calc filename)`

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_with_phases_fo_alpha_calc("tutorial-modern.pdb")` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(read-cif-data-with-phases-fo-alpha-calc "tutorial-modern.pdb")` | stopped Coot when tried without a window (not checked with a window) |

### read_cif_data_with_phases_fo_fc

Python: `read_cif_data_with_phases_fo_fc(filename)`  
Scheme: `(read-cif-data-with-phases-fo-fc filename)`

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_with_phases_fo_fc("tutorial-modern.pdb")` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(read-cif-data-with-phases-fo-fc "tutorial-modern.pdb")` | stopped Coot when tried without a window (not checked with a window) |

### read_cif_data_with_phases_nfo_fc

Python: `read_cif_data_with_phases_nfo_fc(filename, map_type)`  
Scheme: `(read-cif-data-with-phases-nfo-fc filename map-type)`

Arguments: filename (text), map_type (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_with_phases_nfo_fc("tutorial-modern.pdb", 1)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(read-cif-data-with-phases-nfo-fc "tutorial-modern.pdb" 1)` | stopped Coot when tried without a window (not checked with a window) |

### read_cif_data_with_phases_sigmaa

Python: `read_cif_data_with_phases_sigmaa(filename)`  
Scheme: `(read-cif-data-with-phases-sigmaa filename)`

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_data_with_phases_sigmaa("tutorial-modern.pdb")` | ran, returned `-1` |
| Scheme | `(read-cif-data-with-phases-sigmaa "tutorial-modern.pdb")` | ran, returned `-1` |

Python and Scheme gave the same answer.

### read_cif_dictionary

Python: `read_cif_dictionary(filename)`  
Scheme: `(read-cif-dictionary filename)`

synonym for above.

return the number of bonds read (> 0 can be treated as success)

Arguments: filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_cif_dictionary("tutorial-modern.pdb")` | ran, returned `-1` |
| Scheme | `(read-cif-dictionary "tutorial-modern.pdb")` | ran, returned `-1` |

Python and Scheme gave the same answer.

### read_small_molecule_cif

Python: `read_small_molecule_cif(file_name)`  
Scheme: `(read-small-molecule-cif file-name)`

Arguments: file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_small_molecule_cif("tutorial-modern.pdb")` | ran, returned `-1` |
| Scheme | `(read-small-molecule-cif "tutorial-modern.pdb")` | ran, returned `-1` |

Python and Scheme gave the same answer.

### read_small_molecule_data_cif

Python: `read_small_molecule_data_cif(file_name)`  
Scheme: `(read-small-molecule-data-cif file-name)`

Arguments: file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_small_molecule_data_cif("tutorial-modern.pdb")` | ran, returned `-1` |
| Scheme | `(read-small-molecule-data-cif "tutorial-modern.pdb")` | ran, returned `-1` |

Python and Scheme gave the same answer.

### read_small_molecule_data_cif_and_make_map_using_coords

Python: `read_small_molecule_data_cif_and_make_map_using_coords(file_name, imol_coords)`  
Scheme: `(read-small-molecule-data-cif-and-make-map-using-coords file-name imol-coords)`

Arguments: file_name (text), imol_coords (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `read_small_molecule_data_cif_and_make_map_using_coords("tutorial-modern.pdb", 0)` | ran, returned `-1` |
| Scheme | `(read-small-molecule-data-cif-and-make-map-using-coords "tutorial-modern.pdb" 0)` | ran, returned `-1` |

Python and Scheme gave the same answer.

### write_connectivity

Python: `write_connectivity(monomer_name, filename)`  
Scheme: `(write-connectivity monomer-name filename)`

Arguments: monomer_name (text), filename (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_connectivity("my-name", "tutorial-modern.pdb")` | ran, returned `0` |
| Scheme | `(write-connectivity "my-name" "tutorial-modern.pdb")` | ran, returned `0` |

Python and Scheme gave the same answer.

