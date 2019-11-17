import PrepareData as prepData
import Query
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# get the raw dataset
hdfc_df = Query.getDataSet()
hdfc_data = np.array(hdfc_df)

# get processed data
result = prepData.getLRData(hdfc_data, True, deci=3)
features, labels, dates = result["features"], result["labels"], result["dates"]

data_split = 380
# seperate features and labels for training and validation
train_features, test_features = features[:data_split], features[data_split:]
train_labels, test_labels = labels[:data_split], labels[data_split:]

# get 5 DMA model
DMA5 = LinearRegression()
DMA5.fit(train_features[:, 0:6], train_labels)
DMA5_pred = DMA5.predict(test_features[:, 0:6])
acc5 = DMA5.score(test_features[:, 0:6], test_labels)

# get 10 DMA model
DMA10 = LinearRegression()
DMA10.fit(train_features[:, [0, 1, 2, 3, 4, 6]], train_labels)
DMA10_pred = DMA10.predict(test_features[:, [0, 1, 2, 3, 4, 6]])
acc10 = DMA10.score(test_features[:, [0, 1, 2, 3, 4, 6]], test_labels)

# get 20 DMA model
DMA20 = LinearRegression()
DMA20.fit(train_features[:, [0, 1, 2, 3, 4, 7]], train_labels)
DMA20_pred = DMA20.predict(test_features[:, [0, 1, 2, 3, 4, 7]])
acc20 = DMA20.score(test_features[:, [0, 1, 2, 3, 4, 7]], test_labels)

# get 50 DMA model
DMA50 = LinearRegression()
DMA50.fit(train_features[:, [0, 1, 2, 3, 4, 8]], train_labels)
DMA50_pred = DMA50.predict(test_features[:, [0, 1, 2, 3, 4, 8]])
acc50 = DMA50.score(test_features[:, [0, 1, 2, 3, 4, 8]], test_labels)

# get accuracy of the model
print("\nAccuracy for 5 DMA:"+str(acc5*100))
print("RMSE with 5 DMA:"+str(np.sqrt(mean_squared_error(test_labels, DMA5_pred))))
print("\nAccuracy for 10 DMA:"+str(acc10*100))
print("RMSE with 10 DMA:"+str(np.sqrt(mean_squared_error(test_labels, DMA10_pred))))
print("\nAccuracy for 20 DMA:"+str(acc20*100))
print("RMSE with 20 DMA:"+str(np.sqrt(mean_squared_error(test_labels, DMA20_pred))))
print("\nAccuracy for 50 DMA:"+str(acc50*100))
print("RMSE with 50 DMA:"+str(np.sqrt(mean_squared_error(test_labels, DMA50_pred))))

# plot actual, predicted and 5SMA values for test duration
plt.plot(dates[data_split:], result["labelsMean"]*DMA5_pred, linewidth=2, color="black")
plt.plot(dates[data_split:], result["labelsMean"]*DMA10_pred, linewidth=2, color="orange")
plt.plot(dates[data_split:], result["labelsMean"]*DMA20_pred, linewidth=2, color="blue")
plt.plot(dates[data_split:], result["labelsMean"]*DMA50_pred, linewidth=2, color="purple")
plt.plot(dates[data_split:], result["labelsMean"] *
         test_labels, color="green", linewidth=2)
plt.plot(dates[data_split:], ((result["featuresMean"].astype(float))
                       * features[data_split:])[:, 5], color="red", linewidth=2)
plt.legend(["Using 5 DMA","Using 10 DMA","Using 20 DMA","Using 50 DMA", "actual", "5DMA"])
plt.title("Time vs Prices plot")
plt.show()
