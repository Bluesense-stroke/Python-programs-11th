print("The series is 1+x+x^2+x^3....+x^n")
x=int(input("Enter the value of x"))
n=int(input("Enter the value of n"))
s=0
for i in range(0,n+1):
    s=s+(x**i)
print("sum",s)

