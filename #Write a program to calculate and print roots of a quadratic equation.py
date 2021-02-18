#Write a program to calculate and print roots of a quadratic equation
#ax2+bx+c=0 ( a != 0).
from math import sqrt 

a=int(input("Enter the variable value (a)"))
b=int(input("Enter the variable value (b)"))
c=int(input("Enter the variable value (c)"))
d=(b**2)-(4*a*c)

if d>0:
    x1=(((-b) + sqrt(d))/(2*a))
    x2=(((-b) - sqrt(d))/(2*a))
    print("The roots are real and unequal",x1,x2)
elif d==0:
    x3=(-b)/2*a
    print("The roots are real and equal",x3)
else:
    print("The roots are imaginary and not exist ")


