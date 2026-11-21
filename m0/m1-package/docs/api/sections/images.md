# Images

[Scripting reference](../README.md) > Images (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### text_png_as_string

Python: `text_png_as_string(text_info_dict)`

make a png given the info in text_info_dict
fields: text, font, size, colour, slant, weight

Arguments: text_info_dict (a list or value). Returns: text.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `len(text_png_as_string({"text": "Coot", "font-size": 20, "fg-colour": "#202080"}))` | ran, returned `1031` |

Example written and checked by hand on the test data. Expected: returns a PNG image (as a string) of the text with the given font, size and colours.

Note: Returns the PNG data as a (binary) string; the example shows only its length.

