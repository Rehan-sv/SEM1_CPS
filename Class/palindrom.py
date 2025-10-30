n=list(eval(input("enter the list element")))
c=len(n)-1
flag=False
for i in range(len(n)):
    if n[i]==n[c]:
        flag=True
    else:
        flag=False
        break
    c-=1
if flag==True:
    print(n,'is palindrome list')