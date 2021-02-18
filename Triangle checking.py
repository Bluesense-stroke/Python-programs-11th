a=int(input("Enter the side 1"))
b=int(input("Enter the side 2"))
c=int(input("Enter the side 3"))

if a+b > c and b+c > a and c + a > b :
    print("It forms a Triangle")
else:
    print("It not forms a triangle ")