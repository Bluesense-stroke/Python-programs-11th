#Employeee details
n=int(input("ENter the number of employee"))
emp={}
for i in range(n):
    eno=input("Enter the eno")
    ename=input("Enter the ename")
    sal=int(input("Enter the sal"))
    emp[eno]=[ename,sal]
print(emp)

#to look up name and salary based on eno
no=input("Enter the employee code to be searched")
print(emp[no])
