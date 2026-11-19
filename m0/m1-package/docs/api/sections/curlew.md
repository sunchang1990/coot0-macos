# curlew

[Scripting reference](../README.md) > curlew (3 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### register_extension

Python: `register_extension(name, version)`  
Scheme: `(register-extension name version)`

register an extension

Arguments: name (text), version (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `register_extension("my-name", "hello")` | not tried |
| Scheme | `(register-extension "my-name" "hello")` | not tried |

### remove_file_curlew_menu_item_maybe

Python: `remove_file_curlew_menu_item_maybe()`  
Scheme: `(remove-file-curlew-menu-item-maybe)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_file_curlew_menu_item_maybe()` | not tried |
| Scheme | `(remove-file-curlew-menu-item-maybe)` | not tried |

### version_for_extension

Python: `version_for_extension(name)`  
Scheme: `(version-for-extension name)`

Arguments: name (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `version_for_extension("my-name")` | not tried |
| Scheme | `(version-for-extension "my-name")` | not tried |

