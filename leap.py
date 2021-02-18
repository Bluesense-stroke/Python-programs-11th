#To check whether a yeap input is leap year
y=int(input("Enter the year"))
if y%4==0 and y%400!=0:
    if y%100==0:
        print("Not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")
