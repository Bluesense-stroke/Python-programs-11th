r=0
n=int(input("Enter a number"))
while n>0:
    d=n%10
    r=r*10+d
    n=n//10
print("reverse",r)