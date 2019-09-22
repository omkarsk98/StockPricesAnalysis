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
    return features, labels
