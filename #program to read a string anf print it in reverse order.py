#program to read a string anf print it in reverse order
s=input("Enter your name")

l=len(s)
print("length of the string",l)
for i in range(l-1,-1,-1):
    print(s[i],end=" ")
