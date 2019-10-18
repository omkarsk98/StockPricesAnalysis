import numpy as np


def prepareData(data, steps):
    """ 
      data: input data. It contains the following columns:
        date, open, high, low, close, volume, 5SMA, next day open
      steps: number of s=days to be considered for trend formation
      returns data having two values as features and labels:
        features: It has a shape of(x,steps,6) 
          for x as number of records, steps as steps mentioned above and 
          6 as the number of features that has open, high, low, close, volume and 5SMA
        labels: It has a shape of (x,1)
          for x as number of records having the opening value of steps+1th day for each
    """
    X, y = list(), list()
    for i in range(len(data)):
        # find the end of this pattern
        end_ix = i + steps
        # check if we are beyond the dataset
        if end_ix > len(data)-1:
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = data[i:end_ix, 1:7], data[end_ix, :][1]
        X.append(seq_x)
        y.append(seq_y)
        features = np.array(X)
        labels = np.array(y)
        labels = labels.reshape((len(labels)), 1)
    return features[:len(features)-1], labels[:len(labels)-1]


def getLRData(data, normalise=False, deci=4):
    ''' 
      Separates and converts data to required format. 
      Params:
        data: (x,8) matrix that has columns as date, open, high, low, close, volume, 5SMA, next day open in the same sequence.
        normalise: boolean variable(default False). If true, columns are divided by means of the respective columns to reduce the data between 0 and 2.
        deci: integer value(default 4). To keep the number of places after decimal
      Return:
        Returns a dictionary containing the folling keys:
          dates: dates of the market
          features: features used for training. Contains Open, High, Low, Close, Volume, 5SMA (columns 1 to 7 of the matrix)
          labels: next day open for the respective dates. (column 8 of the matrix)
          labelsMean: single value that is the mean of the labels
          featuresMean: array of 6 values that are means of the respective columns.
    '''
    features, labels = np.array(
        data[:len(data)-2, 1:7]), np.array(data[:len(data)-2, 7])
    labels = labels.reshape(len(labels), 1)
    dates = np.array(data[:len(data)-2, 0])
    # dates = np.datetime64(dates)
    dates = dates.reshape(len(dates), 1)
    labelsMean, featuresMean = 1, np.array([1, 1, 1, 1, 1, 1])
    if normalise == True:
        featuresMean = np.mean(features, axis=0, keepdims=True)
        labelsMean = np.mean(labels, keepdims=True)
        features, labels = (features/featuresMean), (labels/labelsMean)
        features, labels = np.round(features.astype(np.double), decimals=deci), np.round(
            labels.astype(np.double), decimals=deci)

    result = {"dates": dates, "features": features, "labels": labels,
              "labelsMean": labelsMean, "featuresMean": featuresMean}
    return result
