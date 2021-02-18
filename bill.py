#program to get the discount
Bamt=float(input("Enter billing amount"))
#discount 10 %
if Bamt>5000:
    dis=Bamt*10/100
    famt=Bamt-dis
else:
    dis=0
    
print("Discount=",dis)
print("Final Amount",famt)
