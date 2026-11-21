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
| Python | first `obj = new_generic_object_number("bond")`, then `add_generic_object_bond(0, 0, atom_spec_from_python_expression(["A", 41, "", " CA ", ""]), atom_spec_from_python_expression(["A", 43, "", " CA ", ""]), obj, "red")` | ran (no return value, nothing visible changed) |
| Scheme | first `(define obj (new-generic-object-number "bond"))`, then `(add-generic-object-bond 0 0 (atom-spec-from-scm-expression (list "A" 41 "" " CA " "")) (atom-spec-from-scm-expression (list "A" 43 "" " CA " "")) obj "red")` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: draws a dashed line between the two atoms in the generic object. The atom specs must be C++ atom_spec_t objects (made with atom_spec_from_python_expression / atom-spec-from-scm-expression); plain lists give a TypeError.

### apply_sequence_to_fragment

Python: `apply_sequence_to_fragment(imol, chain_id, resno_start, resno_end, imol_map, file_name_for_sequences)`  
Scheme: `(apply-sequence-to-fragment imol chain-id resno-start resno-end imol-map file-name-for-sequences)`

Arguments: imol (a whole number), chain_id (text), resno_start (a whole number), resno_end (a whole number), imol_map (a whole number), file_name_for_sequences (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `apply_sequence_to_fragment(0, "A", 41, 45, 1, "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(apply-sequence-to-fragment 0 "A" 41 45 1 "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

### assign_sequence_to_active_fragment

Python: `assign_sequence_to_active_fragment()`  
Scheme: `(assign-sequence-to-active-fragment)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `assign_sequence_to_active_fragment()` | ran (no return value); changed: molecule 0: atoms of 8 residue(s) (A4, A26, A34, A50 ...); n_atoms(0): 1465 -> 1473 |
| Scheme | `(assign-sequence-to-active-fragment)` | ran (no return value, nothing visible changed) |

### atom_spec_from_python_expression

Python: `atom_spec_from_python_expression(expr)`

Arguments: expr (a list or value). Returns: `coot::atom_spec_t`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `atom_spec_from_python_expression(["A", 41, "", " CA ", ""])` | ran, returned `<coot.atom_spec_t; proxy of <Swig Object of type 'coot::atom_spec_t *' at 0x10c767840> >` |

Example written and checked by hand on the test data. Expected: a C++ atom_spec_t object made from [chain, resno, ins-code, atom-name, alt-conf]; pass it to functions that need one (e.g. add_generic_object_bond). (Python only.).

### atom-spec-from-scm-expression

Scheme: `(atom-spec-from-scm-expression expr)`

expects an expr of length 5, ie: (list chain-id res-no ins-cod atom-name alt-conf)

Arguments: expr (a list or value). Returns: `coot::atom_spec_t`.
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | `(atom-spec-from-scm-expression (list "A" 41 "" " CA " ""))` | ran, returned `#<collectable-swig-pointer coot::atom_spec_t * 8ef1915e0>` |

Example written and checked by hand on the test data. Expected: a C++ atom_spec_t object made from (chain resno ins-code atom-name alt-conf). (Scheme only.).

### atom_spec_to_py

Python: `atom_spec_to_py(spec)`  
Scheme: `(atom-spec-to-scm spec)`

Arguments: spec (`coot::atom_spec_t`). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `atom_spec_to_py(atom_spec_from_python_expression(["A", 41, "", " CA ", ""]))` | ran, returned `[-1, 'A', 41, '', ' CA ', '']` |
| Scheme | `(atom-spec-to-scm (atom-spec-from-scm-expression (list "A" 41 "" " CA " "")))` | ran, returned `(-1 "A" 41 "" " CA " "")` |

Example written and checked by hand on the test data. Expected: the atom spec as a list [model/imol (-1 = unset), chain, resno, ins-code, atom-name, alt-conf].

Python and Scheme gave the same answer.

### coot_get_url

Python: `coot_get_url(url, file_name)`  
Scheme: `(coot-get-url url file-name)`

return 0 on success.

Arguments: url (text), file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_get_url("https://files.rcsb.org/download/1ehz.pdb", "1ehz-dl.pdb")` | not run: needs the network (downloads with libcurl) |
| Scheme | `(coot-get-url "https://files.rcsb.org/download/1ehz.pdb" "1ehz-dl.pdb")` | not run: needs the network (downloads with libcurl) |

Example written and checked by hand on the test data. Expected: downloads the URL to the file; returns 0 on success.

### coot_get_url_and_activate_curl_hook

Python: `coot_get_url_and_activate_curl_hook(url, file_name, do_hook_flag)`  
Scheme: `(coot-get-url-and-activate-curl-hook url file-name do-hook-flag)`

Arguments: url (text), file_name (text), do_hook_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_get_url_and_activate_curl_hook("https://files.rcsb.org/download/1ehz.pdb", "1ehz-dl.pdb", 1)` | not run: needs the network (downloads with libcurl) |
| Scheme | `(coot-get-url-and-activate-curl-hook "https://files.rcsb.org/download/1ehz.pdb" "1ehz-dl.pdb" 1)` | not run: needs the network (downloads with libcurl) |

Example written and checked by hand on the test data. Expected: downloads the URL to the file and then runs the download-finished hook; returns 0 on success.

### coot_get_url_as_string

Python: `coot_get_url_as_string(url)`  
Scheme: `(coot-get-url-as-string url)`

this handles URLs that are strings, not binaries.

Arguments: url (text). Returns: a value (see the result of the example).
Also available in Python as `coot_get_url_as_string_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_get_url_as_string("https://files.rcsb.org/header/1ehz.pdb")` | not run: needs the network (downloads with libcurl) |
| Scheme | `(coot-get-url-as-string "https://files.rcsb.org/header/1ehz.pdb")` | not run: needs the network (downloads with libcurl) |

Example written and checked by hand on the test data. Expected: the text at the URL as a string.

### coot_get_url_as_string_internal

Python: `coot_get_url_as_string_internal(url)`  
Scheme: `(coot-get-url-as-string-internal url)`

internal use (strings, not binaries).

Arguments: url (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_get_url_as_string_internal("https://files.rcsb.org/header/1ehz.pdb")` | not run: needs the network (downloads with libcurl) |
| Scheme | `(coot-get-url-as-string-internal "https://files.rcsb.org/header/1ehz.pdb")` | not run: needs the network (downloads with libcurl) |

Example written and checked by hand on the test data. Expected: internal form of coot_get_url_as_string: the text at the URL.

### curl_progress_info

Python: `curl_progress_info(file_name)`  
Scheme: `(curl-progress-info file-name)`

for the callback of the update binary progress bar. How much done
is the file that I am downloading? Not absolutely required for python

Arguments: file_name (text). Returns: a value (see the result of the example).
Also available in Python as `curl_progress_info_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `curl_progress_info("x.pdb")` | ran, returned `False` |
| Scheme | `(curl-progress-info "x.pdb")` | ran, returned `#f` |

Example written and checked by hand on the test data. Expected: progress information of a running download to that file; False when none is running.

Python and Scheme gave the same answer.

### fetch_alphafold_model_for_uniprot_id

Python: `fetch_alphafold_model_for_uniprot_id(uniprot_id)`  
Scheme: `(fetch-alphafold-model-for-uniprot-id uniprot-id)`

return the model number

Arguments: uniprot_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fetch_alphafold_model_for_uniprot_id("P00698")` | not run: needs the network (downloads with libcurl) |
| Scheme | `(fetch-alphafold-model-for-uniprot-id "P00698")` | not run: needs the network (downloads with libcurl) |

Example written and checked by hand on the test data. Expected: downloads the AlphaFold model for the UniProt id and returns its new molecule number.

### fetch_and_superpose_alphafold_models

Python: `fetch_and_superpose_alphafold_models(imol)`  
Scheme: `(fetch-and-superpose-alphafold-models imol)`

fetch and superpose AlphaFold models corresponding to model
model must have Uniprot DBREF info in the header.

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fetch_and_superpose_alphafold_models(0)` | not run: needs the network (downloads with libcurl) |
| Scheme | `(fetch-and-superpose-alphafold-models 0)` | not run: needs the network (downloads with libcurl) |

Example written and checked by hand on the test data. Expected: downloads the AlphaFold models for the UniProt DBREF records of molecule 0 and superposes them (tutorial-modern.pdb has no DBREF: nothing would be fetched).

### generic_int_vector_to_list_internal

Python: `generic_int_vector_to_list_internal(v)`  
Scheme: `(generic-int-vector-to-list-internal v)`

Arguments: v (a list). Returns: a value (see the result of the example).
Also available in Python as `generic_int_vector_to_list_internal_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `generic_int_vector_to_list_internal([1, 2, 3])` | ran, returned `[1, 2, 3]` |
| Scheme | `(generic-int-vector-to-list-internal (list 1 2 3))` | ran, returned `(1 2 3)` |

Example written and checked by hand on the test data. Expected: the same numbers as a list (converter between C++ std::vector<int> and lists; internal helper).

Python and Scheme gave the same answer.

### generic_list_to_string_vector_internal

Python: `generic_list_to_string_vector_internal(l)`  
Scheme: `(generic-list-to-string-vector-internal l)`

Arguments: l (a list or value). Returns: a list.
Also available in Python as `generic_list_to_string_vector_internal_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `generic_list_to_string_vector_internal(["a", "b"])` | ran, returned `('a', 'b')` |
| Scheme | `(generic-list-to-string-vector-internal (list "a" "b"))` | ran, returned `#("a" "b")` |

Example written and checked by hand on the test data. Expected: the strings converted to a C++ std::vector<string>, shown as a tuple (Python) / vector (Scheme); internal helper.

Python and Scheme gave the same answer.

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
| Python | `get_coords_for_accession_code("hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(get-coords-for-accession-code "hello")` | ran (no return value, nothing visible changed) |

### get_drug_mdl_via_wikipedia_and_drugbank

Python: `get_drug_mdl_via_wikipedia_and_drugbank(drugname)`  
Scheme: `(get-drug-mdl-via-wikipedia-and-drugbank drugname)`

Arguments: drugname (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_drug_mdl_via_wikipedia_and_drugbank("my-name")` | ran, returned `''` |
| Scheme | `(get-drug-mdl-via-wikipedia-and-drugbank "my-name")` | ran, returned `""` |

Python and Scheme gave the same answer.

### inverse_rtop

Python: `inverse_rtop(rtop_py)`  
Scheme: `(inverse-rtop rtop-scm)`

Arguments: rtop_py (a list or value). Returns: a value (see the result of the example).
Also available in Python as `inverse_rtop_py`.
Also available in Scheme as `inverse-rtop-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `inverse_rtop([[1, 0, 0, 0, 1, 0, 0, 0, 1], [1.0, 2.0, 3.0]])` | ran, returned `[[1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [-1.0, -2.0, -3.0]]` |
| Scheme | `(inverse-rtop (list (list 1 0 0 0 1 0 0 0 1) (list 1.0 2.0 3.0)))` | ran, returned `((1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0) (-1.0 -2.0 -3.0))` |

Example written and checked by hand on the test data. Expected: the inverse of the operator [rotation (9 numbers, row by row), translation]: here identity and the negated shift.

Python and Scheme gave the same answer.

### is_interesting_dots_object_next_p

Python: `is_interesting_dots_object_next_p(vs)`  
Scheme: `(is-interesting-dots-object-next-p vs)`

return a clean name and a flag to say that this was something that
we were interested to make a graphics object from (rather than just
header info)

Arguments: vs (a list). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `is_interesting_dots_object_next_p("hello")` | ran, returned `<Swig Object of type 'std::pair< short,std::string > *' at 0x10a4570c0>` |
| Scheme | `(is-interesting-dots-object-next-p "hello")` | error: In procedure is-interesting-dots-object-next-p: Wrong type argument in position 1: "hello" |

### make_complementary_dotted_surfaces

Python: `make_complementary_dotted_surfaces(imol_1, imol_2, r1, r2)`  
Scheme: `(make-complementary-dotted-surfaces imol-1 imol-2 r1 r2)`

Arguments: imol_1 (a whole number), imol_2 (a whole number), r1 (a list), r2 (a list). Returns: `clipper::Coord_orth`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `specs_a = residue_records_list_py_to_residue_specs([{"seq_num": "40", "ins_code": ""}], "A")`, then `specs_b = residue_records_list_py_to_residue_specs([{"seq_num": "40", "ins_code": ""}], "B")`, then `make_complementary_dotted_surfaces(0, 0, specs_a, specs_b)` | ran, returned `<Swig Object of type 'clipper::Coord_orth *' at 0x10a3f0150>`; changed: n_dots_sets(0): 0 -> 2 |
| Scheme | first `(define mk (record-constructor (make-record-type 'residue-rec '(seq-num ins-code))))`, then `(make-complementary-dotted-surfaces 0 0 (residue-records-list-scm-to-residue-specs (list (mk "40" "")) "A") (residue-records-list-scm-to-residue-specs (list (mk "40" "")) "B"))` | ran, returned `#<collectable-swig-pointer clipper::Coord_orth * 897855f80>`; changed: n_dots_sets(0): 2 -> 4 |

Example written and checked by hand on the test data. Expected: adds two dot surfaces (one per residue set) to molecule 0 and returns their mid point as a C++ Coord_orth (used by the PISA interface code). Residue lists must be C++ vectors (made with residue_records_list_*_to_residue_specs).

### orient_view

Python: `orient_view(imol, central_residue_spec, neighbour_residue_spec)`  
Scheme: `(orient-view imol central-residue-spec neighbour-residue-spec)`

orient the graphics somehow so that the interaction between
central_residue and neighbour_residue is perpendicular to screen z.

Arguments: imol (a whole number), central_residue_spec (`coot::residue_spec_t`), neighbour_residue_spec (`// ligand typically  coot::residue_spec_t`). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `orient_view(0, residue_spec_t("A", 41, ""), residue_spec_t("A", 43, ""))` | ran (no return value, nothing visible changed) |
| Scheme | `(orient-view 0 (new-residue-spec-t "A" 41 "") (new-residue-spec-t "A" 43 ""))` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: turns the view so that the A41 -> A43 vector lies in the screen plane; only acts with a graphics window (no-op headless). The residues must be C++ residue_spec_t objects; plain lists give a TypeError.

### pisa_interfaces_display_only

Python: `pisa_interfaces_display_only(imol_1, imol_2, centre_pt)`  
Scheme: `(pisa-interfaces-display-only imol-1 imol-2 centre-pt)`

Arguments: imol_1 (a whole number), imol_2 (a whole number), centre_pt (`clipper::Coord_orth`). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `specs_a = residue_records_list_py_to_residue_specs([{"seq_num": "40", "ins_code": ""}], "A")`, then `specs_b = residue_records_list_py_to_residue_specs([{"seq_num": "40", "ins_code": ""}], "B")`, then `c = make_complementary_dotted_surfaces(0, 0, specs_a, specs_b)`, then `pisa_interfaces_display_only(0, 0, c)` | ran (no return value); changed: rotation centre moved 15.1 A to (31.6, 6.5, 24.0) |
| Scheme | first `(define mk (record-constructor (make-record-type 'residue-rec '(seq-num ins-code))))`, then `(define c (make-complementary-dotted-surfaces 0 0 (residue-records-list-scm-to-residue-specs (list (mk "40" "")) "A") (residue-records-list-scm-to-residue-specs ...`, then `(pisa-interfaces-display-only 0 0 c)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: shows only the two interface molecules and centres the view on the interface point.

Note: Python cannot pass the Coord_orth that make_complementary_dotted_surfaces returns (an untyped pointer object), so the Python version is unusable from scripts; Scheme works.

### residue_records_list_py_to_residue_specs

Python: `residue_records_list_py_to_residue_specs(mol_1_residue_records, chain_id)`

Arguments: mol_1_residue_records (a list or value), chain_id (text). Returns: a list.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_records_list_py_to_residue_specs([{"seq_num": "40", "ins_code": ""}, {"seq_num": "45", "ins_code": ""}], "A")` | ran, returned `<Swig Object of type 'std::vector< coot::residue_spec_t,std::allocator< coot::residue_spec_t > > *' at 0x10785f5a0>` |

Example written and checked by hand on the test data. Expected: a C++ vector of residue specs from PISA-style residue records (dicts with seq_num/ins_code as strings) in chain A. (Python only.).

### residue-records-list-scm-to-residue-specs

Scheme: `(residue-records-list-scm-to-residue-specs mol-1-residue-records chain-id)`

Arguments: mol-1-residue-records (a list or value), chain-id (text). Returns: a list.
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | first `(define mk (record-constructor (make-record-type 'residue-rec '(seq-num ins-code))))`, then `(residue-records-list-scm-to-residue-specs (list (mk "40" "") (mk "45" "")) "A")` | ran, returned `#<collectable-swig-pointer std::vector< coot::residue_spec_t > * a45167d00>` |

Example written and checked by hand on the test data. Expected: a C++ vector of residue specs from PISA residue records (Guile records with fields seq-num and ins-code, as strings). (Scheme only.).

### rtop-to-scm

Scheme: `(rtop-to-scm rtop)`

Arguments: rtop (`clipper::RTop_orth`). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | `(rtop-to-scm (list (list 1 0 0 0 1 0 0 0 1) (list 1.0 2.0 3.0)))` | not run: not callable from scripting: needs a C++ clipper::RTop_orth object that scripts cannot make |

Example written and checked by hand on the test data. Expected: converts a C++ clipper RTop_orth to a list; no script function returns an RTop_orth, so it cannot be used from scripts (inverse-rtop shows the list format).

### rtop_to_python

Python: `rtop_to_python(rtop)`

Arguments: rtop (`clipper::RTop_orth`). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `rtop_to_python([[1, 0, 0, 0, 1, 0, 0, 0, 1], [1.0, 2.0, 3.0]])` | not run: not callable from scripting: needs a C++ clipper::RTop_orth object that scripts cannot make |

Example written and checked by hand on the test data. Expected: converts a C++ clipper RTop_orth to a list; not usable from scripts (inverse_rtop shows the list format).

### sequence_from_map

Python: `sequence_from_map(imol, chain_id, resno_start, resno_end, imol_map)`  
Scheme: `(sequence-from-map imol chain-id resno-start resno-end imol-map)`

Arguments: imol (a whole number), chain_id (text), resno_start (a whole number), resno_end (a whole number), imol_map (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `sequence_from_map(0, "A", 41, 45, 1)` | ran, returned `'XXXXX'` |
| Scheme | `(sequence-from-map 0 "A" 41 45 1)` | ran, returned `"XXXXX"` |

Python and Scheme gave the same answer.

### set_display_control_button_state

Python: `set_display_control_button_state(imol, button_type, state)`  
Scheme: `(set-display-control-button-state imol button-type state)`

Arguments: imol (a whole number), button_type (text), state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_display_control_button_state(0, "hello", 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-display-control-button-state 0 "hello" 1)` | ran (no return value, nothing visible changed) |

### stop_curl_download

Python: `stop_curl_download(file_name)`  
Scheme: `(stop-curl-download file-name)`

Arguments: file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `stop_curl_download("x.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(stop-curl-download "x.pdb")` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: asks a running download to that file to stop; no effect when none is running.

### symbol-value-from-record

Scheme: `(symbol-value-from-record record-1 symbol)`

Arguments: record-1 (a list or value), symbol (text). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | first `(define mk (record-constructor (make-record-type 'residue-rec '(seq-num ins-code))))`, then `(symbol-value-from-record (mk "41" "") "seq-num")` | ran, returned `"41"` |

Example written and checked by hand on the test data. Expected: the value of the named field of a Guile record (helper of the PISA code). (Scheme only.).

### topological_equivalence_chiral_centres

Python: `topological_equivalence_chiral_centres(residue_type)`  
Scheme: `(topological-equivalence-chiral-centres residue-type)`

return a list of chiral centre ids as determined from topological
 equivalence analysis based on the bond info (and element names).

Arguments: residue_type (text). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `topological_equivalence_chiral_centres("ALA")` | ran, returned `()` |
| Scheme | `(topological-equivalence-chiral-centres "ALA")` | ran, returned `#()` |

Python and Scheme gave the same answer.

### untangle_mmdb_chain_id_string

Python: `untangle_mmdb_chain_id_string(mmdb_chain_id_in)`  
Scheme: `(untangle-mmdb-chain-id-string mmdb-chain-id-in)`

Arguments: mmdb_chain_id_in (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `untangle_mmdb_chain_id_string("A")` | ran, returned `'A'` |
| Scheme | `(untangle-mmdb-chain-id-string "A")` | ran, returned `"A"` |

Python and Scheme gave the same answer.

### wrapped_curl_easy_perform

Python: `wrapped_curl_easy_perform(data)`  
Scheme: `(wrapped-curl-easy-perform data)`

Arguments: data (`void *`). Returns: `void *`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `wrapped_curl_easy_perform(None)` | not run: internal libcurl callback with raw pointer arguments: not usable from scripts (Python call with None can crash Coot) |
| Scheme | `(wrapped-curl-easy-perform #f)` | not run: internal libcurl callback with raw pointer arguments: not usable from scripts (Python call with None can crash Coot) |

Example written and checked by hand on the test data. Expected: internal libcurl callback (takes raw C pointers); not for scripts.

### write_coot_curl_data

Python: `write_coot_curl_data(buffer, size, nmemb, userp)`  
Scheme: `(write-coot-curl-data buffer size nmemb userp)`

internal use

Arguments: buffer (`void *`), size (a whole number), nmemb (a whole number), userp (`void *`). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_coot_curl_data(None, 1, 1, None)` | not run: internal libcurl callback with raw pointer arguments: not usable from scripts (Python call with None can crash Coot) |
| Scheme | `(write-coot-curl-data #f 1 1 #f)` | not run: internal libcurl callback with raw pointer arguments: not usable from scripts (Python call with None can crash Coot) |

Example written and checked by hand on the test data. Expected: internal libcurl callback (takes raw C pointers); not for scripts.

### write_coot_curl_data_to_file

Python: `write_coot_curl_data_to_file(buffer, size, nmemb, userp)`  
Scheme: `(write-coot-curl-data-to-file buffer size nmemb userp)`

internal use

Arguments: buffer (`void *`), size (a whole number), nmemb (a whole number), userp (`void *`). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_coot_curl_data_to_file(None, 1, 1, None)` | not run: internal libcurl callback with raw pointer arguments: not usable from scripts (Python call with None can crash Coot) |
| Scheme | `(write-coot-curl-data-to-file #f 1 1 #f)` | not run: internal libcurl callback with raw pointer arguments: not usable from scripts (Python call with None can crash Coot) |

Example written and checked by hand on the test data. Expected: internal libcurl callback (takes raw C pointers); not for scripts.

Note: Python call with None arguments crashes Coot (NULL FILE pointer).

