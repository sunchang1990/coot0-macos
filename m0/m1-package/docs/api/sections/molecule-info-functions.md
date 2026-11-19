# Molecule Info Functions

[Scripting reference](../README.md) > Molecule Info Functions (26 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_header_secondary_structure_info

Python: `add_header_secondary_structure_info(imol)`  
Scheme: `(add-header-secondary-structure-info imol)`

add secondary structure info to the
 internal representation of the model

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_header_secondary_structure_info(0)` | ran (no return value) |
| Scheme | `(add-header-secondary-structure-info 0)` | ran (no return value) |

### add_ligand_delete_residue_copy_molecule

Python: `add_ligand_delete_residue_copy_molecule(imol_ligand_new, chain_id_ligand_new, resno_ligand_new, imol_current, chain_id_ligand_current, resno_ligand_current)`  
Scheme: `(add-ligand-delete-residue-copy-molecule imol-ligand-new chain-id-ligand-new resno-ligand-new imol-current chain-id-ligand-current resno-ligand-current)`

Copy a molecule with addition of a ligand and a deletion of
 current ligand.

 This function is used when adding a new (modified) ligand to a
 structure. It creates a new molecule that is a copy of the current
 molecule except that the new ligand is added and the current
 ligand/residue is deleted.

Arguments: imol_ligand_new (a whole number), chain_id_ligand_new (text), resno_ligand_new (a whole number), imol_current (a whole number), chain_id_ligand_current (text), resno_ligand_current (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_ligand_delete_residue_copy_molecule(0, "B", 41, 0, "A", 41)` | ran, returned `2` |
| Scheme | `(add-ligand-delete-residue-copy-molecule 0 "B" 41 0 "A" 41)` | ran, returned `2` |

### chain_id

Python: `chain_id(imol, ichain)`  
Scheme: `(chain-id imol ichain)`

Arguments: imol (a whole number), ichain (a whole number). Returns: a value (see the result of the example).
Also available in Python as `chain_id_py`.
Also available in Scheme as `chain-id-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `chain_id(0, 1)` | ran, returned `'B'` |
| Scheme | `(chain-id 0 1)` | ran, returned `"B"` |

### chain_n_residues

Python: `chain_n_residues(chain_id, imol)`  
Scheme: `(chain-n-residues chain-id imol)`

the number of residues in chain chain_id and molecule number imol
 Returns the number of residues

Arguments: chain_id (text), imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `chain_n_residues("A", 0)` | ran, returned `93` |
| Scheme | `(chain-n-residues "A" 0)` | ran, returned `93` |

### copy_molecule

Python: `copy_molecule(imol)`  
Scheme: `(copy-molecule imol)`

copy molecule imol

Returns the new molecule number.
Return -1 on failure to copy molecule (out of range, or molecule is
closed)

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `copy_molecule(0)` | ran, returned `2` |
| Scheme | `(copy-molecule 0)` | ran, returned `2` |

### exchange_chain_ids_for_seg_ids

Python: `exchange_chain_ids_for_seg_ids(imol)`  
Scheme: `(exchange-chain-ids-for-seg-ids imol)`

Experimental interface for Ribosome People.

Ribosome People have many chains in their pdb file, they prefer segids
to chainids (chainids are only 1 character). But coot uses the
concept of chain ids and not seg-ids. mmdb allow us to use more than
one char in the chainid, so after we read in a pdb, let's replace the
chain ids with the segids. Will that help?

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `exchange_chain_ids_for_seg_ids(0)` | ran, returned `0` |
| Scheme | `(exchange-chain-ids-for-seg-ids 0)` | ran, returned `0` |

### insertion_code_from_serial_number

Python: `insertion_code_from_serial_number(imol, chain_id, serial_num)`  
Scheme: `(insertion-code-from-serial-number imol chain-id serial-num)`

the insertion code of the residue.

 Returns NULL (scheme False) on failure.

Arguments: imol (a whole number), chain_id (text), serial_num (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `insertion_code_from_serial_number(0, "A", 1)` | not tried |
| Scheme | `(insertion-code-from-serial-number 0 "A" 1)` | not tried |

### is_nucleotide_chain_p

Python: `is_nucleotide_chain_p(imol, chain_id)`  
Scheme: `(is-nucleotide-chain-p imol chain-id)`

is this a nucleic acid chain? [Raw function]

 This is a raw interface function, you should generally not use
 this, but instead use (is-nucleicacid-chain? imol chain-id)

 Returns -1 on error, 0 for no, 1 for is "a nucleicacid chain". We
 wouldn't want to be doing rotamer searches and the like on such a
 chain.

 This wraps the mmdb function isNucleotideChain().
 For completeness.

Arguments: imol (a whole number), chain_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `is_nucleotide_chain_p(0, "A")` | not tried |
| Scheme | `(is-nucleotide-chain-p 0 "A")` | not tried |

### is_protein_chain_p

Python: `is_protein_chain_p(imol, chain_id)`  
Scheme: `(is-protein-chain-p imol chain-id)`

is this a protein chain? [Raw function]

 This is a raw interface function, you should generally not use
 this, but instead use (is-protein-chain? imol chain-id)

 Returns -1 on error, 0 for no, 1 for is "a protein chain". We
 wouldn't want to be doing rotamer searches and the like on such a
 chain.

 This wraps the mmdb function isAminoacidChain().

Arguments: imol (a whole number), chain_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `is_protein_chain_p(0, "A")` | not tried |
| Scheme | `(is-protein-chain-p 0 "A")` | not tried |

### is_solvent_chain_p

Python: `is_solvent_chain_p(imol, chain_id)`  
Scheme: `(is-solvent-chain-p imol chain-id)`

is this a solvent chain? [Raw function]

 This is a raw interface function, you should generally not use
 this, but instead use (is-solvent-chain? imol chain-id)

 Returns -1 on error, 0 for no, 1 for is "a solvent chain". We
 wouldn't want to be doing rotamer searches and the like on such a
 chain.

 This wraps the mmdb function isSolventChain().

Arguments: imol (a whole number), chain_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `is_solvent_chain_p(0, "A")` | not tried |
| Scheme | `(is-solvent-chain-p 0 "A")` | not tried |

### model_composition_statistics_py

Python: `model_composition_statistics_py(imol)`  
Scheme: `(model-composition-statistics-scm imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `model_composition_statistics_py(0)` | not tried |
| Scheme | `(model-composition-statistics-scm 0)` | not tried |

### molecule_centre_internal

Python: `molecule_centre_internal(imol, iaxis)`  
Scheme: `(molecule-centre-internal imol iaxis)`

internal function for molecule centre

Returns status, less than -9999 is for failure (eg. bad imol);

Arguments: imol (a whole number), iaxis (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `molecule_centre_internal(0, 1)` | not tried |
| Scheme | `(molecule-centre-internal 0 1)` | not tried |

### n_atoms

Python: `n_atoms(imol)`  
Scheme: `(n-atoms imol)`

return the ATOMs of residues in the molecule,

return -1 if this is a map or closed. HETATMs are not counted.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `n_atoms(0)` | not tried |
| Scheme | `(n-atoms 0)` | not tried |

### n_chains

Python: `n_chains(imol)`  
Scheme: `(n-chains imol)`

number of chains in molecule number imol

 Returns the number of chains

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `n_chains(0)` | not tried |
| Scheme | `(n-chains 0)` | not tried |

### n_models

Python: `n_models(imol)`  
Scheme: `(n-models imol)`

return the number of models in molecule number imol

useful for NMR or other such multi-model molecules.

return the number of models or -1 if there was a problem with the
given molecule.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `n_models(0)` | not tried |
| Scheme | `(n-models 0)` | not tried |

### n_residues

Python: `n_residues(imol)`  
Scheme: `(n-residues imol)`

return the number of residues in the molecule,

return -1 if this is a map or closed.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `n_residues(0)` | not tried |
| Scheme | `(n-residues 0)` | not tried |

### print_header_secondary_structure_info

Python: `print_header_secondary_structure_info(imol)`  
Scheme: `(print-header-secondary-structure-info imol)`

simply print secondary structure info to the
 terminal/console. In future, this could/should return the info.

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `print_header_secondary_structure_info(0)` | not tried |
| Scheme | `(print-header-secondary-structure-info 0)` | not tried |

### python_representation_kk

Python: `python_representation_kk(imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `python_representation_kk(0)` | not tried |

### remarks

Python: `remarks(imol)`  
Scheme: `(remarks imol)`

return a list or python false

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `remarks_py`.
Also available in Scheme as `remarks-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remarks(0)` | not tried |
| Scheme | `(remarks 0)` | not tried |

### remarks_dialog

Python: `remarks_dialog(imol)`  
Scheme: `(remarks-dialog imol)`

a gui dialog showing remarks header info (for a model molecule).

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remarks_dialog(0)` | not tried |
| Scheme | `(remarks-dialog 0)` | not tried |

### residue_centre

Python: `residue_centre(imol, chain_id, resno, ins_code)`  
Scheme: `(residue-centre imol chain-id resno ins-code)`

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text). Returns: a value (see the result of the example).
Also available in Python as `residue_centre_py`.
Also available in Scheme as `residue-centre-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_centre(0, "A", 41, "")` | not tried |
| Scheme | `(residue-centre 0 "A" 41 "")` | not tried |

### seqnum_from_serial_number

Python: `seqnum_from_serial_number(imol, chain_id, serial_num)`  
Scheme: `(seqnum-from-serial-number imol chain-id serial-num)`

a residue seqnum (normal residue number) from a residue
 serial number

 Returns < -9999 on failure

Arguments: imol (a whole number), chain_id (text), serial_num (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `seqnum_from_serial_number(0, "A", 1)` | not tried |
| Scheme | `(seqnum-from-serial-number 0 "A" 1)` | not tried |

### show_remarks_browswer

Python: `show_remarks_browswer()`  
Scheme: `(show-remarks-browswer)`

show the remarks browser

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_remarks_browswer()` | not tried |
| Scheme | `(show-remarks-browswer)` | not tried |

### sort_chains

Python: `sort_chains(imol)`  
Scheme: `(sort-chains imol)`

sort the chain ids of the imol-th molecule in lexographical order

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `sort_chains(0)` | not tried |
| Scheme | `(sort-chains 0)` | not tried |

### sort_residues

Python: `sort_residues(imol)`  
Scheme: `(sort-residues imol)`

sort the residues of the imol-th molecule

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `sort_residues(0)` | not tried |
| Scheme | `(sort-residues 0)` | not tried |

### write_header_secondary_structure_info

Python: `write_header_secondary_structure_info(imol, file_name)`  
Scheme: `(write-header-secondary-structure-info imol file-name)`

Placeholder only.

 not documented, it doesn't work yet, because CalcSecStructure()
 creates SS type on the residues, it does not build and store
 CHelix, CStrand, CSheet records.

Arguments: imol (a whole number), file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_header_secondary_structure_info(0, "tutorial-modern.pdb")` | not tried |
| Scheme | `(write-header-secondary-structure-info 0 "tutorial-modern.pdb")` | not tried |

