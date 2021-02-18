n1=float(input("enter th first number"))
n2=float(input("enter the second number"))
n3=float(input("enter the third number"))
if n2>=n1:
    if n2>=n3:
        if n3>=n1:
            max,mid,min=n2,n3,n1
        else:
            max,mid,min=n2,n1,n3
    else:
        max,mid,min=n3,n2,n1
else:
    if n1>=n3:
        if n2>=n3:
            max,mid,min=n1,n2,n3
        else:
            max,mid,min=n1,n3,n2
    else:
        max,mid,min=n3,n1,n2
print(min,mid,max,sep=" , ",end=" ")
print("is the ascending order")
