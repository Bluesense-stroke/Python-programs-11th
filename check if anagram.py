s1=str(input("enter a word"))
s2=str(input("enter another word"))
s10=sorted(s1)
print(s10)
s20=sorted(s2)
print(s20)
if s10==s20:
    print(s1,"and",s2," are anagram")
else:
    print(s1,"and",s2," are not anagram")
