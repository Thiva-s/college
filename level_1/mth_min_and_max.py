nums = list(map(int, input("Enter list elements:").split()))
m = int(input())

nums.sort()

print("Mth Minimum:", nums[m-1])
print("Mth Maximum:", nums[-m])