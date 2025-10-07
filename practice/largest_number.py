largest =0
while True:
    n1=float(input("enter a number : "))
    if n1<=0:
        break
    if n1>largest:
        largest=n1
print("the largest number is :",largest)