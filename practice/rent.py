floor = 3
room = 10
rent = 1000
nights = int(input("Enter number of nights: "))

total = 0   # total for hotel

for f in range(floor):
    per_floor = 0
    for r in range(room):
        per_floor += rent * nights
    print("Floor", f + 1, "total:", per_floor)
    total += per_floor

print("Hotel total revenue: ₹", total)
