# Skeletonization Interface

[Scripting reference](../README.md) > Skeletonization Interface (11 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_text_for_skeleton_box_size_entry

Python: `get_text_for_skeleton_box_size_entry()`  
Scheme: `(get-text-for-skeleton-box-size-entry)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_text_for_skeleton_box_size_entry()` | ran, returned `<Swig Object of type 'gchar *' at 0x10a26d740>` |
| Scheme | `(get-text-for-skeleton-box-size-entry)` | ran, returned `#<swig-pointer gchar * 814678210>` |

### get_text_for_skeletonization_level_entry

Python: `get_text_for_skeletonization_level_entry()`  
Scheme: `(get-text-for-skeletonization-level-entry)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_text_for_skeletonization_level_entry()` | ran, returned `<Swig Object of type 'gchar *' at 0x10a26c9c0>` |
| Scheme | `(get-text-for-skeletonization-level-entry)` | ran, returned `#<swig-pointer gchar * 814768130>` |

### set_initial_map_for_skeletonize

Python: `set_initial_map_for_skeletonize()`  
Scheme: `(set-initial-map-for-skeletonize)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_initial_map_for_skeletonize()` | ran (no return value) |
| Scheme | `(set-initial-map-for-skeletonize)` | ran (no return value) |

### set_max_skeleton_search_depth

Python: `set_max_skeleton_search_depth(v)`  
Scheme: `(set-max-skeleton-search-depth v)`

set the skeleton search depth, used in baton building

 For high resolution maps, you need to search deeper down the skeleton tree. This
 limit needs to be increased to 20 or so for high res maps (it is 10 by default)

Arguments: v (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_max_skeleton_search_depth(1)` | ran (no return value) |
| Scheme | `(set-max-skeleton-search-depth 1)` | ran (no return value) |

### set_skeleton_box_size

Python: `set_skeleton_box_size(f)`  
Scheme: `(set-skeleton-box-size f)`

the box size (in Angstroms) for which the skeleton is displayed

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_skeleton_box_size(1.0)` | ran (no return value) |
| Scheme | `(set-skeleton-box-size 1.0)` | ran (no return value) |

### set_skeleton_box_size_from_widget

Python: `set_skeleton_box_size_from_widget(txt)`  
Scheme: `(set-skeleton-box-size-from-widget txt)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: txt (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_skeleton_box_size_from_widget("hello")` | ran (no return value) |
| Scheme | `(set-skeleton-box-size-from-widget "hello")` | ran (no return value) |

### set_skeletonization_level_from_widget

Python: `set_skeletonization_level_from_widget(txt)`  
Scheme: `(set-skeletonization-level-from-widget txt)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: txt (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_skeletonization_level_from_widget("hello")` | ran (no return value) |
| Scheme | `(set-skeletonization-level-from-widget "hello")` | ran (no return value) |

### skel_greer_off

Python: `skel_greer_off()`  
Scheme: `(skel-greer-off)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `skel_greer_off()` | ran (no return value) |
| Scheme | `(skel-greer-off)` | ran (no return value) |

### skel_greer_on

Python: `skel_greer_on()`  
Scheme: `(skel-greer-on)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `skel_greer_on()` | ran (no return value) |
| Scheme | `(skel-greer-on)` | ran (no return value) |

### skeletonize_map

Python: `skeletonize_map(imol, prune_flag)`  
Scheme: `(skeletonize-map imol prune-flag)`

skeletonize molecule number imol

 the prune_flag should almost always be 0.

 NOTE:: The arguments to have been reversed for coot 0.8.3 and later
 (now the molecule number comes first).

Arguments: imol (a whole number), prune_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `skeletonize_map(0, 1)` | ran, returned `0` |
| Scheme | `(skeletonize-map 0 1)` | ran, returned `0` |

Python and Scheme gave the same answer.

### unskeletonize_map

Python: `unskeletonize_map(imol)`  
Scheme: `(unskeletonize-map imol)`

undisplay the skeleton on molecule number imol

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `unskeletonize_map(0)` | ran, returned `0` |
| Scheme | `(unskeletonize-map 0)` | ran, returned `0` |

Python and Scheme gave the same answer.

