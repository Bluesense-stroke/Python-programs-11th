ch=input("Enter a single character character")  
ch=ch.upper()   #methods
if len(ch)==1 :
    l=["A","E","I","O","U"]
    if ch in l :
        print(ch,"is vowel")
    else :
        print(ch,"is consonant")
else :
    print("Enter a single character")

