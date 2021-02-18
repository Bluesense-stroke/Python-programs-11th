#To find the sum of indivual digits of a number
sum=0
n=int(input("Enter the number"))
while n>0:
    d=n%10
    print(d)
    sum=sum+d
    n=n//10
print("The sum of individual digits of the number",sum)
