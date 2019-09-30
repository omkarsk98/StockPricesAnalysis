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
n_steps = 5

features, labels = prepData.prepareData(hdfc_data, n_steps)




# """ Failed code """
# # (1114, 30, 6) shape for features
# # print(features.shape)
# n_features = features.shape[2]

# model = keras.models.Sequential()
# model.add(keras.layers.convolutional.Conv1D(filters=64, kernel_size=2, activation='relu',
#                                             input_shape=(n_steps, n_features,)))
# model.add(keras.layers.convolutional.MaxPooling1D(pool_size=2))
# model.add(keras.layers.Flatten())
# model.add(keras.layers.Dense(50, activation='relu'))
# model.add(keras.layers.Dense(1))
# model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

# """ # fit model """
# model.fit(features[0:1100], labels[0:1100], epochs=5000, verbose=1)

# # model = keras.models.load_model("./Analysis/analysis.h5")
# check_features = features[1100:1101]
# # check_labels = features[1001]
# print(check_features)

# output = model.predict(check_features, verbose=1)
# # model.save("./Analysis/analysis.h5")
# print("Output:", output)
# print("Found label as:", labels[1001])
