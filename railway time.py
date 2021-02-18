#to convert into railway time
a=input("Am/Pm")
h=int(input("Enter hours"))
min=int(input("enter minutes"))
if a=="Am":
    print("railway time",h,":",min,"hours")
elif a=="Pm":
    print("railway time",h+12,":",min,"hours")

                   
