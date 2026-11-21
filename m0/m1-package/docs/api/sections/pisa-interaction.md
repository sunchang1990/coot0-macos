# PISA Interaction

[Scripting reference](../README.md) > PISA Interaction (6 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_pisa_interface_bond

Python: `add_pisa_interface_bond(imol_1, imol_2, pisa_bond_py, interface_number)`  
Scheme: `(add-pisa-interface-bond-scm imol-1 imol-2 pisa-bond-scm interface-number)`

PyObject *pisa_molecule_record_chain_id_py(PyObject *molecule_record_1);

Arguments: imol_1 (a whole number), imol_2 (a whole number), pisa_bond_py (a list or value), interface_number (a whole number). Returns: nothing.
Also available in Python as `add_pisa_interface_bond_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `imol_a = new_molecule_by_atom_selection(0, "//A")`, then `imol_b = new_molecule_by_atom_selection(0, "//B")`, then `add_pisa_interface_bond(imol_a, imol_b, ["h-bonds", ["A", 41, "", " OE1", ""], ["B", 41, "", " OE1", ""]], 1)` | ran (no return value, nothing visible changed) |
| Scheme | first `(define imol-a (new-molecule-by-atom-selection 0 "//A"))`, then `(define imol-b (new-molecule-by-atom-selection 0 "//B"))`, then `(add-pisa-interface-bond-scm imol-a imol-b (list 'salt-bridges (list "A" 41 "" " OE1" "") (list "B" 41 "" " OE1" "")) 1)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: draws a bond of the given type between the two atoms as a generic object for interface 1 (bond type is a string in Python, a symbol in Scheme).

### handle_pisa_interfaces

Python: `handle_pisa_interfaces(interfaces_description_py)`  
Scheme: `(handle-pisa-interfaces interfaces-description-scm)`

the scripting interface, called from parsing the PISA XML
 interface description

 An interface_description_scm is a record detailing the interface.
 A record contains the bsa, asa, and 2 molecule records. Molecule
 records contain list of residue records. The interface (dots) is
 be made from these lists of residue records. Note of course that
 imol_2 (or 1) can be a symmetry copy of (part of) mol_1 (or 2).

 Return the dot indexes (currently -1)

Arguments: interfaces_description_py (a list or value). Returns: a value (see the result of the example).
Also available in Python as `handle_pisa_interfaces_py`.
Also available in Scheme as `handle-pisa-interfaces-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_pisa_interfaces([])` | ran, returned `-1` |
| Scheme | `(handle-pisa-interfaces (list))` | ran, returned `-1` |

Example written and checked by hand on the test data. Expected: internal: called by the PISA XML parser with the interface records; an empty list returns -1.

Note: a real description is a nested record list made by parse_pisa_xml.py (molecule pairs, bonds, areas) and ends in a tree-view window; only the empty case was run

Python and Scheme gave the same answer.

### pisa_clear_interfaces

Python: `pisa_clear_interfaces()`  
Scheme: `(pisa-clear-interfaces)`

clear out and undisplay all pisa interface descriptions.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `pisa_clear_interfaces()` | ran (no return value, nothing visible changed) |
| Scheme | `(pisa-clear-interfaces)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: clears and undisplays all PISA interface objects (nothing to clear in a fresh Coot).

### pisa_interaction

Python: `pisa_interaction(imol_1, imol_2)`  
Scheme: `(pisa-interaction imol-1 imol-2)`

return the molecule number of the interacting
 residues. Return -1 if no new model was created. Old, not very useful.

Arguments: imol_1 (a whole number), imol_2 (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `imol_a = new_molecule_by_atom_selection(0, "//A")`, then `imol_b = new_molecule_by_atom_selection(0, "//B")`, then `pisa_interaction(imol_a, imol_b)` | ran, returned `5`; changed: new molecule 5 (model, interacting residues from 3); new molecule 6 (model, interacting residues from 4); first_small_coords_imol(): -1 -> 5; graphics_n_molecules(): 5 -> 7 |
| Scheme | first `(define imol-a (new-molecule-by-atom-selection 0 "//A"))`, then `(define imol-b (new-molecule-by-atom-selection 0 "//B"))`, then `(pisa-interaction imol-a imol-b)` | ran, returned `5`; changed: new molecule 5 (model, interacting residues from 3); new molecule 6 (model, interacting residues from 4); first_small_coords_imol(): -1 -> 5; graphics_n_molecules(): 5 -> 7 |

Example written and checked by hand on the test data. Expected: makes two new molecules with the residues of each molecule within 4 A of the other; returns the first new molecule number (-1 if none).

Python and Scheme gave the same answer.

### pisa-molecule-record-chain-id

Scheme: `(pisa-molecule-record-chain-id molecule-record-1)`

Arguments: molecule-record-1 (a list or value). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | first `(define rt (make-record-type 'pisa-molecule '(chain-id residues)))`, then `(define rec ((record-constructor rt) "A" (list (list "A" 41 ""))))`, then `(pisa-molecule-record-chain-id rec)` | ran, returned `"A"` |

Example written and checked by hand on the test data. Expected: returns the chain-id field of a PISA molecule record (Scheme only, internal).

### pisa-molecule-record-residues

Scheme: `(pisa-molecule-record-residues molecule-record-1)`

internal function

Arguments: molecule-record-1 (a list or value). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | first `(define rt (make-record-type 'pisa-molecule '(chain-id residues)))`, then `(define rec ((record-constructor rt) "A" (list (list "A" 41 ""))))`, then `(pisa-molecule-record-residues rec)` | ran, returned `(("A" 41 ""))` |

Example written and checked by hand on the test data. Expected: returns the residues field of a PISA molecule record (Scheme only, internal).

