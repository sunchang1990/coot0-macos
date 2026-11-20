# PHENIX Support

[Scripting reference](../README.md) > PHENIX Support (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### set_button_label_for_external_refinement

Python: `set_button_label_for_external_refinement(button_label)`  
Scheme: `(set-button-label-for-external-refinement button-label)`

set the button label of the external Refinement program

Arguments: button_label (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_button_label_for_external_refinement("hello")` | not run: not run automatically (external: exits, uses the network, an external program, files or a screen) |
| Scheme | `(set-button-label-for-external-refinement "hello")` | not run: not run automatically (external: exits, uses the network, an external program, files or a screen) |

