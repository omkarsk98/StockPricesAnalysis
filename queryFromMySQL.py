import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="StockAdmin",
    passwd="random",
    database="Stocks"
)

mycursor = mydb.cursor()

mycursor.execute(
    "select date, open, high, low, close, volume, (select open from hdfc h1 where h1.id>h.id order by id asc limit 1) as 'next day open' from hdfc h limit 10;")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
