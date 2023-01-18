n=int(input("Enter the value for n:"))
x=int(input("Enter the value for x:"))
sum=0
for i in range(n,x-1,-2):
    sum=sum+i

print(sum)