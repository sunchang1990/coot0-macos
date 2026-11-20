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
| Python | `clear_generic_objects_dialog_pointer()` | ran (no return value) |
| Scheme | `(clear-generic-objects-dialog-pointer)` | ran (no return value) |

### close_all_generic_objects

Python: `close_all_generic_objects()`  
Scheme: `(close-all-generic-objects)`

close all generic display objects

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `close_all_generic_objects()` | ran (no return value) |
| Scheme | `(close-all-generic-objects)` | ran (no return value) |

### compare_atom_specs_user_float

Python: `compare_atom_specs_user_float()`  
Scheme: `(compare-atom-specs-user-float)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `compare_atom_specs_user_float()` | error: TypeError: compare_atom_specs_user_float() missing 2 required positional arguments: 'a1' and 'a2' |
| Scheme | `(compare-atom-specs-user-float)` | error: Wrong number of arguments to #<procedure compare-atom-specs-user-float (_ _)> |

### compare_atom_specs_user_float_in_pair

Python: `compare_atom_specs_user_float_in_pair()`  
Scheme: `(compare-atom-specs-user-float-in-pair)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `compare_atom_specs_user_float_in_pair()` | error: TypeError: compare_atom_specs_user_float_in_pair() missing 2 required positional arguments: 'a' and 'b' |
| Scheme | `(compare-atom-specs-user-float-in-pair)` | error: Wrong number of arguments to #<procedure compare-atom-specs-user-float-in-pair (_ _)> |

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
| Python | `generic_objects_gui_wrapper()` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(generic-objects-gui-wrapper)` | stopped Coot when tried without a window (not checked with a window) |

### link_atoms

Python: `link_atoms()`  
Scheme: `(link-atoms)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `link_atoms()` | error: TypeError: Wrong number or type of arguments for overloaded function 'link_atoms'.   Possible C/C++ prototypes are:     coot::link_atoms(mmd ... |
| Scheme | `(link-atoms)` | error: In procedure link-atoms: No matching method for generic function 'link_atoms' |

### set_display_all_generic_objects

Python: `set_display_all_generic_objects(state)`  
Scheme: `(set-display-all-generic-objects state)`

display (1) or undisplay (0) all generic display objects

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_display_all_generic_objects(1)` | ran (no return value) |
| Scheme | `(set-display-all-generic-objects 1)` | ran (no return value) |

### try_load_python_extras_dir

Python: `try_load_python_extras_dir()`

Arguments: none. Returns: nothing.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `try_load_python_extras_dir()` | ran (no return value) |

### try-load-scheme-extras-dir

Scheme: `(try-load-scheme-extras-dir)`

Arguments: none. Returns: nothing.
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | `(try-load-scheme-extras-dir)` | ran (no return value) |

