pro=int(input("Enter the numbers of products that u have brought"))

if pro>=0 and pro<10:
    cost=pro*120
    print(cost,"The total cost of buying")
elif pro>=10 and pro <=99:
    cost=pro*100
    print(cost,"The total cost of buying")
else:
    cost=pro*70
    print(cost,"The total cost of buying")