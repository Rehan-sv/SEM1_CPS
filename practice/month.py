n=int(input("enter the number of values"))
a=b=c=e=f=0
for i in range (n):
        
    month=int(input("Enter the month(1-12)"))
    if month==3 or month==4:
            print("wheat")
            a+=1
    if month==9  or month== 10:
            print("Rice")  
            b+=1
    if month==10 or month== 11:
            print("soybean")
            c+=1
    if  month==5 or month==6:
            print("watermelon")
            e+=1
    if month ==2 or month==3:
            print("onion")
            f+=1
    if month== 1 or month ==12:
        print("no crops")
print("wheat",a)
print("Rice",b)
print("soybean",c)
print("watermelon",e)
print("onion",f)
        
        
    