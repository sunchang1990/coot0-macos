# Monomer

[Scripting reference](../README.md) > Monomer (14 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_non_auto_load_residue_name

Python: `add_non_auto_load_residue_name(s)`  
Scheme: `(add-non-auto-load-residue-name s)`

add residue name to the list of residue names that don't
 get auto-loaded from the Refmac dictionary.

Arguments: s (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_non_auto_load_residue_name("hello")` | ran (no return value) |
| Scheme | `(add-non-auto-load-residue-name "hello")` | ran (no return value) |

### auto_load_dictionary

Python: `auto_load_dictionary(comp_id)`  
Scheme: `(auto-load-dictionary comp-id)`

try to auto-load the dictionary for comp_id from the refmac monomer library.

 return 0 on failure.
 return 1 on successful auto-load.
 return 2 on already-read.

Arguments: comp_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `auto_load_dictionary("ALA")` | ran, returned `2` |
| Scheme | `(auto-load-dictionary "ALA")` | ran, returned `2` |

Python and Scheme gave the same answer.

### comp_id2name

Python: `comp_id2name(comp_id)`  
Scheme: `(comp-id->name comp-id)`

return the monomer name

 return python false if not found

Arguments: comp_id (text). Returns: a value (see the result of the example).
Also available in Python as `comp_id_to_name`, `comp_id_to_name_py`.
Also available in Scheme as `comp-id-to-name-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `comp_id2name("ALA")` | ran, returned `'ALANINE'` |
| Scheme | `(comp-id->name "ALA")` | ran, returned `"ALANINE"` |

Python and Scheme gave the same answer.

### get_monomer

Python: `get_monomer(comp_id)`  
Scheme: `(get-monomer comp-id)`

import libcheck monomer give the 3-letter code. 

Returns the new molecule number, if not -1 (error).

Arguments: comp_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_monomer("ALA")` | ran, returned `2` |
| Scheme | `(get-monomer "ALA")` | ran, returned `2` |

Python and Scheme gave the same answer.

### get_monomer_for_molecule

Python: `get_monomer_for_molecule(comp_id, imol)`  
Scheme: `(get-monomer-for-molecule comp-id imol)`

get the monomer for the given molecule

Arguments: comp_id (text), imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_monomer_for_molecule("ALA", 0)` | ran, returned `2` |
| Scheme | `(get-monomer-for-molecule "ALA" 0)` | ran, returned `2` |

Python and Scheme gave the same answer.

### get_monomer_for_molecule_by_index

Python: `get_monomer_for_molecule_by_index(dict_idx, imol_enc)`  
Scheme: `(get-monomer-for-molecule-by-index dict-idx imol-enc)`

Arguments: dict_idx (a whole number), imol_enc (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_monomer_for_molecule_by_index(1, 0)` | ran, returned `2` |
| Scheme | `(get-monomer-for-molecule-by-index 1 0)` | ran, returned `2` |

Python and Scheme gave the same answer.

### get_monomer_from_dictionary

Python: `get_monomer_from_dictionary(comp_id, idealised_flag)`  
Scheme: `(get-monomer-from-dictionary comp-id idealised-flag)`

Use the protein geometry dictionary to retrieve a set of
 coordinates quickly from cif data read in from the RCSB's Chemical
 Component Library. There are no restraints from this method
 though.

Arguments: comp_id (text), idealised_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_monomer_from_dictionary("ALA", 1)` | ran, returned `2` |
| Scheme | `(get-monomer-from-dictionary "ALA" 1)` | ran, returned `2` |

Python and Scheme gave the same answer.

### import_python_module

Python: `import_python_module(module_name, use_namespace)`  
Scheme: `(import-python-module module-name use-namespace)`

import python module

Arguments: module_name (text), use_namespace (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `import_python_module("my-name", 1)` | ran, returned `-1` |
| Scheme | `(import-python-module "my-name" 1)` | ran, returned `-1` |

Python and Scheme gave the same answer.

### matching_compound_names_from_dictionary

Python: `matching_compound_names_from_dictionary(compound_name_fragment, allow_minimal_descriptions_flag)`  
Scheme: `(matching-compound-names-from-dictionary compound-name-fragment allow-minimal-descriptions-flag)`

return a list of compoundIDs in the dictionary which the
 given string is a substring of the compound name

Arguments: compound_name_fragment (text), allow_minimal_descriptions_flag (a whole number). Returns: a value (see the result of the example).
Also available in Python as `matching_compound_names_from_dictionary_py`.
Also available in Scheme as `matching-compound-names-from-dictionary-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `matching_compound_names_from_dictionary("my-name", 1)` | ran, returned `[]` |
| Scheme | `(matching-compound-names-from-dictionary "my-name" 1)` | ran, returned `()` |

Python and Scheme gave the same answer.

### reload_dictionary

Python: `reload_dictionary(comp_id)`  
Scheme: `(reload-dictionary comp-id)`

as above, but dictionary is cleared and re-read if it already exists

Arguments: comp_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `reload_dictionary("ALA")` | ran, returned `1` |
| Scheme | `(reload-dictionary "ALA")` | ran, returned `1` |

Python and Scheme gave the same answer.

### remove_non_auto_load_residue_name

Python: `remove_non_auto_load_residue_name(s)`  
Scheme: `(remove-non-auto-load-residue-name s)`

remove residue name from the list of residue names that don't
 get auto-loaded from the Refmac dictionary.

Arguments: s (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_non_auto_load_residue_name("hello")` | ran (no return value) |
| Scheme | `(remove-non-auto-load-residue-name "hello")` | ran (no return value) |

### run_guile_script

Python: `run_guile_script(filename)`  
Scheme: `(run-guile-script filename)`

guile run script file

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_guile_script("tutorial-modern.pdb")` | not run: not run automatically (run: exits, uses the network, an external program, files or a screen) |
| Scheme | `(run-guile-script "tutorial-modern.pdb")` | not run: not run automatically (run: exits, uses the network, an external program, files or a screen) |

### run_python_script

Python: `run_python_script(filename)`  
Scheme: `(run-python-script filename)`

run python script file

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_python_script("tutorial-modern.pdb")` | not run: not run automatically (run: exits, uses the network, an external program, files or a screen) |
| Scheme | `(run-python-script "tutorial-modern.pdb")` | not run: not run automatically (run: exits, uses the network, an external program, files or a screen) |

### run_script

Python: `run_script(filename)`  
Scheme: `(run-script filename)`

run script file

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_script("tutorial-modern.pdb")` | not run: not run automatically (run: exits, uses the network, an external program, files or a screen) |
| Scheme | `(run-script "tutorial-modern.pdb")` | not run: not run automatically (run: exits, uses the network, an external program, files or a screen) |

