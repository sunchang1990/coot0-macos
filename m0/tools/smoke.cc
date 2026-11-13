#include <iostream>
#include "coot-utils/atom-selection-container.hh"
#include "coot-utils/coot-coord-utils.hh"
#include <clipper/core/spacegroup.h>
int main(int argc, char **argv) {
  atom_selection_container_t asc = get_atom_selection(argv[1], false, true, false);
  if (!asc.mol) { std::cout << "FAIL: could not read " << argv[1] << "\n"; return 1; }
  int n_atoms = asc.n_selected_atoms;
  std::pair<bool, clipper::Coord_orth> cp = coot::centre_of_molecule(asc.mol); clipper::Coord_orth c = cp.second;
  std::cout << "read OK: atoms=" << n_atoms << " centre=(" << c.x() << "," << c.y() << "," << c.z() << ")\n";
  clipper::Spacegroup sg(clipper::Spgr_descr("P 21 21 21"));
  std::cout << "clipper spacegroup: " << sg.symbol_hm() << " nsym=" << sg.num_symops() << "\n";
  return 0;
}
