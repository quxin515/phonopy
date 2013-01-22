from phonopy import Phonopy
from phonopy.interface.vasp import read_vasp
from phonopy.hphonopy.file_IO import parse_FORCE_SETS, parse_BORN
import numpy as np

cell = read_vasp("POSCAR")

# Initialize phonon. Supercell matrix has to have the shape of (3, 3)
phonon = Phonopy(cell, np.diag([3, 3, 2]))

symmetry = phonon.get_symmetry()
print "Space group:", symmetry.get_international_table()

# Read forces and displacements
force_sets = parse_FORCE_SETS(cell.get_number_of_atoms() * 18)

# Sets of forces have to be set before phonon.set_post_process or
# at phonon.set_post_process(..., sets_of_forces=sets_of_forces, ...).
phonon.set_force_sets(force_sets)
phonon.set_post_process()

# Character table
phonon.set_character_table([1./3, 1./3, 0], 1e-4)
phonon.show_character_table()
