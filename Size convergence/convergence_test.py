#!/usr/bin/env python -i

from lammps import lammps


size = "30.0" # Size of simulation in lattice units
seeds = ["1679"] # Random seed for velocity distribution
time_step = "0.01" # Time step

for seed in seeds:
	lmp = lammps()
	lmp.command("clear")

	# initialise and set lattice
	lmp.file("in.p1")

	# define simulation box size
	lmp.command("region sim_box block 0.0 "+size+" 0.0 "+size+" 0.0 1.0 units lattice")

	# create box, create atoms, set potential
	lmp.file("in.p2")

	# set velocity seed
	lmp.command("velocity all create 600 "+seed+" rot yes dist gaussian")

	# equilibrate, set computes and variables
	lmp.file("in.p3")

	# set run name defined by size, seed, date and time step
	lmp.command("variable run_name string size"+size+"_seed"+seed+"_", "ts"+time_step+"_"+date)

	# read in strain and rate from file, fix deform, fix data output
	lmp.file("in.p4")

	lmp.command("timestep "+time_step)

	lmp.command("run 17000") # it ends before reaching the end of the data read in. that is fine. 

