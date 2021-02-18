hr=int(input("ENter the hour between 1-12"))
ah=int(input("How many hours ahead "))

if hr<=12:
    new=ah+hr
    if new>12:
        new=new-12
    print("Time at that time would be",new,"o'clock")