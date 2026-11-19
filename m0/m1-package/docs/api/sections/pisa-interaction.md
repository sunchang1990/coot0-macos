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
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

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
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### pisa_clear_interfaces

Python: `pisa_clear_interfaces()`  
Scheme: `(pisa-clear-interfaces)`

clear out and undisplay all pisa interface descriptions.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `pisa_clear_interfaces()` | not tried |
| Scheme | `(pisa-clear-interfaces)` | not tried |

### pisa_interaction

Python: `pisa_interaction(imol_1, imol_2)`  
Scheme: `(pisa-interaction imol-1 imol-2)`

return the molecule number of the interacting
 residues. Return -1 if no new model was created. Old, not very useful.

Arguments: imol_1 (a whole number), imol_2 (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `pisa_interaction(0, 0)` | not tried |
| Scheme | `(pisa-interaction 0 0)` | not tried |

### pisa-molecule-record-chain-id

Scheme: `(pisa-molecule-record-chain-id molecule-record-1)`

Arguments: molecule-record-1 (a list or value). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | (no automatic example) | not tried |

### pisa-molecule-record-residues

Scheme: `(pisa-molecule-record-residues molecule-record-1)`

internal function

Arguments: molecule-record-1 (a list or value). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | (no automatic example) | not tried |

