#sum of the individual digits of a number
sum=0
n=int(input("enter the number"))
while n>0:
    t=n%10
    sum+=t
    n//=10
print("sum of the individual digit of the given number is ",sum)
