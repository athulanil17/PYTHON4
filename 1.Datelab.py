from datetime import datetime

now = datetime.now()
currentmonth = now.strftime("%B")
currentweek = now.strftime("%U")
datetimeSTR=now.strftime("%d/%m/%Y %H:%M:%S")
MonthSTR=now.strftime("%m")
weekdayofweek=now.weekday()
dayoftheyear=now.strftime("%j")
dayofthemonth=now.strftime("%d")
dayoftheweek=now.strftime("%A")
print("1.Current date and time is:", datetimeSTR)
print("2.Current year is:", now.year)
print("3.Current Month of the year is:", currentmonth)
print("4.Current Week of the year is:", currentweek)
print("5.Current Week day of the week:", weekdayofweek)
print("6.Current day of the year:", dayoftheyear)
print("7.Current day of th month:", dayofthemonth)
print("8.Current day of the week:", dayoftheweek)