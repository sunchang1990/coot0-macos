# Ligands

[Scripting reference](../README.md) > Ligands (36 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_dictionary_from_residue

Python: `add_dictionary_from_residue(imol, chain_id, res_no, ins_code)`  
Scheme: `(add-dictionary-from-residue imol chain-id res-no ins-code)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_dictionary_from_residue(0, "A", 41, "")` | ran (no return value, nothing visible changed) |
| Scheme | `(add-dictionary-from-residue 0 "A" 41 "")` | ran (no return value, nothing visible changed) |

### comprised_of_organic_set_p

Python: `comprised_of_organic_set_p(rn)`  
Scheme: `(comprised-of-organic-set-p rn)`

return False if unknown

Arguments: rn (text). Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `read_cif_dictionary("NAG.cif")`, then `comprised_of_organic_set_p("NAG")` | ran, returned `True` |
| Scheme | first `(read-cif-dictionary "NAG.cif")`, then `(comprised-of-organic-set-p "NAG")` | ran, returned `#t` |

Example written and checked by hand on the test data. Expected: True when the dictionary of that residue type has only organic-set elements (C, N, O, H, ...); False if unknown.

Python and Scheme gave the same answer.

### coot_add_hydrogen_atoms

Python: `coot_add_hydrogen_atoms(imol)`  
Scheme: `(coot-add-hydrogen-atoms imol)`

this is not a ligand function - it does not belong here.
 add Hydrogen atoms to the molecule

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_add_hydrogen_atoms(0)` | ran (no return value); changed: molecule 0: atoms of 188 residue(s) (A1, A2, A3, A4 ...); n_atoms(0): 1465 -> 2825 |
| Scheme | `(coot-add-hydrogen-atoms 0)` | ran (no return value); changed: molecule 0: atoms of 188 residue(s) (A1, A2, A3, A4 ...); n_atoms(0): 1465 -> 2825 |

### coot_all_atom_contact_dots

Python: `coot_all_atom_contact_dots(imol)`  
Scheme: `(coot-all-atom-contact-dots imol)`

all-atom contact dots. This is not the place for this declaration (not a ligand function)
 calculate all-atom contact dots
remove contact dots objects using the Generic Display Objects dialog

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_all_atom_contact_dots(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(coot-all-atom-contact-dots 0)` | ran (no return value, nothing visible changed) |

### coot_contact_dots_for_ligand

Python: `coot_contact_dots_for_ligand(imol, ligand_spec)`  
Scheme: `(coot-contact-dots-for-ligand-scm imol residue-spec-scm)`

Arguments: imol (a whole number), ligand_spec (a list or value). Returns: nothing.
Also available in Python as `coot_contact_dots_for_ligand`, `coot_contact_dots_for_ligand_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_contact_dots_for_ligand(0, ["A", 41, ""])` | ran (no return value, nothing visible changed) |
| Scheme | `(coot-contact-dots-for-ligand-scm 0 (list "A" 41 ""))` | ran (no return value, nothing visible changed) |

### coot_reduce

Python: `coot_reduce(imol)`  
Scheme: `(coot-reduce imol)`

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_reduce(0)` | not run: runs the external program reduce |
| Scheme | `(coot-reduce 0)` | not run: runs the external program reduce |

Example written and checked by hand on the test data. Expected: adds hydrogens to molecule 0 with reduce.

### display_residue_distortions

Python: `display_residue_distortions(imol, chain_id, res_no, ins_code)`  
Scheme: `(display-residue-distortions imol chain-id res-no ins-code)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `display_residue_distortions(0, "A", 41, "")` | ran (no return value, nothing visible changed) |
| Scheme | `(display-residue-distortions 0 "A" 41 "")` | ran (no return value, nothing visible changed) |

### display_residue_hydrogen_bond_atom_status_using_dictionary

Python: `display_residue_hydrogen_bond_atom_status_using_dictionary(imol, chain_id, res_no, ins_code)`  
Scheme: `(display-residue-hydrogen-bond-atom-status-using-dictionary imol chain-id res-no ins-code)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `display_residue_hydrogen_bond_atom_status_using_dictionary(0, "A", 41, "")` | ran (no return value, nothing visible changed) |
| Scheme | `(display-residue-hydrogen-bond-atom-status-using-dictionary 0 "A" 41 "")` | ran (no return value, nothing visible changed) |

### enhanced_ligand_coot_p

Python: `enhanced_ligand_coot_p()`  
Scheme: `(enhanced-ligand-coot-p)`

is this an "enhanced-ligand" version?

Arguments: none. Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `enhanced_ligand_coot_p()` | ran, returned `True` |
| Scheme | `(enhanced-ligand-coot-p)` | ran, returned `#t` |

Python and Scheme gave the same answer.

### get_intermediate_atoms_distortions

Python: `get_intermediate_atoms_distortions()`

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `get_intermediate_atoms_distortions_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_zone(0, "A", 41, 43, ""); print(get_intermediate_atoms_distortions())` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: during a refinement returns the distortion of every restraint on the moving atoms; False when no refinement is running.

### get_ligand_distortion_summary_info

Python: `get_ligand_distortion_summary_info(imol, residue_spec)`  
Scheme: `(get-ligand-distortion-summary-info-scm imol residue-spec)`

return the summary info for ligand distortion

Arguments: imol (a whole number), residue_spec (a list or value). Returns: a value (see the result of the example).
Also available in Python as `get_ligand_distortion_summary_info_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_ligand_distortion_summary_info(0, ["A", 41, ""])` | ran, returned `[2203.7119153114145, {'restraint_type': 'Chiral', 'target_value': 0.0, 'sigma': 0.1, 'fixed_atom_flags': [0, 0, 0, 0]}]` |
| Scheme | `(get-ligand-distortion-summary-info-scm 0 (list "A" 41 ""))` | ran, returned `(2203.7119153114145 (("restraint-type" . "Chiral") ("target-value" . 0.0) ("sigma" . 0.1) ("fixed-atom-flags" 0 0 0 0)))` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### get_ligand_percentile

Python: `get_ligand_percentile(metric_name, metric_value, reverse_order)`  
Scheme: `(get-ligand-percentile metric-name metric-value reverse-order)`

we want to read in the built-in database to convert these scores to percentiles
return -1 (test for negative) on failure
metric_name examples: density_correlation coot_diff_map_KS_2 mogul_z_worst bumps_1
range: 0->100
reverse order for mogul and bumps (for example) because low-is-good

Arguments: metric_name (text), metric_value (a number), reverse_order (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_ligand_percentile("density_correlation", 0.8, 0)` | ran, returned `24.48417314639074` |
| Scheme | `(get-ligand-percentile "density_correlation" 0.8 0)` | ran, returned `24.48417314639074` |

Example written and checked by hand on the test data. Expected: returns the percentile (0-100) of the value among PDB ligands for metric density_correlation, coot_diff_map_correlation, bumps_1 or mogul_z_worst; -1 for an unknown metric.

Python and Scheme gave the same answer.

### get_monomer_molecule_by_network_and_dict_gen

Python: `get_monomer_molecule_by_network_and_dict_gen(text)`  
Scheme: `(get-monomer-molecule-by-network-and-dict-gen text)`

return a new molecule number

Arguments: text (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_monomer_molecule_by_network_and_dict_gen("ATP")` | not run: uses the network and a dictionary generator |
| Scheme | `(get-monomer-molecule-by-network-and-dict-gen "ATP")` | not run: uses the network and a dictionary generator |

Example written and checked by hand on the test data. Expected: downloads the compound and makes a dictionary; returns the new molecule number.

### gsl_sf_erf_scm

Python: `gsl_sf_erf_scm(v)`  
Scheme: `(gsl-sf-erf-scm v)`

Arguments: v (a number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `gsl_sf_erf_scm(1.0)` | ran, returned `0.8427007929497149` |
| Scheme | `(gsl-sf-erf-scm 1.0)` | ran, returned `0.8427007929497149` |

Python and Scheme gave the same answer.

### gui_ligand_metrics

Python: `gui_ligand_metrics(ligand_spec, ligand_metrics, percentile_limit)`  
Scheme: `(gui-ligand-metrics-scm ligand-spec ligand-metrics percentile-limit)`

Arguments: ligand_spec (a list or value), ligand_metrics (a list or value), percentile_limit (a number). Returns: nothing.
Also available in Python as `gui_ligand_metrics_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: shows a window with the ligand metrics and their percentiles.

### import_rdkit_mol_from_smiles

Python: `import_rdkit_mol_from_smiles(smiles, comp_id)`  
Scheme: `(import-rdkit-mol-from-smiles smiles comp-id)`

import a molecule from a smiles string
RDKit is used to interpret the SMILES string
no dictionary is generated
Returns a molecule number or -1 on failure

Arguments: smiles (text), comp_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `import_rdkit_mol_from_smiles("CC(=O)Nc1ccc(O)cc1", "TYL")` | ran, returned `3`; changed: new molecule 3 (model, Imported TYL); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | `(import-rdkit-mol-from-smiles "CC(=O)Nc1ccc(O)cc1" "TYL")` | ran, returned `3`; changed: new molecule 3 (model, Imported TYL); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the number of a new molecule built from the SMILES by RDKit (no dictionary is made); -1 on failure.

Python and Scheme gave the same answer.

### invert_chiral_centre

Python: `invert_chiral_centre(imol, chain_id, res_no, ins_code, atom_name)`  
Scheme: `(invert-chiral-centre imol chain-id res-no ins-code atom-name)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), atom_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `invert_chiral_centre(0, "A", 41, "", " CA ")` | ran (no return value); changed: new molecule 3 (model, New Residue GL2); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | `(invert-chiral-centre 0 "A" 41 "" " CA ")` | ran (no return value); changed: new molecule 3 (model, New Residue GL2); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

### jed_flip_intermediate_atoms

Python: `jed_flip_intermediate_atoms()`  
Scheme: `(jed-flip-intermediate-atoms)`

JED-Flip the bond of the active atoms

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_zone(0, "A", 41, 43, ""); print(jed_flip_intermediate_atoms())` | ran (no return value, nothing visible changed) |
| Scheme | `(begin (refine-zone 0 "A" 41 43 "") (jed-flip-intermediate-atoms))` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: during a refinement JED-flips the active bond of the moving atoms and returns 1; 0 without intermediate atoms.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### kolmogorov_smirnov

Python: `kolmogorov_smirnov(l1, l2)`  
Scheme: `(kolmogorov-smirnov l1 l2)`

Arguments: l1 (a list or value), l2 (a list or value). Returns: a number.
Also available in Python as `kolmogorov_smirnov_py`.
Also available in Scheme as `kolmogorov-smirnov-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `kolmogorov_smirnov([1.0, 2.0, 3.0, 4.0, 5.0], [1.5, 2.5, 3.5, 4.5, 9.0])` | ran, returned `0.20000000000000007` |
| Scheme | `(kolmogorov-smirnov (list 1.0 2.0 3.0 4.0 5.0) (list 1.5 2.5 3.5 4.5 9.0))` | ran, returned `0.20000000000000007` |

Example written and checked by hand on the test data. Expected: returns the Kolmogorov-Smirnov statistic D (largest gap between the two cumulative distributions); -1 if the arguments are not lists.

Note: Python only counts float items (ints are silently dropped).

Python and Scheme gave the same answer.

### kolmogorov_smirnov_vs_normal

Python: `kolmogorov_smirnov_vs_normal(l1, mean, std_dev)`  
Scheme: `(kolmogorov-smirnov-vs-normal-scm l1 mean std-dev)`

Arguments: l1 (a list or value), mean (a number), std_dev (a number). Returns: a number.
Also available in Python as `kolmogorov_smirnov_vs_normal_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `kolmogorov_smirnov_vs_normal([-1.2, -0.3, 0.1, 0.4, 1.1, 0.0, -0.5], 0.0, 1.0)` | ran, returned `0.16568039586884403` |
| Scheme | `(kolmogorov-smirnov-vs-normal-scm (list -1.2 -0.3 0.1 0.4 1.1 0.0 -0.5) 0.0 1.0)` | ran, returned `0.16568039586884403` |

Example written and checked by hand on the test data. Expected: returns the Kolmogorov-Smirnov D of the values against a normal distribution with that mean and sd.

Python and Scheme gave the same answer.

### kullback_liebler

Python: `kullback_liebler(l1, l2)`  
Scheme: `(kullback-liebler l1 l2)`

Arguments: l1 (a list or value), l2 (a list or value). Returns: a value (see the result of the example).
Also available in Python as `kullback_liebler_py`.
Also available in Scheme as `kullback-liebler-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `kullback_liebler([1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 4.0], [1.0, 2.0, 3.0, 3.0, 4.0, 4.0, 5.0])` | ran, returned `[0.27279178641206264, -0.01682614795091192]` |
| Scheme | `(kullback-liebler (list 1.0 2.0 2.0 3.0 3.0 3.0 4.0) (list 1.0 2.0 3.0 3.0 4.0 4.0 5.0))` | ran, returned `(0.27279178641206264 -0.01682614795091192)` |

Example written and checked by hand on the test data. Expected: returns the two Kullback-Leibler divergences of the value distributions as a list.

Note: Fixed in coot0 build 31: the Scheme version computed the two numbers but returned #f (Coot 0.9.8.96).

Python and Scheme gave the same answer.

### ligand_atom_overlaps

Python: `ligand_atom_overlaps(imol, ligand_spec, neighb_radius)`  
Scheme: `(ligand-atom-overlaps-scm imol ligand-spec neighb-radius)`

internal bumps scoring, sphere overlap

Arguments: imol (a whole number), ligand_spec (a list or value), neighb_radius (a number). Returns: a value (see the result of the example).
Also available in Python as `ligand_atom_overlaps_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ligand_atom_overlaps(0, ["A", 41, ""], 5.0)` | ran, returned `[[[-1, 'A', 41, '', ' N  ', ''], [-1, 'A', 42, '', ' N  ', ''], 0.3194418392156972, False], [[-1, 'A', 41, '', ' N  ', ' ...` |
| Scheme | `(ligand-atom-overlaps-scm 0 (list "A" 41 "") 5.0)` | ran, returned `(((-1 "A" 41 "" " N  " "") (-1 "A" 42 "" " N  " "") 0.3194418392156972 #f) ((-1 "A" 41 "" " N  " "") (-1 "A" 40 "" " N   ...` |

Python and Scheme gave the same answer.

### linked_residues

Python: `linked_residues(residue_centre, imol, close_dist_max)`  
Scheme: `(linked-residues residue-centre imol close-dist-max)`

find all the residues that are linked to this reside (and those that are attached to those and so on)
the attachment test is trivial: is an atom of a potential neighber within close_dist_max of
an atom of the current residue?

Arguments: residue_centre (a list or value), imol (a whole number), close_dist_max (a number). Returns: a value (see the result of the example).
Also available in Python as `linked_residues_py`.
Also available in Scheme as `linked-residues-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `set_add_linked_residue_do_fit_and_refine(0)`, then `add_linked_residue(0, "A", 39, "", "NAG", "NAG-ASN", 1)`, then `len(linked_residues(["A", 39, ""], 0, 2.0))` | ran, returned `94` |
| Scheme | first `(set-add-linked-residue-do-fit-and-refine 0)`, then `(add-linked-residue 0 "A" 39 "" "NAG" "NAG-ASN" 1)`, then `(length (linked-residues (list "A" 39 "") 0 2.0))` | ran, returned `94` |

Example written and checked by hand on the test data. Expected: returns the residues linked (atoms within close_dist_max) to the start residue and, recursively, to those: for a protein residue that is the whole chain plus attached sugars.

Python and Scheme gave the same answer.

### match_residue_and_dictionary

Python: `match_residue_and_dictionary(imol, chain_id, res_no, ins_code, cif_dict_in, cif_dict_out, cif_dict_comp_id, reference_comp_id, output_comp_id, output_compound_name)`  
Scheme: `(match-residue-and-dictionary imol chain-id res-no ins-code cif-dict-in cif-dict-out cif-dict-comp-id reference-comp-id output-comp-id output-compound-name)`

Read cif_dict_in, match the atoms there-in to those of the dictionary of reference_comp_id.
Write a new dictionary to cif_dict_out.
Return 1 if was successful in doing the atom matching and writing the cif file.
e.g: match_residue_and_dictionary(0, "A", 1, "", "DRG-pyrogen.cif", "DRG-renamed.cif", "DRG", "LYS")

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), cif_dict_in (text), cif_dict_out (text), cif_dict_comp_id (text), reference_comp_id (text), output_comp_id (text), output_compound_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `match_residue_and_dictionary(0, "A", 1, "", "NAG.cif", "nag-matched.cif", "NAG", "NDG", "NAX", "my-sugar")` | ran, returned `0` |
| Scheme | `(match-residue-and-dictionary 0 "A" 1 "" "NAG.cif" "nag-matched.cif" "NAG" "NDG" "NAX" "my-sugar")` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: writes a new dictionary (cif_dict_out) with the atom names of cif_dict_in matched to the reference comp id; the return value is always 0 (the residue arguments are not used).

Note: Return value is always 0 even on success (result is never set in c-interface-ligands.cc).

Python and Scheme gave the same answer.

### match_this_residue_and_dictionary

Python: `match_this_residue_and_dictionary(imol, chain_id, res_no, ins_code, cif_dict_out, reference_comp_id, output_comp_id)`  
Scheme: `(match-this-residue-and-dictionary imol chain-id res-no ins-code cif-dict-out reference-comp-id output-comp-id)`

This is the GUI interface: User sits over on top of the residue
they want to change and provides an output dictionary cif file
name, a reference-comp-id and a compd-id for the new residue (type).

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), cif_dict_out (text), reference_comp_id (text), output_comp_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `read_cif_dictionary("NAG.cif")`, then `imol_nag = read_pdb("nag_only.pdb")`, then `match_this_residue_and_dictionary(imol_nag, "A", 1, "", "nag-this.cif", "NDG", "NAY")` | ran, returned `0` |
| Scheme | first `(read-cif-dictionary "NAG.cif")`, then `(define imol-nag (read-pdb "nag_only.pdb"))`, then `(match-this-residue-and-dictionary imol-nag "A" 1 "" "nag-this.cif" "NDG" "NAY")` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: writes a dictionary for the residue's type with atom names matched to the reference type and the new comp id; returns 0 (not used as a status).

Python and Scheme gave the same answer.

### print_residue_distortions

Python: `print_residue_distortions(imol, chain_id, res_no, ins_code)`  
Scheme: `(print-residue-distortions imol chain-id res-no ins-code)`

Returning void ATM. We shoud return an interesting object at some
stage. Perhaps a coot::geometry_distortion_info_container_t?

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `print_residue_distortions(0, "A", 41, "")` | ran, returned `2304.3666726013203` |
| Scheme | `(print-residue-distortions 0 "A" 41 "")` | ran, returned `2304.3666726013203` |

Python and Scheme gave the same answer.

### probe_clash_score

Python: `probe_clash_score(dots_file_name)`  
Scheme: `(probe-clash-score dots-file-name)`

return scheme false on failure or a scheme list
(n_bad_overlaps n_hydrogen_bonds n_small_overlaps n_close_contacts
n_wide_contacts)

Arguments: dots_file_name (text). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `open("dots.txt", "w").write(":1->1:bo: A   1 ASP  C   : A  89 PHE  CE2 :-0.420:-0.413:47.591:11.736:7.127:0.206:-0.1289:C:C:47.772:11.643:7.156:30.58:38.68\n:1- ...`, then `probe_clash_score("dots.txt")` | ran, returned `[1, 0, 1, 0, 1]` |
| Scheme | first `(call-with-output-file "dots.txt" (lambda (p) (display ":1->1:bo: A   1 ASP  C   : A  89 PHE  CE2 :-0.420:-0.413:47.591:11.736:7.127:0.206:-0.1289:C:C:47.772:11 ...`, then `(probe-clash-score "dots.txt")` | ran, returned `#<collectable-swig-pointer coot::probe_clash_score_t * 92e20d360>` |

Example written and checked by hand on the test data. Expected: reads a probe -u dots file (no probe run) and returns the counts [bad overlaps, H-bonds, small overlaps, close contacts, wide contacts].

Note: Scheme 'probe-clash-score' is the raw C++ function and returns a SWIG pointer; the list version probe_clash_score_scm is not exported under this name (Python redefines probe_clash_score = probe_clash_score_py). Python and Scheme disagree.

### residue_to_mdl_file_for_mogul

Python: `residue_to_mdl_file_for_mogul(imol, chain_id, resno, ins_code, mdl_file_name)`  
Scheme: `(residue-to-mdl-file-for-mogul imol chain-id resno ins-code mdl-file-name)`

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), mdl_file_name (text). Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `read_cif_dictionary("NAG.cif")`, then `imol_nag = read_pdb("nag_only.pdb")`, then `residue_to_mdl_file_for_mogul(imol_nag, "A", 1, "", "nag.mdl")` | ran, returned `True` |
| Scheme | first `(read-cif-dictionary "NAG.cif")`, then `(define imol-nag (read-pdb "nag_only.pdb"))`, then `(residue-to-mdl-file-for-mogul imol-nag "A" 1 "" "nag.mdl")` | ran, returned `#t` |

Example written and checked by hand on the test data. Expected: writes the residue as an MDL mol file for Mogul (does not run Mogul) and returns True.

Note: Only writes a file; the old 'not run (mogul)' classification was wrong.

Python and Scheme gave the same answer.

### residue_to_sdf_file

Python: `residue_to_sdf_file(imol, chain_id, resno, ins_code, sdf_file_name, kekulize)`  
Scheme: `(residue-to-sdf-file imol chain-id resno ins-code sdf-file-name kekulize)`

20140226: now we change things so that the interface functions always get generated,
 and what the function does depends on MAKE_ENHANCED_LIGAND_TOOLS
#ifdef MAKE_ENHANCED_LIGAND_TOOLS
was it OK or not? (i.e. did we not catch an exception)

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), sdf_file_name (text), kekulize (true or false). Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `read_cif_dictionary("NAG.cif")`, then `imol_nag = read_pdb("nag_only.pdb")`, then `residue_to_sdf_file(imol_nag, "A", 1, "", "nag.sdf", True)` | ran, returned `True` |
| Scheme | first `(read-cif-dictionary "NAG.cif")`, then `(define imol-nag (read-pdb "nag_only.pdb"))`, then `(residue-to-sdf-file imol-nag "A" 1 "" "nag.sdf" #t)` | ran, returned `#t` |

Example written and checked by hand on the test data. Expected: returns True and writes the residue (with its dictionary) as an SDF file, kekulized if asked.

Python and Scheme gave the same answer.

### residues_distortions

Python: `residues_distortions(imol, residue_spec_list)`  
Scheme: `(residues-distortions-scm imol residue-spec-list-scm)`

this is not a ligands function (although it can be used for ligands)
it doesn't belong here

Arguments: imol (a whole number), residue_spec_list (a list or value). Returns: a value (see the result of the example).
Also available in Python as `residues_distortions_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residues_distortions(0, [["A", 41, ""], ["A", 42, ""]])[0]` | ran, returned `{'distortion_score': 54.900434002892354, 'restraint': {'restraint_type': 'Bond', 'target_value': 1.4869999885559082, 'si ...` |
| Scheme | `(length (residues-distortions-scm 0 (list (list "A" 41 "") (list "A" 42 ""))))` | ran, returned `866` |

Example written and checked by hand on the test data. Expected: returns one entry per geometry restraint of the residues with its distortion score (needs a refinement map set).

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### residues_torsions_match

Python: `residues_torsions_match(imol_1, res_1, imol_2, res_2, tolerance)`  
Scheme: `(residues-torsions-match-scm imol-1 res-1 imol-2 res-2 tolerance)`

Arguments: imol_1 (a whole number), res_1 (a list or value), imol_2 (a whole number), res_2 (a list or value), tolerance (a number). Returns: true or false.
Also available in Python as `residues_torsions_match_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residues_torsions_match(0, ["A", 41, ""], 0, ["A", 41, ""], 10.0)` | ran, returned `False` |
| Scheme | `(residues-torsions-match-scm 0 (list "A" 41 "") 0 (list "A" 41 "") 10.0)` | ran, returned `#f` |

Example written and checked by hand on the test data. Expected: should be True when all torsions of the two residues agree within the tolerance (degrees).

Note: Always False: the comparison (coot::compare_residue_torsions) is commented out in the C++ (c-interface-ligands.cc ~2674), so the result is never set.

Python and Scheme gave the same answer.

### reverse_jed_flip_intermediate_atoms

Python: `reverse_jed_flip_intermediate_atoms()`  
Scheme: `(reverse-jed-flip-intermediate-atoms)`

JED-Flip the bond of the active atoms using reversed atom selection (wag the dog)

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refine_zone(0, "A", 41, 43, ""); print(reverse_jed_flip_intermediate_atoms())` | ran (no return value, nothing visible changed) |
| Scheme | `(begin (refine-zone 0 "A" 41 43 "") (reverse-jed-flip-intermediate-atoms))` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: as jed_flip_intermediate_atoms with the other side moved; 1 during a refinement, 0 otherwise.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### set_all_atom_contact_dots_ignore_water

Python: `set_all_atom_contact_dots_ignore_water(state)`  
Scheme: `(set-all-atom-contact-dots-ignore-water state)`

set if all atom contact should ignore water-water interactions (default off)

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_all_atom_contact_dots_ignore_water(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-all-atom-contact-dots-ignore-water 1)` | ran (no return value, nothing visible changed) |

### show_feats

Python: `show_feats(imol, chain_id, resno, ins_code)`  
Scheme: `(show-feats imol chain-id resno ins-code)`

rdkit chemical features.

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text). Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `read_cif_dictionary("NAG.cif")`, then `imol_nag = read_pdb("nag_only.pdb")`, then `show_feats(imol_nag, "A", 1, "")` | ran, returned `True` |
| Scheme | first `(read-cif-dictionary "NAG.cif")`, then `(define imol-nag (read-pdb "nag_only.pdb"))`, then `(show-feats imol-nag "A" 1 "")` | ran, returned `#t` |

Example written and checked by hand on the test data. Expected: returns True and draws the RDKit chemical features (donors, acceptors, rings) of the residue in the graphics; False if the residue type has no dictionary.

Python and Scheme gave the same answer.

### switch_HIS_protonation

Python: `switch_HIS_protonation(imol, residue_spec)`  
Scheme: `(switch-HIS-protonation-scm imol residue-spec-scm)`

change HE2 to HD1 and vice versa

Arguments: imol (a whole number), residue_spec (a list or value). Returns: nothing.
Also available in Python as `switch_HIS_protonation`, `switch_HIS_protonation_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `switch_HIS_protonation(0, ["A", 41, ""])` | ran (no return value, nothing visible changed) |
| Scheme | `(switch-HIS-protonation-scm 0 (list "A" 41 ""))` | ran (no return value, nothing visible changed) |

### write_dictionary_from_residue

Python: `write_dictionary_from_residue(imol, chain_id, res_no, ins_code, cif_file_name)`  
Scheme: `(write-dictionary-from-residue imol chain-id res-no ins-code cif-file-name)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), cif_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_dictionary_from_residue(0, "A", 41, "", "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(write-dictionary-from-residue 0 "A" 41 "" "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

