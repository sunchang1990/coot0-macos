
# RDKit ("enhanced ligand tools") checks that need no window: SMILES -> 3D molecule in Coot -> PDB / MDL molfile
import os, coot
res = []
def check(name, fn):
    try:
        v = fn(); res.append((name, bool(v), repr(v)[:90]))
    except Exception as e: res.append((name, False, "EXC " + repr(e)[:110]))
work = os.path.join(os.environ["COOT_PREFIX"], "work"); os.makedirs(work, exist_ok=True)

def pdb_atoms(path):
    out = []
    for l in open(path):
        if l.startswith(("ATOM", "HETATM")):
            out.append((l[12:16].strip(), l[76:78].strip() or l[12:16].strip()[0], float(l[30:38]), float(l[38:46]), float(l[46:54]), l[21], int(l[22:26])))
    return out
def dist(a, b): return ((a[2]-b[2])**2 + (a[3]-b[3])**2 + (a[4]-b[4])**2) ** 0.5

# aspirin, C9H8O4: 13 heavy atoms + 8 H = 21 atoms
imol = coot.import_rdkit_mol_from_smiles("CC(=O)Oc1ccccc1C(=O)O", "ASA")
check("import_rdkit_mol_from_smiles gives a model molecule (aspirin)", lambda: imol >= 0 and coot.is_valid_model_molecule(imol))
pdb = os.path.join(work, "rdkit_aspirin.pdb")
check("molecule can be written as PDB", lambda: coot.write_pdb_file(imol, pdb) in (0, None) and os.path.exists(pdb))
atoms = pdb_atoms(pdb)
from collections import Counter
check("atom content is C9 H8 O4", lambda: Counter(a[1].upper() for a in atoms) == Counter({"C": 9, "H": 8, "O": 4}))
def nn_ok():
    heavy = [a for a in atoms if a[1].upper() != "H"]
    bad = []
    for a in atoms:
        d = sorted(dist(a, b) for b in atoms if b is not a)
        if not (0.9 < d[0] < 1.65): bad.append((a[0], round(d[0], 2)))
    return not bad, bad[:3]
check("every atom has a bonded neighbour at 0.9-1.65 A, none closer (3D embedding + UFF worked)", lambda: nn_ok()[0])
def ring_ok():   # the six aromatic carbons: C-C 1.34-1.46 A
    c = [a for a in atoms if a[1].upper() == "C"]
    n = 0
    for i, a in enumerate(c):
        for b in c[i+1:]:
            if 1.30 < dist(a, b) < 1.46: n += 1
    return n >= 6
check("six or more aromatic-range C-C bonds (ring perceived)", ring_ok)
check("bad SMILES is rejected without crashing (returns -1)", lambda: coot.import_rdkit_mol_from_smiles("C1CC(", "BAD") == -1)
check("atom names are unique and none is the placeholder ZZZZ", lambda: len(set(a[0] for a in atoms)) == len(atoms) and all(a[0] != "ZZZZ" for a in atoms))
# MDL molfile export needs the bonds, i.e. a residue that has a restraints dictionary (the SMILES import makes none): use NAG from the monomer library
nag = coot.get_monomer("NAG")
nag_pdb = os.path.join(work, "rdkit_nag.pdb"); coot.write_pdb_file(nag, nag_pdb)
first = [l for l in open(nag_pdb) if l.startswith(("ATOM", "HETATM"))][0]
ch, rn = first[21], int(first[22:26])
sdf = os.path.join(work, "rdkit_nag.sdf")
check("residue_to_sdf_file writes an MDL molfile (NAG from the monomer library)", lambda: coot.residue_to_sdf_file(nag, ch, rn, "", sdf) and os.path.exists(sdf))
def sdf_counts():
    lines = open(sdf).read().splitlines()
    cl = [l for l in lines if "V2000" in l][0]
    return int(cl[0:3]), int(cl[3:6])
check("molfile counts line: NAG C8H15NO6 = 30 atoms, 30 bonds", lambda: sdf_counts() == (30, 30))
# penicillin G, with stereo: C16H18N2O4S, 41 atoms
imol2 = coot.import_rdkit_mol_from_smiles("CC1([C@@H](N2[C@H](S1)[C@@H](C2=O)NC(=O)CC3=CC=CC=C3)C(=O)O)C", "PNG")
pdb2 = os.path.join(work, "rdkit_pengG.pdb"); coot.write_pdb_file(imol2, pdb2)
check("penicillin G (stereo SMILES): C16 H18 N2 O4 S", lambda: Counter(a[1].upper() for a in pdb_atoms(pdb2)) == Counter({"C": 16, "H": 18, "N": 2, "O": 4, "S": 1}))
w = max(len(r[0]) for r in res)
for n, ok, v in res: print(("PASS " if ok else "FAIL ") + n.ljust(w) + "  " + v)
print("SUMMARY", sum(1 for r in res if r[1]), "/", len(res), flush=True)
coot.coot_real_exit(0)
