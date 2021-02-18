#sum of N natural numbers of a number
n=int(input("Enter the number"))
sum=0
print("number\tCumulative sum")
for i in range(1,n+1):
    sum+=i
    print(i,"\t",sum)
print("sum of natural numbers till",n,"is",sum)
