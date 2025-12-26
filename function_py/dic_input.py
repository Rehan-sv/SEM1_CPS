menu = {}

n = int(input("Enter number of menu items: "))

for i in range(n):
    item = input("Enter item name: ")
    price = float(input("Enter price: "))
    menu[item] = price

print(menu)
