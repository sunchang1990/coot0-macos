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

Python and Scheme gave the same answer.

### add_hydrogen_atoms_to_residue

Python: `add_hydrogen_atoms_to_residue(imol, chain_id, res_no, ins_code)`  
Scheme: `(add-hydrogen-atoms-to-residue imol chain-id res-no ins-code)`

add hydrogen atoms to the specified residue

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_hydrogen_atoms_to_residue(0, "A", 41, "")` | ran (no return value); changed: molecule 0: atoms of 1 residue(s) (A41); n_atoms(0): 1465 -> 1471 |
| Scheme | `(add-hydrogen-atoms-to-residue 0 "A" 41 "")` | ran (no return value); changed: molecule 0: atoms of 1 residue(s) (A41); n_atoms(0): 1465 -> 1471 |

### add_hydrogens_from_file

Python: `add_hydrogens_from_file(imol, pdb_with_Hs_file_name)`  
Scheme: `(add-hydrogens-from-file imol pdb-with-Hs-file-name)`

Add hydrogens to imol from the given pdb file

Arguments: imol (a whole number), pdb_with_Hs_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_hydrogens_from_file(0, "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(add-hydrogens-from-file 0 "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

### add_molecule

Python: `add_molecule(molecule_expression, name)`  
Scheme: `(add-molecule molecule-expression name)`

return a molecule number, -1 on error

Arguments: molecule_expression (a list or value), name (text). Returns: a whole number.
Also available in Python as `add_molecule_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_molecule([[[ch[0], [[r[0], r[1], r[2], [a[:3] for a in r[3]]] for r in ch[1]]] for ch in m] for m in python_representation(0)], "copy of molecule 0")` | ran, returned `3`; changed: new molecule 3 (model, copy of molecule 0); graphics_n_molecules(): 3 -> 4 |
| Scheme | `(add-molecule (scheme-representation 0) "copy of molecule 0")` | ran, returned `3`; changed: new molecule 3 (model, copy of molecule 0); graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the new molecule number; a model molecule with the same atoms as molecule 0 appears.

Note: python_representation() atoms carry a 4th element (atom index) that add_molecule rejects ('bad atom expression'): add_molecule(python_representation(0), ...) returns a molecule number but the molecule is EMPTY/invalid. The example strips the 4th element (a[:3]). Scheme round-trips directly. Likely bug (Python representation not compatible with its reader).

Python and Scheme gave the same answer.

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

Python and Scheme gave the same answer.

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

Example written and checked by hand on the test data. Expected: should return the chain fragments of molecule 0.

Note: Both chain_fragments_py and chain_fragments_scm compute the fragments but never fill the return value: always False/#f (stub in 0.9.8.96).

Python and Scheme gave the same answer.

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
| Python | `clear_and_update_molecule(0, [[[c[0], [[r[0], r[1], r[2], [a[:3] for a in r[3]]] for r in c[1]]] for c in python_representation(0)[0] if c[0] == "A"]])` | ran, returned `1`; changed: molecule 0: deleted 96 residue(s) (B1, B2, B3, B4 ...); n_atoms(0): 1465 -> 720; n_chains(0): 2 -> 1; n_residues(0): 189 -> 93 |
| Scheme | `(clear-and-update-molecule 0 (list (list (car (car (scheme-representation 0))))))` | ran, returned `1`; changed: molecule 0: deleted 96 residue(s) (B1, B2, B3, B4 ...); first_molecule_with_symmetry_displayed(): 0 -> -1; get_symmetry(0): ['x,y,z', '-x+1/2,-y,z+1/2', 'x+1/2,-y+1/2,-z', '-x,y+1/2,-z -> []; n_atoms(0): 1465 -> 720 ... |

Example written and checked by hand on the test data. Expected: returns 1 and molecule 0 is replaced by the given representation (here only chain A is kept).

Note: A malformed Python expression (e.g. residues as [[1,'','ALA'], atoms] or python_representation() atoms with the extra index) gives an empty model, still returns 1 and closes the molecule (is_valid_model_molecule -> 0). Python representation needs the a[:3] strip, see add_molecule.

Python and Scheme gave the same answer.

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

Python and Scheme gave the same answer.

### hydrogenate_region

Python: `hydrogenate_region(radius)`  
Scheme: `(hydrogenate-region radius)`

find the active residue, find the near residues (within radius)
create a new molecule, run reduce on that, import hydrogens from
the result and apply them to the molecule of the active residue.

Arguments: radius (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `hydrogenate_region(5.0)` | ran (no return value); changed: molecule 0: atoms of 10 residue(s) (A1, A39, A40, A41 ...); n_atoms(0): 1465 -> 1543 |
| Scheme | `(hydrogenate-region 5.0)` | ran (no return value); changed: molecule 0: atoms of 10 residue(s) (A1, A39, A40, A41 ...); n_atoms(0): 1465 -> 1543 |

### molecule_to_pdb_string_py

Python: `molecule_to_pdb_string_py(imol)`  
Scheme: `(molecule-to-pdb-string-scm imol)`

Return the molecule as a PDB string

Arguments: imol (a whole number). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `molecule_to_pdb_string_py(0)` | ran, returned `'HEADER    ----                                             \nCOMPND    ---                                              ...` |
| Scheme | `(molecule-to-pdb-string-scm 0)` | ran, returned `"HEADER    ----                                             \nCOMPND    ---                                              ...` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### residue_centre_from_spec

