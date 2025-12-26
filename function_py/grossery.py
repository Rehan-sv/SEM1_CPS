a={}
n=int(input("ENter the number of items: "))
for i in range(n):
    item=input("Enter the item Name:")
    mrp=float(input("Enter the price:"))
    stocks=int(input("Enter the number of stocks it haas"))
    a[item]={"price":mrp,"stock":stocks}
    print(a)

def add(a):
    item=input("ENter the adding one:")
    mrp=float(input("Enter the price:"))
    stocks=int(input("Enter the stocks"))
    a[item]={"price":mrp,"stock":stocks}
    return(a)

def stock(a,stock):
    if i in a:
        if a[i]["stock"]>=stock:
            a[i]["stock"]-=stock
            print("successful")
        else:
            print("Not enough stocks")
            
def total_inventory_value():
    total = 0
    for item in a:
        total += a[item]["price"] * a[item]["stock"]
    return total    