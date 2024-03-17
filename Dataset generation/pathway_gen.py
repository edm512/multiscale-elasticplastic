#!/usr/bin/env python -i

import numpy as np
from random import randrange
from random import choice
from datetime import date
from compression import compression
from expansion import expansion
from scipy.ndimage import uniform_filter1d


def pathway_gen(VRange, compressionTypes, holdRange, expansionTypes, ExpFraction, compTimeRange, expTimeRange, initialStateTime, endStateTime, timestep):
	print(VRange[0], VRange[1])
	print(int(VRange[0]*10000), int(VRange[1]*10000))


	V = randrange(int(VRange[0]*10000), int(VRange[1]*10000))/10000
	print('V = ', V)
	compPathway = choice(compressionTypes)
	hold = randrange(holdRange[0], holdRange[1])
	expPathway = choice(expansionTypes)
	
	compTime = randrange(compTimeRange[0], compTimeRange[1])
	expTime = randrange(expTimeRange[0], expTimeRange[1])
	ExpV = V * (1+ExpFraction) 
	totalSteps = int((initialStateTime+compTime+hold+expTime+endStateTime)/timestep)
	compVol = compression(V, compPathway, compTime, timestep)
	expVol = expansion(V, ExpV, expPathway, expTime, timestep)
	print(initialStateTime/timestep, compTime/timestep, hold/timestep, expTime/timestep, endStateTime/timestep)

	initialVol = np.full(int(initialStateTime/timestep), compVol[0])
	holdVol = np.full(int(hold/timestep), compVol[-1])
	endVol = np.full(int(endStateTime/timestep), expVol[-1])
	print(len(initialVol), len(compVol), len(holdVol), len(expVol), len(endVol))

	fullPathway = np.concatenate((initialVol, compVol, holdVol, expVol, endVol))
	smoothPathway = uniform_filter1d(fullPathway, size=int(len(fullPathway)/10))

	np.savetxt('volratio.txt', smoothPathway)
	np.savetxt('volrate.txt', np.gradient(smoothPathway))
	runName = str(date.today())+'_'+compPathway+str(compTime)+'_'+expPathway+str(expTime)+'_'+str(V)
	return runName, totalSteps
