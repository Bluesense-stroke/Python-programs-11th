#program to input n. if n is multiple of the three print "fizz" and if is multiple of
# five print "buzz" . if n is both then print "fizzbuzz"
n=int(input("Enter the number"))
if n%3==0 and n%5!=0:
    print("FIZZ")
elif n%5==0 and n%3!=0:
    print("BUZZ")
elif n%5==0 and n%3==0:
    print("FIZZBUZZ")


    

    
