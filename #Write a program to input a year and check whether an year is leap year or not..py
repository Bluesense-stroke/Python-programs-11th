#Write a program to input a year and check whether an year is leap year or not.

year=int(input("Enter the year"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year,"It's a leap year")
        else:
            print(year,"It,s not a leap year")
    else:
        print(year,"It's a leap year")
else:
    print(year,"It's not a leap year")
    
        
        
