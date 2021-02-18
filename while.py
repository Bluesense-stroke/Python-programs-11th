#program to calculate sum of digits
n=int(input("Enter the number"))
sum=0
while n>0:
    d=n%10
    sum=d+sum
    n=n//10
print("Sum of digits",sum)
