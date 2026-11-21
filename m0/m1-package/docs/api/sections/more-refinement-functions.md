# More Refinement Functions

[Scripting reference](../README.md) > More Refinement Functions (8 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### convert_dictionary_planes_to_improper_dihedrals

Python: `convert_dictionary_planes_to_improper_dihedrals()`  
Scheme: `(convert-dictionary-planes-to-improper-dihedrals)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `convert_dictionary_planes_to_improper_dihedrals()` | ran (no return value, nothing visible changed) |
| Scheme | `(convert-dictionary-planes-to-improper-dihedrals)` | ran (no return value, nothing visible changed) |

### crankshaft_peptide_rotation_optimization_py

Python: `crankshaft_peptide_rotation_optimization_py(imol, residue_spec_py)`  
Scheme: `(crankshaft-peptide-rotation-optimization-scm imol residue-spec-smc)`

Apply crankshaft peptide rotation optimization to the specified residue

Arguments: imol (a whole number), residue_spec_py (a list or value). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `crankshaft_peptide_rotation_optimization_py(0, ["A", 41, ""])` | ran (no return value); changed: molecule 0: coordinates of 4 residue(s) (A40, A41, A42, A43) |
| Scheme | `(crankshaft-peptide-rotation-optimization-scm 0 (list "A" 41 ""))` | ran (no return value); changed: molecule 0: coordinates of 4 residue(s) (A40, A41, A42, A43) |

### get_refinement_geman_mcclure_alpha

Python: `get_refinement_geman_mcclure_alpha()`  
Scheme: `(get-refinement-geman-mcclure-alpha)`

get the Geman-McClure distance alpha value (weight)

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_refinement_geman_mcclure_alpha()` | ran, returned `1.0` |
| Scheme | `(get-refinement-geman-mcclure-alpha)` | ran, returned `1.0` |

Python and Scheme gave the same answer.

### set_log_cosh_target_distance_scale_factor

Python: `set_log_cosh_target_distance_scale_factor(sf)`  
Scheme: `(set-log-cosh-target-distance-scale-factor sf)`

set the log cosh scale factor for target position restraints

Arguments: sf (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_log_cosh_target_distance_scale_factor(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-log-cosh-target-distance-scale-factor 1.0)` | ran (no return value, nothing visible changed) |

### set_refinement_geman_mcclure_alpha

Python: `set_refinement_geman_mcclure_alpha(alpha)`  
Scheme: `(set-refinement-geman-mcclure-alpha alpha)`

set the Geman-McClure distance alpha value (weight)

Arguments: alpha (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refinement_geman_mcclure_alpha(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refinement-geman-mcclure-alpha 1.0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_refinement_geman_mcclure_alpha was 1.0, set to 2.0, read back 2.0; Scheme: get-refinement-geman-mcclure-alpha was 1.0, set to 2.0, read back 2.0.

### set_refinement_lennard_jones_epsilon

Python: `set_refinement_lennard_jones_epsilon(epsilon)`  
Scheme: `(set-refinement-lennard-jones-epsilon epsilon)`

set the Lennard Jones epsilon parameter

Arguments: epsilon (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refinement_lennard_jones_epsilon(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refinement-lennard-jones-epsilon 1.0)` | ran (no return value, nothing visible changed) |

### use_unimodal_ring_torsion_restraints

Python: `use_unimodal_ring_torsion_restraints(res_name)`  
Scheme: `(use-unimodal-ring-torsion-restraints res-name)`

use unimodal ring torsion restraints (e.g. for carbohydrate pyranose)
 uses built-in list of of torsions for specific residue types

Arguments: res_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `use_unimodal_ring_torsion_restraints("ALA")` | ran (no return value, nothing visible changed) |
| Scheme | `(use-unimodal-ring-torsion-restraints "ALA")` | ran (no return value, nothing visible changed) |

### use_unimodal_ring_torsion_restraints_for_residue

Python: `use_unimodal_ring_torsion_restraints_for_residue(res_name, torsions_info_list)`

use unimodal ring torsion restraints (e.g. for carbohydrate pyranose)
 allow user definition of torsions for given residue
 @var{torsions_info_list} is a list of item that are of the form
 @var{[atom_name_1, atom_name_2, atom_name_3, atom_name_4, double torsion_1234]}

Arguments: res_name (text), torsions_info_list (a list or value). Returns: nothing.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `use_unimodal_ring_torsion_restraints_for_residue("NAG", [[" C1 ", " C2 ", " C3 ", " C4 ", -55.0], [" C2 ", " C3 ", " C4 ", " C5 ", 55.0]])` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: replaces the ring torsions of the NAG dictionary by the given single-minimum torsions (Python only); monomer_restraints('NAG') shows ring-torsion-N entries.

Note: the torsion value must be a Python float (-55.0, not -55)

