# find the largest and lowest number
flar,slar=-9999,-9999
for i in range(10):
    a=int(input("Enter the number"))
    if a>flar:
       slar=flar
       flar=a
    if a<flar and a>slar:
        slar=a
    print(flar,slar)
print("Largest=",flar,"Secondlargest=",slar)


