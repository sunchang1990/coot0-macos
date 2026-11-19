# SBase interface

[Scripting reference](../README.md) > SBase interface (5 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_linked_residue

Python: `add_linked_residue(imol, chain_id, resno, ins_code, new_residue_comp_id, link_type, mode)`  
Scheme: `(add-linked-residue imol chain-id resno ins-code new-residue-comp-id link-type mode)`

add a linked residue based purely on dictionary template.
 For addition of NAG to ASNs typically.

 This doesn't work with residues with alt confs.

 Link type is the refmac dictionary link type (e.g. "ASN-NAG").

 return success status (0 = fail).

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), new_residue_comp_id (text), link_type (text), mode (a whole number). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_linked_residue(0, "A", 41, "", "hello", "hello", 1)` | ran, returned `False` |
| Scheme | `(add-linked-residue 0 "A" 41 "" "hello" "hello" 1)` | ran, returned `#f` |

### get_ccp4srs_monomer_and_dictionary

Python: `get_ccp4srs_monomer_and_dictionary(comp_id)`  
Scheme: `(get-ccp4srs-monomer-and-dictionary comp-id)`

return the new molecule number of the monomer.

The monomer will have chainid "A" and residue number 1.

Return -1 on failure to get monomer.

Arguments: comp_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_ccp4srs_monomer_and_dictionary("ALA")` | ran, returned `-1` |
| Scheme | `(get-ccp4srs-monomer-and-dictionary "ALA")` | ran, returned `-1` |

### get_sbase_monomer

Python: `get_sbase_monomer(comp_id)`  
Scheme: `(get-sbase-monomer comp-id)`

same as above but using old name for back-compatibility

Arguments: comp_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_sbase_monomer("ALA")` | ran, returned `-1` |
| Scheme | `(get-sbase-monomer "ALA")` | ran, returned `-1` |

### matching_compound_names_from_sbase

Python: `matching_compound_names_from_sbase(compound_name_fragment)`  
Scheme: `(matching-compound-names-from-sbase compound-name-fragment)`

return a list of compoundIDs of in SBase of which the
 given string is a substring of the compound name

Arguments: compound_name_fragment (text). Returns: a value (see the result of the example).
Also available in Python as `matching_compound_names_from_sbase_py`.
Also available in Scheme as `matching-compound-names-from-sbase-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `matching_compound_names_from_sbase("my-name")` | not tried |
| Scheme | `(matching-compound-names-from-sbase "my-name")` | not tried |

### set_add_linked_residue_do_fit_and_refine

Python: `set_add_linked_residue_do_fit_and_refine(state)`  
Scheme: `(set-add-linked-residue-do-fit-and-refine state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_linked_residue_do_fit_and_refine(1)` | not tried |
| Scheme | `(set-add-linked-residue-do-fit-and-refine 1)` | not tried |

