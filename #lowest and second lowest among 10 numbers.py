#lowest and second lowest among 10 numbers
flow,slow=9999,9999
for i in range(10):
    a=int(input("Enter the numbers"))
    if a<flow :
          slow=flow
          flow=a
    if a>flow and a<slow:
          slow=a
    print(flow,slow)
print("Lowest=",flow,"seconf=",slow)
