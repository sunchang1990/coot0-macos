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
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### get_residue_by_type

Python: `get_residue_by_type(, residue_type)`  
Scheme: `(get-residue-by-type imol residue-type)`

return a residue spec or Python False.

Arguments: ? (a whole number), residue_type (text). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_residue_by_type(1, "ALA")` | ran, returned `False` |
| Scheme | `(get-residue-by-type 0 "ALA")` | ran, returned `#<collectable-swig-pointer coot::residue_spec_t * 814d5bcf0>` |

### get_residue_specs_in_mol

Python: `get_residue_specs_in_mol(imol, residue_type)`  
Scheme: `(get-residue-specs-in-mol imol residue-type)`

Always returns a list

Arguments: imol (a whole number), residue_type (text). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_residue_specs_in_mol(0, "ALA")` | ran, returned `[[True, 'A', 10, ''], [True, 'A', 15, ''], [True, 'A', 23, ''], [True, 'A', 62, ''], [True, 'A', 75, ''], [True, 'A', 87 ...` |
| Scheme | `(get-residue-specs-in-mol 0 "ALA")` | ran, returned `#<collectable-swig-pointer std::vector< coot::residue_spec_t > * 8145dfc40>` |

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
| Python | `pyrun_simple_string("hello")` | not run: not run automatically (run: exits, uses the network, an external program, files or a screen) |
| Scheme | `(pyrun-simple-string "hello")` | not run: not run automatically (run: exits, uses the network, an external program, files or a screen) |

### residue_spec_from_py

Python: `residue_spec_from_py(residue_in)`  
Scheme: `(residue-spec-from-scm residue-in)`

Arguments: residue_in (a list or value). Returns: `coot::residue_spec_t`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `residue_spec_from_py(["A", 41, ""])` | ran, returned `<coot.residue_spec_t; proxy of <Swig Object of type 'coot::residue_spec_t *' at 0x1077a5260> >` |
| Scheme | `(residue-spec-from-scm (list "A" 41 ""))` | ran, returned `#<collectable-swig-pointer coot::residue_spec_t * 77f04e9e0>` |

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
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### run-python-command

Scheme: `(run-python-command python-command)`

Arguments: python-command (text). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | `(run-python-command "hello")` | not run: not run automatically (run: exits, uses the network, an external program, files or a screen) |

### run_scheme_command

Python: `run_scheme_command(scheme_command)`

we ignore return values for now

Arguments: scheme_command (text). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_scheme_command("hello")` | not run: not run automatically (run: exits, uses the network, an external program, files or a screen) |

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
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### show_fix_nomenclature_errors_gui

Python: `show_fix_nomenclature_errors_gui(imol, nomenclature_errors)`  
Scheme: `(show-fix-nomenclature-errors-gui imol nomenclature-errors)`

Arguments: imol (a whole number), nomenclature_errors (a list). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_fix_nomenclature_errors_gui(0, "hello")` | error: TypeError: in method 'show_fix_nomenclature_errors_gui', argument 2 of type 'std::vector< std::pair< std::string,coot::residue_spec_t >,std: ... |
| Scheme | `(show-fix-nomenclature-errors-gui 0 "hello")` | error: In procedure show-fix-nomenclature-errors-gui: Wrong type argument in position 2: "hello" |

