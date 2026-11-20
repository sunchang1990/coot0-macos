# Recover Session Function

[Scripting reference](../README.md) > Recover Session Function (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### recover_session

Python: `recover_session()`  
Scheme: `(recover-session)`

recover session

 After a crash, we provide this convenient interface to restore the
 session. It runs through all the molecules with models and looks
 at the coot backup directory looking for related backup files that
 are more recent that the read file. (Not very good, because you
 need to remember which files you read in before the crash - should
 be improved.)

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `recover_session()` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(recover-session)` | stopped Coot when tried without a window (not checked with a window) |

