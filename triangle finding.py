#triangel finding

a=int(input("ENter side a"))
b=int(input("Enter side b"))
c=int(input("Enter side c"))
if a==b==c:
    print("Triangle is equilateral")
elif a==b or b==c or c==a:
    print("Triangle is isoceles")
else:
    print("Trinagle is scalence")
    
