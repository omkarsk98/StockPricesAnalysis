import PrepareData as prepData
import Query
import numpy as np
import keras
# clear console after printing keras logs
import os
os.system('clear')

hdfc_df = Query.getDataSet()

hdfc_data = np.array(hdfc_df)
# choose a number of time steps, this says the number of days to be taken for trend formation
# n_steps + 1 will be used as day for which opening is to be predicted
n_steps = 10

features, labels = prepData.prepareData(hdfc_data, n_steps)
print(features[0], labels[0])



""" Failed code """
# (1134, 10, 6) shape for features
# print(labels[0:1000].shape)
# n_features = features.shape[2]

# model = keras.models.Sequential()
# model.add(keras.layers.convolutional.Conv1D(filters=64, kernel_size=2, activation='relu',
#                                             input_shape=(n_steps, n_features,)))
# model.add(keras.layers.convolutional.MaxPooling1D(pool_size=2))
# model.add(keras.layers.Flatten())
# model.add(keras.layers.Dense(50, activation='relu'))
# model.add(keras.layers.Dense(n_features))
# model.compile(optimizer='adam', loss='mse')

# # fit model
# model.fit(features[0:1000], labels[0:1000], epochs=3000, verbose=1)

# check_features = features[1001]
# # check_labels = features[1001]

# output = model.predict(check_features, verbose=1)
# print(output)
