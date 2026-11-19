# Browser Interface

[Scripting reference](../README.md) > Browser Interface (3 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### browser_url

Python: `browser_url(url)`  
Scheme: `(browser-url url)`

try to open given url in Web browser

Arguments: url (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `browser_url("hello")` | not run: not run automatically (url: exits, uses the network, an external program, files or a screen) |
| Scheme | `(browser-url "hello")` | not run: not run automatically (url: exits, uses the network, an external program, files or a screen) |

### handle_online_coot_search_request

Python: `handle_online_coot_search_request(entry_text)`  
Scheme: `(handle-online-coot-search-request entry-text)`

the search interface

find words, construct a url and open it.

Arguments: entry_text (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_online_coot_search_request("hello")` | ran (no return value) |
| Scheme | `(handle-online-coot-search-request "hello")` | ran (no return value) |

### set_browser_interface

Python: `set_browser_interface(browser)`  
Scheme: `(set-browser-interface browser)`

set command to open the web browser,

examples are "open" or "mozilla"

Arguments: browser (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_browser_interface("hello")` | not tried |
| Scheme | `(set-browser-interface "hello")` | not tried |

