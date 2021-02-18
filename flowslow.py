#lowest and second lowest among 10 numbers
flow,slow=99999,99999
for i in range(10):
    a=int(input("Enter the number"))
    if a<flow:
        slow=flow
        flow=a
    if a>flow and a<slow:
        slow=a
    print(flow,slow)
print("Lowest=",flow,"second lowest=",slow)
