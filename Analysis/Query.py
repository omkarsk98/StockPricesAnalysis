import pandas as pd

def getDataSet():
    """
    Returns a python data frame having the following columns
        date:date of that instance
        open:opening price of the stock for that day
        high:highest price of the stock for that day
        low: lowest price of the stock for that day
        close: closing price of the stock for that day
        volume: number of stocks traded on that day
        5 days moving average: moving average of the closing price of last 5 days for that day
        next day open: opening price for the next day   
    """
    hdfc_data = pd.read_csv("../DataSource/hdfc.csv")
    hdfc_data["date"] = pd.to_datetime(hdfc_data["date"])
    hdfc_data['next day open'] = hdfc_data['next day open'].astype(float)
    return hdfc_data
