elements=input("Enter the values with spaces in between:")
values=elements.split(" ")
lists=list(values)
print(lists)
print(type(lists))
sum=0
for i in lists:
    sum=sum+int(i)
    
print("The sum of the list of numbers = ",sum)