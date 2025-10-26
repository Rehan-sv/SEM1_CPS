num=1
n=int(input("ENter the number "))
for i in range (n+1):
    for j in range(i):
         print((i+j)%2,end=" ")
         num+=1
    print()                        