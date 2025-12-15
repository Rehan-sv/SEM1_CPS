products = []
c=int(input("enter the no of components:"))
for i in range(c):
    d={}
    id=int(input("enter the id:"))
    d["id"]=id
    name=input("enter the name:")
    d["name"]=name
    price=int(input("enter the price:"))
    d["price"]=price
    stock=int(input("enter the stock:"))
    d["stock"]=stock
    products.append(d)
print(products)
def sort_price(p):
    n=len(p)
    for i in range(n):
        for j in range(n-i-1):
            if p[j]["price"]>p[j+1]["price"]:
                p[j],p[j+1]=p[j+1],p[j]
    for i in p:
        print(i)
def sort_stock(p):
    n=len(p)
    for i in range(n):
        for j in range(n-i-1):
            if p[j]["stock"]<p[j+1]["stock"]:
                p[j],p[j+1]=p[j+1],p[j]
    return p
def sort_name(p):
    n=len(p)
    for i in range(n):
        for j in range(n-i-1):
            if p[j]["name"].lower()>p[j+1]["name"].lower():
                p[j],p[j+1]=p[j+1],p[j]
    return p
p_id=int(input("enter the product id:"))
def id(p,p_id,l,h):
    while l<= h:
        mid=(l + h) // 2
        if p_id == p[mid]["id"]:
            return p[mid]
        elif p_id <p[mid]["id"]:
            h= mid - 1
        else:
            l= mid + 1
    return -1
print(id(products,p_id,0,len(products)-1))
name=input("enter the name:")
def sort(p,name):
    for i in range(len(p)):
        if p[i]["name"].lower()==name.lower():
            return p[i]
l=int(input("enter the minimum range:"))
h=int(input("enter the highest range:"))
def pro(p,l,h):
    a=[]
    for i in p:
        if i["price"]>=l and i["price"]<=h:
            a.append(i)
    return a
print(pro(products,l,h))