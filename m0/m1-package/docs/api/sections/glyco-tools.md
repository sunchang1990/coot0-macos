# Glyco Tools

[Scripting reference](../README.md) > Glyco Tools (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### print_glyco_tree

Python: `print_glyco_tree(imol, chain_id, resno, ins_code)`  
Scheme: `(print-glyco-tree imol chain-id resno ins-code)`

print the glycosylation tree that contains the specified residue

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `print_glyco_tree(0, "A", 41, "")` | not tried |
| Scheme | `(print-glyco-tree 0 "A" 41 "")` | not tried |

