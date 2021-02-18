#Check hether a number is palindrome
rev=0
n=int(input("ENter the number"))
num=n
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print("Reverse of the number",rev)
if num==rev:
      print("The number is palinndrome")
else:
    print("number is not palindrome")
