#count the frequency of words in a sentence using a dictionary
sen=input("Enter the sentence")
l=sen.split()
d={}
for i in l:
    if i not in d:
        d[i]=l.count(i)
print(d)
