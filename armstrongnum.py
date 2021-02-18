#armstrong or not
n=int(input("Enter the number"))
num=n
sc=0
while n>0:
    d=n%10
    sc=sc+d**3
    n=n//10
if num==sc:
    print("armstrong number")
else:
    print("not a armstrong number")
