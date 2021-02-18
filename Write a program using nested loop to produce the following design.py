#19.Write a program using nested loop to produce the following design.
'''
  *
 * *
* * *
 * *
  *
  '''

  
a=3
for i in range(3):
    for s in range(a):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    a=a-1
    print()
    
a=2
for i in range(2):
    for j in range(i+1):
        print(" ",end="")
    for s in range(a):
        print(" *",end="")
    a=a-1
    print()
