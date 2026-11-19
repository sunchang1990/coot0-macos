# Atom Labelling

[Scripting reference](../README.md) > Atom Labelling (8 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_atom_label

Python: `add_atom_label(imol, chain_id, iresno, atom_id)`  
Scheme: `(add-atom-label imol chain-id iresno atom-id)`

Note we have to search for " CA " etc

Arguments: imol (a whole number), chain_id (text), iresno (a whole number), atom_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_atom_label(0, "A", 41, "hello")` | ran, returned `-1` |
| Scheme | `(add-atom-label 0 "A" 41 "hello")` | ran, returned `-1` |

### brief_atom_labels_state

Python: `brief_atom_labels_state()`  
Scheme: `(brief-atom-labels-state)`

the brief atom label state

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `brief_atom_labels_state()` | ran, returned `0` |
| Scheme | `(brief-atom-labels-state)` | ran, returned `0` |

### centre_atom_label_status

Python: `centre_atom_label_status()`  
Scheme: `(centre-atom-label-status)`

0 for off, 1 or on

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `centre_atom_label_status()` | ran, returned `1` |
| Scheme | `(centre-atom-label-status)` | ran, returned `1` |

### remove_all_atom_labels

Python: `remove_all_atom_labels()`  
Scheme: `(remove-all-atom-labels)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_all_atom_labels()` | not tried |
| Scheme | `(remove-all-atom-labels)` | not tried |

### remove_atom_label

Python: `remove_atom_label(imol, chain_id, iresno, atom_id)`  
Scheme: `(remove-atom-label imol chain-id iresno atom-id)`

Arguments: imol (a whole number), chain_id (text), iresno (a whole number), atom_id (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_atom_label(0, "A", 41, "hello")` | not tried |
| Scheme | `(remove-atom-label 0 "A" 41 "hello")` | not tried |

### set_brief_atom_labels

Python: `set_brief_atom_labels(istat)`  
Scheme: `(set-brief-atom-labels istat)`

use brief atom names for on-screen labels

 call with istat=1 to use brief labels, istat=0 for normal labels

Arguments: istat (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_brief_atom_labels(1)` | not tried |
| Scheme | `(set-brief-atom-labels 1)` | not tried |

### set_label_on_recentre_flag

Python: `set_label_on_recentre_flag(i)`  
Scheme: `(set-label-on-recentre-flag i)`

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_label_on_recentre_flag(1)` | not tried |
| Scheme | `(set-label-on-recentre-flag 1)` | not tried |

### set_seg_ids_in_atom_labels

Python: `set_seg_ids_in_atom_labels(istat)`  
Scheme: `(set-seg-ids-in-atom-labels istat)`

set if brief atom labels should have seg-ids also

Arguments: istat (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_seg_ids_in_atom_labels(1)` | not tried |
| Scheme | `(set-seg-ids-in-atom-labels 1)` | not tried |

