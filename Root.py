#program to find the roots,sum of roots,product of roots and nature of the roots of a quadratic eqn

print("Let the quadratic equation be ax^2+bx=c")
a=float(input("Enter the value of a "))
b=float(input("Enter the value of b "))
c=float(input("Enter the value of c "))
D=b**2-4*a*c

if a!=0:
    if D>0 :
        x1=(-b+D**0.5)/(2*a)
        x2=(-b-D**0.5)/(2*a)
        print("The roots are real and distinct")
        print("alpha=",x1)
        print("beta=",x2)
        print("Sum of roots",-b/a)
        print("Product of roots",c/a)
    elif D==0 :
       x1=(-b)/(2*a)
       x2=(-b)/(2*a)
       print("The roots are real and equal")
       print("alpha=",x1)
       print("beta=",x2)
       print("Sum of roots",-b/a)
       print("Product of roots",c/a)

    else :
        print("The roots are imaginary")
else :
    print("The equation is not quadratic")


