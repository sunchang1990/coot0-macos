# Scripting

[Scripting reference](../README.md) > Scripting (14 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### coot-has-python-p

Scheme: `(coot-has-python-p)`

Arguments: none. Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | `(coot-has-python-p)` | ran, returned `#t` |

### display_python

Python: `display_python(o)`

This is a common denominator really. It does not depend on mmdb,
but it can't be declared in c-interface.h because then we'd have to
include c-interface.h which would cause (resolvable, I think, not
checked) problems.
return a python string, decode to c++ using scm_to_locale_string();

Arguments: o (a list or value). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `display_python([1, "a", 2.5])` | ran, returned `"object: [1, 'a', 2.5]\n"` |

Example written and checked by hand on the test data. Expected: a printable string describing the Python object (internal helper for messages). (Python only.).

### make_atom_spec

Python: `make_atom_spec(spec)`

Arguments: spec (a list or value). Returns: a list.
Also available in Python as `make_atom_spec_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_atom_spec(["A", 41, ""])` | ran, returned `<Swig Object of type 'std::pair< bool,coot::atom_spec_t > *' at 0x10a3f38d0>` |

### make_residue_spec_py

Python: `make_residue_spec_py(spec)`

Arguments: spec (a list or value). Returns: a list.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_residue_spec_py(["A", 41, ""])` | ran, returned `<Swig Object of type 'std::pair< bool,coot::residue_spec_t > *' at 0x10c5c17d0>` |

### py_clean_internal

Python: `py_clean_internal(obj)`

Arguments: obj (a list or value). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `py_clean_internal([[1.0, "x"], True])` | ran, returned `[[1.0, 'x'], True]` |

Example written and checked by hand on the test data. Expected: the same object back (it only replaces internal 'None'-like values in nested lists); internal helper. (Python only.).

### run_generic_script

Python: `run_generic_script(cmd_strings)`  
Scheme: `(run-generic-script cmd-strings)`

Is this a repeat of something? I don't know.

Arguments: cmd_strings (a list). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_generic_script(["set-rotation-centre", "10", "10", "10"])` | ran (no return value); changed: rotation centre moved 31.8 A to (10.0, 10.0, 10.0) |
| Scheme | `(run-generic-script (list "set-rotation-centre" "10" "10" "10"))` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: builds the Scheme command (set-rotation-centre 10 10 10) from the list (function name, then arguments) and runs it.

Note: The list is always turned into a SCHEME command (Guile is built in), also when called from Python: give Scheme names.

### safe_python_command

Python: `safe_python_command(python_command)`

do nothing

Arguments: python_command (text). Returns: nothing.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `safe_python_command("hello")` | ran (no return value, nothing visible changed) |

### safe_python_command_by_char_star

Python: `safe_python_command_by_char_star(python_command)`

Arguments: python_command (text). Returns: nothing.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `safe_python_command_by_char_star("hello")` | ran (no return value, nothing visible changed) |

### safe_python_command_test

Python: `safe_python_command_test(cmd)`

Arguments: cmd (text). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `safe_python_command_test("hello")` | ran (no return value, nothing visible changed) |

### safe_python_command_with_return

Python: `safe_python_command_with_return(python_cmd)`

Arguments: python_cmd (text). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `safe_python_command_with_return("hello")` | ran (no return value, nothing visible changed) |

### safe_python_command_with_unsafe_thread

Python: `safe_python_command_with_unsafe_thread(cmd)`

Arguments: cmd (text). Returns: nothing.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `safe_python_command_with_unsafe_thread("print('hello')")` | not run: crashes Coot when called from Python: it releases the Python lock and then runs Python code without it (internal helper) |

Example written and checked by hand on the test data. Expected: runs a Python command string with the interpreter lock released; meant only for C++ code, not for scripts.

Note: Calling it from a script always crashes (Py_BEGIN_ALLOW_THREADS then PyRun_SimpleString). Use run_python_command / exec instead.

### safe_scheme_command

Python: `safe_scheme_command(scheme_command)`  
Scheme: `(safe-scheme-command scheme-command)`

Arguments: scheme_command (text). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `safe_scheme_command("hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(safe-scheme-command "hello")` | ran (no return value, nothing visible changed) |

### safe-scheme-command-test

Scheme: `(safe-scheme-command-test cmd)`

Arguments: cmd (text). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | `(safe-scheme-command-test "hello")` | ran (no return value, nothing visible changed) |

### test-mol-triangles-scm

Scheme: `(test-mol-triangles-scm i-scm j-scm)`

Arguments: i-scm (a list or value), j-scm (a list or value). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | `(test-mol-triangles-scm 0 0)` | ran, returned `#f` |

Example written and checked by hand on the test data. Expected: developer test: returns #f; it only draws a ribbon when Coot is built with MoleculesToTriangles (not in this build). (Scheme only.).

