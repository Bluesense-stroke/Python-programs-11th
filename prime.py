#program to find prime num
n=int(input("Enter the number"))
for i in range(2,(n)//2+1):
    if n%i==0:
        print(n,"is composite")
        break
else:
    print(n,"is prime")
        
    
   
        
        
