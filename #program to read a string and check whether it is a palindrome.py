#program to read a string and check whether it is a palindrome
s=input("enter the word ")
rev=''
l=len(s)
print("length of the string",l)
for i in range(l-1,-1,-1):
    rev=rev+s[i]
if s==rev:
    print("it is a palindrome")
else:
    print("not a palindrome")
