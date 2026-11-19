# Atom Selection Utilities

[Scripting reference](../README.md) > Atom Selection Utilities (18 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### atom_index

Python: `atom_index(imol, chain_id, iresno, atom_id)`  
Scheme: `(atom-index imol chain-id iresno atom-id)`

return -1 if atom not found.

Arguments: imol (a whole number), chain_id (text), iresno (a whole number), atom_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `atom_index(0, "A", 41, "hello")` | ran, returned `-1` |
| Scheme | `(atom-index 0 "A" 41 "hello")` | ran, returned `-1` |

### atom_index_first_atom_in_residue

Python: `atom_index_first_atom_in_residue(imol, chain_id, iresno, ins_code)`  
Scheme: `(atom-index-first-atom-in-residue imol chain-id iresno ins-code)`

index from a given residue to use with refine_zone(). Return -1 on failure

Arguments: imol (a whole number), chain_id (text), iresno (a whole number), ins_code (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `atom_index_first_atom_in_residue(0, "A", 41, "")` | ran, returned `294` |
| Scheme | `(atom-index-first-atom-in-residue 0 "A" 41 "")` | ran, returned `294` |

### atom_index_first_atom_in_residue_with_altconf

Python: `atom_index_first_atom_in_residue_with_altconf(imol, chain_id, iresno, ins_code, alt_conf)`  
Scheme: `(atom-index-first-atom-in-residue-with-altconf imol chain-id iresno ins-code alt-conf)`

For rotamers, we are given a residue spec (and altconf), we need
 the index of the first atom of this type, no atom name is given,
 hence we cannot use full_atom_spec_to_atom_index().

Arguments: imol (a whole number), chain_id (text), iresno (a whole number), ins_code (text), alt_conf (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `atom_index_first_atom_in_residue_with_altconf(0, "A", 41, "", "")` | ran, returned `294` |
| Scheme | `(atom-index-first-atom-in-residue-with-altconf 0 "A" 41 "" "")` | ran, returned `294` |

### atom_index_full

Python: `atom_index_full(imol, chain_id, iresno, inscode, atom_id, altconf)`  
Scheme: `(atom-index-full imol chain-id iresno inscode atom-id altconf)`

return -1 if atom not found.

Arguments: imol (a whole number), chain_id (text), iresno (a whole number), inscode (text), atom_id (text), altconf (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `atom_index_full(0, "A", 41, "", "hello", "")` | ran, returned `-1` |
| Scheme | `(atom-index-full 0 "A" 41 "" "hello" "")` | ran, returned `-1` |

### average_temperature_factor

Python: `average_temperature_factor(imol)`  
Scheme: `(average-temperature-factor imol)`

return the average temperature factor for the atoms in imol

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `average_temperature_factor(0)` | ran, returned `17.467004776000977` |
| Scheme | `(average-temperature-factor 0)` | ran, returned `17.467004776000977` |

### centre_of_mass_string

Python: `centre_of_mass_string(imol)`  
Scheme: `(centre-of-mass-string imol)`

Arguments: imol (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `centre_of_mass_string(0)` | ran, returned `'[41.53,8.73,12.87]'` |
| Scheme | `(centre-of-mass-string 0)` | ran, returned `"(41.53 8.73 12.87)"` |

### clear_pending_picks

Python: `clear_pending_picks()`  
Scheme: `(clear-pending-picks)`

clear pending picks (stop coot thinking that the user is about to pick an atom).

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_pending_picks()` | ran (no return value) |
| Scheme | `(clear-pending-picks)` | ran (no return value) |

### default_new_atoms_b_factor

Python: `default_new_atoms_b_factor()`  
Scheme: `(default-new-atoms-b-factor)`

return the default temperature factor for newly created atoms

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `default_new_atoms_b_factor()` | ran, returned `30.0` |
| Scheme | `(default-new-atoms-b-factor)` | ran, returned `30.0` |

### get_reset_b_factor_moved_atoms_state

Python: `get_reset_b_factor_moved_atoms_state()`  
Scheme: `(get-reset-b-factor-moved-atoms-state)`

return the state if temperature factors shoudl be reset for
 moved atoms

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_reset_b_factor_moved_atoms_state()` | ran, returned `0` |
| Scheme | `(get-reset-b-factor-moved-atoms-state)` | ran, returned `0` |

### median_temperature_factor

Python: `median_temperature_factor(imol)`  
Scheme: `(median-temperature-factor imol)`

return the median temperature factor for imol

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `median_temperature_factor(0)` | not tried |
| Scheme | `(median-temperature-factor 0)` | not tried |

### set_atom_attribute

Python: `set_atom_attribute(imol, chain_id, resno, ins_code, atom_name, alt_conf, attribute_name, val)`  
Scheme: `(set-atom-attribute imol chain-id resno ins-code atom-name alt-conf attribute-name val)`

set a numberical attibute to the atom with the given specifier.

Attributes can be "x", "y","z", "B", "occ" and the attribute val is a floating point number

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), atom_name (text), alt_conf (text), attribute_name (text), val (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_atom_attribute(0, "A", 41, "", " CA ", "", "my-name", 1.0)` | not tried |
| Scheme | `(set-atom-attribute 0 "A" 41 "" " CA " "" "my-name" 1.0)` | not tried |

### set_atom_attributes

Python: `set_atom_attributes(attribute_expression_list)`  
Scheme: `(set-atom-attributes attribute-expression-list)`

set lots of atom attributes at once by-passing the rebonding and redrawing of the above 2 functions

Arguments: attribute_expression_list (a list or value). Returns: a whole number.
Also available in Python as `set_atom_attributes_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

### set_atom_string_attribute

Python: `set_atom_string_attribute(imol, chain_id, resno, ins_code, atom_name, alt_conf, attribute_name, attribute_value)`  
Scheme: `(set-atom-string-attribute imol chain-id resno ins-code atom-name alt-conf attribute-name attribute-value)`

set a string attibute to the atom with the given specifier.

Attributes can be "atom-name", "alt-conf", "element" or "segid".

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), atom_name (text), alt_conf (text), attribute_name (text), attribute_value (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_atom_string_attribute(0, "A", 41, "", " CA ", "", "my-name", "hello")` | not tried |
| Scheme | `(set-atom-string-attribute 0 "A" 41 "" " CA " "" "my-name" "hello")` | not tried |

### set_default_temperature_factor_for_new_atoms

Python: `set_default_temperature_factor_for_new_atoms(new_b)`  
Scheme: `(set-default-temperature-factor-for-new-atoms new-b)`

set the default temperature factor for newly created atoms
 (initial default 20)

Arguments: new_b (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_default_temperature_factor_for_new_atoms(1.0)` | not tried |
| Scheme | `(set-default-temperature-factor-for-new-atoms 1.0)` | not tried |

### set_reset_b_factor_moved_atoms

Python: `set_reset_b_factor_moved_atoms(state)`  
Scheme: `(set-reset-b-factor-moved-atoms state)`

reset temperature factor for all moved atoms to the default
 for new atoms (usually 30)

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_reset_b_factor_moved_atoms(1)` | not tried |
| Scheme | `(set-reset-b-factor-moved-atoms 1)` | not tried |

### set_residue_name

Python: `set_residue_name(imol, chain_id, res_no, ins_code, new_residue_name)`  
Scheme: `(set-residue-name imol chain-id res-no ins-code new-residue-name)`

set the residue name of the specified residue

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), new_residue_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_residue_name(0, "A", 41, "", "my-name")` | not tried |
| Scheme | `(set-residue-name 0 "A" 41 "" "my-name")` | not tried |

### set-temperature-factors-for-atoms-in-residue-scm

Scheme: `(set-temperature-factors-for-atoms-in-residue-scm imol residue-spec-scm bf)`

Arguments: imol (a whole number), residue-spec-scm (a list or value), bf (a number). Returns: nothing.
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | `(set-temperature-factors-for-atoms-in-residue-scm 0 (list "A" 41 "") 20.0)` | not tried |

### standard_deviation_temperature_factor

Python: `standard_deviation_temperature_factor(imol)`  
Scheme: `(standard-deviation-temperature-factor imol)`

return the standard deviation of the atom temperature factors for imol

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `standard_deviation_temperature_factor(0)` | not tried |
| Scheme | `(standard-deviation-temperature-factor 0)` | not tried |

