fib=(0,1)
n=int(input("Enter the number "))
for i in range(2,n):
    fib+=(fib[i-1]+fib[i-2],)
print("Fibonacci serious")
print(fib)
