#prime or not
n=int(input("enter a number"))
x=n//2
if n!=1:
    for i in range(2,x+1):
        if n%i==0:
            print(n,"is composite number")
            break
    else:
        print(n,"is a prime number")
        5454
    
else:
    print(n,"is neither prime nor composite")
