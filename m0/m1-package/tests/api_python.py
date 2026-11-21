
import sys, os, traceback
res = []
def check(name, fn):
    try:
        v = fn()
        ok = True if v is None else bool(v)
        res.append((name, ok, repr(v)[:80]))
    except Exception as e:
        res.append((name, False, "EXC " + repr(e)[:110]))
print("PYVER", sys.version.split()[0], flush=True)
import coot
check("import coot (SWIG _coot)", lambda: coot.__name__ == "coot")
check("coot_version -> str", lambda: isinstance(coot.coot_version(), str) and coot.coot_version())
imol = coot.read_pdb(os.path.join(os.environ["COOT_PREFIX"], "test-data", "standard-residues.pdb"))
check("read_pdb -> valid imol", lambda: imol >= 0 and coot.is_valid_model_molecule(imol))
check("molecule_name -> str", lambda: isinstance(coot.molecule_name(imol), str) and coot.molecule_name(imol).endswith("standard-residues.pdb"))
check("n_chains -> int", lambda: isinstance(coot.n_chains(imol), int) and coot.n_chains(imol) > 0)
check("chain_id_py -> str", lambda: isinstance(coot.chain_id_py(imol, 0), str))
c0 = coot.chain_id_py(imol, 0)
check("chain_n_residues -> int", lambda: coot.chain_n_residues(c0, imol) > 0)
r0 = coot.seqnum_from_serial_number(imol, c0, 0)
check("residue_name -> str", lambda: isinstance(coot.residue_name(imol, c0, r0, ""), str))
check("residue_info_py -> list of atoms", lambda: isinstance(coot.residue_info_py(imol, c0, r0, ""), list) and len(coot.residue_info_py(imol, c0, r0, "")) > 0)
check("atom names are str (not bytes)", lambda: all(isinstance(a[0][0], str) for a in coot.residue_info_py(imol, c0, r0, "")))
check("symmetry_operators_py (patched PyBool_Check)", lambda: coot.symmetry_operators_py(imol) is not None)
check("symmetry_operators_to_xHM_py (patched)", lambda: coot.symmetry_operators_to_xHM_py(["x,y,z", "-x,y+1/2,-z"]) is not None)
check("non-ASCII path arg -> -1", lambda: coot.read_pdb("/nonexistent/\u00e9.pdb") == -1)
check("write_pdb_file", lambda: coot.write_pdb_file(imol, os.path.join(os.environ["COOT_PREFIX"], "work", "out.pdb")) in (0, None))
g = globals()
check("script layer loaded into __main__ (chain_ids, is_protein_chain_qm)", lambda: "chain_ids" in g and "is_protein_chain_qm" in g)
check("chain_ids -> list[str]", lambda: isinstance(g["chain_ids"](imol), list) and all(isinstance(c, str) for c in g["chain_ids"](imol)))
check("is_protein_chain_qm(imol, chain)", lambda: g["is_protein_chain_qm"](imol, c0) in (0, 1))
check("residue_spec helper (str ops ported)", lambda: g["residue_spec_to_chain_id"](["A", 1, ""]) == "A")
check("atom_spec -> residue_spec", lambda: g["atom_spec_to_residue_spec"](["A", 1, "", " CA ", ""]) is not None)
def sanitise_active():   # build 30: coot_utils took chain, residue and insertion code all from active_atom[2]
    coot.set_go_to_atom_molecule(imol); coot.set_go_to_atom_chain_residue_atom_name(c0, r0, " CA ")
    coot.set_atom_string_attribute(imol, c0, r0, "", " CA ", "", "alt-conf", "A")
    before = [a[0][1] for a in coot.residue_info_py(imol, c0, r0, "") if a[0][0] == " CA "]
    g["sanitise_alt_confs_active_residue"]()
    after = [a[0][1] for a in coot.residue_info_py(imol, c0, r0, "") if a[0][0] == " CA "]
    return True if (before == ["A"] and after == [""]) else (before, after)
check("sanitise_alt_confs_active_residue clears an orphan alt conf", sanitise_active)
def ligand_overlaps():   # build 30: the C++ of 0.9.8.96 never filled the list ("FIXME"): always False
    im = coot.read_pdb(os.path.join(os.environ["COOT_PREFIX"], "test-data", "tutorial-modern.pdb"))
    r = g["ligand_atom_overlaps"](im, ["A", 41, ""], 5.0)
    return True if (isinstance(r, list) and r and all(len(x) == 4 and x[0][1] == "A" for x in r)) else r
check("ligand_atom_overlaps returns the overlaps (as Scheme does)", ligand_overlaps)
def cif_twice():          # build 31: mmdb's WriteCIFASCII kept its CIF data: each write_cif_file call wrote the model again
    im = coot.read_pdb(os.path.join(os.environ["COOT_PREFIX"], "test-data", "tutorial-modern.pdb"))
    p = os.path.join(os.environ["COOT_PREFIX"], "work", "twice.cif")
    sizes = []
    for i in range(3):
        coot.write_cif_file(im, p); sizes.append(os.path.getsize(p))
    back = coot.read_pdb(p)
    if sizes[0] == sizes[2] and coot.is_valid_model_molecule(back) and g["n_atoms"](back) == g["n_atoms"](im): return True
    raise AssertionError("sizes %r, atoms read back %r of %r" % (sizes, g["n_atoms"](back) if back >= 0 else back, g["n_atoms"](im)))
check("write_cif_file three times: same file each time, reads back with the same atoms", cif_twice)
nfun = sum(1 for k, v in g.items() if callable(v) and not k.startswith("_"))
print("INFO callables visible in __main__:", nfun)
w = max(len(r[0]) for r in res)
for n, ok, v in res: print(("PASS " if ok else "FAIL ") + n.ljust(w) + "  " + v)
print("SUMMARY", sum(1 for r in res if r[1]), "/", len(res), flush=True)
