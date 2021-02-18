#Fibonacci sequence 0,1,1,2,3,5,8,13...........
fir,sec=0,1
n=int(input("Enter the limit"))
if n==1:
    print(fir)
elif n==2:
    print(fir,sec)
else:
    print(fir,sec,sep=" ",end=" ")
    for i in range(3,n+1):
        next=fir+sec
        fir,sec=sec,next
        print(next,end=" ")
        
