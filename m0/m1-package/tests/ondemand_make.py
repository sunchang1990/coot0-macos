
import os, coot
mon = os.environ["CLIBD_MON"]
coot.read_cif_dictionary(os.path.join(mon, "n", "NAG.cif"))
imol = coot.get_monomer("NAG")
print("DBG made NAG molecule:", imol, coot.is_valid_model_molecule(imol))
print("DBG write:", coot.write_pdb_file(imol, os.path.join(os.environ["COOT_PREFIX"], "test-data", "nag_only.pdb")))
