#pgm to divsilbe by 7 and multiple by 5
n=int(input("Enter the number"))
if n%7==0 and n%5==0:
    print("the number is div by 7 and multiple of 5")
elif n%7==0:
    print(n,"is only divisble by 7")
elif n%5==0:
    print(n,"is multiple of 5")
else:
    print("enot div by both")
