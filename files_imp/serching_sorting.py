products = [
    {"id": 101, "name": "Laptop", "price": 900, "stock": 12},
    {"id": 205, "name": "Keyboard", "price": 25, "stock": 85},
    {"id": 150, "name": "Monitor", "price": 180, "stock": 30},
]
query=int(input("Enter the Id to find: "))
low_p=int(input("Enter the min range shoukd be : "))
high_p=int(input("Enter the max range should be : "))
def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    

def sorting_price(products):
    n = len(products)
    for i in range(n):
        for j in range(n - i - 1):
            if products[j]["price"] > products[j + 1]["price"]: 
                swap(products, j, j + 1)
    return products


def sorting_stock(products):
    n = len(products)
    for i in range(n):
        for j in range(n - i - 1):
            if products[j]["stock"] < products[j + 1]["stock"]:  # descending
                swap(products, j, j + 1)
    return products


def sort_by_name(products):
    n = len(products)
    for i in range(n):
        for j in range(n - i - 1):
            if products[j]["name"].lower() > products[j + 1]["name"].lower():
                swap(products, j, j + 1)
    return products

def search_ID(products,query):
    value=[]
    for i in range(len(products)):
        if products[i]["id"] == query:
            value.append (products[i])
    return value

def price_range(products, low_p, high_p):
    results = []
    for p in products:
        if p["price"] >= low_p and p["price"] <= high_p:
            results.append(p)
    return results
    
print("ID u serched for is :")
print(search_ID(products,query))
print("Sorted by price (low → high):")
print(sorting_price(products.copy()))

print("\nSorted by stock (high → low):")
print(sorting_stock(products.copy()))

print("\nSorted by name (A → Z):")
print(sort_by_name(products.copy()))

print("range of price")
print(price_range(products,low_p,high_p))
