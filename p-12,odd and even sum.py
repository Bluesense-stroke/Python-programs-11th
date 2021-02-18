#to find the sum of even numbers and odd nummbers from first n natural number
n=int(input("enter a natural number"))
odd_sum=0
even_sum=0
for i in range(1,n+1,2):
    odd_sum+=i
    
for k in range(2,n+1,2):
    even_sum+=k
print(even_sum,"is the sum of first even natural number till n")
print(odd_sum, "is the sum of first odd number till n")
