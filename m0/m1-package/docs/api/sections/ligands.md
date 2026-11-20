# Ligands

[Scripting reference](../README.md) > Ligands (36 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_dictionary_from_residue

Python: `add_dictionary_from_residue(imol, chain_id, res_no, ins_code)`  
Scheme: `(add-dictionary-from-residue imol chain-id res-no ins-code)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_dictionary_from_residue(0, "A", 41, "")` | ran (no return value) |
| Scheme | `(add-dictionary-from-residue 0 "A" 41 "")` | ran (no return value) |

### comprised_of_organic_set_p

Python: `comprised_of_organic_set_p(rn)`  
Scheme: `(comprised-of-organic-set-p rn)`

return False if unknown

Arguments: rn (text). Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `comprised_of_organic_set_p("hello")` | ran, returned `False` |
| Scheme | `(comprised-of-organic-set-p "hello")` | ran, returned `#f` |

Python and Scheme gave the same answer.

### coot_add_hydrogen_atoms

Python: `coot_add_hydrogen_atoms(imol)`  
Scheme: `(coot-add-hydrogen-atoms imol)`

this is not a ligand function - it does not belong here.
 add Hydrogen atoms to the molecule

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_add_hydrogen_atoms(0)` | ran (no return value) |
| Scheme | `(coot-add-hydrogen-atoms 0)` | ran (no return value) |

### coot_all_atom_contact_dots

Python: `coot_all_atom_contact_dots(imol)`  
Scheme: `(coot-all-atom-contact-dots imol)`

all-atom contact dots. This is not the place for this declaration (not a ligand function)
 calculate all-atom contact dots
remove contact dots objects using the Generic Display Objects dialog

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_all_atom_contact_dots(0)` | ran (no return value) |
| Scheme | `(coot-all-atom-contact-dots 0)` | ran (no return value) |

### coot_contact_dots_for_ligand

Python: `coot_contact_dots_for_ligand(imol, ligand_spec)`  
Scheme: `(coot-contact-dots-for-ligand-scm imol residue-spec-scm)`

Arguments: imol (a whole number), ligand_spec (a list or value). Returns: nothing.
Also available in Python as `coot_contact_dots_for_ligand`, `coot_contact_dots_for_ligand_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_contact_dots_for_ligand(0, ["A", 41, ""])` | ran (no return value) |
| Scheme | `(coot-contact-dots-for-ligand-scm 0 (list "A" 41 ""))` | ran (no return value) |

### coot_reduce

Python: `coot_reduce(imol)`  
Scheme: `(coot-reduce imol)`

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_reduce(0)` | not run: not run automatically (reduce: exits, uses the network, an external program, files or a screen) |
| Scheme | `(coot-reduce 0)` | not run: not run automatically (reduce: exits, uses the network, an external program, files or a screen) |

### display_residue_distortions

Python: `display_residue_distortions(imol, chain_id, res_no, ins_code)`  
Scheme: `(display-residue-distortions imol chain-id res-no ins-code)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `display_residue_distortions(0, "A", 41, "")` | ran (no return value) |
| Scheme | `(display-residue-distortions 0 "A" 41 "")` | ran (no return value) |

### display_residue_hydrogen_bond_atom_status_using_dictionary

Python: `display_residue_hydrogen_bond_atom_status_using_dictionary(imol, chain_id, res_no, ins_code)`  
Scheme: `(display-residue-hydrogen-bond-atom-status-using-dictionary imol chain-id res-no ins-code)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `display_residue_hydrogen_bond_atom_status_using_dictionary(0, "A", 41, "")` | ran (no return value) |
| Scheme | `(display-residue-hydrogen-bond-atom-status-using-dictionary 0 "A" 41 "")` | ran (no return value) |

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
| Python | `get_intermediate_atoms_distortions()` | ran, returned `False` |

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
| Python | `get_ligand_percentile("my-name", 1.0, 1)` | ran, returned `-1.0` |
| Scheme | `(get-ligand-percentile "my-name" 1.0 1)` | ran, returned `-1.0` |

Python and Scheme gave the same answer.

### get_monomer_molecule_by_network_and_dict_gen

Python: `get_monomer_molecule_by_network_and_dict_gen(text)`  
Scheme: `(get-monomer-molecule-by-network-and-dict-gen text)`

return a new molecule number

Arguments: text (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_monomer_molecule_by_network_and_dict_gen("hello")` | not run: not run automatically (network: exits, uses the network, an external program, files or a screen) |
| Scheme | `(get-monomer-molecule-by-network-and-dict-gen "hello")` | not run: not run automatically (network: exits, uses the network, an external program, files or a screen) |

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
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

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
| Python | `import_rdkit_mol_from_smiles("hello", "ALA")` | ran, returned `-1` |
| Scheme | `(import-rdkit-mol-from-smiles "hello" "ALA")` | ran, returned `-1` |

Python and Scheme gave the same answer.

### invert_chiral_centre

Python: `invert_chiral_centre(imol, chain_id, res_no, ins_code, atom_name)`  
Scheme: `(invert-chiral-centre imol chain-id res-no ins-code atom-name)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), atom_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `invert_chiral_centre(0, "A", 41, "", " CA ")` | ran (no return value) |
| Scheme | `(invert-chiral-centre 0 "A" 41 "" " CA ")` | ran (no return value) |

### jed_flip_intermediate_atoms

Python: `jed_flip_intermediate_atoms()`  
Scheme: `(jed-flip-intermediate-atoms)`

JED-Flip the bond of the active atoms

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `jed_flip_intermediate_atoms()` | ran, returned `0` |
| Scheme | `(jed-flip-intermediate-atoms)` | ran, returned `0` |

Python and Scheme gave the same answer.

### kolmogorov_smirnov

Python: `kolmogorov_smirnov(l1, l2)`  
Scheme: `(kolmogorov-smirnov l1 l2)`

Arguments: l1 (a list or value), l2 (a list or value). Returns: a number.
Also available in Python as `kolmogorov_smirnov_py`.
Also available in Scheme as `kolmogorov-smirnov-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### kolmogorov_smirnov_vs_normal

Python: `kolmogorov_smirnov_vs_normal(l1, mean, std_dev)`  
Scheme: `(kolmogorov-smirnov-vs-normal-scm l1 mean std-dev)`

Arguments: l1 (a list or value), mean (a number), std_dev (a number). Returns: a number.
Also available in Python as `kolmogorov_smirnov_vs_normal_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### kullback_liebler

Python: `kullback_liebler(l1, l2)`  
Scheme: `(kullback-liebler l1 l2)`

Arguments: l1 (a list or value), l2 (a list or value). Returns: a value (see the result of the example).
Also available in Python as `kullback_liebler_py`.
Also available in Scheme as `kullback-liebler-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

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
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

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
| Python | `match_residue_and_dictionary(0, "A", 41, "", "hello", "hello", "hello", "hello", "hello", "my-name")` | ran, returned `0` |
| Scheme | `(match-residue-and-dictionary 0 "A" 41 "" "hello" "hello" "hello" "hello" "hello" "my-name")` | ran, returned `0` |

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
| Python | `match_this_residue_and_dictionary(0, "A", 41, "", "hello", "hello", "hello")` | ran, returned `0` |
| Scheme | `(match-this-residue-and-dictionary 0 "A" 41 "" "hello" "hello" "hello")` | ran, returned `0` |

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
| Python | `probe_clash_score("tutorial-modern.pdb")` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |
| Scheme | `(probe-clash-score "tutorial-modern.pdb")` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |

### residue_to_mdl_file_for_mogul

Python: `residue_to_mdl_file_for_mogul(imol, chain_id, resno, ins_code, mdl_file_name)`  
Scheme: `(residue-to-mdl-file-for-mogul imol chain-id resno ins-code mdl-file-name)`

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), mdl_file_name (text). Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_to_mdl_file_for_mogul(0, "A", 41, "", "tutorial-modern.pdb")` | not run: not run automatically (mogul: exits, uses the network, an external program, files or a screen) |
| Scheme | `(residue-to-mdl-file-for-mogul 0 "A" 41 "" "tutorial-modern.pdb")` | not run: not run automatically (mogul: exits, uses the network, an external program, files or a screen) |

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
| Python | `residue_to_sdf_file(0, "A", 41, "", "tutorial-modern.pdb", True)` | ran, returned `False` |
| Scheme | `(residue-to-sdf-file 0 "A" 41 "" "tutorial-modern.pdb" 1)` | error: In procedure residue-to-sdf-file: No matching method for generic function 'residue_to_sdf_file' |

### residues_distortions

Python: `residues_distortions(imol, residue_spec_list)`  
Scheme: `(residues-distortions-scm imol residue-spec-list-scm)`

this is not a ligands function (although it can be used for ligands)
it doesn't belong here

Arguments: imol (a whole number), residue_spec_list (a list or value). Returns: a value (see the result of the example).
Also available in Python as `residues_distortions_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residues_distortions(0, ["A", 41, ""])` | error: SystemError: <built-in function residues_distortions_py> returned a result with an exception set |
| Scheme | `(residues-distortions-scm 0 (list "A" 41 ""))` | error: In procedure length: Wrong type argument in position 1: "A" |

### residues_torsions_match

Python: `residues_torsions_match(imol_1, res_1, imol_2, res_2, tolerance)`  
Scheme: `(residues-torsions-match-scm imol-1 res-1 imol-2 res-2 tolerance)`

Arguments: imol_1 (a whole number), res_1 (a list or value), imol_2 (a whole number), res_2 (a list or value), tolerance (a number). Returns: true or false.
Also available in Python as `residues_torsions_match_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### reverse_jed_flip_intermediate_atoms

