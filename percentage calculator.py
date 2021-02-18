print("percentage of mark (Total mark of each sub=80)")
P=float(input("physics mark="))
C=float(input("chemistry mark="))
M=float(input("maths marks="))
cs=float(input("computer science mark="))
E=float(input("english mark="))
A=float(input("any other 6th sub?if not there press 0     "))
N=float(input("if only 5 subject press 1 otherwise press 0     "))
S=float(input("if  6 subject press 1 otherwise press 0     "))
pt=(P+C+M+cs+E)*N*10/8+(P+C+M+cs+E+A)*S*100/480

print("your perncentage=",float(pt))
      
