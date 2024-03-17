This folder contains the code required to reproduce the work in the paper "Including material elasto-plastic properties in hydrodynamic simulations via Non Equilibrium Molecular Dynamics trained model", Liam Douglas-Mann, Luca Antonelli, Andrew Higginbotham

Each folder contains a README.txt file which gives detail on its contents. In the order they appear in the paper, the folders are:

1) Size convergence
Section 2.2 of paper. Contains LAAMPS scripts and Python wrapper for convergence testing of simulations of local ramp compression.

2) NEMD piston simulation
Section 2.3 of paper. Contains LAMMPS scripts and Python wrapper for non-equilibrium molecular dynamics simulations of ramp compression using the piston method.

3) Uniform uniaxial compression
Section 2.4 of paper. LAMMPS script for uniform uniaxial compression simulation.

4) Dataset generation
Section 3.2.2 of paper. LAMMPS scripts and Python wrapper for training set generation. 

5) Neural network training and hydrocode run
3.2.3 and 3.2.4 of paper. Python files for building and training neural networks, creating input files for hydrocode, and running hydrocode. Instructions for downloading other required packages in folder's README. 

