a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
x = a.intersection(b)
print("The intersection between a and b is:", x)
# Remove intersection values from each set
a = a - x
b = b - x
print("After removing intersection values from a:", a)
print("After removing intersection values from b:", b)
