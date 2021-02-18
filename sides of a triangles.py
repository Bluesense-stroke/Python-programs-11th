#program to check if inputed values of sides of a triangle is valid or not
a=float(input("Enter the value of side a"))
b=float(input("Enter the value of side b"))
c=float(input("Enter the value of side c"))

if a + b > c and b + c > a and c + a > b :
    print("Sides are valid")
else :
    print("Invalid")

    
