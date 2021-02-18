#reverse the sum
n=int(input("Enter the number"))
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print("Reverse of the number",rev)
