# FLE-View

[Scripting reference](../README.md) > FLE-View (9 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### fle_view_internal

Python: `fle_view_internal(imol, chain_id, res_no, ins_code, imol_ligand_fragment, prodrg_output_flat_mol_file_name, prodrg_output_flat_pdb_file_name, prodrg_output_3d_pdb_file_name, prodrg_output_dict_cif_file_name)`  
Scheme: `(fle-view-internal imol chain-id res-no ins-code imol-ligand-fragment prodrg-output-flat-mol-file-name prodrg-output-flat-pdb-file-name prodrg-output-3d-pdb-file-name prodrg-output-dict-cif-file-name)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), imol_ligand_fragment (a whole number), prodrg_output_flat_mol_file_name (text), prodrg_output_flat_pdb_file_name (text), prodrg_output_3d_pdb_file_name (text), prodrg_output_dict_cif_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fle_view_internal(0, "A", 41, "", 0, "tutorial-modern.pdb", "tutorial-modern.pdb", "tutorial-modern.pdb", "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(fle-view-internal 0 "A" 41 "" 0 "tutorial-modern.pdb" "tutorial-modern.pdb" "tutorial-modern.pdb" "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

### fle_view_internal_to_png

Python: `fle_view_internal_to_png(imol, chain_id, res_no, ins_code, imol_ligand_fragment, prodrg_output_flat_mol_file_name, prodrg_output_flat_pdb_file_name, prodrg_output_3d_pdb_file_name, prodrg_output_dict_cif_file_name, output_to_png_file_flag, png_file_name)`  
Scheme: `(fle-view-internal-to-png imol chain-id res-no ins-code imol-ligand-fragment prodrg-output-flat-mol-file-name prodrg-output-flat-pdb-file-name prodrg-output-3d-pdb-file-name prodrg-output-dict-cif-file-name output-to-png-file-flag png-file-name)`

for command-line operation

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), imol_ligand_fragment (a whole number), prodrg_output_flat_mol_file_name (text), prodrg_output_flat_pdb_file_name (text), prodrg_output_3d_pdb_file_name (text), prodrg_output_dict_cif_file_name (text), output_to_png_file_flag (a whole number), png_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fle_view_internal_to_png(0, "A", 41, "", 0, "tutorial-modern.pdb", "tutorial-modern.pdb", "tutorial-modern.pdb", "tutorial-modern.pdb", 1, "tutorial-modern.pdb")` | not run: needs PRODRG output files (flat mol/pdb, 3d pdb, dictionary) from an external program |
| Scheme | `(fle-view-internal-to-png 0 "A" 41 "" 0 "tutorial-modern.pdb" "tutorial-modern.pdb" "tutorial-modern.pdb" "tutorial-modern.pdb" 1 "tutorial-modern.pdb")` | not run: needs PRODRG output files (flat mol/pdb, 3d pdb, dictionary) from an external program |

Example written and checked by hand on the test data. Expected: draws the 2D ligand environment (FLEV) from PRODRG output files into a PNG.

### fle_view_set_h_bond_dist_max

Python: `fle_view_set_h_bond_dist_max(h_bond_dist_max)`  
Scheme: `(fle-view-set-h-bond-dist-max h-bond-dist-max)`

set the maximum considered hydrogen bond distance

default 3.9 A.

Arguments: h_bond_dist_max (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fle_view_set_h_bond_dist_max(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(fle-view-set-h-bond-dist-max 1.0)` | ran (no return value, nothing visible changed) |

### fle_view_set_water_dist_max

Python: `fle_view_set_water_dist_max(dist_max)`  
Scheme: `(fle-view-set-water-dist-max dist-max)`

set the maximum considered distance to water

default 3.25 A.

Arguments: dist_max (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fle_view_set_water_dist_max(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(fle-view-set-water-dist-max 1.0)` | ran (no return value, nothing visible changed) |

### fle_view_with_rdkit

Python: `fle_view_with_rdkit(imol, chain_id, res_no, ins_code, residues_near_radius)`  
Scheme: `(fle-view-with-rdkit imol chain-id res-no ins-code residues-near-radius)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), residues_near_radius (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fle_view_with_rdkit(0, "A", 41, "", 5.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(fle-view-with-rdkit 0 "A" 41 "" 5.0)` | ran (no return value, nothing visible changed) |

### fle_view_with_rdkit_internal

Python: `fle_view_with_rdkit_internal(imol, chain_id, res_no, ins_code, residues_near_radius, file_format, file_name)`  
Scheme: `(fle-view-with-rdkit-internal imol chain-id res-no ins-code residues-near-radius file-format file-name)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), residues_near_radius (a number), file_format (text), file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fle_view_with_rdkit_internal(0, "A", 41, "", 5.0, "tutorial-modern.pdb", "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(fle-view-with-rdkit-internal 0 "A" 41 "" 5.0 "tutorial-modern.pdb" "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

### fle_view_with_rdkit_to_png

Python: `fle_view_with_rdkit_to_png(imol, chain_id, res_no, ins_code, residues_near_radius, png_file_name)`  
Scheme: `(fle-view-with-rdkit-to-png imol chain-id res-no ins-code residues-near-radius png-file-name)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), residues_near_radius (a number), png_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `read_cif_dictionary("NAG.cif")`, then `fle_view_with_rdkit_to_png(read_pdb("nag_only.pdb"), "A", 1, "", 4.0, "nag-fle.png")` | ran (no return value); changed: new molecule 3 (model, nag_only.pdb); rotation centre moved 44.4 A to (-0.0, -0.0, -0.0); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | first `(read-cif-dictionary "NAG.cif")`, then `(fle-view-with-rdkit-to-png (read-pdb "nag_only.pdb") "A" 1 "" 4.0 "nag-fle.png")` | ran (no return value); changed: new molecule 3 (model, nag_only.pdb); rotation centre moved 44.4 A to (-0.0, -0.0, -0.0); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: writes a 2D ligand-environment picture of NAG A1 (residues within 4 A) to nag-fle.png.

### fle_view_with_rdkit_to_svg

Python: `fle_view_with_rdkit_to_svg(imol, chain_id, res_no, ins_code, residues_near_radius, svg_file_name)`  
Scheme: `(fle-view-with-rdkit-to-svg imol chain-id res-no ins-code residues-near-radius svg-file-name)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), residues_near_radius (a number), svg_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fle_view_with_rdkit_to_svg(0, "A", 41, "", 5.0, "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(fle-view-with-rdkit-to-svg 0 "A" 41 "" 5.0 "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

### sprout_hydrogens

Python: `sprout_hydrogens(imol, chain_id, res_no, ins_code)`  
Scheme: `(sprout-hydrogens imol chain-id res-no ins-code)`

Add hydrogens to specificied residue

Returns success status.

use RDKit for enterprise version

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `read_cif_dictionary("NAG.cif")`, then `imol_nag = read_pdb("nag_only.pdb")`, then `delete_hydrogens(imol_nag)`, then `sprout_hydrogens(imol_nag, "A", 1, "")` | ran, returned `1`; changed: molecule 3: atoms of 1 residue(s) (A1) |
| Scheme | first `(read-cif-dictionary "NAG.cif")`, then `(define imol-nag (read-pdb "nag_only.pdb"))`, then `(delete-hydrogens imol-nag)`, then `(sprout-hydrogens imol-nag "A" 1 "")` | ran, returned `1`; changed: molecule 3: atoms of 1 residue(s) (A1) |

Example written and checked by hand on the test data. Expected: returns 1 and adds the dictionary's hydrogens to the residue (needs a dictionary; the residue must have no hydrogens yet).

Note: On a protein residue (0 "A" 41) and on a residue that already has hydrogens it returns 0 (RDKit add_hydrogens refuses ligands with some H; the info_dialog message is invisible headless).

Python and Scheme gave the same answer.

