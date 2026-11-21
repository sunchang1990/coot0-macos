# Rotamer Scoring

[Scripting reference](../README.md) > Rotamer Scoring (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### score_rotamers

Python: `score_rotamers(imol, chain_id, res_no, ins_code, alt_conf, imol_map, clash_flag, lowest_probability)`  
Scheme: `(score-rotamers imol chain-id res-no ins-code alt-conf imol-map clash-flag lowest-probability)`

return a list (possibly empty)

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), alt_conf (text), imol_map (a whole number), clash_flag (a whole number), lowest_probability (a number). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `score_rotamers(0, "A", 41, "", "", 1, 1, 1.0)` | ran, returned `[['mt-10 ', 33.0, -0.625325620174408, [[' N  ', 1.7893829345703125], [' CA ', -0.008128275163471699], [' CB ', -0.222001 ...` |
| Scheme | `(score-rotamers 0 "A" 41 "" "" 1 1 1.0)` | ran, returned `(("mt-10 " 33.0 ((" N  " 1.7893829345703125) (" CA " -0.008128275163471699) (" CB " -0.22200140357017517) (" CG " 0.1372 ...` |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

