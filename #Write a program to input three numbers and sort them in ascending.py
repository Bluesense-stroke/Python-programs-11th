#Write a program to input three numbers and sort them in ascending
#order.(Nested if)

a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
c=float(input("Enter the third number:"))
if a>b and a>c:
    if b>c:
        x,y,z=a,b,c
    else:
        x,y,z=a,c,b
elif b>a and b>c:
    if a>c:
        y,x,z=a,b,c
    else:
        z,x,y=a,b,c
else:
    if a>b:
        y,z,x=a,b,c
    else:
        z,y,x=a,b,c
print(x,y,z,sep=">")

