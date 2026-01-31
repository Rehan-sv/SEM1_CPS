ingredient=[]
low_stock_list=[]
supplier=set()
def add_ingredient(inv,lst,igd):
    d={}
    lstd={}
    d['Low Stock List'] = lst
    d['Ingredient Detail'] = igd
    inv.append(d)
    if igd[3] < 10:
        lstd[igd[0]] = igd[3]
    lst.append(lstd)
    return inv,lst

def update_stock(inv,lst,id,nst):
    for i in lst:
        for j in i:
            if j == id:
                i.pop(id)
                break
    for i in inv:
        for j in i:
            if j == 'Ingredient Detail':
                if i[j][0] == id:
                    i[j][3] = nst

    return inv,lst
    
def check_supplier_status(sup, inv, id):
    for i in inv:
        if i['Ingredient Detail'][0] == id:
            if i['Ingredient Detail'][2] in sup:
                print('Supplier is present')
            else:
                print('Supplier not found')



while True:
    print('''1) add ingredient
          2)update stock
          3)supplier status
          4)exit''')
    ch=int(input('Enter your choice:'))
    if ch == 1:
        inv=[]
        id=int(input('Enter the product id:'))
        nam=input('Enter the name of the product:')
        sup = input('Enter the name of supplier:')
        st=int(input('Enter the stock:'))
        supplier.add(sup)
        pri=float(input('Enter the price:'))
        inv=[id,nam,sup,st,pri]
        add_ingredient(ingredient,low_stock_list,inv)

    elif ch == 2:
        id=int(input('Enter the stock update id:'))
        st=int(input('Enter update stock value:'))
        update_stock(ingredient,low_stock_list,id,st)
    elif ch == 3:
        id= int(input('Enter the id:'))
        check_supplier_status(supplier,ingredient,id)

    elif ch == 4:
        break