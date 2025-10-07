r1=float(input("enter the firsst resistance : "))
r2=float(input("enter the second resistance : "))
r3=float(input("enter the third resistance : "))
v=float(input("enter the voltage : "))
req=1/((1/r1+1/r2+1/r3))
print("the total resistance is : ",req)
I=v/req
print("the total current is : ",I)
