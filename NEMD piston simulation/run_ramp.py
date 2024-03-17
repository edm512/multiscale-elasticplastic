# python wrapper for running piston simulation. 

from lammps import lammps
lmp = lammps()
lmp.command("clear")

lmp.file("in.init_long") # Initialise simulation
lmp.file("in.equil") # Equilibration
lmp.file("in.regions_groups") # Define regions and groups
lmp.file("in.set_comp_var") # Computes and variables for whole system
lmp.file("in.group_info") # Computes and variables for groups
lmp.file("in.output") # Define output 
lmp.file("in.run_sim_long") # Add voids and run simulation

lmp.close()
