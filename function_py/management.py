def load_products():
    products = []
    f = open("function_py\\products.txt", "r")
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
                "name": name,
                "category": cat,
                "price": price,
                "quantity": qty
            })
    f.close()
    return products
m=load_products()

def  update_quantity(m,pid,qty):
    for i in m:
        if i["id"]==pid:
            i["quantity"]=qty
            print("quantity is updated is",qty)
            return
        print("product not found")
        
        
        
print("===== SMART GROCERY STORE SYSTEM =====")
print("1. Display all products")
print("2. Search by Category")
print("3. Update Quantity")
print("4. Costliest Product")
print("5. Category-wise Summary")
print("6. Save Data to File")
print("7. Exit")


while True:
    c=int(input("enter the choice(1-7):"))
    if c==1:
        print("ID Name Category Price Quantity")
        print("------------------------------------------------")
        for i in m:
           for j in i.values():
               print(j,end=' ')
           print()
    elif c==2:
        cat=input("enter the category:")
        print("category entered:",cat)
        print("------------------------------------------------")
        
        found=False
        for i in m:
            if i["category"].lower()==cat.lower():
                print(i["id"],i["name"],i["price"],i["quantity"])
                found=True
        if not found:
            print("it is not found")
    elif c==3:
        pid=input("enter the product id:")
        qty=int(input("enter the new quantity:"))
        update_quantity(m,pid,qty)
    elif c==4:
        max_p=m[0]
        for i in m:
            if i["price"]>max_p["price"]:
                max_p=i
        print("the costliest product")
        print("------------------------------------------------")
        print(max_p["id"],max_p["name"],max_p["category"],max_p["price"],max_p["quantity"])
    elif c==5:
        s={}
        for i in m:
            cat=i["category"]
            qty=i["quantity"]
            if cat in s:
                s[cat]+=qty
            else:
                s[cat]=qty
        for j in s:
            print(j,":",s[j])
    elif c == 6:
        f = open("products.txt", "w")
        for p in m:
            f.write(f"{p['id']}, {p['name']}, {p['category']}, {p['price']}, {p['quantity']}\n")
        f.close()
        print("Data saved!")
    elif c==7:
        print("exiting")
        break
    else:
        print("invalid choice")


