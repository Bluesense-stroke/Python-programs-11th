n1=float(input("enter th first number"))
n2=float(input("enter the second number"))
n3=float(input("enter the third number"))
if n2>=n1:
    if n2>=n3:
        big=n2
    else:
        big=n3
else:
    if n1>=n3:
        big=n1
    else:
        big=n3
print(big)
