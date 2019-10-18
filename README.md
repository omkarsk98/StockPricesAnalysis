# Objective
HDFC bank\'s stock prices are considered for this project. The objective is to predict the next day opening price on the basis of open(the price at which the stock opened on a specific day), high(highest price the stock had on a specific day), low(lowest price the stock had on a specific day), close(the price at which the stock closed on a day), volume(number of transaction that occured for this company. i.e. HDFC bank on a specific day), 5DMA(5 days moving average of the opening price).

# data

Data contains date, open, high, low, close, volume, 5 days moving average, next day open.  
Last attribute will be used as label and all the remaining attributes will be used as features.

| date       | open | high | low | close | volume  | 5 days moving average | next day open |
| ---------- | ---- | ---- | --- | ----- | ------- | --------------------- | ------------- |
| 2015-01-01 | 951  | 954  | 945 | 952   | 886235  | 952.00                | 950           |
| 2015-01-02 | 950  | 969  | 950 | 965   | 1475096 | 958.50                | 970           |
| 2015-01-05 | 970  | 971  | 955 | 957   | 1199000 | 958.00                | 954           |
| 2015-01-06 | 954  | 957  | 938 | 942   | 2054920 | 954.67                | 940           |
| 2015-01-07 | 940  | 951  | 936 | 945   | 1436528 | 948.00                | 954           |
| 2015-01-08 | 954  | 969  | 948 | 965   | 2381456 | 952.25                | 973           |
| 2015-01-09 | 973  | 980  | 967 | 976   | 2246296 | 957.00                | 969           |
| 2015-01-12 | 969  | 974  | 965 | 967   | 1031603 | 969.33                | 969           |
| 2015-01-13 | 969  | 972  | 956 | 963   | 1457087 | 968.67                | 960           |
| 2015-01-14 | 960  | 975  | 960 | 964   | 921308  | 964.67                | 990           |


# Visualisation
The visualisation is performed using Japnese Candle Stick Pattern and an addional line graph to plot the 5 days moving average. [This](./Visualisations/Explorative/OHLC_with_5SMA(total).png) plot demonstrates the entire data since 2015. It plot the OHLC and 5SMA. Since this graph is difficult to understand, [this](./Visualisations/Explorative/OHLC_with_5SMA(latest_100).png) can be seen (also mentioned below). This graph plots the OHLC price and 5SMA. Green color indicates a positive day and red color indicates a negative day. <br>
![Alt text](./Visualisations/Explorative/OHLC_with_5SMA(latest_100).png)


# run
`python3 Analysis/LinearRegression.py` <br>  
This file will develop the Linear Regression model and plot a graph containing the following plots.<br>
1. Predicted opening price for the next day by linear regression.<br>
2. Value of next day opening on the basis of 5SMA. Generally this 5SMA is also used as a method to predict the next day open. <br>
3. Actual opening price for the next day.<br>
*The graph contains the respective labels for the plots.*

# Outcome
Linear Regression Model predicts the next day opening price with an accuracy of 95% <br>
![Alt text](./Results/LinearRegression.png) <br>
*This linear regression model has an accuracy of 95%*