#check whether a number is palindrome
n=int(input("Enter the number"))
rev=0
num=n
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
if num==rev:
    print("The number is palindrome")
else:
    print("The number is not a palindrome")
    
