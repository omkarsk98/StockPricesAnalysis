import mysql.connector
import plotly.graph_objects as go
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="StockAdmin",
    passwd="random",
    database="Stocks"
)

mycursor = mydb.cursor()

mycursor.execute(
    "select date, open, high, low, close, volume, (select open from hdfc h1 where h1.id>h.id order by id asc limit 1) as 'next day open' from hdfc h;")

myresult = mycursor.fetchall()

df = pd.DataFrame(myresult, columns=[
                  'date', 'open', 'high', 'low', 'close', 'volume', 'next day open'])
# print(df)
fig = go.Figure(data=[go.Candlestick(x=df['date'],
                                     open=df['open'], high=df['high'],
                                     low=df['low'], close=df['close'])
                      ])

fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()
