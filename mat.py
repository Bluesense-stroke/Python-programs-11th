'''
5 0 0
0 5 0
0 0 5'''
for r in range(0,3):
    for c in range(0,3):
        if r==c:
            print("5",end=" ")
        else:
            print("0",end=" ")
    print()
