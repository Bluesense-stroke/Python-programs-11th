#sum of N natural numbers

n=int(input("Enter the number "))
os,es=0,0
for i in range(1,n+1,2):
    os+=i
    print(i,os)
for i in range(2,n+1,2):
    es+=i
    print(i,es)
