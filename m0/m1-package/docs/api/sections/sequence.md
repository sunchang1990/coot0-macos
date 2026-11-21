# Sequence

[Scripting reference](../README.md) > Sequence (7 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### apply_fasta_multi_to_fragment

Python: `apply_fasta_multi_to_fragment(imol, chain_id, resno_start, resno_end, imol_map, fam)`  
Scheme: `(apply-fasta-multi-to-fragment imol chain-id resno-start resno-end imol-map fam)`

Arguments: imol (a whole number), chain_id (text), resno_start (a whole number), resno_end (a whole number), imol_map (a whole number), fam (`coot::fasta_multi`). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `apply_fasta_multi_to_fragment(0, "A", 1, 93, 1, "tutorial-modern.fasta")` | not run: not callable from scripting: its coot::fasta_multi argument cannot be created from Python or Scheme |
| Scheme | `(apply-fasta-multi-to-fragment 0 "A" 1 93 1 "tutorial-modern.fasta")` | not run: not callable from scripting: its coot::fasta_multi argument cannot be created from Python or Scheme |

Example written and checked by hand on the test data. Expected: internal C++ helper (needs a coot::fasta_multi object that scripts cannot make); use assign_sequences_to_best_matching_chain_from_fasta("tutorial-modern.fasta").

### apply_pir_alignment

Python: `apply_pir_alignment(imol, chain_id)`  
Scheme: `(apply-pir-alignment imol chain-id)`

apply the mutations of the associated alignment

Arguments: imol (a whole number), chain_id (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `apply_pir_alignment(0, "A")` | ran (no return value, nothing visible changed) |
| Scheme | `(apply-pir-alignment 0 "A")` | ran (no return value, nothing visible changed) |

### assign_sequence_to_best_matching_chain

Python: `assign_sequence_to_best_matching_chain(sequence)`  
Scheme: `(assign-sequence-to-best-matching-chain sequence)`

Arguments: sequence (text). Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `assign_sequence_to_best_matching_chain("DVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLID")` | ran, returned `True` |
| Scheme | `(assign-sequence-to-best-matching-chain "DVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLID")` | ran, returned `#t` |

Example written and checked by hand on the test data. Expected: True: the sequence is assigned to the chain(s) it matches (here both NCS chains A and B); see sequence_info(0).

Python and Scheme gave the same answer.

### assign_sequences_to_best_matching_chain_from_fasta

Python: `assign_sequences_to_best_matching_chain_from_fasta(fasta_file_name)`  
Scheme: `(assign-sequences-to-best-matching-chain-from-fasta fasta-file-name)`

Arguments: fasta_file_name (text). Returns: true or false.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `assign_sequences_to_best_matching_chain_from_fasta("tutorial-modern.fasta")` | ran, returned `True` |
| Scheme | `(assign-sequences-to-best-matching-chain-from-fasta "tutorial-modern.fasta")` | ran, returned `#t` |

Example written and checked by hand on the test data. Expected: True; every sequence of the FASTA file is assigned to its best-matching chain(s).

Note: With two near-identical sequences both are assigned to both chains (4 entries), so alignment_mismatches then reports mutations A94-96 from the longer chain_B sequence.

Python and Scheme gave the same answer.

### associate_pir_alignment

Python: `associate_pir_alignment(imol, chain_id, pir_alignment)`  
Scheme: `(associate-pir-alignment imol chain-id pir-alignment)`

associate an alignment with a chain in a model molecule
The pir_alignment is a string (with newlines)

Arguments: imol (a whole number), chain_id (text), pir_alignment (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `associate_pir_alignment(0, "A", "hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(associate-pir-alignment 0 "A" "hello")` | ran (no return value, nothing visible changed) |

### associate_pir_alignment_from_file

Python: `associate_pir_alignment_from_file(imol, chain_id, pir_alignment_file_name)`  
Scheme: `(associate-pir-alignment-from-file imol chain-id pir-alignment-file-name)`

associate an alignment in a file with a chain in a model molecule

Arguments: imol (a whole number), chain_id (text), pir_alignment_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `associate_pir_alignment_from_file(0, "A", "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(associate-pir-alignment-from-file 0 "A" "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

### sequence_comparison_to_chains

Python: `sequence_comparison_to_chains(imol, sequence)`  
Scheme: `(sequence-comparison-to-chains imol sequence)`

Arguments: imol (a whole number), sequence (text). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `sequence_comparison_to_chains(0, "ACDEFGHIKLMNPQRSTVWY")` | ran, returned `<Swig Object of type 'std::vector< coot::chain_mutation_info_container_t,std::allocator< coot::chain_mutation_info_conta ...` |
| Scheme | `(sequence-comparison-to-chains 0 "ACDEFGHIKLMNPQRSTVWY")` | ran, returned `#<collectable-swig-pointer std::vector< coot::chain_mutation_info_container_t > * c6ad9ec00>` |

