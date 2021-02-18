#Sum even numbers and oddd numbers till n
n=int(input("Enter the number"))
osum,esum=0,0
for i in range(1,n+1):
    osum+=i
for i in range(2,n+1,2):
    esum+=i

print("Sum of even numbers till",n,"is",esum)
print("Sum of the odd numbers till",n,"is",osum)
