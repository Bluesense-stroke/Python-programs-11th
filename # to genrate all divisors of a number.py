# to genrate all divisors of a number
n=int(input("Enter the number"))
print("The divisors are")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
