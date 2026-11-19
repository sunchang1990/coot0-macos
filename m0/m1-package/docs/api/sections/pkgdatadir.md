# PKGDATADIR

[Scripting reference](../README.md) > PKGDATADIR (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_pkgdatadir

Python: `get_pkgdatadir()`  
Scheme: `(pkgdatadir)`

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `pkgdatadir`, `get_pkgdatadir_py`.
Also available in Scheme as `get-pkgdatadir-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_pkgdatadir()` | ran, returned `'/usr/local/share/coot'` |
| Scheme | `(pkgdatadir)` | ran, returned `"/usr/local/share/coot"` |

