from datetime import datetime,timedelta

now=datetime.now()
print("Current date:",now)
difference=now-timedelta(days=5)
print("5 days before the date was:", difference)
