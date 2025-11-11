# Program 5: No common elements
x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
z = {8}

print("Compare x and y:", x.isdisjoint(y))
print("Compare x and z:", x.isdisjoint(z))
print("Compare y and z:", y.isdisjoint(z))
