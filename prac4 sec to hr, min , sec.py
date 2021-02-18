#program to convert second int hour:minutes:secs
s=int(input('enter the total seconds:'))
hr=s//3600
x=s%3600
min=x//60
sec=x%60
print(hr,"hrs:",min,"mins:",sec,"secs")
