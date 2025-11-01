a = int(input("Enter the total number of subjects: "))
b = []  # empty list to store marks

for i in range(a):
    marks = int(input(f"Enter mark for subject {i+1}: "))
    b.append(marks)

# Initialize min and max with first element
minimum = b[0]
maximum = b[0]
total = 0

for mark in b:
    if mark < minimum:
        minimum = mark
    if mark > maximum:
        maximum = mark
    total += mark

average = total / a

print("Marks List:", b)
print("Minimum Mark:", minimum)
print("Maximum Mark:", maximum)
print("Average Mark:", average)
