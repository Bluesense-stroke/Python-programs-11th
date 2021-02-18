#PROGRAM TO CALCULATE THE ETA OF MAP

hrs=int(input("Enter the hrs "))
min=int(input("Enter the minutes"))
sec=int(input("Enter the Seconds"))


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
        print("YOUR DEPARTURE TIME IS",hrs+8,":",min,"hours")
    

    if pla=="BCT" and pld=="VSKP":
        print("YOUR DEPARTURE TIME IS",hrs+13,":",min,"hours")
    else:
        print
    

place()



