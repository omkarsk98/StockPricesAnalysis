# run

`python3 visualise.py.py`
This file will output the visualisation of the data. The latest output results in formation of ohlc graph with '5 Days Moving Average' of the entire data. The graph for the same can be found in ./Visualisations/Explorative/OHLC_with_5SMA(total).png

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

# File Structures

```bash
.  
├── Queries  
│   └── queries.json  
├── README.md  
├── Visualisations  
│   └── Explorative  
│       ├── CandleStickPatter_50days.png  
│       ├── CandleStickPattern_1000days.png  
│       ├── CandleStickPattern_100days.png  
│       ├── CandleStickPattern_200days.png  
│       ├── CandleStickPattern_500days.png  
│       ├── CandleStickPattern_AllData.png  
│       ├── Latest 100 days moving average.png  
│       ├── Line_Graph_1000days.png  
│       ├── Line_Graph_100days.png  
│       ├── Line_Graph_200days.png  
│       ├── Line_Graph_500days.png  
│       ├── Line_Graph_50days.png  
│       ├── Line_Graph_AllData.png  
│       ├── OHLC_with_5SMA(latest 100).png  
│       └── OHLC_with_5SMA(total).png  
└── visualise.py  
  
3 directories, 18 files  
```
