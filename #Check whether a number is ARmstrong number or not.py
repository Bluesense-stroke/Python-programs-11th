#Check whether a number is ARmstrong number or not
sum=0
n=int(input("ENter the number"))
num=n
while n>0:
    d=n%10
    sum=sum+d**3
    n=n//10
print("ARmstrong number",sum)
if num==sum:
      print("The number is ARmstrong number ")
else:
    print("number is not ARmstrong number")
