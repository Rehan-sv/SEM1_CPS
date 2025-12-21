a=input("Enter the numbers").split()
l=[]

for i in a:
    l.append(i)

b=input("Enter the numbers").split()
s=set()
for j in b:
    s.add(j)

common_element=[]
def common(l):
    for k in l:
        if k in s:
            common_element.append(k)
    return common_element
print(common(l))
            