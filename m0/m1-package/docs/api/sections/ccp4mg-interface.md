# CCP4mg Interface

[Scripting reference](../README.md) > CCP4mg Interface (3 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### ccp4i_projects

Python: `ccp4i_projects()`  
Scheme: `(ccp4i-projects)`

return a list of pairs of strings, the project names and
 the directory. Include aliases.

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `ccp4i_projects_py`.
Also available in Scheme as `ccp4i-projects-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ccp4i_projects()` | not run: not run automatically (ccp4i: exits, uses the network, an external program, files or a screen) |
| Scheme | `(ccp4i-projects)` | not run: not run automatically (ccp4i: exits, uses the network, an external program, files or a screen) |

### set_add_ccp4i_projects_to_file_dialogs

Python: `set_add_ccp4i_projects_to_file_dialogs(state)`  
Scheme: `(set-add-ccp4i-projects-to-file-dialogs state)`

allow the user to not add ccp4i directories to the file choosers

use state=0 to turn it off

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_add_ccp4i_projects_to_file_dialogs(1)` | not run: not run automatically (ccp4i: exits, uses the network, an external program, files or a screen) |
| Scheme | `(set-add-ccp4i-projects-to-file-dialogs 1)` | not run: not run automatically (ccp4i: exits, uses the network, an external program, files or a screen) |

### write_ccp4mg_picture_description

Python: `write_ccp4mg_picture_description(filename)`  
Scheme: `(write-ccp4mg-picture-description filename)`

write a ccp4mg picture description file

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `write_ccp4mg_picture_description("tutorial-modern.pdb")` | not run: not run automatically (ccp4mg: exits, uses the network, an external program, files or a screen) |
| Scheme | `(write-ccp4mg-picture-description "tutorial-modern.pdb")` | not run: not run automatically (ccp4mg: exits, uses the network, an external program, files or a screen) |

