#pgm 3
n=int(input("Enter thw order of square martix"))
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            print("5",end=" ")
        else:
            print("0",end=" ")
    print()
    
