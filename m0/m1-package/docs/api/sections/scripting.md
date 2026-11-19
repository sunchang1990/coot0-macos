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
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### make_atom_spec

Python: `make_atom_spec(spec)`

Arguments: spec (a list or value). Returns: a list.
Also available in Python as `make_atom_spec_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_atom_spec(["A", 41, ""])` | not tried |

### make_residue_spec_py

Python: `make_residue_spec_py(spec)`

Arguments: spec (a list or value). Returns: a list.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_residue_spec_py(["A", 41, ""])` | not tried |

### py_clean_internal

Python: `py_clean_internal(obj)`

Arguments: obj (a list or value). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |

### run_generic_script

Python: `run_generic_script(cmd_strings)`  
Scheme: `(run-generic-script cmd-strings)`

Is this a repeat of something? I don't know.

Arguments: cmd_strings (a list). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_generic_script("hello")` | not tried |
| Scheme | `(run-generic-script "hello")` | not tried |

### safe_python_command

Python: `safe_python_command(python_command)`

do nothing

Arguments: python_command (text). Returns: nothing.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `safe_python_command("hello")` | not tried |

### safe_python_command_by_char_star

Python: `safe_python_command_by_char_star(python_command)`

Arguments: python_command (text). Returns: nothing.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `safe_python_command_by_char_star("hello")` | not tried |

### safe_python_command_test

Python: `safe_python_command_test(cmd)`

Arguments: cmd (text). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `safe_python_command_test("hello")` | not tried |

### safe_python_command_with_return

Python: `safe_python_command_with_return(python_cmd)`

Arguments: python_cmd (text). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `safe_python_command_with_return("hello")` | not tried |

### safe_python_command_with_unsafe_thread

Python: `safe_python_command_with_unsafe_thread(cmd)`

Arguments: cmd (text). Returns: nothing.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `safe_python_command_with_unsafe_thread("hello")` | not tried |

### safe_scheme_command

Python: `safe_scheme_command(scheme_command)`  
Scheme: `(safe-scheme-command scheme-command)`

Arguments: scheme_command (text). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `safe_scheme_command("hello")` | not tried |
| Scheme | `(safe-scheme-command "hello")` | not tried |

### safe-scheme-command-test

Scheme: `(safe-scheme-command-test cmd)`

Arguments: cmd (text). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | `(safe-scheme-command-test "hello")` | not tried |

### test-mol-triangles-scm

Scheme: `(test-mol-triangles-scm i-scm j-scm)`

Arguments: i-scm (a list or value), j-scm (a list or value). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | (no automatic example) | not tried |

