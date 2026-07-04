import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

abalone_train = pd.read_csv(
  "abalone_data.csv",
  names=[
    "Length", "Diameter", "Height", "Whole weight",
    "Shucked weight", "Viscera weight", "Shell weight", "Age"
  ]
)

abalone_features = abalone_train.copy()
abalone_labels = abalone_features.pop('Age')

# convert to np array
abalone_features = np.array(abalone_features)

# implement model (using tf.keras) to predict age

model = tf.keras.Sequential([
  layers.Dense(64, activation='relu'),
  layers.Dense(1)

])

# compile the model here
model.compile(
  optimizer =tf.keras.optimizers.Adam(),
  loss = tf.keras.losses.MeanSquaredError()
)

# fit the model here

history = model.fit(
  abalone_features,
  abalone_labels,
  epochs = 10,
  verbose =0

)

print(history.history)
model.summary()