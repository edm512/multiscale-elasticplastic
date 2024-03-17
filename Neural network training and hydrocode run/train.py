import numpy as np
import tensorflow as tf
import random as python_random
import pandas as pd

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

print(tf.__version__)

from getData import getData
from scaling import scaling
from buildModel import buildModel
from writeInput import writeInput
import os
import subprocess


file_location = './data/'

data = getData(file_location)

# Split into train and test

train_dataset = data.sample(frac=0.9)
test_dataset = data.drop(train_dataset.index)

scalings, train_dataset, test_dataset = scaling(train_dataset, test_dataset)


train_features = train_dataset[['norm_sr', 'norm_OldS3', 'norm_OldP2', 'norm_old_T', 'norm_voidSize']]
test_features = test_dataset[['norm_sr', 'norm_OldS3', 'norm_OldP2', 'norm_old_T', 'norm_voidSize']]

train_labels = train_dataset[['norm_dS3dt', 'norm_dP2dt', 'norm_dTdt']]
test_labels = test_dataset[['norm_dS3dt', 'norm_dP2dt', 'norm_dTdt']]

learning_rate = 0.0001 

i = os.getenv('SLURM_ARRAY_TASK_ID')

model = buildModel(learning_rate)

# Train the model
history = model.fit(
    train_features, train_labels,
    validation_split=0.1,
    verbose=2, epochs=500)

loss = np.array([history.history['loss'], history.history['val_loss']]).T

modelname = 'model_testTrainingTime160622_'+str(i)
model.save('./models/'+modelname+'.h5', include_optimizer=False)
np.savetxt('./models/'+modelname+'.scaling', scalings)
np.savetxt('./lossData/'+modelname+'_loss.txt', loss)
subprocess.run(['python3', 'convert_model.py', './models/'+modelname+'.h5', './models/'+modelname+'.json'])
writeInput(modelname)




