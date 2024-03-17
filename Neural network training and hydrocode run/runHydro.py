import os
import subprocess

i = os.getenv('SLURM_ARRAY_TASK_ID')

NN_location = './inputs/'

modelname = "model_temp040322_"+str(i)+"void6.0_newParams"
subprocess.run(['./codeName', '-in', NN_location+'in.'+modelname])
subprocess.run(['mkdir', 'hydroData/'+modelname])
subprocess.run(["mv "+modelname+".*dump* hydroData/"+modelname], shell=True)

