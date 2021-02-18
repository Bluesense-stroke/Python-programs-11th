#factorial using while loop
fact=1
n=int(input("Enter the number"))
i=1

while i<=n:
    fact=fact*i
    i=i+1
print("The factorial of the number",fact)
