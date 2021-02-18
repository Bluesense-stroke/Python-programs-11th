#Input of 2 numbers and whether they are divisble by each other

a=float(input("Enter the First number"))
b=float(input("Enter the second number"))

div=a//b
if a%b==0:
    print(a,"is divisble by ",b)
if a%b!=0:
    print(a,"is not divisble by ",b)
