list=[1,3,2,4,4,3,2]
count=0
a=int(input("enter the number : "))
for x in list:
    if x==a:
        count+=1
print("total :",count)