# to count the character frequency
s=input("enter the string")
d={}
for i in s:
    if i not in d:
        d[i]=s.count(i)

print(d)
