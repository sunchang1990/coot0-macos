# Mogul

[Scripting reference](../README.md) > Mogul (6 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_mogul_max_badness

Python: `get_mogul_max_badness()`  
Scheme: `(get-mogul-max-badness)`

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_mogul_max_badness()` | not run: not run automatically (mogul: exits, uses the network, an external program, files or a screen) |
| Scheme | `(get-mogul-max-badness)` | not run: not run automatically (mogul: exits, uses the network, an external program, files or a screen) |

### mogul_markup

Python: `mogul_markup(imol, chain_id, res_no, ins_code, mogul_out_file_name)`  
Scheme: `(mogul-markup imol chain-id res-no ins-code mogul-out-file-name)`

src/c-interface-mogul.hh

Copyright 2011 by the University of Oxford
Author: Paul Emsley

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), mogul_out_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mogul_markup(0, "A", 41, "", "tutorial-modern.pdb")` | not run: not run automatically (mogul: exits, uses the network, an external program, files or a screen) |
| Scheme | `(mogul-markup 0 "A" 41 "" "tutorial-modern.pdb")` | not run: not run automatically (mogul: exits, uses the network, an external program, files or a screen) |

### mogul_results_py

Python: `mogul_results_py(mogul_out_file_name)`  
Scheme: `(mogul-results-scm mogul-out-file-name)`

Arguments: mogul_out_file_name (text). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mogul_results_py("tutorial-modern.pdb")` | not run: not run automatically (mogul: exits, uses the network, an external program, files or a screen) |
| Scheme | `(mogul-results-scm "tutorial-modern.pdb")` | not run: not run automatically (mogul: exits, uses the network, an external program, files or a screen) |

### mogul-results-process-many

Scheme: `(mogul-results-process-many glob-str glob-dir)`

Arguments: glob-str (text), glob-dir (text). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | `(mogul-results-process-many "hello" ".")` | not run: not run automatically (mogul: exits, uses the network, an external program, files or a screen) |

### set_mogul_max_badness

Python: `set_mogul_max_badness(b)`  
Scheme: `(set-mogul-max-badness b)`

Arguments: b (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_mogul_max_badness(0.5)` | not run: not run automatically (mogul: exits, uses the network, an external program, files or a screen) |
| Scheme | `(set-mogul-max-badness 0.5)` | not run: not run automatically (mogul: exits, uses the network, an external program, files or a screen) |

### update_restraints_using_mogul

Python: `update_restraints_using_mogul(imol, chain_id, res_no, ins_code, residue_type, mogul_out_file_name)`  
Scheme: `(update-restraints-using-mogul imol chain-id res-no ins-code residue-type mogul-out-file-name)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), residue_type (text), mogul_out_file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_restraints_using_mogul(0, "A", 41, "", "ALA", "tutorial-modern.pdb")` | not run: not run automatically (mogul: exits, uses the network, an external program, files or a screen) |
| Scheme | `(update-restraints-using-mogul 0 "A" 41 "" "ALA" "tutorial-modern.pdb")` | not run: not run automatically (mogul: exits, uses the network, an external program, files or a screen) |

