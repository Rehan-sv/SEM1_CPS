n=int(input("Enter the number"))
flage=True
for i in range(2,n+1):
    if (n%i==0):
        flage=False
        break
    if flage==False:
        print("composite")
    else:
        print("prime")
        break
            
        
