# Align and Mutate

[Scripting reference](../README.md) > Align and Mutate (4 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### align_and_mutate

Python: `align_and_mutate(imol, chain_id, fasta_maybe, renumber_residues_flag)`  
Scheme: `(align-and-mutate imol chain-id fasta-maybe renumber-residues-flag)`

align and mutate the given chain to the given sequence

Arguments: imol (a whole number), chain_id (text), fasta_maybe (text), renumber_residues_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `align_and_mutate(0, "A", "DVSGTACLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLIDQTC", 0)` | ran (no return value); changed: molecule 0: atoms of 1 residue(s) (A6); n_atoms(0): 1465 -> 1463 |
| Scheme | `(align-and-mutate 0 "B" "DVSGTACLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLIDQTC" 0)` | ran (no return value); changed: molecule 0: atoms of 1 residue(s) (B6); n_atoms(0): 1465 -> 1463 |

Example written and checked by hand on the test data. Expected: chain is aligned to the sequence and mismatching residues are mutated (here V6A).

### alignment_results

Python: `alignment_results(imol, chain_id, seq)`  
Scheme: `(alignment-results-scm imol chain-id seq)`

Arguments: imol (a whole number), chain_id (text), seq (text). Returns: a value (see the result of the example).
Also available in Python as `alignment_results_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `alignment_results(0, "A", "DVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLIDQTC")` | ran, returned `False` |
| Scheme | `(alignment-results-scm 0 "A" "DVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLIDQTC")` | ran, returned `#f` |

Example written and checked by hand on the test data. Expected: should return the alignment of the chain against the sequence.

Note: Both C++ functions (alignment_results_py / alignment_results_scm) are empty stubs in 0.9.8.96: they always return False/#f.

Python and Scheme gave the same answer.

### nearest_residue_by_sequence

Python: `nearest_residue_by_sequence(imol, chain_id, resno, ins_code)`  
Scheme: `(nearest-residue-by-sequence imol chain-id resno ins-code)`

return the residue spec of the nearest residue by sequence
 numbering. Return Python False if not possible

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text). Returns: a value (see the result of the example).
Also available in Python as `nearest_residue_by_sequence_py`.
Also available in Scheme as `nearest-residue-by-sequence-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `nearest_residue_by_sequence(0, "A", 41, "")` | ran, returned `[True, 'A', 41, '']` |
| Scheme | `(nearest-residue-by-sequence 0 "A" 41 "")` | ran, returned `(#t "A" 41 "")` |

Python and Scheme gave the same answer.

### set_alignment_gap_and_space_penalty

Python: `set_alignment_gap_and_space_penalty(wgap, wspace)`  
Scheme: `(set-alignment-gap-and-space-penalty wgap wspace)`

set the penalty for affine gap and space when aligning, defaults -3.0 and -0.4

Arguments: wgap (a number), wspace (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_alignment_gap_and_space_penalty(1.0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-alignment-gap-and-space-penalty 1.0 1.0)` | ran (no return value, nothing visible changed) |

