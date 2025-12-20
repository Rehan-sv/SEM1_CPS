a={}
n=int(input("enter the no of genre:"))
for i in range(n):
    f={}
    g=input(f"enter the genre {i+1}:")
    f=set(input("enter the formats:").split())
    artist=input("enter the artist:")
    stock=int(input("enter the stocks:"))
    a[g]={"formats":f,"artist":artist,"stock":stock}
print(a)
def high(a):
    k=0
    j=""
    for i in a:
        if a[i]["stock"]>k:
            k=a[i]["stock"]
            j=i
    return j

# def album(a):
#     s=set()
#     for i in a:
#         s|=a[i]["formats"] #|= (union,for not taking the dup from the set)
        
def album(a):
    s = set()
    for i in a:
        for j in a[i]["formats"]:
            s.add(j)
    return s

def men(a,f):
    l=[]
    for i in a:
        if a[i]["formats"] in f:
            l.append(i)
    return l

def gen(a,g):
    if g in a:
        return len(a[g]["formats"])
    else:
        print("the genre is not available")
        
def l(a):
    k=[]
    for i in a:
        if a[i]["stocks"]<500:
            k.append(a[i]["artist"])
    return k

print("the genre with highest stock:",high(a))
print("formats:",album(a))
f=input("enter the format:")
print("genres of",f,":",men(a,f))
g=input("enter the genre:")
print("the no of formats in",g,":",gen(a,g))
print("the artists with less stock:",l(a))