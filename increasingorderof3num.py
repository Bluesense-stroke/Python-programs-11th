#progam to input numbers and to ouput increasing order of the number
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>b>c:
    f,s,t=c,b,a
elif b>a>c:
    f,s,t=c,a,b
elif a>c>b:
    f,s,t=b,c,a
elif b>c>a:
    f,s,t=a,c,b
elif c>b>a :
    f,s,t=a,b,c
elif c>a>b :
    f,s,t=b,a,c
print(f,s,t)
