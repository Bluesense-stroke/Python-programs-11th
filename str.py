str=input("Enter your name")
"""for c in str:
    print(c,end="")"""
l=len(str)
print("length of the string",l)
for i in range(l):
    print(i,',',str[i])

str[5]="t"
