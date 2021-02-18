#checking uppercase,lowercase,Digit,special case
c=ord(input("Enter a single character"))
if 65<=c<=90:
    print("Uppercase Alphabet")
elif 97<=c<=122:
    print("lowercase Alphabet")
elif 48<=c<=57:
    print("Digit")
else:
    print("special case")
    

