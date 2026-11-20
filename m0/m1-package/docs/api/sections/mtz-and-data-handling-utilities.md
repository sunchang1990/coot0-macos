# MTZ and data handling utilities

[Scripting reference](../README.md) > MTZ and data handling utilities (9 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_d_cols

Python: `get_d_cols(mtz_file_name)`  
Scheme: `(get-d-cols mtz-file-name)`

Arguments: mtz_file_name (text). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_d_cols("rnasa-1.8-all_refmac1.mtz")` | ran, returned `()` |
| Scheme | `(get-d-cols "rnasa-1.8-all_refmac1.mtz")` | ran, returned `#()` |

Python and Scheme gave the same answer.

### get_f_cols

Python: `get_f_cols(mtz_file_name)`  
Scheme: `(get-f-cols mtz-file-name)`

Arguments: mtz_file_name (text). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_f_cols("rnasa-1.8-all_refmac1.mtz")` | ran, returned `('/RNASE3GMP/COMPLEX/FGMP18', '/RNASE3GMP/COMPLEX/FC', '/RNASE3GMP/COMPLEX/FC_ALL', '/RNASE3GMP/COMPLEX/FWT', '/RNASE3GM ...` |
| Scheme | `(get-f-cols "rnasa-1.8-all_refmac1.mtz")` | ran, returned `#("/RNASE3GMP/COMPLEX/FGMP18" "/RNASE3GMP/COMPLEX/FC" "/RNASE3GMP/COMPLEX/FC_ALL" "/RNASE3GMP/COMPLEX/FWT" "/RNASE3GMP/C ...` |

Python and Scheme gave the same answer.

### get_mtz_columns

Python: `get_mtz_columns(filename)`  
Scheme: `(get-mtz-columns filename)`

Arguments: filename (text). Returns: `mtz_column_types_info_t`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_mtz_columns("tutorial-modern.pdb")` | ran, returned `<coot.mtz_column_types_info_t; proxy of <Swig Object of type 'coot::mtz_column_types_info_t *' at 0x10a26d200> >` |
| Scheme | `(get-mtz-columns "tutorial-modern.pdb")` | ran, returned `#<collectable-swig-pointer coot::mtz_column_types_info_t * 8154681c0>` |

### get_phi_cols

Python: `get_phi_cols(mtz_file_name)`  
Scheme: `(get-phi-cols mtz-file-name)`

Arguments: mtz_file_name (text). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_phi_cols("rnasa-1.8-all_refmac1.mtz")` | ran, returned `('/RNASE3GMP/COMPLEX/PHIC', '/RNASE3GMP/COMPLEX/PHIC_ALL', '/RNASE3GMP/COMPLEX/PHWT', '/RNASE3GMP/COMPLEX/PHDELWT', '/RN ...` |
| Scheme | `(get-phi-cols "rnasa-1.8-all_refmac1.mtz")` | ran, returned `#("/RNASE3GMP/COMPLEX/PHIC" "/RNASE3GMP/COMPLEX/PHIC_ALL" "/RNASE3GMP/COMPLEX/PHWT" "/RNASE3GMP/COMPLEX/PHDELWT" "/RNASE ...` |

Python and Scheme gave the same answer.

### get_r_free_cols

Python: `get_r_free_cols(mtz_file_name)`  
Scheme: `(get-r-free-cols mtz-file-name)`

Arguments: mtz_file_name (text). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_r_free_cols("rnasa-1.8-all_refmac1.mtz")` | ran, returned `('/HKL_base/HKL_base/FreeR_flag',)` |
| Scheme | `(get-r-free-cols "rnasa-1.8-all_refmac1.mtz")` | ran, returned `#("/HKL_base/HKL_base/FreeR_flag")` |

Python and Scheme gave the same answer.

### get_sigf_cols

Python: `get_sigf_cols(mtz_file_name)`  
Scheme: `(get-sigf-cols mtz-file-name)`

Arguments: mtz_file_name (text). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_sigf_cols("rnasa-1.8-all_refmac1.mtz")` | ran, returned `('/RNASE3GMP/COMPLEX/SIGFGMP18',)` |
| Scheme | `(get-sigf-cols "rnasa-1.8-all_refmac1.mtz")` | ran, returned `#("/RNASE3GMP/COMPLEX/SIGFGMP18")` |

Python and Scheme gave the same answer.

### get_weight_cols

Python: `get_weight_cols(mtz_file_name)`  
Scheme: `(get-weight-cols mtz-file-name)`

Arguments: mtz_file_name (text). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_weight_cols("rnasa-1.8-all_refmac1.mtz")` | ran, returned `('/RNASE3GMP/COMPLEX/FOM',)` |
| Scheme | `(get-weight-cols "rnasa-1.8-all_refmac1.mtz")` | ran, returned `#("/RNASE3GMP/COMPLEX/FOM")` |

Python and Scheme gave the same answer.

### manage_column_selector

Python: `manage_column_selector(filename)`  
Scheme: `(manage-column-selector filename)`

given a filename, try to read it as a data file

 We try as .phs and .cif files first

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `manage_column_selector("tutorial-modern.pdb")` | ran (no return value) |
| Scheme | `(manage-column-selector "tutorial-modern.pdb")` | ran (no return value) |

### my_combo_box_text_add_items

Python: `my_combo_box_text_add_items(combobox, labels, active_label_index)`  
Scheme: `(my-combo-box-text-add-items combobox labels active-label-index)`

Arguments: combobox (`GtkComboBox *`), labels (a list), active_label_index (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

