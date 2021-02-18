#linear serach
l=eval(input("Enter a list in[]"))
ele=int(input("Enter the element to be searched"))
c=0
for i in l:
    if i==ele:
        c+=1
        p=l.index(i)
else:
    if c>0:
        print("Element found and it occurs",c,"times")
        print("postions",p)
    else:
        print("Element not found",)
        
