# Problem 1: Find common integers between two inputs (list and set)

# Read first line as list
list_input = input("Enter numbers for first list: ").split()
list1 = []
for i in list_input:
    list1.append(int(i))
print(list1)

# Read second line as set
set_input = input("Enter numbers for second set: ").split()
set1 = set()
for j in set_input:
    set1.add(int(j))

# Find common numbers (including duplicates from the list)
common = []
for k in list1:
    if k in set1:
        common.append(k)

# Output result
print(common)
