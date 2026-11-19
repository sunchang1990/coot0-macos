# Coot scripting reference (coot0 0.9.8.96-b26)

Every function that Coot 0.9.8.96 offers to Python and Scheme scripts: 1735 functions, 1717 in Python and 1689 in Scheme. For each one: its Python and Scheme names, what Coot's own source says about it, a concrete example on the test data, and what happened when the example was tried.

For recipes that do whole tasks (refine, edit, customize the toolbar, batch scripts...), see the [cookbook](../cookbook/README.md).

## How to read it

- **Names.** Python uses `_`, Scheme uses `-`: Python `residue_name(0, "A", 41, "")` is Scheme `(residue-name 0 "A" 41 "")`.
- **Examples** use the test data in the package (`test-data/`): molecule **0** is `tutorial-modern.pdb` (chains A and B, residues 1-93 and 1-96; residue A41 is a glutamate), molecule **1** is the 2Fo-Fc map made from `rnasa-1.8-all_refmac1.mtz` (`make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)`). Load them in this order in a new Coot and every example runs as written. With your own data, change the molecule number, chain, residue number and file names.
- **Residue specs** are lists: `["A", 41, ""]` in Python, `(list "A" 41 "")` in Scheme (chain, residue number, insertion code). **Atom names** have 4 characters as in a PDB file: `" CA "`.
- **The examples were made by a program** from the argument names (a chain gets `"A"`, a residue number 41, a flag 1, ...). For most functions that gives a sensible call; for some the values are only placeholders (`"hello"` for a text, 1 for a number) that you should replace.
- **"When tried"** is what happened when the example was run on the test data by `tests/run-api-examples.sh`, without a window: *ran* (with the value it returned), *error* (with Coot's message; usually the example needs other values), *stopped Coot (no window)* (the function needs the graphics window; it was not checked with one), *not run* (it would quit Coot, use the network, run an external program, or needs a widget). *Ran* means only that Coot accepted the call; the result was not checked.

## Results of trying the examples

| | Ran | Error | Stopped Coot (no window) | No answer in 60 s | Not run |
|---|---|---|---|---|---|
| Python | 522 | 6 | 18 | 3 | 84 |
| Scheme | 511 | 7 | 17 | 3 | 80 |

## Sections

Coot's own section names, in alphabetical order. Also: [all functions A-Z](A-Z.md), [functions in only one language](one-language-only.md).

| Section | Functions |
|---|---|
| [180 Flip Side chain](sections/180-flip-side-chain.md) | 3 |
| [Add A Residue Functions](sections/add-a-residue-functions.md) | 1 |
| [Add Terminal Residue Functions](sections/add-terminal-residue-functions.md) | 15 |
| [Align and Mutate](sections/align-and-mutate.md) | 4 |
| [Alternative Conformation](sections/alternative-conformation.md) | 15 |
| [Anisotropic Atoms Interface](sections/anisotropic-atoms-interface.md) | 9 |
| [Atom Info Interface](sections/atom-info-interface.md) | 1 |
| [Atom Information functions](sections/atom-information-functions.md) | 17 |
| [Atom Labelling](sections/atom-labelling.md) | 8 |
| [Atom Selection Utilities](sections/atom-selection-utilities.md) | 18 |
| [Aux functions](sections/aux-functions.md) | 1 |
| [Background Colour](sections/background-colour.md) | 3 |
| [Backrubbing function](sections/backrubbing-function.md) | 2 |
| [Backup Functions](sections/backup-functions.md) | 16 |
| [Baton Build Interface Functions](sections/baton-build-interface-functions.md) | 11 |
| [Bond Representation](sections/bond-representation.md) | 46 |
| [Browser Interface](sections/browser-interface.md) | 3 |
| [CCP4mg Interface](sections/ccp4mg-interface.md) | 3 |
| [Change Chain ID](sections/change-chain-id.md) | 2 |
| [check Waters Interface](sections/check-waters-interface.md) | 10 |
| [Clipping Functions](sections/clipping-functions.md) | 2 |
| [Close Molecule Functions](sections/close-molecule-functions.md) | 1 |
| [CNS Data Functions](sections/cns-data-functions.md) | 2 |
| [Colour](sections/colour.md) | 13 |
| [Coot's Hole implementation](sections/coot-s-hole-implementation.md) | 7 |
| [Crosshairs Interface](sections/crosshairs-interface.md) | 2 |
| [curlew](sections/curlew.md) | 3 |
| [Cursor Function](sections/cursor-function.md) | 5 |
| [Delete Residues](sections/delete-residues.md) | 46 |
| [Density Functions](sections/density-functions.md) | 37 |
| [Density Increment](sections/density-increment.md) | 20 |
| [Dictionary Functions](sections/dictionary-functions.md) | 5 |
| [Dipoles](sections/dipoles.md) | 5 |
| [Display Functions](sections/display-functions.md) | 24 |
| [Display Lists for Maps](sections/display-lists-for-maps.md) | 3 |
| [Dock Sidechains](sections/dock-sidechains.md) | 1 |
| [Dots Representation](sections/dots-representation.md) | 6 |
| [Drag and Drop Functions](sections/drag-and-drop-functions.md) | 1 |
| [Dynamic Map](sections/dynamic-map.md) | 9 |
| [Edit Chi Angles](sections/edit-chi-angles.md) | 12 |
| [Edit Fuctions](sections/edit-fuctions.md) | 4 |
| [EM interface](sections/em-interface.md) | 5 |
| [Execute Refmac](sections/execute-refmac.md) | 43 |
| [Experimental](sections/experimental.md) | 9 |
| [External Ray-Tracing](sections/external-ray-tracing.md) | 15 |
| [Extra Ligand Functions](sections/extra-ligand-functions.md) | 4 |
| [Extra Map Functions](sections/extra-map-functions.md) | 18 |
| [FFFearing](sections/fffearing.md) | 3 |
| [File Selection Functions](sections/file-selection-functions.md) | 1 |
| [File System Functions](sections/file-system-functions.md) | 22 |
| [FLE-View](sections/fle-view.md) | 9 |
| [Font Parameters](sections/font-parameters.md) | 4 |
| [General (cc-interface)](sections/general-cc-interface.md) | 21 |
| [Generic Objects](sections/generic-objects.md) | 21 |
| [Get Sequence](sections/get-sequence.md) | 22 |
| [Glyco Tools](sections/glyco-tools.md) | 1 |
| [Go To Atom Widget Functions](sections/go-to-atom-widget-functions.md) | 31 |
| [graphics 2D ligand view](sections/graphics-2d-ligand-view.md) | 1 |
| [Graphics Move](sections/graphics-move.md) | 4 |
| [Graphics Text](sections/graphics-text.md) | 4 |
| [Graphics Utility Functions](sections/graphics-utility-functions.md) | 45 |
| [Helices and Strands](sections/helices-and-strands.md) | 8 |
| [History Functions](sections/history-functions.md) | 4 |
| [Images](sections/images.md) | 1 |
| [Info Dialog](sections/info-dialog.md) | 3 |
| [Interface Preferences](sections/interface-preferences.md) | 62 |
| [Intermediate Atom Manipulation Interface](sections/intermediate-atom-manipulation-interface.md) | 3 |
| [Jiggle Fit](sections/jiggle-fit.md) | 5 |
| [Least-Squares matching](sections/least-squares-matching.md) | 10 |
| [Library and Utility Functions](sections/library-and-utility-functions.md) | 16 |
| [Ligand Builder (Lidia)](sections/ligand-builder-lidia.md) | 2 |
| [Ligand Fitting Functions](sections/ligand-fitting-functions.md) | 26 |
| [Ligands](sections/ligands.md) | 36 |
| [LSQ-improve](sections/lsq-improve.md) | 9 |
| [Mainchain Building Functions](sections/mainchain-building-functions.md) | 3 |
| [Map and Molecule Control](sections/map-and-molecule-control.md) | 24 |
| [Map colour](sections/map-colour.md) | 3 |
| [Map Contouring Functions](sections/map-contouring-functions.md) | 6 |
| [Map Functions](sections/map-functions.md) | 35 |
| [Map Sharpening Interface](sections/map-sharpening-interface.md) | 4 |
| [Map to Model Correlation](sections/map-to-model-correlation.md) | 11 |
| [Marking Fixed Atom Interface](sections/marking-fixed-atom-interface.md) | 6 |
| [Masks](sections/masks.md) | 5 |
| [Merge Fragments](sections/merge-fragments.md) | 1 |
| [mmCIF Functions](sections/mmcif-functions.md) | 20 |
| [Model/Fit/Refine Functions](sections/model-fit-refine-functions.md) | 9 |
| [Mogul](sections/mogul.md) | 6 |
| [Molecule Info Functions](sections/molecule-info-functions.md) | 26 |
| [Molprobity Interface](sections/molprobity-interface.md) | 11 |
| [Monomer](sections/monomer.md) | 14 |
| [More Refinement Functions](sections/more-refinement-functions.md) | 8 |
| [More Symmetry Functions](sections/more-symmetry-functions.md) | 5 |
| [Mouse Buttons](sections/mouse-buttons.md) | 6 |
| [Movies Interface](sections/movies-interface.md) | 5 |
| [MTZ and data handling utilities](sections/mtz-and-data-handling-utilities.md) | 9 |
| [Multi-Residue Torsion](sections/multi-residue-torsion.md) | 1 |
| [Mutate Functions](sections/mutate-functions.md) | 17 |
| [NCS](sections/ncs.md) | 29 |
| [New Molecule by Section Interface](sections/new-molecule-by-section-interface.md) | 2 |
| [Nomenclature Errors](sections/nomenclature-errors.md) | 2 |
| [Nucleotides](sections/nucleotides.md) | 1 |
| [Orthogonal Axes](sections/orthogonal-axes.md) | 1 |
| [Other functions](sections/other-functions.md) | 11 |
| [Parameters from map](sections/parameters-from-map.md) | 7 |
| [Partial Charges](sections/partial-charges.md) | 1 |
| [PDB Functions](sections/pdb-functions.md) | 7 |
| [Pep-flip Interface](sections/pep-flip-interface.md) | 5 |
| [PHENIX Support](sections/phenix-support.md) | 1 |
| [PISA Interaction](sections/pisa-interaction.md) | 6 |
| [PKGDATADIR](sections/pkgdatadir.md) | 1 |
| [Pointer Atom Functions](sections/pointer-atom-functions.md) | 8 |
| [Pointer Functions](sections/pointer-functions.md) | 2 |
| [Pointer Position Function](sections/pointer-position-function.md) | 1 |
| [protein-db](sections/protein-db.md) | 2 |
| [Ramachandran Plot Functions](sections/ramachandran-plot-functions.md) | 14 |
| [Read Phases File Functions](sections/read-phases-file-functions.md) | 9 |
| [Recover Session Function](sections/recover-session-function.md) | 1 |
| [Refinement with specs](sections/refinement-with-specs.md) | 20 |
| [Refmac Functions](sections/refmac-functions.md) | 6 |
| [Regularization and Refinement](sections/regularization-and-refinement.md) | 113 |
| [Remote Control](sections/remote-control.md) | 7 |
| [Renumber Residue Range](sections/renumber-residue-range.md) | 2 |
| [Residue Environment Functions](sections/residue-environment-functions.md) | 11 |
| [Residue Info](sections/residue-info.md) | 13 |
| [Restraints Interface](sections/restraints-interface.md) | 16 |
| [Rigid Body Refinement Interface](sections/rigid-body-refinement-interface.md) | 6 |
| [RNA/DNA](sections/rna-dna.md) | 5 |
| [Rotamer Functions](sections/rotamer-functions.md) | 20 |
| [Rotamer Scoring](sections/rotamer-scoring.md) | 1 |
| [Rotation Centre](sections/rotation-centre.md) | 11 |
| [Save Coordinates](sections/save-coordinates.md) | 4 |
| [SBase interface](sections/sbase-interface.md) | 5 |
| [Screen Rotation](sections/screen-rotation.md) | 4 |
| [Screen Translation](sections/screen-translation.md) | 3 |
| [Scripting](sections/scripting.md) | 14 |
| [Scripting Interface](sections/scripting-interface.md) | 9 |
| [Sequence](sections/sequence.md) | 7 |
| [Sequence File (Assignment/Association)](sections/sequence-file-assignment-association.md) | 12 |
| [Sequence from Map](sections/sequence-from-map.md) | 36 |
| [Sequence View Interface](sections/sequence-view-interface.md) | 15 |
| [SHELXL Functions](sections/shelxl-functions.md) | 6 |
| [Simplex Refinement Interface](sections/simplex-refinement-interface.md) | 2 |
| [single-model view](sections/single-model-view.md) | 7 |
| [Skeletonization Interface](sections/skeletonization-interface.md) | 11 |
| [SMILES](sections/smiles.md) | 2 |
| [Smooth Scrolling](sections/smooth-scrolling.md) | 8 |
| [Spin Search Functions](sections/spin-search-functions.md) | 9 |
| [Startup Functions](sections/startup-functions.md) | 2 |
| [State Functions](sections/state-functions.md) | 8 |
| [status bar string functions](sections/status-bar-string-functions.md) | 1 |
| [Superposition (SSM)](sections/superposition-ssm.md) | 3 |
| [Surface Interface](sections/surface-interface.md) | 7 |
| [Symmetry Functions](sections/symmetry-functions.md) | 27 |
| [Terminal OXT Atom](sections/terminal-oxt-atom.md) | 1 |
| [The Virtual Trackball](sections/the-virtual-trackball.md) | 2 |
| [Trim](sections/trim.md) | 3 |
| [Unit Cell interface](sections/unit-cell-interface.md) | 4 |
| [Using S-expression molecules](sections/using-s-expression-molecules.md) | 10 |
| [Validation Functions](sections/validation-functions.md) | 24 |
| [Variance Map](sections/variance-map.md) | 1 |
| [Views Interface](sections/views-interface.md) | 20 |
| [Water Chain Functions](sections/water-chain-functions.md) | 2 |
| [Water Fitting Functions](sections/water-fitting-functions.md) | 15 |
| [Widget Utilities](sections/widget-utilities.md) | 2 |
| [Zoom Functions](sections/zoom-functions.md) | 8 |

## How this reference is made

`m0/tools/gen_api_index.py` reads Coot's SWIG wrappers (the functions really available) and its headers (signatures and descriptions); `tests/run-api-examples.sh` tries every example in Python and Scheme; `m0/tools/gen_api_docs.py` writes these pages. To check your own installation run `tests/run-api-examples.sh` (30-90 minutes).
