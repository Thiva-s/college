num = int(input("Enter a number: "))
num = abs(num)  

lsd = num % 10

while num >= 10:
    num = num // 10

msd = num

print("MSD:", msd)
print("LSD:", lsd)