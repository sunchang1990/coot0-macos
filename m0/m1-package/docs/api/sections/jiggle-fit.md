# Jiggle Fit

[Scripting reference](../README.md) > Jiggle Fit (5 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### fit_chain_to_map_by_random_jiggle

Python: `fit_chain_to_map_by_random_jiggle(imol, chain_id, n_trials, jiggle_scale_factor)`  
Scheme: `(fit-chain-to-map-by-random-jiggle imol chain-id n-trials jiggle-scale-factor)`

jiggle fit the chain to the current refinment map. return < -100 if
 not possible, else return the new best fit for this chain.

Arguments: imol (a whole number), chain_id (text), n_trials (a whole number), jiggle_scale_factor (a number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fit_chain_to_map_by_random_jiggle(0, "A", 1, 1.0)` | ran, returned `-999.0` |
| Scheme | `(fit-chain-to-map-by-random-jiggle 0 "A" 1 1.0)` | ran, returned `-999.0` |

Python and Scheme gave the same answer.

### fit_chain_to_map_by_random_jiggle_and_blur

Python: `fit_chain_to_map_by_random_jiggle_and_blur(imol, chain_id, n_trials, jiggle_scale_factor, map_blur_factor)`  
Scheme: `(fit-chain-to-map-by-random-jiggle-and-blur imol chain-id n-trials jiggle-scale-factor map-blur-factor)`

jiggle fit the chain to the current refinment map
Use a map that is blurred by the give factor for fitting.
Returns < -100 if not possible, else return the new best fit for this chain.

Arguments: imol (a whole number), chain_id (text), n_trials (a whole number), jiggle_scale_factor (a number), map_blur_factor (a number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fit_chain_to_map_by_random_jiggle_and_blur(0, "A", 1, 1.0, 1.0)` | ran, returned `-100.0` |
| Scheme | `(fit-chain-to-map-by-random-jiggle-and-blur 0 "A" 1 1.0 1.0)` | ran, returned `-100.0` |

Python and Scheme gave the same answer.

### fit_molecule_to_map_by_random_jiggle

Python: `fit_molecule_to_map_by_random_jiggle(imol, n_trials, jiggle_scale_factor)`  
Scheme: `(fit-molecule-to-map-by-random-jiggle imol n-trials jiggle-scale-factor)`

jiggle fit the molecule to the current refinment map. return < -100 if
 not possible, else return the new best fit for this molecule.

Arguments: imol (a whole number), n_trials (a whole number), jiggle_scale_factor (a number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fit_molecule_to_map_by_random_jiggle(0, 1, 1.0)` | ran, returned `0.0` |
| Scheme | `(fit-molecule-to-map-by-random-jiggle 0 1 1.0)` | ran, returned `0.0` |

Python and Scheme gave the same answer.

### fit_molecule_to_map_by_random_jiggle_and_blur

Python: `fit_molecule_to_map_by_random_jiggle_and_blur(imol, n_trials, jiggle_scale_factor, map_blur_factor)`  
Scheme: `(fit-molecule-to-map-by-random-jiggle-and-blur imol n-trials jiggle-scale-factor map-blur-factor)`

jiggle fit the molecule to the current refinment map. return < -100 if
 not possible, else return the new best fit for this molecule - create a map that is blurred
 by the given factor for fitting

Arguments: imol (a whole number), n_trials (a whole number), jiggle_scale_factor (a number), map_blur_factor (a number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fit_molecule_to_map_by_random_jiggle_and_blur(0, 1, 1.0, 1.0)` | ran, returned `0.0` |
| Scheme | `(fit-molecule-to-map-by-random-jiggle-and-blur 0 1 1.0 1.0)` | ran, returned `0.0` |

Python and Scheme gave the same answer.

### fit_to_map_by_random_jiggle

Python: `fit_to_map_by_random_jiggle(imol, chain_id, resno, ins_code, n_trials, jiggle_scale_factor)`  
Scheme: `(fit-to-map-by-random-jiggle imol chain-id resno ins-code n-trials jiggle-scale-factor)`

jiggle fit to the current refinment map. return < -100 if
 not possible, else return the new best fit for this residue.

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), n_trials (a whole number), jiggle_scale_factor (a number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fit_to_map_by_random_jiggle(0, "A", 41, "", 1, 1.0)` | ran, returned `19.296470642089844` |
| Scheme | `(fit-to-map-by-random-jiggle 0 "A" 41 "" 1 1.0)` | ran, returned `19.296470642089844` |

Python and Scheme gave the same answer.

