#sum of N natural numbers

n=int(input("Enter the number "))
s=0
print("Number\tcumulative sum")
for i in range(1,n+1):
    s+=i
    print(i,s)
