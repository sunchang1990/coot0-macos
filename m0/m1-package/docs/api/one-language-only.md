# Functions in only one language

Almost every scripting function of Coot exists in both Python and Scheme, with the same name (Python `residue_name`, Scheme `residue-name`). These 18 exist only in Scheme and these 46 only in Python. Most of them convert values between the language and Coot (for example a Scheme list into a residue specification) and have a counterpart with a different name in the other language; the table says which.

From Scheme you can call any Python-only function with `run-python-command`, for example `(run-python-command "all_molecule_ramachandran_region(0)")`; from Python any Scheme-only function with `run_scheme_command`, for example `run_scheme_command('(spherical-density-overlap 0 1)')` (cookbook 7.7).

## Only in Scheme

| Scheme | Counterpart in Python | What it does |
|---|---|---|
| [`atom-spec-from-scm-expression`](sections/sequence-from-map.md#atom-spec-from-scm-expression) | `atom_spec_from_python_expression` | expects an expr of length 5, ie: (list chain-id res-no ins-cod atom-name alt-conf) |
| [`coot-has-python-p`](sections/scripting.md#coot-has-python-p) | `coot_has_guile` | (no description in Coot's headers) |
| [`get-input-model-was-cif-state-scm`](sections/graphics-utility-functions.md#get-input-model-was-cif-state-scm) | `get_input_molecule_was_in_mmcif_state` | - get the name state of the input model. Return false if there was an erro with the molecule index |
| [`map-to-model-correlation-stats-per-residue-scm`](sections/map-to-model-correlation.md#map-to-model-correlation-stats-per-residue-scm) | `map_to_model_correlation_stats_per_residue_range_py` | map to model stats |
| [`mogul-results-process-many`](sections/mogul.md#mogul-results-process-many) | none | (no description in Coot's headers) |
| [`pisa-molecule-record-chain-id`](sections/pisa-interaction.md#pisa-molecule-record-chain-id) | none | (no description in Coot's headers) |
| [`pisa-molecule-record-residues`](sections/pisa-interaction.md#pisa-molecule-record-residues) | none | internal function |
| [`residue-records-list-scm-to-residue-specs`](sections/sequence-from-map.md#residue-records-list-scm-to-residue-specs) | `residue_records_list_py_to_residue_specs` | (no description in Coot's headers) |
| [`rtop-to-scm`](sections/sequence-from-map.md#rtop-to-scm) | `rtop_to_python` | (no description in Coot's headers) |
| [`run-python-command`](sections/restraints-interface.md#run-python-command) | `run_scheme_command` | (no description in Coot's headers) |
| [`safe-scheme-command-test`](sections/scripting.md#safe-scheme-command-test) | `safe_python_command_test` | (no description in Coot's headers) |
| [`scm-symop-strings-to-space-group`](sections/get-sequence.md#scm-symop-strings-to-space-group) | `py_symop_strings_to_space_group` | (no description in Coot's headers) |
| [`scm-to-residue-specs`](sections/get-sequence.md#scm-to-residue-specs) | `py_to_residue_specs` | (no description in Coot's headers) |
| [`set-temperature-factors-for-atoms-in-residue-scm`](sections/atom-selection-utilities.md#set-temperature-factors-for-atoms-in-residue-scm) | `set_b_factor_residues` | (no description in Coot's headers) |
| [`spherical-density-overlap`](sections/get-sequence.md#spherical-density-overlap) | none | (no description in Coot's headers) |
| [`symbol-value-from-record`](sections/sequence-from-map.md#symbol-value-from-record) | none | (no description in Coot's headers) |
| [`test-mol-triangles-scm`](sections/scripting.md#test-mol-triangles-scm) | none | (no description in Coot's headers) |
| [`try-load-scheme-extras-dir`](sections/other-functions.md#try-load-scheme-extras-dir) | `try_load_python_extras_dir` | (no description in Coot's headers) |

## Only in Python

| Python | Counterpart in Scheme | What it does |
|---|---|---|
| [`add_residue_with_atoms_py`](sections/add-a-residue-functions.md#add_residue_with_atoms_py) | none | add a residue with atoms in scripting |
| [`add_target_position_restraint_for_intermediate_atom`](sections/intermediate-atom-manipulation-interface.md#add_target_position_restraint_for_intermediate_atom) | none | add a target position for an intermediate atom and refine |
| [`add_target_position_restraints_for_intermediate_atoms`](sections/intermediate-atom-manipulation-interface.md#add_target_position_restraints_for_intermediate_atoms) | none | and the multiple-atom version of that (so that they can be applied at the same time) |
| [`all_molecule_ramachandran_region`](sections/experimental.md#all_molecule_ramachandran_region) | none | a stub currently |
| [`analyse_map_point_density_change_py`](sections/extra-map-functions.md#analyse_map_point_density_change_py) | none | test function for analysis of multiple map |
| [`atom_spec_from_python_expression`](sections/sequence-from-map.md#atom_spec_from_python_expression) | `atom-spec-from-scm-expression` | (no description in Coot's headers) |
| [`calculate_maps_and_stats_py`](sections/map-functions.md#calculate_maps_and_stats_py) | none | Calculate structure factors and make a 2FoFC map and a Fo-Fc map updating the given |
| [`coot_has_guile`](sections/restraints-interface.md#coot_has_guile) | `coot-has-python-p` | (no description in Coot's headers) |
| [`display_python`](sections/scripting.md#display_python) | none | This is a common denominator really. It does not depend on mmdb, |
| [`get_bonds_representation`](sections/using-s-expression-molecules.md#get_bonds_representation) | none | return a Python object for the bonds |
| [`get_dictionary_radii`](sections/using-s-expression-molecules.md#get_dictionary_radii) | none | return a Python object for the radii of the atoms in the dictionary |
| [`get_environment_distances_representation`](sections/using-s-expression-molecules.md#get_environment_distances_representation) | none | return a Python object for the representation of bump and hydrogen bonds of |
| [`get_generic_object_py`](sections/generic-objects.md#get_generic_object_py) | none | (no description in Coot's headers) |
| [`get_input_molecule_was_in_mmcif_state`](sections/graphics-utility-functions.md#get_input_molecule_was_in_mmcif_state) | `get-input-model-was-cif-state-scm` | - get the name state of the input model |
| [`get_intermediate_atoms_bonds_representation`](sections/using-s-expression-molecules.md#get_intermediate_atoms_bonds_representation) | none | return a Python object for the intermediate atoms bonds |
| [`get_intermediate_atoms_distortions`](sections/ligands.md#get_intermediate_atoms_distortions) | none | (no description in Coot's headers) |
| [`get_pointer_position_frac`](sections/pointer-position-function.md#get_pointer_position_frac) | none | return the [x,y] position of the pointer in fractional coordinates. |
| [`make_atom_spec`](sections/scripting.md#make_atom_spec) | none | (no description in Coot's headers) |
| [`make_residue_spec_py`](sections/scripting.md#make_residue_spec_py) | none | (no description in Coot's headers) |
| [`map_contours`](sections/map-contouring-functions.md#map_contours) | none | (no description in Coot's headers) |
| [`map_peaks_around_molecule`](sections/validation-functions.md#map_peaks_around_molecule) | none | (no description in Coot's headers) |
| [`map_peaks_near_point_from_list`](sections/validation-functions.md#map_peaks_near_point_from_list) | none | (no description in Coot's headers) |
| [`monomer_restraints_for_molecule`](sections/restraints-interface.md#monomer_restraints_for_molecule) | none | (no description in Coot's headers) |
| [`pathology_data`](sections/get-sequence.md#pathology_data) | none | (no description in Coot's headers) |
| [`py_clean_internal`](sections/scripting.md#py_clean_internal) | none | (no description in Coot's headers) |
| [`py_symop_strings_to_space_group`](sections/get-sequence.md#py_symop_strings_to_space_group) | `scm-symop-strings-to-space-group` | (no description in Coot's headers) |
| [`py_to_residue_specs`](sections/get-sequence.md#py_to_residue_specs) | `scm-to-residue-specs` | (no description in Coot's headers) |
| [`python_representation_kk`](sections/molecule-info-functions.md#python_representation_kk) | none | (no description in Coot's headers) |
| [`register_post_intermediate_atoms_moved_hook`](sections/refinement-with-specs.md#register_post_intermediate_atoms_moved_hook) | none | (no description in Coot's headers) |
| [`residue_centre_from_spec`](sections/atom-information-functions.md#residue_centre_from_spec) | none | the expanded form of this is in c-interface.h |
| [`residue_records_list_py_to_residue_specs`](sections/sequence-from-map.md#residue_records_list_py_to_residue_specs) | `residue-records-list-scm-to-residue-specs` | (no description in Coot's headers) |
| [`residue_spec_make_triple`](sections/restraints-interface.md#residue_spec_make_triple) | none | (no description in Coot's headers) |
| [`rtop_to_python`](sections/sequence-from-map.md#rtop_to_python) | `rtop-to-scm` | (no description in Coot's headers) |
| [`run_scheme_command`](sections/restraints-interface.md#run_scheme_command) | `run-python-command` | we ignore return values for now |
| [`safe_python_command`](sections/scripting.md#safe_python_command) | none | do nothing |
| [`safe_python_command_by_char_star`](sections/scripting.md#safe_python_command_by_char_star) | none | (no description in Coot's headers) |
| [`safe_python_command_test`](sections/scripting.md#safe_python_command_test) | `safe-scheme-command-test` | (no description in Coot's headers) |
| [`safe_python_command_with_return`](sections/scripting.md#safe_python_command_with_return) | none | (no description in Coot's headers) |
| [`safe_python_command_with_unsafe_thread`](sections/scripting.md#safe_python_command_with_unsafe_thread) | none | (no description in Coot's headers) |
| [`screen_vectors`](sections/validation-functions.md#screen_vectors) | none | BL says:: this probably shouldnt be here but cluster with KK code |
| [`set_b_factor_residues`](sections/atom-information-functions.md#set_b_factor_residues) | `set-temperature-factors-for-atoms-in-residue-scm` | (no description in Coot's headers) |
| [`set_python_draw_function`](sections/get-sequence.md#set_python_draw_function) | none | client/server functions |
| [`set_user_defined_colours_py`](sections/colour.md#set_user_defined_colours_py) | none | by default user-defined colour indices will use a colour wheel |
| [`text_png_as_string`](sections/images.md#text_png_as_string) | none | make a png given the info in text_info_dict |
| [`try_load_python_extras_dir`](sections/other-functions.md#try_load_python_extras_dir) | `try-load-scheme-extras-dir` | (no description in Coot's headers) |
| [`use_unimodal_ring_torsion_restraints_for_residue`](sections/more-refinement-functions.md#use_unimodal_ring_torsion_restraints_for_residue) | none | use unimodal ring torsion restraints (e.g. for carbohydrate pyranose) |

## The script layers

On top of these built-in functions, Coot loads helper functions written in Python (`share/coot/python/coot_utils.py`, `coot_gui.py`, ...) and in Scheme (`share/coot/scheme/coot-utils.scm`, ...), for example `chain_ids`, `all_residues`, `residues_near_residue`. Most exist in both languages. The menus, windows and toolbar of coot0 are made by the Python layer only (`coot_menubar_menu`, `coot_toolbar_button`, ...): from Scheme use them through `run-python-script` (cookbook 6.1 and 6.2).
