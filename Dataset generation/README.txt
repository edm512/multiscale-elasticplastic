Description of files 
--------------------------------
FILES
--------------------------------
runDataSetGen.py - main script to sequentially run a large number of uniform uniaxial compression LAMMPS simulations. 
Dependencies:
	pathway_gen.py - function to generate run name and number of steps in simulation. Defines compression pathway.
	compression.py - function used in pathway_gen.py to generate compression pathway
	expansion.py - function used in pathway_gen.py to generate expansion pathway
	runLammps.py - script to run LAMMPS simulation
in.part1a - first part of LAMMPS script, used in runLammps.py
in.part1b - second part of LAMMPS script, used in runLammps.py
in.part2 - third part of LAMMPS script, used in runLammps.py
 
