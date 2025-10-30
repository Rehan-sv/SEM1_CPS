fruit=["appple","banana","cherry","kiwi","mango"]
newlist=[]

for x in fruit:                  #newlist=[x for x in fruits if "a" in x]
    if "a" in x:
        newlist.append(x)
print(newlist)