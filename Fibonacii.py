#Fibonacii sequence 0,1,1,2,3,5,8,13............
fi,se=0,1
n=int(input("Enter the limit"))
if n==1:
    print(fi)
elif n==2:
    print(fi,se)
else:
    print(fi,se,sep=" ",end=" ")
    for i in range(3,n+1):
        nex=fi+se
        fi,se=se,nex
        print(nex,end=" ")
        
