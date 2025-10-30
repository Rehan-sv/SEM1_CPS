list = [10, 30, 50, 99]
largest = list[0]
smallest = list[0]

for num in list:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Smallest:", smallest)
print("Largest:", largest)  