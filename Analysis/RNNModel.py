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
# os.system('clear')

# choose a number of time steps, this says the number of days to be taken for trend formation
# n_steps + 1 will be used as day for which opening is to be predicted
n_steps = 60
split_pct = 60
hdfc_df = Query.getDataSet(n_steps)
hdfc_data = np.array(hdfc_df)

features, labels = prepData.prepareData(hdfc_data, n_steps)
# (1144, 6, 1) (1144, 1, 1)
train_features, train_labels = features[:int(
    features.shape[0]*split_pct)], labels[:int(features.shape[0]*split_pct)]
test_features, test_labels = features[int(features.shape[0]*split_pct):int(
    features.shape[0])], labels[int(features.shape[0]*split_pct):int(features.shape[0])]
print("Train features shape", train_features.shape,
      "Train labels shape", train_labels.shape)
# n_features = features.shape[2]
# configure the model

regressor = Sequential()
regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (train_features.shape[1], 1)))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))
regressor.add(Dense(units = 1))

# fit model
os.system("clear")
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
regressor.fit(train_features, train_labels, epochs = 15, batch_size = 32)
print(train_features.shape, train_labels.shape)

predicted_stock_price = regressor.predict(test_features)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

for i in range(10):
    print(yhat[i], labels[i])
