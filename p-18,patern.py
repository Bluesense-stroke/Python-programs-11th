'''        A
         B C
       D F G
      H I J K
'''
n=int(input("no of rows"))
a=n+1
x=ord('a')
for i in range (n):
    for s in range (a):
        print(" ",end=' ')
        for j in range(x,x+n):
            y=chr(j)
            for k in range(i+1):
                print(y,end=" ")
    a=a-1
print()
