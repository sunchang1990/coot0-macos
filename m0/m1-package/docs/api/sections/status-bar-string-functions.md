# status bar string functions

[Scripting reference](../README.md) > status bar string functions (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### atom_info_as_text_for_statusbar

Python: `atom_info_as_text_for_statusbar(atom_index, imol)`  
Scheme: `(atom-info-as-text-for-statusbar atom-index imol)`

Arguments: atom_index (a whole number), imol (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `atom_info_as_text_for_statusbar(0, 0)` | ran, returned `' [ 0 "tutorial-modern.pdb"]  N  /1/A/1 ASP occ: 1.00 bf: 30.17 ele:  N pos: (44.88,12.95,8.76)'` |
| Scheme | `(atom-info-as-text-for-statusbar 0 0)` | ran, returned `" [ 0 \"tutorial-modern.pdb\"]  N  /1/A/1 ASP occ: 1.00 bf: 30.17 ele:  N pos: (44.88,12.95,8.76)"` |

