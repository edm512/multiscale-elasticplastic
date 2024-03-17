#!/usr/bin/env python -i

from pathway_gen import pathway_gen

import subprocess

from random import randrange





# Number of simulations
N = 100

# Ranges for variables
VRange = [0.7, 0.8]
compressionTypes = ['linear', 'squareroot', 'squareroot', 'squareroot']
holdRange = [30, 50]
expansionTypes = ['linear', 'squareroot', 'quadratic', 'cubic', 'sigmoid']
ExpFraction = 0.05
compTimeRange = [30, 100]
expTimeRange = [35, 60]
voidRange = [5.0, 150.0]  

# Fixed values
initialStateTime = 15
endStateTime = 5
timestep = 0.01

# Counter
i = 0

while i < N:

	runName, totalSteps = pathway_gen(VRange, compressionTypes, holdRange, expansionTypes, ExpFraction, compTimeRange, expTimeRange, initialStateTime, endStateTime, timestep)
	print("volratio.txt and volrate.txt ready")
	print("total steps: ", totalSteps)
	subprocess.run(["wc", "-l", "volratio.txt"])
	subprocess.run(["wc", "-l", "volrate.txt"])

	voidSize = randrange(voidRange[0], voidRange[1])/10.0

	subprocess.run(["mpirun", "python", "runLammps.py", runName+"_void"+str(voidSize), str(totalSteps-2), str(voidSize)])

	print("lammps run executed")
	
	i += 1



