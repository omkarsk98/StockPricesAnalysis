import mysql.connector
import pandas as pd
import json
# import query string
QUERIES = json.loads(open("Queries/queries.json").read())
# configure mysql connection
mydb = mysql.connector.connect(
    host="localhost",
    user="StockAdmin",
    passwd="random",
    database="Stocks"
)

mycursor = mydb.cursor()
q = QUERIES["final"] + ";"
# execute query and fetch result
mycursor.execute(q)
myresult = mycursor.fetchall()
# convert to panda dataframe
hdfc_data = pd.DataFrame(myresult, columns=[
    'date', 'open', 'high', 'low', 'close', 'volume', '5 days moving average', 'next day open'])


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
    return hdfc_data
