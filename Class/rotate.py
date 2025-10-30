list=[1,2,3,4,5,6]
k=int(input("Enter the shifting value"))
for i in range(k):
    x=list.pop(0)
    list.append(x)
print(list)