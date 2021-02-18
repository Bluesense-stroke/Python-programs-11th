#count the frequency og words in a sentence using a dictionary
sen=eval(input("Enter the list"))
#l=sen.split()
d={}
for i in sen:
    if i not in d:
        d[i]=sen.count(i)
        
print(d)
