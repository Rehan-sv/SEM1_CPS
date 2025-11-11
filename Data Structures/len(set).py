# Program 7: Find length of set
nums = {2, 3, 5, 10, 15, 20}
print(type(nums))
print("Length (using len):", len(nums))

# Without len()
count = 0
for _ in nums:
    count += 1
print("Length (without len):", count)
