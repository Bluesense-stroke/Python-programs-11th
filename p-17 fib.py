n=int(input("enter the no. of terms in the series"))
a1=0
a2=1
print("the Fibonacci Series with",n,"term(s) is:")
if n==1:
    print(a1)
else:
    print(a1,a2,sep="   ",end="   ")
    for i in range(2,n):
        a3=a1+a2
        a1=a2
        a2=a3
        print(a3,end="   ")
    
