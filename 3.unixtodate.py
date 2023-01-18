from datetime import datetime

UNIX=int(input("Enter a UNIX value:", ))
unixtodate=datetime.fromtimestamp(UNIX).strftime("%d %B %Y %H:%M:%S")
print("Date in readable format is:", unixtodate)