def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
num=int(input("Enter a number: "))
sum=0
for i in range(1,num+1):
    sum=sum+fact(i)
print(sum)