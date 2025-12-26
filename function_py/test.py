def load_data():
    products=[]
    f=open("function_py\products.txt","r")
    for line in f:
        parts=line.strip().split(",")
        if len(parts)==5:

            pid=parts[0].strip()
            name=parts[1].strip()
            cat=parts[2].strip()
            price=float(parts[3].strip())
            quantity=int(parts[4].strip())
            products.append({
                "id":pid,
                "name":name,
                "category":cat,
                "price": price,
                "quantity": quantity
            })
    f.close()
    return products

print("1. Display all products")
print("2. Search by Category")
print("3. Update Quantity")
print("4. Costliest Product")
print("5. Category-wise Summary")
print("6. Save Data to File")
print("7. Exit")
def update_quantity(m, pid, new_qty):
        for i in m:
            if [i]["id"]==pid:
                [i]["quantity"]+=new_qty
        return new_qty
    
m=load_data()
while True:   
    c=int(input("Enter the choice from(1-7)"))
    if c==1:
        for i in m:
            print(i["id"],i["name"],i["category"],i["price"],i["quantity"])
    elif c==2:
        b=input("Enter the cat u want to find").lower()
        for j in m:
            if j["category"]==b:
                print(j["id"],j["name"],j["category"],j["price"],j["quantity"])
    elif c==3:
        pid=input("Enter the new id:")
        new_qty=int(input("Enter the new quantity:"))
        update_quantity(m,pid,new_qty)
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
            cat=[i]["catergory"]
            qty=[i]["quantity"]
            if cat in s:
                s[cat]+=qty
            else:
                s[cat]=qty
    elif c==6:
        a=open("products.txt","w")
        for i in m:
            a.write(f"{i["id"],i["name"],i["category"],i["price"],i["quantity"]}")
    elif c==7:
        print("exiting....")
        break
    else:
        print("wrong input")
                
            
        
                

        