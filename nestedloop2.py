#nested loops
'''
A
A B
A B C
A B C D
'''
n=int(input("Enter n"))
for i in range(n):
    k=65
    for j in range(i+1):
        print(chr(k),end=" ")
        k+=1
    print()
'''
        A
      B   B
    C   C   C
  D  D  D  D  D
  '''
k=65
a=15
for i in range(n):
    for s in range(a):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(k)," ",end=" ")
    k+=1
    a-=1
    print()

'''
        *
      *   *
    *   *   *
  *  *  *  *  *
  '''
a=15
for i in range(n):
    for s in range(a):
        print(" ",end=" ")
    for j in range(i+1):
        print("*"," ",end=" ")
    a-=1
    print()
a=1+a
for i in range(n-1,0,-1):
    for s in range(a):
        print(" ",end=" ")
    for j in range(i+1):
        print("*"," ",end=" ")
    print()

     
