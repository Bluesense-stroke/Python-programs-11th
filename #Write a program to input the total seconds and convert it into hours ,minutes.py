#Write a program to input the total seconds and convert it into hours ,minutes
#,seconds.

def conversion():
    sec1=int(input("Enter the time(in seconds)"))
    hrs=sec1//3600
    rem=sec1%3600
    min=rem//60
    sec=rem%60
    print("hrs:min:sec",hrs,":",min,":",sec)
conversion()
  
