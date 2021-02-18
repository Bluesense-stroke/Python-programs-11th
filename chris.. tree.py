n=int(input("enter how big tree u want"))
a=n+1
for i in range (n):
    for s in range (a):
        print(" ",end=' ')
    for k in range(i+1):
        print("^ ",end=" ")
    a=a-1
    print()
for i in range(n+1,n-3,-1):
    for s in range (a):
        print(" "*n*2,"III",end=" ")
    print()
      
