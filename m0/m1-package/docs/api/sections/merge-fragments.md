# Merge Fragments

[Scripting reference](../README.md) > Merge Fragments (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### merge_fragments

Python: `merge_fragments(imol)`  
Scheme: `(merge-fragments imol)`

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `merge_fragments(0)` | ran, returned `1` |
| Scheme | `(merge-fragments 0)` | ran, returned `1` |

Python and Scheme gave the same answer.

