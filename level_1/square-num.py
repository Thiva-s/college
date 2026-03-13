N=int(input("Enter a limit: "))
count=0
for i in range(1,N+1):
    count=count+i*i
print("The sum of square of N numbers is: ",count)