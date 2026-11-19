# Info Dialog

[Scripting reference](../README.md) > Info Dialog (3 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### info_dialog

Python: `info_dialog(txt)`  
Scheme: `(info-dialog txt)`

create a dialog with information

 create a dialog with information string txt. User has to click to
 dismiss it, but it is not modal (nothing in coot is modal).

Arguments: txt (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `info_dialog("hello")` | not tried |
| Scheme | `(info-dialog "hello")` | not tried |

### info_dialog_and_text

Python: `info_dialog_and_text(txt)`  
Scheme: `(info-dialog-and-text txt)`

create a dialog with information and print to console

 as info_dialog but print to console as well.

Arguments: txt (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `info_dialog_and_text("hello")` | not tried |
| Scheme | `(info-dialog-and-text "hello")` | not tried |

### info_dialog_with_markup

Python: `info_dialog_with_markup(txt)`  
Scheme: `(info-dialog-with-markup txt)`

as above, create a dialog with information

This dialog is left-justified and can use markup such as angled bracketted tt or i

Arguments: txt (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `info_dialog_with_markup("hello")` | not tried |
| Scheme | `(info-dialog-with-markup "hello")` | not tried |

