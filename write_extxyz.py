from ase.io import read,write
from ase import Atoms
import numpy as np
import os
from ase.calculators.singlepoint import SinglePointCalculator


#pressures = [50, 100, 150, 200] folder name
pressures = [125]
all_filtered_atoms = []
for pressure in pressures:
    print(f"Processing pressure {pressure}")
    os.chdir(str(pressure))

    base_atom = read("POSCAR", format="vasp")
    syms = base_atom.get_chemical_symbols()

    # Reading and extracting positions and cells from OUTCAR
    f = open("OUTCAR", "r")
    positions, cells, forces, energies,stresses = [], [], [], [], []
    position, cell, force, energy, stress = [], [], [], [], []
    sig1, sig2, sig3 = False, False, False

    for line in f:
        if sig3 and "--------------------" not in line:
            position.append([float(x) for x in line.split()[:3]])
            force.append([float(x) for x in line.split()[3:]])
            if len(position) == len(syms):
                sig3 = False
        if "POSITION                                       TOTAL-FORCE (eV/Angst)" in line:
            sig3 = True
            position = []
            force = []
        if sig2:
            cell.append([float(x) for x in line.split()[:3]])
            if len(cell) == 3:
                sig2 = False
        if "direct lattice vectors                 reciprocal lattice vectors" in line:
            sig2 = True
            cell = []
        if "aborting loop because EDIFF is reached" in line:
            sig1 = True
        if "free  energy   TOTEN  =" in line:
            print([float(line.split()[4])])
            energies.append(float(line.split()[4]))
            sig1 = False
            positions.append(position)
            cells.append(cell)
            forces.append(force)
        if "in kB " in line:
            stress = [float(x) for x in line.split()[2:8]]
            stress = -1*np.array(stress)/1602
            stresses.append(stress)

        #if "FREE ENERGIE OF THE ION-ELECTRON SYSTEM" in line:
    # Creating atom objects and filtering
    filtered_atoms = []
    atoms = []
    for i in range(len(cells)):
        atom = Atoms(symbols=syms, positions=positions[i], cell=cells[i], pbc=True)
        atom.calc = SinglePointCalculator(energy=energies[i], forces=forces[i], stress=stresses[i], atoms=atom)
        atoms.append(atom)
   # Filter atoms based on similarity
   #     if i % 5 == 0: 
        filtered_atoms.append(atom)
all_filtered_atoms.extend(filtered_atoms)
    os.chdir("..")

out_filename = "nequip-data.extxyz"
try:
    for _, curr_atoms in enumerate(all_filtered_atoms):
#        print(f"Atom {i}: positions={curr_atoms.get_positions()}, energy={curr_atoms.get_potential_energy()}, forces={curr_atoms.get_forces()}")
        write(out_filename, curr_atoms, append=True, format='extxyz')
    print(f"Total filtered atoms for training: {len(all_filtered_atoms)}")
except Exception as e:
    print(f"Error while writing to file: {e}")
