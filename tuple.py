list1 = []
str1 = ' abcdefghijkelmnopqrstuvwxyz'
length = len(str1)
for i in range(1,length):
    c = (str1[i])*i
    list.append(c)
    return(tuple(list1))
print(list1)
