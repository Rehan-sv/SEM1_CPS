# Program 6: Check if a value exists in a set using if loop

nums = {1, 3, 5, 7, 9, 11}
test_values = [6, 7, 11, 0]

print("Original set:", nums)

for val in test_values:
    if val in nums:
        print(f"{val} exists in the set.")
    else:
        print(f"{val} does not exist in the set.")  