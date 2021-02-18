x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
a,b=x,y
while(x!=y):
    if x>y:
        x=x-y
    else :
        y=y-x
gcd=x
lcm=a*b//gcd
print("GCD",gcd,"LCM",lcm,sep=" ")


