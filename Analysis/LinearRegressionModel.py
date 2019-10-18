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

# seperate features and labels for training and validation
train_features, test_features = features[:900], features[900:]
train_labels, test_labels = labels[:900], labels[900:]

# initialise the model and fit it for training data
model = LinearRegression()
model.fit(train_features, train_labels)

# predict values for test data
yhat = model.predict(test_features)

# get accuracy of the model
acc = model.score(test_features, test_labels)
print("Accuracy:"+str(acc*100))
print("RMSE:"+str(np.sqrt(mean_squared_error(test_labels, yhat))))

# plot actual, predicted and 5SMA values for test duration
plt.plot(dates[900:], result["labelsMean"]*yhat, color='blue', linewidth=2)
plt.plot(dates[900:], result["labelsMean"] *
         test_labels, color="green", linewidth=2)
plt.plot(dates[900:], ((result["featuresMean"].astype(float))
                       * features[900:])[:, 5], color="red", linewidth=2)
plt.legend(["predicted", "actual", "5DMA"])
plt.title("Plot of time vs opening price")
plt.show()
