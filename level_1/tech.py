num = int(input("Enter a number: "))

s = str(num)

if len(s) % 2 != 0:
    print("Not a Tech Number")
else:
    mid = len(s) // 2
    first = int(s[:mid])
    second = int(s[mid:])
    
    total = first + second
    
    if total * total == num:
        print("Tech Number")
    else:
        print("Not a Tech Number")