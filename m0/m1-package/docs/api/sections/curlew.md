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
| Python | `register_extension("my-name", "hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(register-extension "my-name" "hello")` | ran (no return value, nothing visible changed) |

### remove_file_curlew_menu_item_maybe

Python: `remove_file_curlew_menu_item_maybe()`  
Scheme: `(remove-file-curlew-menu-item-maybe)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_file_curlew_menu_item_maybe()` | ran (no return value, nothing visible changed) |
| Scheme | `(remove-file-curlew-menu-item-maybe)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: removes File > Curlew from the menubar when Coot was built without Curlew; called at start-up, no effect when called again.

### version_for_extension

Python: `version_for_extension(name)`  
Scheme: `(version-for-extension name)`

Arguments: name (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `version_for_extension("my-name")` | ran, returned `''` |
| Scheme | `(version-for-extension "my-name")` | ran, returned `""` |

Python and Scheme gave the same answer.

