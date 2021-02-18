n=int(input("Enter the n"))
se,so=0,0
for i in range(n+1):
    if i%2==0:
        se+=i
    else:
        so+=i
print("sum of odd numbers =",so)
print("sum of even numbers =",se)