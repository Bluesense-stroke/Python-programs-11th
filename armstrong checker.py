#checking whether a number is armstrong
n=int(input("enter the number"))
sum=0
num=n
while n>0:
    d=n%10
    sum+=d**3
    n//=10
if num==sum:
    print("the given number is armstrong")
else:
    print("the given number is not a armstrong")

