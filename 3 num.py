#largest of 3 number using if else stmt
a=int(input("Enter the value of A"))
b=int(input("Enter the value of B"))
c=int(input("Enter the value of C"))
if (a>b)and(a>c):
    print(a,"is greatest")
else:
    if b>c:
        print(b,"is greatest")
    else:
        print(c,"is greatest")
