#generate all divisors of a num
n=int(input("Enter the value "))
print("The divisors of N")
for i in range(1,n+1):
    if n%i==0:
        print(i,end="  ")
    else:
        pass
