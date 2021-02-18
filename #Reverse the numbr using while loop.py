#Reverse the numbr using while loop
rev=0
n=int(input("ENter the number"))
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print("reverse of the number",rev)
