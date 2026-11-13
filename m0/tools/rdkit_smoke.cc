// Smoke test of the RDKit C++ build used for Coot's enhanced ligand tools: SMILES -> molecule -> 2D depiction -> MDL molblock -> SMILES.
#include <GraphMol/GraphMol.h>
#include <GraphMol/SmilesParse/SmilesParse.h>
#include <GraphMol/SmilesParse/SmilesWrite.h>
#include <GraphMol/Depictor/RDDepictor.h>
#include <GraphMol/FileParsers/FileParsers.h>
#include <GraphMol/Descriptors/MolDescriptors.h>
#include <GraphMol/MolOps.h>
#include <GraphMol/Conformer.h>
#include <GraphMol/FileParsers/MolFileStereochem.h>
#include <RDGeneral/versions.h>
#include <iostream>
int main(int argc, char **argv) {
   std::string smi = argc > 1 ? argv[1] : "CC1([C@@H](N2[C@H](S1)[C@@H](C2=O)NC(=O)CC3=CC=CC=C3)C(=O)O)C";   // penicillin G
   RDKit::RWMol *m = RDKit::SmilesToMol(smi);
   if (!m) { std::cout << "FAIL SmilesToMol\n"; return 1; }
   RDDepict::compute2DCoords(*m, NULL, true);
   // the calls lbg_info_t::rdkit_mol_post_read_handling() makes after reading a SMILES string:
   RDKit::MolOps::Kekulize(*m);
   const RDKit::Conformer conformer = m->getConformer(0);
   RDKit::WedgeMolBonds(*m, &conformer);
   int n_wedged = 0;
   for (unsigned int ib = 0; ib < m->getNumBonds(); ib++) {
      RDKit::Bond::BondDir d = m->getBondWithIdx(ib)->getBondDir();
      if (d == RDKit::Bond::BEGINWEDGE || d == RDKit::Bond::BEGINDASH) n_wedged++;
   }
   std::cout << "wedge/dash bonds after WedgeMolBonds: " << n_wedged << " (2D conformer is3D=" << conformer.is3D() << ")\n";
   if (n_wedged < 1 || conformer.is3D()) { std::cout << "FAIL wedging\n"; return 1; }
   std::string mb = RDKit::MolToMolBlock(*m);
   RDKit::RWMol *m2 = RDKit::MolBlockToMol(mb);
   if (!m2) { std::cout << "FAIL MolBlockToMol\n"; return 1; }
   std::cout << "RDKit " << RDKit::rdkitVersion << "\natoms=" << m->getNumAtoms() << " bonds=" << m->getNumBonds()
             << " conformers=" << m->getNumConformers() << " molblock_lines=" << std::count(mb.begin(), mb.end(), '\n')
             << "\nround-trip SMILES: " << RDKit::MolToSmiles(*m2) << "\nformula: " << RDKit::Descriptors::calcMolFormula(*m)
             << "\nPASS\n";
   delete m; delete m2; return 0;
}
