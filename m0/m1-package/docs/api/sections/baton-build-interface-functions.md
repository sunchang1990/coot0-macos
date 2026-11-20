# Baton Build Interface Functions

[Scripting reference](../README.md) > Baton Build Interface Functions (11 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### accept_baton_position

Python: `accept_baton_position()`  
Scheme: `(accept-baton-position)`

accept the baton tip position - a prime candidate for a key binding

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `accept_baton_position()` | ran (no return value) |
| Scheme | `(accept-baton-position)` | ran (no return value) |

### baton_build_delete_last_residue

Python: `baton_build_delete_last_residue()`  
Scheme: `(baton-build-delete-last-residue)`

delete the most recently build CA position

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `baton_build_delete_last_residue()` | ran (no return value) |
| Scheme | `(baton-build-delete-last-residue)` | ran (no return value) |

### baton_tip_previous

Python: `baton_tip_previous()`  
Scheme: `(baton-tip-previous)`

move the baton tip to the previous position

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `baton_tip_previous()` | ran (no return value) |
| Scheme | `(baton-tip-previous)` | ran (no return value) |

### baton_tip_try_another

Python: `baton_tip_try_another()`  
Scheme: `(baton-tip-try-another)`

move the baton tip position - another prime candidate for a key binding

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `baton_tip_try_another()` | ran (no return value) |
| Scheme | `(baton-tip-try-another)` | ran (no return value) |

### lengthen_baton

Python: `lengthen_baton()`  
Scheme: `(lengthen-baton)`

lengthen the baton

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `lengthen_baton()` | ran (no return value) |
| Scheme | `(lengthen-baton)` | ran (no return value) |

### reverse_direction_of_fragment

Python: `reverse_direction_of_fragment(imol, chain_id, resno)`  
Scheme: `(reverse-direction-of-fragment imol chain-id resno)`

Reverse the direction of a the fragment of the clicked on
 atom/residue.

 A fragment is a consecutive range of residues -
 where there is a gap in the numbering, that marks breaks between
 fragments in a chain. There also needs to be a distance break - if
 the CA of the next/previous residue is more than 5A away, that also
 marks a break. Throw away all atoms in fragment other than CAs.

Arguments: imol (a whole number), chain_id (text), resno (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `reverse_direction_of_fragment(0, "A", 41)` | ran (no return value) |
| Scheme | `(reverse-direction-of-fragment 0 "A" 41)` | ran (no return value) |

### set_baton_build_params

Python: `set_baton_build_params(istart_resno, chain_id, direction)`  
Scheme: `(set-baton-build-params istart-resno chain-id direction)`

set the parameters for the start of a new baton-built fragment. direction can either
 be "forwards" or "backwards"

Arguments: istart_resno (a whole number), chain_id (text), direction (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_baton_build_params(41, "A", ".")` | ran (no return value) |
| Scheme | `(set-baton-build-params 41 "A" ".")` | ran (no return value) |

### set_baton_mode

Python: `set_baton_mode(i)`  
Scheme: `(set-baton-mode i)`

toggle so that mouse movement moves the baton not rotates the view.

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_baton_mode(1)` | ran (no return value) |
| Scheme | `(set-baton-mode 1)` | ran (no return value) |

### setup_reverse_direction

Python: `setup_reverse_direction(i)`  
Scheme: `(setup-reverse-direction i)`

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_reverse_direction(1)` | ran (no return value) |
| Scheme | `(setup-reverse-direction 1)` | ran (no return value) |

### shorten_baton

Python: `shorten_baton()`  
Scheme: `(shorten-baton)`

shorten the baton length

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `shorten_baton()` | ran (no return value) |
| Scheme | `(shorten-baton)` | ran (no return value) |

### try_set_draw_baton

Python: `try_set_draw_baton(i)`  
Scheme: `(try-set-draw-baton i)`

draw the baton or not

Arguments: i (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `try_set_draw_baton(1)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(try-set-draw-baton 1)` | stopped Coot when tried without a window (not checked with a window) |

