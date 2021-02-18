 '''                                     *
                                       *   *
                                     *   *   *
                                   *   *   *   *
                                     *   *   *
                                       *   *
                                         *
'''n=int(input("enter the number of rows"))
k=20
for i in range(n):
    for s in range(k):
        print(" ",end=" ")
    for j in range(i+1):
        print(" * ",end=" ")
    k=k-1
    print()
k=k+1
for r in range(n-1,0,-1):
    k=k+1
    for s in range(k):
        print(" ",end=" ")
    for j in range(r):
        print(" * ",end=" ")
    print()