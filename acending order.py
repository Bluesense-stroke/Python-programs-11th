num_1=float(input("enter the first number:"))
num_2=float(input("enter the second number:"))
num_3=float(input("enter the third number:"))
if num_1>num_2 and num_1>num_3:
    if num_2>num_3:
        a,b,c=num_1,num_2,num_3
    else:
        a,c,b=num_1,num_2,num_3
elif num_2>num_1 and num_2>num_3:
    if num_1>num_3:
        b,a,c=num_1,num_2,num_3
    else:
        c,a,b=num_1,num_2,num_3
else:
    if num_1>num_2:
        b,c,a=num_1,num_2,num_3
    else:
        c,b,a=num_1,num_2,num_3
print(a,b,c,sep="   ")
print(sum)
