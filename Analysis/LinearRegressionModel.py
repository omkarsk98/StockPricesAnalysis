import PrepareData as prepData
import Query
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

hdfc_df = Query.getDataSet()
hdfc_data = np.array(hdfc_df)

result = prepData.getLRData(hdfc_data, True, deci=3)
features, labels, dates = result["features"], result["labels"], result["dates"]

train_features, test_features = features[:900], features[900:]
train_labels, test_labels = labels[:900], labels[900:]

model = LinearRegression()
model.fit(train_features, train_labels)
yhat = model.predict(test_features)

acc = model.score(test_features, test_labels)
print("Accuracy:"+str(acc*100))
if result["labelsMean"]==None:
    result["labelsMean"] = 1

plt.plot(dates[900:], yhat, color='blue', linewidth=2)
plt.plot(dates[900:], test_labels, color="green", linewidth=2)
plt.plot(dates[900:], features[900:,5], color="red", linewidth=2)
plt.legend(["predicted","actual", "5DMA"])
plt.title("Plot of time vs opening price")
plt.show()