import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


def buildModel(learning_rate):
	model = keras.Sequential([
	      layers.Dense(62, activation='relu', input_shape=(5,)),
	      layers.Dense(100, activation='relu'),
	      layers.Dense(100, activation='relu'),
	      layers.Dense(62, activation='relu'),
	      layers.Dense(3)
	  ])

	# Set the learning rate
	model.compile(loss='mean_absolute_error',
		        optimizer=tf.keras.optimizers.Adam(learning_rate))

	return model
