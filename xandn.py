#sum of the series 1+x^1+x^2....
x=int(input("Enter the value of x"))
n=int(input("Enter the value of n"))
sum=0
for i in range(0,n+1):
    sum=sum+x**i
print("sum of series",sum)
