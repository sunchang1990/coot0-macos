# File System Functions

[Scripting reference](../README.md) > File System Functions (22 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_coordinates_glob_extension

Python: `add_coordinates_glob_extension(ext)`  
Scheme: `(add-coordinates-glob-extension ext)`

add an extension to be treated as coordinate files

Arguments: ext (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_coordinates_glob_extension("hello")` | ran (no return value) |
| Scheme | `(add-coordinates-glob-extension "hello")` | ran (no return value) |

### add_data_glob_extension

Python: `add_data_glob_extension(ext)`  
Scheme: `(add-data-glob-extension ext)`

add an extension to be treated as data (reflection) files

Arguments: ext (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_data_glob_extension("hello")` | ran (no return value) |
| Scheme | `(add-data-glob-extension "hello")` | ran (no return value) |

### add_dictionary_glob_extension

Python: `add_dictionary_glob_extension(ext)`  
Scheme: `(add-dictionary-glob-extension ext)`

add an extension to be treated as geometry dictionary files

Arguments: ext (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_dictionary_glob_extension("hello")` | ran (no return value) |
| Scheme | `(add-dictionary-glob-extension "hello")` | ran (no return value) |

### add_map_glob_extension

Python: `add_map_glob_extension(ext)`  
Scheme: `(add-map-glob-extension ext)`

add an extension to be treated as geometry map files

Arguments: ext (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_map_glob_extension("hello")` | ran (no return value) |
| Scheme | `(add-map-glob-extension "hello")` | ran (no return value) |

### export_map_gui

Python: `export_map_gui(export_map_fragment)`  
Scheme: `(export-map-gui export-map-fragment)`

show the export map GUI

Arguments: export_map_fragment (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `export_map_gui(1)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(export-map-gui 1)` | stopped Coot when tried without a window (not checked with a window) |

### file_chooser_overwrite_state

Python: `file_chooser_overwrite_state()`  
Scheme: `(file-chooser-overwrite-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `file_chooser_overwrite_state()` | ran, returned `1` |
| Scheme | `(file-chooser-overwrite-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### file_chooser_selector_state

Python: `file_chooser_selector_state()`  
Scheme: `(file-chooser-selector-state)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `file_chooser_selector_state()` | ran, returned `1` |
| Scheme | `(file-chooser-selector-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### file_type_coords

Python: `file_type_coords(file_name)`  
Scheme: `(file-type-coords file-name)`

is the given file name suitable to be read as coordinates?

Arguments: file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `file_type_coords("tutorial-modern.pdb")` | ran, returned `1` |
| Scheme | `(file-type-coords "tutorial-modern.pdb")` | ran, returned `1` |

Python and Scheme gave the same answer.

### filter_fileselection_filenames_state

Python: `filter_fileselection_filenames_state()`  
Scheme: `(filter-fileselection-filenames-state)`

, return the state of the above variable

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `filter_fileselection_filenames_state()` | ran, returned `0` |
| Scheme | `(filter-fileselection-filenames-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### make_directory_maybe

Python: `make_directory_maybe(dir)`  
Scheme: `(make-directory-maybe dir)`

make a directory dir (if it doesn't exist) and return error code

 If it can be created, create the directory dir, return the success status
 like mkdir: mkdir

 Returns zero on success, or -1 if an error occurred.
 If dir already exists as a directory, return 0 of course.

Arguments: dir (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_directory_maybe(".")` | ran, returned `0` |
| Scheme | `(make-directory-maybe ".")` | ran, returned `0` |

Python and Scheme gave the same answer.

### open_coords_dialog

Python: `open_coords_dialog()`  
Scheme: `(open-coords-dialog)`

display the open coordinates dialog

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `open_coords_dialog()` | ran (no return value) |
| Scheme | `(open-coords-dialog)` | ran (no return value) |

### remove_coordinates_glob_extension

Python: `remove_coordinates_glob_extension(ext)`  
Scheme: `(remove-coordinates-glob-extension ext)`

remove an extension to be treated as coordinate files

Arguments: ext (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_coordinates_glob_extension("hello")` | ran (no return value) |
| Scheme | `(remove-coordinates-glob-extension "hello")` | ran (no return value) |

### remove_data_glob_extension

Python: `remove_data_glob_extension(ext)`  
Scheme: `(remove-data-glob-extension ext)`

remove an extension to be treated as data (reflection) files

Arguments: ext (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_data_glob_extension("hello")` | ran (no return value) |
| Scheme | `(remove-data-glob-extension "hello")` | ran (no return value) |

### remove_dictionary_glob_extension

Python: `remove_dictionary_glob_extension(ext)`  
Scheme: `(remove-dictionary-glob-extension ext)`

remove an extension to be treated as geometry dictionary files

Arguments: ext (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_dictionary_glob_extension("hello")` | ran (no return value) |
| Scheme | `(remove-dictionary-glob-extension "hello")` | ran (no return value) |

### remove_map_glob_extension

Python: `remove_map_glob_extension(ext)`  
Scheme: `(remove-map-glob-extension ext)`

remove an extension to be treated as geometry map files

Arguments: ext (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_map_glob_extension("hello")` | ran (no return value) |
| Scheme | `(remove-map-glob-extension "hello")` | ran (no return value) |

### set_file_chooser_overwrite

Python: `set_file_chooser_overwrite(istate)`  
Scheme: `(set-file-chooser-overwrite istate)`

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_file_chooser_overwrite(1)` | ran (no return value) |
| Scheme | `(set-file-chooser-overwrite 1)` | ran (no return value) |

### set_file_chooser_selector

Python: `set_file_chooser_selector(istate)`  
Scheme: `(set-file-chooser-selector istate)`

--- CHECKME - do these need to be here? ---

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_file_chooser_selector(1)` | ran (no return value) |
| Scheme | `(set-file-chooser-selector 1)` | ran (no return value) |

### set_filter_fileselection_filenames

Python: `set_filter_fileselection_filenames(istate)`  
Scheme: `(set-filter-fileselection-filenames istate)`

on opening a file selection dialog, pre-filter the files.

set to 1 to pre-filter, [0 (off, non-pre-filtering) is the default

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_filter_fileselection_filenames(1)` | ran (no return value) |
| Scheme | `(set-filter-fileselection-filenames 1)` | ran (no return value) |

### set_show_paths_in_display_manager

Python: `set_show_paths_in_display_manager(i)`  
Scheme: `(set-show-paths-in-display-manager i)`

Show Paths in Display Manager?

 Some people don't like to see the full path names in the display manager
 here is the way to turn them off, with an argument of 1.

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_show_paths_in_display_manager(1)` | ran (no return value) |
| Scheme | `(set-show-paths-in-display-manager 1)` | ran (no return value) |

### set_sticky_sort_by_date

Python: `set_sticky_sort_by_date()`  
Scheme: `(set-sticky-sort-by-date)`

sort files in the file selection by date?

 some people like to have their files sorted by date by default

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_sticky_sort_by_date()` | ran (no return value) |
| Scheme | `(set-sticky-sort-by-date)` | ran (no return value) |

### show_paths_in_display_manager_state

Python: `show_paths_in_display_manager_state()`  
Scheme: `(show-paths-in-display-manager-state)`

return the internal state

 What is the internal flag?

 Returns 1 for "yes, display paths" , 0 for not

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_paths_in_display_manager_state()` | ran, returned `0` |
| Scheme | `(show-paths-in-display-manager-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### unset_sticky_sort_by_date

Python: `unset_sticky_sort_by_date()`  
Scheme: `(unset-sticky-sort-by-date)`

do not sort files in the file selection by date?

 removes the sorting of files by date

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `unset_sticky_sort_by_date()` | ran (no return value) |
| Scheme | `(unset-sticky-sort-by-date)` | ran (no return value) |

