l=eval(input("ENter the nested list"))
m=len(l) #no of rows
n=len(l[0]) #no  of coloums

for i in range(m):
    rs=0
    for j in range(n):
        rs+=1[i][j]
    print("Sum of",i,"row",rs)
for j in range(n):
   cs=0
   for i in range(m):
       cs += 1[i][j]
   print("Sum of", j,"col",s)
