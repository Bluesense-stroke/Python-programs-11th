ch=input("Enter a string")
if ch.isalpha():
    print("It contains only alphasets")
elif ch.isdigit():
    print("it contains on;y digits")
elif ch.isalnum():
    print("it is alphanumeric")
else:
    print("none")
    