Python: `reverse_jed_flip_intermediate_atoms()`  
Scheme: `(reverse-jed-flip-intermediate-atoms)`

JED-Flip the bond of the active atoms using reversed atom selection (wag the dog)

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `reverse_jed_flip_intermediate_atoms()` | ran, returned `0` |
| Scheme | `(reverse-jed-flip-intermediate-atoms)` | ran, returned `0` |

Python and Scheme gave the same answer.

### set_all_atom_contact_dots_ignore_water

Python: `set_all_atom_contact_dots_ignore_water(state)`  
Scheme: `(set-all-atom-contact-dots-ignore-water state)`

set if all atom contact should ignore water-water interactions (default off)

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_all_atom_contact_dots_ignore_water(1)` | ran (no return value) |
| Scheme | `(set-all-atom-contact-dots-ignore-water 1)` | ran (no return value) |

### show_feats

Python: `show_feats(imol, chain_id, resno, ins_code)`  
Scheme: `(show-feats imol chain-id resno ins-code)`

rdkit chemical features.

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text). Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_feats(0, "A", 41, "")` | ran, returned `False` |
| Scheme | `(show-feats 0 "A" 41 "")` | ran, returned `#f` |

Python and Scheme gave the same answer.

### switch_HIS_protonation

Python: `switch_HIS_protonation(imol, residue_spec)`  
Scheme: `(switch-HIS-protonation-scm imol residue-spec-scm)`

change HE2 to HD1 and vice versa

Arguments: imol (a whole number), residue_spec (a list or value). Returns: nothing.
Also available in Python as `switch_HIS_protonation`, `switch_HIS_protonation_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `switch_HIS_protonation(0, ["A", 41, ""])` | ran (no return value) |
| Scheme | `(switch-HIS-protonation-scm 0 (list "A" 41 ""))` | ran (no return value) |

### write_dictionary_from_residue

Python: `write_dictionary_from_residue(imol, chain_id, res_no, ins_code, cif_file_name)`  
Scheme: `(write-dictionary-from-residue imol chain-id res-no ins-code cif-file-name)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), cif_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_dictionary_from_residue(0, "A", 41, "", "tutorial-modern.pdb")` | ran (no return value) |
| Scheme | `(write-dictionary-from-residue 0 "A" 41 "" "tutorial-modern.pdb")` | ran (no return value) |

