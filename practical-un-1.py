n=int(input("enter the number of elements"))
l= []
for i in range(97,97+n):
    c = chr(i)*(i- 96)
    l.append(c)
print(l)
