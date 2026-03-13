nums = list(map(int, input("Enter elements: ").split()))

element = int(input("Enter element to insert: "))
position = int(input("Enter position: "))

nums.insert(position, element)

print("Updated List:", nums)