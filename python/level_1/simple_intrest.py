p=int(input("Enter the principal amount: "))
n=int(input("Enter the number of years: "))
sc=input("Senior citizen (Y/N):")
g=input("male/female:")
if sc=="Y" and g=="M":
    print("The simple interest is:",(p*n*12)/100)
elif sc=="Y" and g=="F":
    print("The simple interest is:",(p*n*15)/100)
else:
    print("The simple interest is:",(p*n*10)/100)