# Mogul

[Scripting reference](../README.md) > Mogul (6 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_mogul_max_badness

Python: `get_mogul_max_badness()`  
Scheme: `(get-mogul-max-badness)`

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_mogul_max_badness()` | ran, returned `5.0` |
| Scheme | `(get-mogul-max-badness)` | ran, returned `5.0` |

Example written and checked by hand on the test data. Expected: returns the |z| above which Mogul markup shows a bond/angle as bad (default 5.0).

Python and Scheme gave the same answer.

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
| Python | first `open("mogul.out", "w").write("BOND,1 2,1.46,500,1.459,1.459,0.012,0.08,0,1.40,1.52,0.01,12\nANGLE,1 2 3,111.0,300,110.5,110.6,2.0,0.25,0,100,120,1,20\n")`, then `mogul_markup(0, "A", 41, "", "mogul.out")` | ran (no return value, nothing visible changed) |
| Scheme | first `(call-with-output-file "mogul.out" (lambda (port) (display "BOND,1 2,1.46,500,1.459,1.459,0.012,0.08,0,1.40,1.52,0.01,12\nANGLE,1 2 3,111.0,300,110.5,110.6,2.0, ...`, then `(mogul-markup 0 "A" 41 "" "mogul.out")` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: draws Mogul results for residue A41 as generic display objects (atom indices in the file are 1-based within the residue).

Note: the example file is a hand-written 2-line Mogul CSV (mogul itself is not run)

### mogul_results_py

Python: `mogul_results_py(mogul_out_file_name)`  
Scheme: `(mogul-results-scm mogul-out-file-name)`

Arguments: mogul_out_file_name (text). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `open("mogul.out", "w").write("BOND,1 2,1.46,500,1.459,1.459,0.012,0.08,0,1.40,1.52,0.01,12\nANGLE,1 2 3,111.0,300,110.5,110.6,2.0,0.25,0,100,120,1,20\n")`, then `mogul_results_py("mogul.out")` | ran, returned `[0.07692667096853256, 0.25]` |
| Scheme | first `(call-with-output-file "mogul.out" (lambda (port) (display "BOND,1 2,1.46,500,1.459,1.459,0.012,0.08,0,1.40,1.52,0.01,12\nANGLE,1 2 3,111.0,300,110.5,110.6,2.0, ...`, then `(mogul-results-scm "mogul.out")` | ran, returned `(0.25 0.07692667096853256)` |

Example written and checked by hand on the test data. Expected: returns a list of z-values, one per bond/angle/torsion in the Mogul output file (False if the file has none).

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### mogul-results-process-many

Scheme: `(mogul-results-process-many glob-str glob-dir)`

Arguments: glob-str (text), glob-dir (text). Returns: a value (see the result of the example).
**Scheme only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Scheme | first `(call-with-output-file "mogul-out-1abc-GLU-A.out" (lambda (port) (display "BOND,1 2,1.46,500,1.459,1.459,0.012,0.08,0,1.40,1.52,0.01,12\nANGLE,1 2 3,111.0,300,1 ...`, then `(mogul-results-process-many "." "mogul-out-*")` | ran, returned `(("1abc" 0.20000076293945312))` |

Example written and checked by hand on the test data. Expected: for each Mogul output file matching the glob (names like x-y-ACCESSION-COMPID-z) returns (accession-code worst-z); Scheme only.

### set_mogul_max_badness

Python: `set_mogul_max_badness(b)`  
Scheme: `(set-mogul-max-badness b)`

Arguments: b (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_mogul_max_badness(3.5)` | ran (no return value); changed: get_mogul_max_badness(): 5 -> 3.5 |
| Scheme | `(set-mogul-max-badness 4.5)` | ran (no return value); changed: get_mogul_max_badness(): 3.5 -> 4.5 |

Example written and checked by hand on the test data. Expected: sets the Mogul badness limit; get_mogul_max_badness() returns the new value.

Setting checked (set to another value and read back, then put back): Python: get_mogul_max_badness was 5.0, set to 8.0, read back 8.0; Scheme: get-mogul-max-badness was 5.0, set to 8.0, read back 8.0.

### update_restraints_using_mogul

Python: `update_restraints_using_mogul(imol, chain_id, res_no, ins_code, residue_type, mogul_out_file_name)`  
Scheme: `(update-restraints-using-mogul imol chain-id res-no ins-code residue-type mogul-out-file-name)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), residue_type (text), mogul_out_file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `open("mogul.out", "w").write("BOND,1 2,1.46,500,1.459,1.459,0.012,0.08,0,1.40,1.52,0.01,12\nANGLE,1 2 3,111.0,300,110.5,110.6,2.0,0.25,0,100,120,1,20\n")`, then `update_restraints_using_mogul(0, "A", 41, "", "GLU", "mogul.out")` | ran, returned `1` |
| Scheme | first `(call-with-output-file "mogul.out" (lambda (port) (display "BOND,1 2,1.46,500,1.459,1.459,0.012,0.08,0,1.40,1.52,0.01,12\nANGLE,1 2 3,111.0,300,110.5,110.6,2.0, ...`, then `(update-restraints-using-mogul 0 "A" 41 "" "GLU" "mogul.out")` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 when the monomer restraints for the residue type were updated from the Mogul output file.

Note: the example file is a hand-written 2-line Mogul CSV; this changes the in-memory GLU dictionary

Python and Scheme gave the same answer.

