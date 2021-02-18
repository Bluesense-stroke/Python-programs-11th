#To convert the number into words

import inflect

n=int(input("Enter the number"))
p=inflect.engine()
n1=p.number_to_words(n)
print(n1)
