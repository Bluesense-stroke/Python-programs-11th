a=input("ENter the string to be sorted")

up_case=0
lo_case=0
nu=0
spec=0

for i in range (len(a)):
    if a[i] >= "A" and a[i] <= 'Z':
        up_case+=1
    elif a[i] >= 'a' and a[i] <= 'z':
        lo_case+=1
    elif a[i] >= '0' and a[i] <= '9':
        nu+=1
    else:
        spec+=1

print(a)
print()
print("Upper Cases",up_case)
print("Lower Cases",lo_case)
print("Numbers",nu)
print("Special Characters",spec)
