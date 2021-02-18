#FInding maximum among N numbers
n=int(input("Enter how many number"))
max=-9999
for i in range(n):
    a=int(input("Enter the numbers"))
    if a>max:
        max=a
print("Maximum",max)
