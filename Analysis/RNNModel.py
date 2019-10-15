import PrepareData as prepData
import Query
import numpy as np
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
# import lstm
import time
# clear console after printing keras logs
import os
os.system('clear')

hdfc_df = Query.getDataSet()

hdfc_data = np.array(hdfc_df)

# choose a number of time steps, this says the number of days to be taken for trend formation
# n_steps + 1 will be used as day for which opening is to be predicted
n_steps = 60

features, labels = prepData.prepareData(hdfc_data, n_steps)
# print(features.shape, labels.shape)
# (1144, 6, 1) (1144, 1, 1)

train_features, train_labels = features[:900], labels[:900]
test_features, test_labels = features[900:1000], labels[900:1000]
print(train_features.shape, train_labels.shape)

# n_features = features.shape[2]

# configure the model

model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(n_steps,1)))
model.add(LSTM(units=50))
model.add(Dense(6))
model.compile(loss='mean_squared_error', optimizer='adam')
# fit model
model.fit(train_features, train_labels, epochs=10, batch_size=1, verbose=1)

yhat = model.predict(test_features, verbose=0)

for i in range(10):
    print(yhat[i], labels[i])
