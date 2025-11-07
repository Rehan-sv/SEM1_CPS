# Python program to check if a given set is a superset of itself 
# and a superset of another given set
nums = {40, 10, 50, 20, 30}
print("Original set:", nums)

# Check if the set is a superset of itself
print("If nums is superset of itself?")
print(nums.issuperset(nums))  # A set is always a superset of itself

# Define three sets
num1 = {1, 2, 3, 4, 5, 7}
num2 = {2, 4}
num3 = {2, 4}

# Check superset relationships
print("num1 =", num1)
print("num2 =", num2)
print("num3 =", num3)

print("If num1 is superset of num2:")
print(num1.issuperset(num2))

print("If num2 is superset of num3:")
print(num2.issuperset(num3))

print("If num3 is superset of num2:")
print(num3.issuperset(num2))
