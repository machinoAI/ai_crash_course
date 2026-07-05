import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

data = pd.read_csv(
  "abalone_data.csv",
  names=[
    "Length", "Diameter", "Height", "Whole weight",
    "Shucked weight", "Viscera weight", "Shell weight", "Age"
  ]
)
data_features = data.copy()
data_labels = data_features.pop('Age')

# convert to np array
data_features = np.array(data_features)

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
  data_features,
  data_labels,
  epochs = 10,
  verbose =0

)

print(history.history)
model.summary()