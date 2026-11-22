# How Refine/Improve Ramachandran Plot (try peptide flips) decides

Calculate > All Molecule... > Refine/Improve Ramachandran Plot (try peptide flips)... is new in coot0 (build 21; map check build 23; report build 24). This page describes how it decides whether to keep a flip, and how to change its limits.

For each residue *i* that is joined to *i*+1 by a peptide bond, the zone *i*-1 .. *i*+1 is refined twice with
Ramachandran restraints: **A** as it is, and **B** after Coot's Pep-flip of the peptide *i* / *i*+1 (the C=O of *i*
turned 180 degrees round the CA(*i*)-CA(*i*+1) axis). Each result is scored with numbers Coot itself provides:

```
rho(x)     = density of the refinement map at point x (Coot's density_at_point, linear interpolation), in map units
sigma      = r.m.s. deviation of the map from its mean (Coot's map_sigma)
O          = rho(O_i) / sigma                                     carbonyl O of residue i, in sigma
P          = ( rho(C_i) + rho(O_i) + rho(N_i+1) ) / sigma         the peptide C, O, N together, in sigma
F          = sum over the atoms a of residues i and i+1 of  rho(a) * occupancy(a)     (Coot's density_score_residue)
R          = sum over residues i and i+1 of their Ramachandran region (outlier 0, allowed 1, favoured 2; Coot's own classification)
```

(With alternate conformations each conformer is scored on its own atoms plus the shared ones.) Flip B is kept over A
only if all of these hold:

```
R_B >= R_A                                    (no residue goes to a worse Ramachandran region)
O_B >= O_A - rama_flip_max_o_loss             (default 0.3 sigma)
P_B >= P_A - rama_flip_max_peptide_loss       (default 0.6 sigma)
F_B >= F_A - rama_flip_max_fit_loss * |F_A|   (default 0.02, i.e. 2 %)
```

and then either `R_B > R_A`, or (same regions) `O_B >= O_A + rama_flip_o_gain` and `P_B >= P_A + rama_flip_o_gain`
(default 1.0 sigma) and `F_B > F_A + rama_flip_density_gain * |F_A|` (default 0). Without a map nothing is flipped. So
"the carbonyl O left the density" means: after the flip, the map value at the O position dropped (for example from 7.3
to -0.8 sigma), which the old rule (Ramachandran first) accepted and this one does not.

The report counts a peptide as **turned** when its carbonyl O ends up more than `rama_flip_turn_angle` (default 90)
degrees from where it was at the start of the run, measured round the CA(*i*)-CA(*i*+1) axis. The terminal shows both
scores of every try (`INFO:: rama flip A 43 '' kept original A (R, n, F, O, P) B (...)`).

**Changing the limits.** They are Python variables. Type the new value in Calculate > Scripting > Python... before the
run, for example `rama_flip_o_gain = 1.5` (stricter: a flip with the same regions needs 1.5 sigma more at the O) or
`rama_flip_max_o_loss = 0.0`. To keep them, put such lines in a `.py` file in coot0's preferences folder, which is
`~/Library/Application Support/coot0/home/.coot-preferences/` when installed with `install.sh` (coot0 uses its own
home, so your `~/.coot-preferences` is not read unless you start it with `COOT_USE_HOME=1`).

| Variable | Default | Meaning |
|---|---|---|
| `rama_flip_max_o_loss` | 0.3 | the flipped carbonyl O may lose at most this much density (sigma) |
| `rama_flip_max_peptide_loss` | 0.6 | the peptide C + O + N may lose at most this much (sigma, sum) |
| `rama_flip_max_fit_loss` | 0.02 | the map fit of residues *i*, *i*+1 may drop at most this fraction |
| `rama_flip_o_gain` | 1.0 | same Ramachandran regions: O and C + O + N must each gain this much (sigma) |
| `rama_flip_density_gain` | 0.0 | same regions: extra fraction by which the map fit must improve |
| `rama_flip_turn_angle` | 90 | degrees the carbonyl O must turn for the report to count a peptide as turned |
