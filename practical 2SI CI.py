#Program to find simple interest and compound interest

p=float(input("principal amount="))
n=float(input("no. of time period elapsed(in years)"))
r=float(input("rate of interest="))
si=p*n*r/100
ci=p*(1+r/100)**n

print("Simple Interest=",si)
print("compound interest = ",ci)
