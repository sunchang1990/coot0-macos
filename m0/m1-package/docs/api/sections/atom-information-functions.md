# Atom Information functions

[Scripting reference](../README.md) > Atom Information functions (17 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### active_residue

Python: `active_residue()`  
Scheme: `(active-residue)`

Return a list of [imol, chain-id, resno, ins-code, atom-name,
alt-conf] for atom that is closest to the screen centre. If there
are multiple models with the same coordinates at the screen centre,
return the attributes of the atom in the highest number molecule
number.
return False if no active residue

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `active_residue_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `active_residue()` | ran, returned `[0, 'A', 42, '', ' CA ', '']` |
| Scheme | `(active-residue)` | ran, returned `(0 "A" 42 "" " CA " "")` |

### add_hydrogen_atoms_to_residue

Python: `add_hydrogen_atoms_to_residue(imol, chain_id, res_no, ins_code)`  
Scheme: `(add-hydrogen-atoms-to-residue imol chain-id res-no ins-code)`

add hydrogen atoms to the specified residue

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_hydrogen_atoms_to_residue(0, "A", 41, "")` | ran (no return value) |
| Scheme | `(add-hydrogen-atoms-to-residue 0 "A" 41 "")` | ran (no return value) |

### add_hydrogens_from_file

Python: `add_hydrogens_from_file(imol, pdb_with_Hs_file_name)`  
Scheme: `(add-hydrogens-from-file imol pdb-with-Hs-file-name)`

Add hydrogens to imol from the given pdb file

Arguments: imol (a whole number), pdb_with_Hs_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_hydrogens_from_file(0, "tutorial-modern.pdb")` | ran (no return value) |
| Scheme | `(add-hydrogens-from-file 0 "tutorial-modern.pdb")` | ran (no return value) |

### add_molecule

Python: `add_molecule(molecule_expression, name)`  
Scheme: `(add-molecule molecule-expression name)`

return a molecule number, -1 on error

Arguments: molecule_expression (a list or value), name (text). Returns: a whole number.
Also available in Python as `add_molecule_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### atom_info_string

Python: `atom_info_string(imol, chain_id, resno, ins_code, atname, altconf)`  
Scheme: `(atom-info-string imol chain-id resno ins-code atname altconf)`

output atom info in a python list for use in scripting:
in this format [occ, temp_factor, element, x, y, z]. Return empty
list if atom not found.

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), atname (text), altconf (text). Returns: a value (see the result of the example).
Also available in Python as `atom_info_string_py`.
Also available in Scheme as `atom-info-string-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `atom_info_string(0, "A", 41, "", " CA ", "")` | ran, returned `[1.0, 14.8, ' C', 47.072, 10.589, 17.411]` |
| Scheme | `(atom-info-string 0 "A" 41 "" " CA " "")` | ran, returned `(1.0 14.8 " C" 47.072 10.589 17.411)` |

### chain_fragments

Python: `chain_fragments(imol, screen_output_also)`  
Scheme: `(chain-fragments imol screen-output-also)`

Arguments: imol (a whole number), screen_output_also (a whole number). Returns: a value (see the result of the example).
Also available in Python as `chain_fragments_py`.
Also available in Scheme as `chain-fragments-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `chain_fragments(0, 1)` | ran, returned `False` |
| Scheme | `(chain-fragments 0 1)` | ran, returned `#f` |

### clear_and_update_molecule

Python: `clear_and_update_molecule(molecule_number, molecule_expression)`  
Scheme: `(clear-and-update-molecule molecule-number molecule-expression)`

And going the other way, given an python-expression, update
molecule_number by the given molecule. Clear what's currently
there first though.

Arguments: molecule_number (a whole number), molecule_expression (a list or value). Returns: a whole number.
Also available in Python as `clear_and_update_molecule_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### closest_atom

Python: `closest_atom(imol)`  
Scheme: `(closest-atom imol)`

return closest atom in imolth molecule
Return a list of [imol, chain-id, resno, ins-code, atom-name,
alt-conf, [x, y, z]] for atom that is closest to the screen
centre in the given molecule (unlike active-residue, no account is
taken of the displayed state of the molecule). If there is no
atom, or if imol is not a valid model molecule, return False.

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `closest_atom_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `closest_atom(0)` | ran, returned `[0, 'A', 42, '', ' CA ', '', 44.346, 10.357, 15.014]` |
| Scheme | `(closest-atom 0)` | ran, returned `(0 "A" 42 "" " CA " "" 44.346 10.357 15.014)` |

