def load_products():
    products = []
    f = open("products.txt", "r")
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 5:
            pid = parts[0].strip()
            name = parts[1].strip()
            cat = parts[2].strip()
            price = float(parts[3].strip())
            qty = int(parts[4].strip())

            products.append({
                "id": pid,
                "name": name.lower(),
                "category": cat.lower(),
                "price": price,
                "quantity": qty
            })
    f.close()
    return products
k=load_products()

def search(cat):
    print("---------------------------------")
    for i in k:
        if cat==i["category"]:
            print(i["id"],i["name"],i["price"],i["quantity"])
            
            
print("===== SMART GROCERY STORE SYSTEM =====")
print("1. Display all products")
print("2. Search by Category")
print("3. Update Quantity")
print("4. Costliest Product")
print("5. Category-wise Summary")
print("6. Save Data to File")
print("7. Exit")
while True:
    
    c=int(input("enter the choices:"))
    if c==1:
        print("ID Name Category Price Quantity")
        print("------------------------------------------------")
        for i in k:
            print(i["id"]," ",i["name"]," ",i["category"]," ",i["price"]," ",i["quantity"])
    elif c==2:
        cat=input("enter the category to search:").lower()
        search(cat)
    elif c==3:
        e=input("enter the product id:")
        q=int(input("enter the new quantity:"))
        for i in k:
            if i["id"] in e:
                i["quantity"]+=q
        print("the updated quantity is",q)
        print("the quantity updated successfully")
    elif c==4:
        print("the costliest product")
        print("-------------------------")
        l=0
        for i in k:
            if i["price"]>l:
                l=i["price"]
        for i in k:
            if i["price"]==l:
                print("ID:",i["id"])
                print("name:",i["name"])
                print("price:",i["price"])
                print("quantity:",i["quantity"])
    elif c==5:
        print("Category-wise Quantity Summary")
        print("-------------------------")
        for i in k:
            print(i["category"],":",i["quantity"])
    elif c==6:
        a=open("products.txt","w")
        for i in k:
            a.write(f"{i['id']},{i['name']},{i['category']},{i['price']},{i['quantity']}\n")
        a.close()
        print("data saved successfully")
    elif c==7:
        print("exiting....")
        break
    else:
        print("wrong input")