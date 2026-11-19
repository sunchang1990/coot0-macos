# Ligand Builder (Lidia)

[Scripting reference](../README.md) > Ligand Builder (Lidia) (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### residue_to_ligand_builder

Python: `residue_to_ligand_builder(imol, chain_id, resno, ins_code, weight_for_3d_distances)`  
Scheme: `(residue-to-ligand-builder imol chain-id resno ins-code weight-for-3d-distances)`

20140226: now we change things so that the interface functions always get generated,
 and what the function does depends on MAKE_ENHANCED_LIGAND_TOOLS
#ifdef MAKE_ENHANCED_LIGAND_TOOLS

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), weight_for_3d_distances (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_to_ligand_builder(0, "A", 41, "", 1.0)` | not tried |
| Scheme | `(residue-to-ligand-builder 0 "A" 41 "" 1.0)` | not tried |

### smiles_to_ligand_builder

Python: `smiles_to_ligand_builder(smiles_string)`  
Scheme: `(smiles-to-ligand-builder smiles-string)`

Arguments: smiles_string (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `smiles_to_ligand_builder("hello")` | not tried |
| Scheme | `(smiles-to-ligand-builder "hello")` | not tried |