### hydrogenate_region

Python: `hydrogenate_region(radius)`  
Scheme: `(hydrogenate-region radius)`

find the active residue, find the near residues (within radius)
create a new molecule, run reduce on that, import hydrogens from
the result and apply them to the molecule of the active residue.

Arguments: radius (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `hydrogenate_region(5.0)` | ran (no return value) |
| Scheme | `(hydrogenate-region 5.0)` | not tried |

### molecule_to_pdb_string_py

Python: `molecule_to_pdb_string_py(imol)`  
Scheme: `(molecule-to-pdb-string-scm imol)`

Return the molecule as a PDB string

Arguments: imol (a whole number). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `molecule_to_pdb_string_py(0)` | not tried |
| Scheme | `(molecule-to-pdb-string-scm 0)` | not tried |

### residue_centre_from_spec

Python: `residue_centre_from_spec(imol, spec_py)`

the expanded form of this is in c-interface.h

Arguments: imol (a whole number), spec_py (a list or value). Returns: a value (see the result of the example).
Also available in Python as `residue_centre_from_spec_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_centre_from_spec(0, ["A", 41, ""])` | not tried |

### residue_info

Python: `residue_info(imol, chain_id, resno, ins_code)`  
Scheme: `(residue-info imol chain-id resno ins-code)`

Return a list of atom info for each atom in the specified residue:
output is like this:
[
 [[atom-name,alt-conf]
 [occ,temp_fact,element]
 [x,y,z]]]

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text). Returns: a value (see the result of the example).
Also available in Python as `residue_info_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_info(0, "A", 41, "")` | not tried |
| Scheme | `(residue-info 0 "A" 41 "")` | not tried |

### residue_name

Python: `residue_name(imol, chain_id, resno, ins_code)`  
Scheme: `(residue-name imol chain-id resno ins-code)`

return the residue name of the specified residue

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_name(0, "A", 41, "")` | not tried |
| Scheme | `(residue-name 0 "A" 41 "")` | not tried |

### residues_near_residue

Python: `residues_near_residue(imol, residue_in, radius)`  
Scheme: `(residues-near-residue imol residue-in-scm radius)`

Return residue specs for residues that have atoms that are
closer than radius Angstroems to any atom in the residue
specified by residue_in.

Arguments: imol (a whole number), residue_in (a list or value), radius (a number). Returns: a value (see the result of the example).
Also available in Python as `residues_near_residue_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residues_near_residue(0, ["A", 41, ""], 5.0)` | not tried |
| Scheme | `(residues-near-residue 0 (list "A" 41 "") 5.0)` | not tried |

### resname_from_serial_number

Python: `resname_from_serial_number(imol, chain_id, serial_num)`  
Scheme: `(resname-from-serial-number imol chain-id serial-num)`

return the rename from a residue serial number

 Returns blank ("") on failure.

Arguments: imol (a whole number), chain_id (text), serial_num (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `resname_from_serial_number(0, "A", 1)` | not tried |
| Scheme | `(resname-from-serial-number 0 "A" 1)` | not tried |

### serial_number_from_residue_specs

Python: `serial_number_from_residue_specs(imol, chain_id, res_no, ins_code)`  
Scheme: `(serial-number-from-residue-specs imol chain-id res-no ins-code)`

return the serial number of the specified residue
Returns -1 on failure to find the residue

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `serial_number_from_residue_specs(0, "A", 41, "")` | not tried |
| Scheme | `(serial-number-from-residue-specs 0 "A" 41 "")` | not tried |

### set_b_factor_residues

Python: `set_b_factor_residues(imol, residue_specs_b_value_tuple_list_py)`

Arguments: imol (a whole number), residue_specs_b_value_tuple_list_py (a list or value). Returns: nothing.
Also available in Python as `set_b_factor_residues_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_b_factor_residues(0, ["A", 41, ""])` | not tried |

