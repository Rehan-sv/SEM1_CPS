num=int(input("enter a number : "))
flag= False
for i in range(2,num):
    if(num%i==0):
        flag = True
        break
    if(flag==False):
        print("composite")
        break
    else:
        print("prime")
        