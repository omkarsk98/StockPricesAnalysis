import mysql.connector
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt

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

hdfc_dataframe = pd.DataFrame(myresult, columns=[
                  'date', 'open', 'high', 'low', 'close', 'volume', 'next day open'])
# candlestickGraph = go.Figure(data=[go.Candlestick(x=hdfc_dataframe['date'],
#                                      open=hdfc_dataframe['open'], high=hdfc_dataframe['high'],
#                                      low=hdfc_dataframe['low'], close=hdfc_dataframe['close'])
#                       ])

# candlestickGraph.update_layout(title=go.layout.Title(
#         text="Candle Stick",
#         xref="container",
#         x=0.5,
#     ),xaxis_rangeslider_visible=False)
# candlestickGraph.show()


# plt.plot(hdfc_dataframe['date'],hdfc_dataframe['open'])
# plt.plot(hdfc_dataframe['date'],hdfc_dataframe['high'])
# plt.plot(hdfc_dataframe['date'],hdfc_dataframe['low'])
# plt.plot(hdfc_dataframe['date'],hdfc_dataframe['close'])
# plt.legend(['open price', 'high price', 'low price', 'close price'], loc='upper left')
# plt.title("Line Graph (Very Messy)",loc="center")
# plt.savefig("./Visualisations/Explorative/Line_Graph_AllData.png")
# plt.show()