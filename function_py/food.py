menu = {
    "burger": 5.99,
    "pizza": 8.99,
    "salad": 4.99
}

total = 0
for i in menu:
    total += menu[i]

print("Total bill:", total)
