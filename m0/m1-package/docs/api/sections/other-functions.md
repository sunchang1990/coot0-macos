# Other functions

[Scripting reference](../README.md) > Other functions (11 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### clear_generic_objects_dialog_pointer

Python: `clear_generic_objects_dialog_pointer()`  
Scheme: `(clear-generic-objects-dialog-pointer)`

\file
 Coot Scripting Interface - Generic objects

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_generic_objects_dialog_pointer()` | ran (no return value, nothing visible changed) |
| Scheme | `(clear-generic-objects-dialog-pointer)` | ran (no return value, nothing visible changed) |

### close_all_generic_objects

Python: `close_all_generic_objects()`  
Scheme: `(close-all-generic-objects)`

close all generic display objects

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `close_all_generic_objects()` | ran (no return value, nothing visible changed) |
| Scheme | `(close-all-generic-objects)` | ran (no return value, nothing visible changed) |

### compare_atom_specs_user_float

Python: `compare_atom_specs_user_float()`  
Scheme: `(compare-atom-specs-user-float)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `spec1 = atom_spec_t("A", 41, "", " CA ", ""); spec1.float_user_data = 1.0`, then `spec2 = atom_spec_t("A", 42, "", " CA ", ""); spec2.float_user_data = 2.0`, then `compare_atom_specs_user_float(spec1, spec2)` | ran, returned `True` |
| Scheme | first `(define s1 (new-atom-spec-t "A" 41 "" " CA " ""))`, then `(define s2 (new-atom-spec-t "A" 42 "" " CA " ""))`, then `(atom-spec-t-float-user-data-set s1 1.0)`, then `(atom-spec-t-float-user-data-set s2 2.0)`, then `(compare-atom-specs-user-float s1 s2)` | ran, returned `#t` |

Example written and checked by hand on the test data. Expected: C++ sort helper: True when the first spec's float_user_data is smaller than the second's.

Note: Takes atom_spec_t objects (from atom_spec_from_python_expression), not lists.

Python and Scheme gave the same answer.

### compare_atom_specs_user_float_in_pair

Python: `compare_atom_specs_user_float_in_pair()`  
Scheme: `(compare-atom-specs-user-float-in-pair)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `compare_atom_specs_user_float_in_pair()` | not run: internal C++ helper: needs a std::pair<atom_spec_t, std::string>, which scripts cannot build |
| Scheme | `(compare-atom-specs-user-float-in-pair)` | not run: internal C++ helper: needs a std::pair<atom_spec_t, std::string>, which scripts cannot build |

Example written and checked by hand on the test data. Expected: C++ sort helper on (atom_spec_t, string) pairs.

### coot_version

Python: `coot_version()`  
Scheme: `(coot-version)`

the coot version string 

 Returns something like "coot-0.1.3". New versions of coot will
 always be lexographically greater than previous versions.

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_version()` | ran, returned `'0.9.8.96'` |
| Scheme | `(coot-version)` | ran, returned `"0.9.8.96"` |

Python and Scheme gave the same answer.

### coot_version_extra_info

Python: `coot_version_extra_info()`  
Scheme: `(coot-version-extra-info)`

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_version_extra_info()` | ran, returned `'(revision-count 10988)\n[with guile 3.0.10 embedded]\n[with python 3.11.18 embedded]\ngit commit: 50638a38145722303017b ...` |
| Scheme | `(coot-version-extra-info)` | ran, returned `"(revision-count 10988)\n[with guile 3.0.10 embedded]\n[with python 3.11.18 embedded]\ngit commit: 50638a38145722303017b ...` |

Python and Scheme gave the same answer.

### generic_objects_gui_wrapper

Python: `generic_objects_gui_wrapper()`  
Scheme: `(generic-objects-gui-wrapper)`

a kludgey thing, so that the generic objects gui can be
 called from a callback.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `generic_objects_gui_wrapper()` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(generic-objects-gui-wrapper)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens the Generic Display Objects window.

### link_atoms

Python: `link_atoms()`  
Scheme: `(link-atoms)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `link_atoms()` | not run: internal C++ helper: needs an mmdb::Link/LinkR pointer, which scripts cannot obtain |
| Scheme | `(link-atoms)` | not run: internal C++ helper: needs an mmdb::Link/LinkR pointer, which scripts cannot obtain |

Example written and checked by hand on the test data. Expected: C++ helper returning the two atom specs of an mmdb Link record.

### set_display_all_generic_objects

Python: `set_display_all_generic_objects(state)`  
Scheme: `(set-display-all-generic-objects state)`

display (1) or undisplay (0) all generic display objects

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_display_all_generic_objects(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-display-all-generic-objects 1)` | ran (no return value, nothing visible changed) |

### try_load_python_extras_dir

Python: `try_load_python_extras_dir()`

Arguments: none. Returns: nothing.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `try_load_python_extras_dir()` | ran (no return value, nothing visible changed) |

### try-load-scheme-extras-dir

Scheme: `(try-load-scheme-extras-dir)`

Arguments: none. Returns: nothing.
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | `(try-load-scheme-extras-dir)` | ran (no return value, nothing visible changed) |

