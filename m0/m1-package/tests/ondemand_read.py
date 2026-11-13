
import os, coot
res = []
def check(name, fn):
    try:
        v = fn(); res.append((name, bool(v), repr(v)[:80]))
    except Exception as e: res.append((name, False, "EXC " + repr(e)[:100]))
pdb = os.path.join(os.environ["COOT_PREFIX"], "test-data", "nag_only.pdb")
imol = coot.read_pdb(pdb)
check("read a PDB whose only residue is NAG (not preloaded)", lambda: coot.is_valid_model_molecule(imol))
check("NAG dictionary was loaded on demand while reading the model", lambda: bool(coot.monomer_restraints_py("NAG")))
check("NAG restraints have atoms and bonds", lambda: len(coot.monomer_restraints_py("NAG").get("_chem_comp_atom", [])) > 10 and len(coot.monomer_restraints_py("NAG").get("_chem_comp_bond", [])) > 10)
w = max(len(r[0]) for r in res)
for n, ok, v in res: print(("PASS " if ok else "FAIL ") + n.ljust(w) + "  " + v)
print("SUMMARY", sum(1 for r in res if r[1]), "/", len(res), flush=True)
