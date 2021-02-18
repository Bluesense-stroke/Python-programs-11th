#PROGRAM TO CALCULATE THE ETA OF MAP

hrs=int(input("Enter the hrs "))
min=int(input("Enter the minutes"))
sec=int(input("Enter the Seconds"))

#Current Day 
day=input("Enter the Current Day")


#Places list
print("MGR CHENNAI CTL=MAS")
print("MUMBAI CENTRAL=BCT")
print("DELHI=DLI")
print("VISAKHAPATNAM=VSKP")


#Confiuring places
MAS="MGR CHENNAI CTL"
VSKP="VISAKHAPATNAM"
BCT="MUMBAI CENTRAL"
DLI="DELHI"

#days

"""
"MGR CHENNAI CTL" = MAS
"MUMBAI CENTRAL" = BCT
"DELHI" = DLI
"VISAKHAPATNAM" = VSKP
"""

def place():
    pla=input("Enter the place (Departure)")
    pld=input("Enter the place (Arrival)")
    
    if pla=="MAS" and pld=="VSKP":
        print("YOUR DEPARTURE TIME IS",hrs+8,":",min,"hours",day)

    
    if pla=="BCT" and pld=="VSKP" and hrs>=12 :
        print("YOUR DEPARTURE TIME IS",hrs+1,":",min,"hours",day+1)
    

place()



