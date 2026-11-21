# Restraints Interface

[Scripting reference](../README.md) > Restraints Interface (16 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### coot_can_do_lidia_p

Python: `coot_can_do_lidia_p()`  
Scheme: `(coot-can-do-lidia-p)`

Arguments: none. Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_can_do_lidia_p()` | ran, returned `True` |
| Scheme | `(coot-can-do-lidia-p)` | ran, returned `#t` |

Python and Scheme gave the same answer.

### coot_has_guile

Python: `coot_has_guile()`

Arguments: none. Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_has_guile()` | ran, returned `True` |

### dipole_to_py

Python: `dipole_to_py(dp)`  
Scheme: `(dipole-to-scm dp)`

Arguments: dp (a list). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no example) | not run: no automatic example (it takes a list, a widget or an object) |

Example written and checked by hand on the test data. Expected: internal: converts a C++ (dipole, imol) pair to a script value.

### get_residue_by_type

Python: `get_residue_by_type(, residue_type)`  
Scheme: `(get-residue-by-type imol residue-type)`

return a residue spec or Python False.

Arguments: ? (a whole number), residue_type (text). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_residue_by_type(0, "ALA")` | ran, returned `[True, 'A', 10, '']` |
| Scheme | `(get-residue-by-type-scm 0 "ALA")` | ran, returned `(#t "A" 10 "")` |

Example written and checked by hand on the test data. Expected: returns the residue spec of the first residue of that type, or False if there is none.

Note: Scheme: the name get-residue-by-type is the C++ function and returns a raw #<swig-pointer residue_spec_t>; use get-residue-by-type-scm

Python and Scheme gave the same answer.

### get_residue_specs_in_mol

Python: `get_residue_specs_in_mol(imol, residue_type)`  
Scheme: `(get-residue-specs-in-mol imol residue-type)`

Always returns a list

Arguments: imol (a whole number), residue_type (text). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_residue_specs_in_mol(0, "ALA")` | ran, returned `[[True, 'A', 10, ''], [True, 'A', 15, ''], [True, 'A', 23, ''], [True, 'A', 62, ''], [True, 'A', 75, ''], [True, 'A', 87 ...` |
| Scheme | `(get-residue-specs-in-mol 0 "ALA")` | ran, returned `#<collectable-swig-pointer std::vector< coot::residue_spec_t > * 94b868c20>` |

### list_nomenclature_errors

Python: `list_nomenclature_errors(imol)`  
Scheme: `(list-nomenclature-errors imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `list_nomenclature_errors_py`.
Also available in Scheme as `list-nomenclature-errors-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `list_nomenclature_errors(0)` | ran, returned `[]` |
| Scheme | `(list-nomenclature-errors 0)` | ran, returned `()` |

Python and Scheme gave the same answer.

### monomer_restraints

Python: `monomer_restraints(monomer_type)`  
Scheme: `(monomer-restraints monomer-type)`

Arguments: monomer_type (text). Returns: a value (see the result of the example).
Also available in Python as `monomer_restraints_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `monomer_restraints("ALA")` | ran, returned `{'_chem_comp': ['ALA', 'ALA', 'ALANINE', 'peptide', 13, 6, '.'], '_chem_comp_atom': [[' N  ', 'N', 'NT3', 0.0, False], [ ...` |
| Scheme | `(monomer-restraints "ALA")` | ran, returned `(("_chem_comp" "ALA" "ALA" "ALANINE" "peptide" 13 6 ".") ("_chem_comp_atom" (" N  " "N" "NT3" 0.0 #f) (" CA " "C" "CH1"  ...` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### monomer_restraints_for_molecule

Python: `monomer_restraints_for_molecule(monomer_type, imol)`

Arguments: monomer_type (text), imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `monomer_restraints_for_molecule_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `monomer_restraints_for_molecule("ALA", 0)` | ran, returned `{'_chem_comp': ['ALA', 'ALA', 'ALANINE', 'peptide', 13, 6, '.'], '_chem_comp_atom': [[' N  ', 'N', 'NT3', 0.0, False], [ ...` |

### pyrun_simple_string

Python: `pyrun_simple_string(python_command)`  
Scheme: `(pyrun-simple-string python-command)`

This is not inside a #ifdef USE_PYTHON because we want to use it
from the guile level and USE_PYTHON is not passed as an argument to
swig when generating coot_wrap_guile.cc.
[Consider removing safe_python_command_by_char_star() which is
conditionally compiled].

Arguments: python_command (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `pyrun_simple_string("print('hi from pyrun'); set_rotation_centre(5, 5, 5)")` | ran, returned `0`; changed: rotation centre moved 37.6 A to (5.0, 5.0, 5.0) |
| Scheme | `(pyrun-simple-string "print('hi from scheme via pyrun')")` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: runs the Python text in Coot's Python; returns 0 on success.

Python and Scheme gave the same answer.

### residue_spec_from_py

Python: `residue_spec_from_py(residue_in)`  
Scheme: `(residue-spec-from-scm residue-in)`

Arguments: residue_in (a list or value). Returns: `coot::residue_spec_t`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_spec_from_py(["A", 41, ""])` | ran, returned `<coot.residue_spec_t; proxy of <Swig Object of type 'coot::residue_spec_t *' at 0x10785f8d0> >` |
| Scheme | `(residue-spec-from-scm (list "A" 41 ""))` | ran, returned `#<collectable-swig-pointer coot::residue_spec_t * a44c39c20>` |

### residue_spec_make_triple

Python: `residue_spec_make_triple(residue_spec_py)`

Arguments: residue_spec_py (a list or value). Returns: a value (see the result of the example).
Also available in Python as `residue_spec_make_triple_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_spec_make_triple(["A", 41, ""])` | ran, returned `['A', 41, '']` |

### residue_spec_to_py

Python: `residue_spec_to_py(res)`  
Scheme: `(residue-spec-to-scm res)`

Return a list describing a residue like that returned by
residues-matching-criteria [return_val, chain_id, resno, ins_code]
This is a library function really. There should be somewhere else to put it.
It doesn't need expression at the scripting level.
return a null list on problem

Arguments: res (`coot::residue_spec_t`). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_spec_to_py(residue_spec_t("A", 41, ""))` | ran, returned `[True, 'A', 41, '']` |
| Scheme | `(residue-spec-to-scm (new-residue-spec-t "A" 41 ""))` | ran, returned `(#t "A" 41 "")` |

Example written and checked by hand on the test data. Expected: converts a SWIG residue_spec_t object into a script list [True, chain, resno, ins].

Python and Scheme gave the same answer.

### run-python-command

Scheme: `(run-python-command python-command)`

Arguments: python-command (text). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | `(run-python-command "2 + 3")` | ran, returned `5` |

Example written and checked by hand on the test data. Expected: evaluates a Python expression from Scheme and returns its value converted to Scheme.

### run_scheme_command

Python: `run_scheme_command(scheme_command)`

we ignore return values for now

Arguments: scheme_command (text). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_scheme_command("(+ 2 3)")` | ran, returned `5` |

Example written and checked by hand on the test data. Expected: evaluates a Scheme expression from Python and returns its value converted to Python.

### set_monomer_restraints

Python: `set_monomer_restraints(monomer_type, restraints)`  
Scheme: `(set-monomer-restraints monomer-type restraints)`

set the monomer restraints of the given monomer_type
 Returns scheme false or true for success or failure to set the
 restrains for monomer_type

Arguments: monomer_type (text), restraints (a list or value). Returns: a value (see the result of the example).
Also available in Python as `set_monomer_restraints_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `r = monomer_restraints("ALA")`, then `r["_chem_comp_bond"] = [b if b[:2] != [" N  ", " CA "] else [b[0], b[1], b[2], 1.50, b[4]] for b in r["_chem_comp_bond"]]`, then `set_monomer_restraints("ALA", r)` | ran, returned `True` |
| Scheme | `(set-monomer-restraints "ALA" (monomer-restraints "ALA"))` | ran, returned `#t` |

Example written and checked by hand on the test data. Expected: replaces the ALA dictionary restraints by the given ones (as returned by monomer_restraints); True on success.

Python and Scheme gave the same answer.

### show_fix_nomenclature_errors_gui

Python: `show_fix_nomenclature_errors_gui(imol, nomenclature_errors)`  
Scheme: `(show-fix-nomenclature-errors-gui imol nomenclature-errors)`

Arguments: imol (a whole number), nomenclature_errors (a list). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_fix_nomenclature_errors_gui(0, "hello")` | not run: needs a C++ vector of (string, residue_spec_t) pairs and opens a dialog; not callable from scripts |
| Scheme | `(show-fix-nomenclature-errors-gui 0 "hello")` | not run: needs a C++ vector of (string, residue_spec_t) pairs and opens a dialog; not callable from scripts |

Example written and checked by hand on the test data. Expected: shows a dialog listing nomenclature errors to fix.

