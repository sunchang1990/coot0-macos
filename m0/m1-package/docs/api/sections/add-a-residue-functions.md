# Add A Residue Functions

[Scripting reference](../README.md) > Add A Residue Functions (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_residue_with_atoms_py

Python: `add_residue_with_atoms_py(imol, residue_spec, res_name, list_of_atoms)`

add a residue with atoms in scripting

 Returns the number of atoms added

Arguments: imol (a whole number), residue_spec (a list or value), res_name (text), list_of_atoms (a list or value). Returns: a whole number.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_residue_with_atoms_py(0, ["A", 200, ""], "HOH", [[[" O  ", ""], [1.0, 20.0, " O", ""], [10.0, 20.0, 30.0]]])` | ran, returned `0`; changed: molecule 0: added 1 residue(s) (A200); n_atoms(0): 1465 -> 1466; n_residues(0): 189 -> 190 |

Example written and checked by hand on the test data. Expected: adds residue A200 (HOH, one O atom) to molecule 0; documented to return the number of atoms added (1).

Note: Returns 0 although the atom IS added: molecule_class_info_t::add_residue_with_atoms never updates r_added (likely upstream bug). Atom format: [[name, altconf], [occ, B, element, segid], [x, y, z]].

