#
a=int(input("enter the leading coefficient:"))
b=int(input("enter th coefficient of x:"))
c=int(input("enter the constant term:"))
D=b**2-4*a*c
print(D)
if D<0:
    print("the QE has imaginary roots")
    x1=(-b+D**0.5)/(2*a)
    x2=(-b-D**0.5)/(2*a)
if D==0:
    print("the QE has two equal real root")
    x1=x2=-b/(2*a)
if D>0:
    print("the QE hars two real distinct roots")
    x1=(-b+D**0.5)/(2*a)
    x2=(-b-D**0.5)/(2*a)
print(type(x1 and x2))
print(x1, x2)
