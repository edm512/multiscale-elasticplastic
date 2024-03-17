Description of files and folders
--------------------------------
FILES
--------------------------------
train.py - main script to build and train models on training data. This is intended to be run in multiple instances in parallel.
Dependencies:
	getData.py - function to retrieve and pre-process training data
	scaling.py - function to scale the training data
	buildModel.py - function to build feedforward neural network using keras
	writeInput.py - function to write input script for hydrocode using built model

runHydro.py - main script to run hydrocodes using neural network models. This is intended to be run in multiple instances in parallel.

--------------------------------
FOLDERS
--------------------------------
data - folder for training data
models - folder for JSON models
lossData - folder for error data from training
inputs - folder for hydrocode input scripts

--------------------------------
PLEASE NOTE
--------------------------------
1) train.py calls convert_model.py, a tool from the frugally-deep library to convert Keras models to JSON for use in C++ applications. 
Please download this package from https://github.com/Dobiasd/frugally-deep.git

2) to run hydrocode with neural network model, please download and set up the 1D-hydrocode package: https://github.com/AndyHYork/MDElasticity.git
The executable codename should be in the same directory as runHydro.py

3) extract data.zip to a folder called 'data' before running



