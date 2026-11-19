# Nomenclature Errors

[Scripting reference](../README.md) > Nomenclature Errors (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### fix_nomenclature_errors

Python: `fix_nomenclature_errors(imol)`  
Scheme: `(fix-nomenclature-errors imol)`

fix nomenclature errors in molecule number imol

 Returns the number of resides altered.

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fix_nomenclature_errors(0)` | ran, returned `0` |
| Scheme | `(fix-nomenclature-errors 0)` | ran, returned `0` |

### set_nomenclature_errors_on_read

Python: `set_nomenclature_errors_on_read(mode)`  
Scheme: `(set-nomenclature-errors-on-read mode)`

set way nomenclature errors should be handled on reading
 coordinates.

 mode should be "auto-correct", "ignore", "prompt". The
 default is "prompt"

Arguments: mode (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_nomenclature_errors_on_read("hello")` | not tried |
| Scheme | `(set-nomenclature-errors-on-read "hello")` | not tried |

