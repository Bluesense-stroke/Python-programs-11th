#factorial of a number
fact=1
n=int(input("Enter the number"))
if n>=0:
    for i in range(1,n+1):
        fact=fact*i
        print(fact)
    print("Factorial of the number",fact)
else:
    print("negative input!!,factorial cant be found")
    

    
