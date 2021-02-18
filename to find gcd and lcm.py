x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
prod=x*y
while (x!=y):
    if x>y:
        x=x-y
    else:
        y=y-x
print("The GCD is",x)
gcd=x
lcm=prod//gcd
print("LCM",lcm)


"""
while (b):
a,b=b,a%b
print("GCD",a)
"""
