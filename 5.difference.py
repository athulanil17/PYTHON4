from datetime import datetime

date1="2000/02/28"
date2="2001/02/28"

str_d1=datetime.strptime(date1,"%Y/%m/%d")
str_d2=datetime.strptime(date2,"%Y/%m/%d")

difference=str_d2-str_d1
print("the Difference between two days is", difference.days)