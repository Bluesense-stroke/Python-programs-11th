#to check whether a number is prime or not
n=int(input("Enter the number "))
for i in range(2,n//2+1):
    if n%i==0:
        print(n,"is composite number")
        break
else:
    print(n,"is a prime number")
