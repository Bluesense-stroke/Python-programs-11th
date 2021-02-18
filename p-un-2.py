l=eval(input("enter a list with only nos as element"))
for i in l:
    if i<0:
        l.remove(i)
        l.append(i)
print(l)
