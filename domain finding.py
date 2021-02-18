s1=input("Enter the string")
s2="@kvhvf.com"
t=s1.partition("@kvhvf.com")
print(t)
if t[0].isalnum() and t[1]=="@kvhvf.com" and t[2]==' ' :
    print("Valid email id in domain")
else:
    print("Invails")