Python: `residue_centre_from_spec(imol, spec_py)`

the expanded form of this is in c-interface.h

Arguments: imol (a whole number), spec_py (a list or value). Returns: a value (see the result of the example).
Also available in Python as `residue_centre_from_spec_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_centre_from_spec(0, ["A", 41, ""])` | ran, returned `[48.17811111111111, 11.594, 17.793222222222226]` |

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
| Python | `residue_info(0, "A", 41, "")` | ran, returned `[[[' N  ', ''], [1.0, 13.57, ' N', ''], [46.374, 11.225, 18.462], 294], [[' CA ', ''], [1.0, 14.8, ' C', ''], [47.072, 1 ...` |
| Scheme | `(residue-info 0 "A" 41 "")` | ran, returned `(((" N  " "") (1.0 13.57 " N" "") (46.374 11.225 18.462)) ((" CA " "") (1.0 14.8 " C" "") (47.072 10.589 17.411)) ((" CB ...` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### residue_name

Python: `residue_name(imol, chain_id, resno, ins_code)`  
Scheme: `(residue-name imol chain-id resno ins-code)`

return the residue name of the specified residue

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_name(0, "A", 41, "")` | ran, returned `'GLU'` |
| Scheme | `(residue-name 0 "A" 41 "")` | ran, returned `"GLU"` |

Python and Scheme gave the same answer.

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
| Python | `residues_near_residue(0, ["A", 41, ""], 5.0)` | ran, returned `[['A', 42, ''], ['B', 61, ''], ['A', 39, ''], ['A', 40, ''], ['A', 43, ''], ['A', 37, ''], ['A', 86, ''], ['A', 44, '']]` |
| Scheme | `(residues-near-residue 0 (list "A" 41 "") 5.0)` | ran, returned `(("A" 44 "") ("A" 86 "") ("A" 37 "") ("A" 43 "") ("A" 40 "") ("A" 39 "") ("B" 61 "") ("A" 42 ""))` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### resname_from_serial_number

Python: `resname_from_serial_number(imol, chain_id, serial_num)`  
Scheme: `(resname-from-serial-number imol chain-id serial-num)`

return the rename from a residue serial number

 Returns blank ("") on failure.

Arguments: imol (a whole number), chain_id (text), serial_num (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `resname_from_serial_number(0, "A", 1)` | ran, returned `'VAL'` |
| Scheme | `(resname-from-serial-number 0 "A" 1)` | ran, returned `"VAL"` |

Python and Scheme gave the same answer.

### serial_number_from_residue_specs

Python: `serial_number_from_residue_specs(imol, chain_id, res_no, ins_code)`  
Scheme: `(serial-number-from-residue-specs imol chain-id res-no ins-code)`

return the serial number of the specified residue
Returns -1 on failure to find the residue

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `serial_number_from_residue_specs(0, "A", 41, "")` | ran, returned `40` |
| Scheme | `(serial-number-from-residue-specs 0 "A" 41 "")` | ran, returned `40` |

Python and Scheme gave the same answer.

### set_b_factor_residues

Python: `set_b_factor_residues(imol, residue_specs_b_value_tuple_list_py)`

Arguments: imol (a whole number), residue_specs_b_value_tuple_list_py (a list or value). Returns: nothing.
Also available in Python as `set_b_factor_residues_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_b_factor_residues(0, ["A", 41, ""])` | ran (no return value, nothing visible changed) |

