#simple factorial program
n=int(input("enter a number"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact,"is the factorial of the number",n)
    
