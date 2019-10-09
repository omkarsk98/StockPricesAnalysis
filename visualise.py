import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from mpl_finance import candlestick2_ohlc
import Analysis.Query

hdfc_df = Analysis.Query.getDataSet()
limit = 50

fig, ax = plt.subplots()
plt.xticks(list(range(len(hdfc_df["date"]))), hdfc_df["date"], rotation=45)
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("HDFC Stock Prices Data")
candlestick2_ohlc(ax, hdfc_df["open"], hdfc_df["high"],
                  hdfc_df["low"], hdfc_df["close"], width=1, colorup='g')
# ax.plot(list(hdfc_df.index.values),hdfc_df['5 days moving average'])
ax.xaxis.set_major_locator(mticker.MaxNLocator(limit/5))
ax.xaxis_date()

plt.show()
