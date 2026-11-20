# Get Sequence

[Scripting reference](../README.md) > Get Sequence (22 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### align_to_closest_chain

Python: `align_to_closest_chain(target_seq, match_fraction)`  
Scheme: `(align-to-closest-chain target-seq match-fraction)`

align sequence to closest chain (compare across all chains
 in all molecules).
Typically match_fraction is 0.95 or so.
Return the molecule number and chain id if successful, return -1 as the
molecule number if not.

Arguments: target_seq (text), match_fraction (a number). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `align_to_closest_chain("ACDEFGHIKLMNPQRSTVWY", 0.5)` | ran, returned `False` |
| Scheme | `(align-to-closest-chain "ACDEFGHIKLMNPQRSTVWY" 0.5)` | ran, returned `#f` |

Python and Scheme gave the same answer.

### decode_ints

Python: `decode_ints(i)`  
Scheme: `(decode-ints i)`

Arguments: i (a whole number). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `decode_ints(1)` | ran, returned `<Swig Object of type 'std::pair< int,int > *' at 0x10b8e1230>` |
| Scheme | `(decode-ints 1)` | ran, returned `#<collectable-swig-pointer std::pair< int,int > * bd70e7090>` |

### encode_ints

Python: `encode_ints(i1, i2)`  
Scheme: `(encode-ints i1 i2)`

encoding of ints
These functions are for storing the molecule number and (some other
number) as an int and used with GPOINTER_TO_INT and GINT_TO_POINTER.

Arguments: i1 (a whole number), i2 (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `encode_ints(1, 1)` | ran, returned `1001` |
| Scheme | `(encode-ints 1 1)` | ran, returned `1001` |

Python and Scheme gave the same answer.

### get_sequence_as_fasta_for_chain

Python: `get_sequence_as_fasta_for_chain(imol, chain_id)`  
Scheme: `(get-sequence-as-fasta-for-chain imol chain-id)`

get the sequence for chain_id in imol

Arguments: imol (a whole number), chain_id (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_sequence_as_fasta_for_chain(0, "A")` | ran, returned `'> tutorial-modern A\n\nDVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYG\nYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLID\ ...` |
| Scheme | `(get-sequence-as-fasta-for-chain 0 "A")` | ran, returned `"> tutorial-modern A\n\nDVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYG\nYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLID\ ...` |

Python and Scheme gave the same answer.

### graphics_to_phenix_geo_representation

Python: `graphics_to_phenix_geo_representation(imol, mode, g)`  
Scheme: `(graphics-to-phenix-geo-representation imol mode g)`

phenix GEO bonds representation

Arguments: imol (a whole number), mode (a whole number), g (`coot::phenix_geo_bonds`). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### key_sym_code

Python: `key_sym_code(po)`  
Scheme: `(key-sym-code s-scm)`

Arguments: po (a list or value). Returns: a whole number.
Also available in Python as `key_sym_code_py`.
Also available in Scheme as `key-sym-code-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### molecule_atom_overlaps

Python: `molecule_atom_overlaps(imol)`  
Scheme: `(molecule-atom-overlaps imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `molecule_atom_overlaps_py`.
Also available in Scheme as `molecule-atom-overlaps-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `molecule_atom_overlaps(0)` | ran, returned `[{'atom-1-spec': [-1, 'A', 2, '', ' CA ', ''], 'atom-2-spec': [-1, 'A', 89, '', ' CZ ', ''], 'overlap-volume': 7.4502435 ...` |
| Scheme | `(molecule-atom-overlaps 0)` | ran, returned `(((-1 "A" 2 "" " CA " "") (-1 "A" 89 "" " CZ " "") 1.7000000476837158 1.7000000476837158 7.450243542341931) ((-1 "A" 2 " ...` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### pathology_data

Python: `pathology_data(mtz_file_name, fp_col, sigfp_col)`

Arguments: mtz_file_name (text), fp_col (text), sigfp_col (text). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `pathology_data("rnasa-1.8-all_refmac1.mtz", "hello", "hello")` | ran, returned `False` |

### prodrg_import_function

Python: `prodrg_import_function(file_name, comp_id)`  
Scheme: `(prodrg-import-function file-name comp-id)`

import given mdl file into prodrg or other 3d generation program
the function passed to lbg, so that it calls it when a new
prodrg-in.mdl file has been made. We no longer have a timeout
function waiting for prodrg-in.mdl to be updated/written.

Arguments: file_name (text), comp_id (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `prodrg_import_function("tutorial-modern.pdb", "ALA")` | not run: not run automatically (prodrg: exits, uses the network, an external program, files or a screen) |
| Scheme | `(prodrg-import-function "tutorial-modern.pdb" "ALA")` | not run: not run automatically (prodrg: exits, uses the network, an external program, files or a screen) |

### py_symop_strings_to_space_group

Python: `py_symop_strings_to_space_group(symop_string_list)`

Arguments: symop_string_list (a list or value). Returns: `clipper::Spacegroup`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### py_to_residue_specs

Python: `py_to_residue_specs(s)`

Arguments: s (a list or value). Returns: a list.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### register_interesting_positions_list

Python: `register_interesting_positions_list(pos_list)`  
Scheme: `(register-interesting-positions-list-scm pos-list)`

Arguments: pos_list (a list or value). Returns: nothing.
Also available in Python as `register_interesting_positions_list_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### resolve_clashing_sidechains_by_deletion

Python: `resolve_clashing_sidechains_by_deletion(imol)`  
Scheme: `(resolve-clashing-sidechains-by-deletion imol)`

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `resolve_clashing_sidechains_by_deletion(0)` | ran (no return value) |
| Scheme | `(resolve-clashing-sidechains-by-deletion 0)` | ran (no return value) |

### resolve_clashing_sidechains_by_rebuilding

Python: `resolve_clashing_sidechains_by_rebuilding(imol)`  
Scheme: `(resolve-clashing-sidechains-by-rebuilding imol)`

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `resolve_clashing_sidechains_by_rebuilding(0)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(resolve-clashing-sidechains-by-rebuilding 0)` | stopped Coot when tried without a window (not checked with a window) |

### sbase_import_function

Python: `sbase_import_function(comp_id)`  
Scheme: `(sbase-import-function comp-id)`

import molecule from CCP4 SRS (or SBase, as it used to be called).
the function passed to lbg, so that it calls it when a new
SBase comp_id is required. We no longer have a timeout
function waiting for prodrg-in.mdl to be updated/written.

Arguments: comp_id (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `sbase_import_function("ALA")` | ran (no return value) |
| Scheme | `(sbase-import-function "ALA")` | ran (no return value) |

### scm-symop-strings-to-space-group

Scheme: `(scm-symop-strings-to-space-group symop-string-list)`

Arguments: symop-string-list (a list or value). Returns: `clipper::Spacegroup`.
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### scm-to-residue-specs

Scheme: `(scm-to-residue-specs s)`

Arguments: s (a list or value). Returns: a list.
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### set_python_draw_function

Python: `set_python_draw_function(command_string)`

client/server functions

Arguments: command_string (text). Returns: nothing.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_python_draw_function("hello")` | ran (no return value) |

### simple_text_dialog

Python: `simple_text_dialog(dialog_title, text, geom_x, geom_y)`  
Scheme: `(simple-text-dialog dialog-title text geom-x geom-y)`

make a simple text dialog.

Arguments: dialog_title (text), text (text), geom_x (a whole number), geom_y (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `simple_text_dialog("hello", "hello", 1, 1)` | ran (no return value) |
| Scheme | `(simple-text-dialog "hello" "hello" 1 1)` | ran (no return value) |

### spherical-density-overlap

Scheme: `(spherical-density-overlap i-scm j-scm)`

Arguments: i-scm (a list or value), j-scm (a list or value). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### store_keyed_user_name

Python: `store_keyed_user_name(key, user_name, passwd)`  
Scheme: `(store-keyed-user-name key user-name passwd)`

store username and password for the database.

Arguments: key (text), user_name (text), passwd (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `store_keyed_user_name("hello", "my-name", "hello")` | ran (no return value) |
| Scheme | `(store-keyed-user-name "hello" "my-name" "hello")` | ran (no return value) |

### write_sequence

Python: `write_sequence(imol, file_name)`  
Scheme: `(write-sequence imol file-name)`

write the sequence for imol as fasta

Arguments: imol (a whole number), file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_sequence(0, "tutorial-modern.pdb")` | ran (no return value) |
| Scheme | `(write-sequence 0 "tutorial-modern.pdb")` | ran (no return value) |

