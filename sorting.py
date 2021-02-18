s1=input("Enter a string")
s2=input("Enter the string2")
l1=sorted(s1.upper())
l2=sorted(s2.upper())
print(l1,l2)
if l1==l2:
    print("they are anagrams")
else :
    print("they are not anagrams")
