#Write a program to input three numbers and find the largest of three
#numbers.

a=int(input("Enter the number 1"))
b=int(input("Enter the number 2"))
c=int(input("Enter the number 3"))

if a > b and a > c :
    largest=a
elif b > c and b > a:
    largest=b
else:
    largest=c
    
print("The largest number is",largest)    
    

