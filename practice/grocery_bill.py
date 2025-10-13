total = 0

while True:
    price = float(input("Enter item price (0 to stop): "))
    if price == 0:
        break
    total = total + price

print("Total bill amount =", total)
