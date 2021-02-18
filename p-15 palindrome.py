#checking whether a number is palindrome
n=int(input("enter the number"))
rev=0
num=n
while n>0:
    d=n%10
    rev=rev*10+d
    n//=10
    print(n,d,rev)
if num==rev:
    print("the given number is palindrome")
else:
    print("the given number is not a palindrome")
