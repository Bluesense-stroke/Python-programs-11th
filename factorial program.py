#factorial of a number
fact=1
n=int(input("enter the number"))
i=1
while i<=n:
    fact*=i
    i+=1
print("the factorial of the number is",fact)
