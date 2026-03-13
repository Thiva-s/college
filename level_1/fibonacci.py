def fiboonaci(n):
    if n < 0:
        print("Input should be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fiboonaci(n - 1) + fiboonaci(n - 2)
num=int(input("Enter a non-negative integer: "))
for i in range(num):
    print(fiboonaci(i))