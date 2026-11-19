# Sequence from Map

[Scripting reference](../README.md) > Sequence from Map (36 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_generic_object_bond

Python: `add_generic_object_bond(imol1, imol2, atom_spec_1, atom_spec_2, generic_object_number, colour)`  
Scheme: `(add-generic-object-bond imol1 imol2 atom-spec-1 atom-spec-2 generic-object-number colour)`

PyObject *symbol_value_from_record(PyObject *record_1, const std::string &symbol);

Arguments: imol1 (a whole number), imol2 (a whole number), atom_spec_1 (`coot::atom_spec_t`), atom_spec_2 (`coot::atom_spec_t`), generic_object_number (a whole number), colour (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### apply_sequence_to_fragment

Python: `apply_sequence_to_fragment(imol, chain_id, resno_start, resno_end, imol_map, file_name_for_sequences)`  
Scheme: `(apply-sequence-to-fragment imol chain-id resno-start resno-end imol-map file-name-for-sequences)`

Arguments: imol (a whole number), chain_id (text), resno_start (a whole number), resno_end (a whole number), imol_map (a whole number), file_name_for_sequences (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `apply_sequence_to_fragment(0, "A", 41, 45, 1, "tutorial-modern.pdb")` | ran (no return value) |
| Scheme | `(apply-sequence-to-fragment 0 "A" 41 45 1 "tutorial-modern.pdb")` | ran (no return value) |

### assign_sequence_to_active_fragment

Python: `assign_sequence_to_active_fragment()`  
Scheme: `(assign-sequence-to-active-fragment)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `assign_sequence_to_active_fragment()` | ran (no return value) |
| Scheme | `(assign-sequence-to-active-fragment)` | ran (no return value) |

### atom_spec_from_python_expression

Python: `atom_spec_from_python_expression(expr)`

Arguments: expr (a list or value). Returns: `coot::atom_spec_t`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### atom-spec-from-scm-expression

Scheme: `(atom-spec-from-scm-expression expr)`

expects an expr of length 5, ie: (list chain-id res-no ins-cod atom-name alt-conf)

Arguments: expr (a list or value). Returns: `coot::atom_spec_t`.
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### atom_spec_to_py

Python: `atom_spec_to_py(spec)`  
Scheme: `(atom-spec-to-scm spec)`

Arguments: spec (`coot::atom_spec_t`). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### coot_get_url

Python: `coot_get_url(url, file_name)`  
Scheme: `(coot-get-url url file-name)`

return 0 on success.

Arguments: url (text), file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_get_url("hello", "tutorial-modern.pdb")` | not run: not run automatically (url: exits, uses the network, an external program, files or a screen) |
| Scheme | `(coot-get-url "hello" "tutorial-modern.pdb")` | not run: not run automatically (url: exits, uses the network, an external program, files or a screen) |

### coot_get_url_and_activate_curl_hook

Python: `coot_get_url_and_activate_curl_hook(url, file_name, do_hook_flag)`  
Scheme: `(coot-get-url-and-activate-curl-hook url file-name do-hook-flag)`

Arguments: url (text), file_name (text), do_hook_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_get_url_and_activate_curl_hook("hello", "tutorial-modern.pdb", 1)` | not run: not run automatically (curl: exits, uses the network, an external program, files or a screen) |
| Scheme | `(coot-get-url-and-activate-curl-hook "hello" "tutorial-modern.pdb" 1)` | not run: not run automatically (curl: exits, uses the network, an external program, files or a screen) |

### coot_get_url_as_string

Python: `coot_get_url_as_string(url)`  
Scheme: `(coot-get-url-as-string url)`

this handles URLs that are strings, not binaries.

Arguments: url (text). Returns: a value (see the result of the example).
Also available in Python as `coot_get_url_as_string_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_get_url_as_string("hello")` | not run: not run automatically (url: exits, uses the network, an external program, files or a screen) |
| Scheme | `(coot-get-url-as-string "hello")` | not run: not run automatically (url: exits, uses the network, an external program, files or a screen) |

### coot_get_url_as_string_internal

Python: `coot_get_url_as_string_internal(url)`  
Scheme: `(coot-get-url-as-string-internal url)`

internal use (strings, not binaries).

Arguments: url (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_get_url_as_string_internal("hello")` | not run: not run automatically (url: exits, uses the network, an external program, files or a screen) |
| Scheme | `(coot-get-url-as-string-internal "hello")` | not run: not run automatically (url: exits, uses the network, an external program, files or a screen) |

### curl_progress_info

Python: `curl_progress_info(file_name)`  
Scheme: `(curl-progress-info file-name)`

for the callback of the update binary progress bar. How much done
is the file that I am downloading? Not absolutely required for python

Arguments: file_name (text). Returns: a value (see the result of the example).
Also available in Python as `curl_progress_info_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `curl_progress_info("tutorial-modern.pdb")` | not run: not run automatically (curl: exits, uses the network, an external program, files or a screen) |
| Scheme | `(curl-progress-info "tutorial-modern.pdb")` | not run: not run automatically (curl: exits, uses the network, an external program, files or a screen) |

### fetch_alphafold_model_for_uniprot_id

Python: `fetch_alphafold_model_for_uniprot_id(uniprot_id)`  
Scheme: `(fetch-alphafold-model-for-uniprot-id uniprot-id)`

return the model number

Arguments: uniprot_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fetch_alphafold_model_for_uniprot_id("hello")` | not run: not run automatically (fetch: exits, uses the network, an external program, files or a screen) |
| Scheme | `(fetch-alphafold-model-for-uniprot-id "hello")` | not run: not run automatically (fetch: exits, uses the network, an external program, files or a screen) |

### fetch_and_superpose_alphafold_models

Python: `fetch_and_superpose_alphafold_models(imol)`  
Scheme: `(fetch-and-superpose-alphafold-models imol)`

fetch and superpose AlphaFold models corresponding to model
model must have Uniprot DBREF info in the header.

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fetch_and_superpose_alphafold_models(0)` | not run: not run automatically (fetch: exits, uses the network, an external program, files or a screen) |
| Scheme | `(fetch-and-superpose-alphafold-models 0)` | not run: not run automatically (fetch: exits, uses the network, an external program, files or a screen) |

### generic_int_vector_to_list_internal

Python: `generic_int_vector_to_list_internal(v)`  
Scheme: `(generic-int-vector-to-list-internal v)`

Arguments: v (a list). Returns: a value (see the result of the example).
Also available in Python as `generic_int_vector_to_list_internal_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### generic_list_to_string_vector_internal

Python: `generic_list_to_string_vector_internal(l)`  
Scheme: `(generic-list-to-string-vector-internal l)`

Arguments: l (a list or value). Returns: a list.
Also available in Python as `generic_list_to_string_vector_internal_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### generic_string_vector_to_list_internal

Python: `generic_string_vector_to_list_internal(v)`  
Scheme: `(generic-string-vector-to-list-internal v)`

Arguments: v (a list). Returns: a value (see the result of the example).
Also available in Python as `generic_string_vector_to_list_internal_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `generic_string_vector_to_list_internal("hello")` | ran, returned `['h', 'e', 'l', 'l', 'o']` |
| Scheme | `(generic-string-vector-to-list-internal "hello")` | error: In procedure generic-string-vector-to-list-internal: Wrong type argument in position 1: "hello" |

### get_coords_for_accession_code

Python: `get_coords_for_accession_code(code)`  
Scheme: `(get-coords-for-accession-code code)`

if possible, read in the new coords getting coords via web.

(no return value because get-url-str does not return one).

Arguments: code (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_coords_for_accession_code("hello")` | ran (no return value) |
| Scheme | `(get-coords-for-accession-code "hello")` | ran (no return value) |

### get_drug_mdl_via_wikipedia_and_drugbank

Python: `get_drug_mdl_via_wikipedia_and_drugbank(drugname)`  
Scheme: `(get-drug-mdl-via-wikipedia-and-drugbank drugname)`

Arguments: drugname (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_drug_mdl_via_wikipedia_and_drugbank("my-name")` | ran, returned `''` |
| Scheme | `(get-drug-mdl-via-wikipedia-and-drugbank "my-name")` | ran, returned `""` |

### inverse_rtop

Python: `inverse_rtop(rtop_py)`  
Scheme: `(inverse-rtop rtop-scm)`

Arguments: rtop_py (a list or value). Returns: a value (see the result of the example).
Also available in Python as `inverse_rtop_py`.
Also available in Scheme as `inverse-rtop-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

### is_interesting_dots_object_next_p

Python: `is_interesting_dots_object_next_p(vs)`  
Scheme: `(is-interesting-dots-object-next-p vs)`

return a clean name and a flag to say that this was something that
we were interested to make a graphics object from (rather than just
header info)

Arguments: vs (a list). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `is_interesting_dots_object_next_p("hello")` | not tried |
| Scheme | `(is-interesting-dots-object-next-p "hello")` | not tried |

### make_complementary_dotted_surfaces

Python: `make_complementary_dotted_surfaces(imol_1, imol_2, r1, r2)`  
Scheme: `(make-complementary-dotted-surfaces imol-1 imol-2 r1 r2)`

Arguments: imol_1 (a whole number), imol_2 (a whole number), r1 (a list), r2 (a list). Returns: `clipper::Coord_orth`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

### orient_view

Python: `orient_view(imol, central_residue_spec, neighbour_residue_spec)`  
Scheme: `(orient-view imol central-residue-spec neighbour-residue-spec)`

orient the graphics somehow so that the interaction between
central_residue and neighbour_residue is perpendicular to screen z.

Arguments: imol (a whole number), central_residue_spec (`coot::residue_spec_t`), neighbour_residue_spec (`// ligand typically  coot::residue_spec_t`). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

### pisa_interfaces_display_only

Python: `pisa_interfaces_display_only(imol_1, imol_2, centre_pt)`  
Scheme: `(pisa-interfaces-display-only imol-1 imol-2 centre-pt)`

Arguments: imol_1 (a whole number), imol_2 (a whole number), centre_pt (`clipper::Coord_orth`). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

### residue_records_list_py_to_residue_specs

Python: `residue_records_list_py_to_residue_specs(mol_1_residue_records, chain_id)`

Arguments: mol_1_residue_records (a list or value), chain_id (text). Returns: a list.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |

### residue-records-list-scm-to-residue-specs

Scheme: `(residue-records-list-scm-to-residue-specs mol-1-residue-records chain-id)`

Arguments: mol-1-residue-records (a list or value), chain-id (text). Returns: a list.
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | (no automatic example) | not tried |

### rtop-to-scm

Scheme: `(rtop-to-scm rtop)`

Arguments: rtop (`clipper::RTop_orth`). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | (no automatic example) | not tried |

### rtop_to_python

Python: `rtop_to_python(rtop)`

Arguments: rtop (`clipper::RTop_orth`). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |

### sequence_from_map

Python: `sequence_from_map(imol, chain_id, resno_start, resno_end, imol_map)`  
Scheme: `(sequence-from-map imol chain-id resno-start resno-end imol-map)`

Arguments: imol (a whole number), chain_id (text), resno_start (a whole number), resno_end (a whole number), imol_map (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `sequence_from_map(0, "A", 41, 45, 1)` | not tried |
| Scheme | `(sequence-from-map 0 "A" 41 45 1)` | not tried |

### set_display_control_button_state

Python: `set_display_control_button_state(imol, button_type, state)`  
Scheme: `(set-display-control-button-state imol button-type state)`

Arguments: imol (a whole number), button_type (text), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_display_control_button_state(0, "hello", 1)` | not tried |
| Scheme | `(set-display-control-button-state 0 "hello" 1)` | not tried |

### stop_curl_download

Python: `stop_curl_download(file_name)`  
Scheme: `(stop-curl-download file-name)`

Arguments: file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `stop_curl_download("tutorial-modern.pdb")` | not tried |
| Scheme | `(stop-curl-download "tutorial-modern.pdb")` | not tried |

### symbol-value-from-record

Scheme: `(symbol-value-from-record record-1 symbol)`

Arguments: record-1 (a list or value), symbol (text). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | (no automatic example) | not tried |

### topological_equivalence_chiral_centres

Python: `topological_equivalence_chiral_centres(residue_type)`  
Scheme: `(topological-equivalence-chiral-centres residue-type)`

return a list of chiral centre ids as determined from topological
 equivalence analysis based on the bond info (and element names).

Arguments: residue_type (text). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `topological_equivalence_chiral_centres("ALA")` | not tried |
| Scheme | `(topological-equivalence-chiral-centres "ALA")` | not tried |

### untangle_mmdb_chain_id_string

Python: `untangle_mmdb_chain_id_string(mmdb_chain_id_in)`  
Scheme: `(untangle-mmdb-chain-id-string mmdb-chain-id-in)`

Arguments: mmdb_chain_id_in (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `untangle_mmdb_chain_id_string("A")` | not tried |
| Scheme | `(untangle-mmdb-chain-id-string "A")` | not tried |

### wrapped_curl_easy_perform

Python: `wrapped_curl_easy_perform(data)`  
Scheme: `(wrapped-curl-easy-perform data)`

Arguments: data (`void *`). Returns: `void *`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

### write_coot_curl_data

Python: `write_coot_curl_data(buffer, size, nmemb, userp)`  
Scheme: `(write-coot-curl-data buffer size nmemb userp)`

internal use

Arguments: buffer (`void *`), size (a whole number), nmemb (a whole number), userp (`void *`). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

### write_coot_curl_data_to_file

Python: `write_coot_curl_data_to_file(buffer, size, nmemb, userp)`  
Scheme: `(write-coot-curl-data-to-file buffer size nmemb userp)`

internal use

Arguments: buffer (`void *`), size (a whole number), nmemb (a whole number), userp (`void *`). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

