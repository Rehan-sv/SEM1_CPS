a=list(map(int, input("Enter elements: ").split()))
n=len(a)
# selection sort
for i in range(n-1):
    m=i
    for j in range(i+1,n):
        if a[j]<a[m]:
            m=j
    a[i],a[m]=a[m],a[i]
# insertion sort
for i in range(1,n):
    key=a[i]
    j=i-1
    while j>=0 and a[j]>key:
        a[j+1]=a[j]
        j-=1
    a[j+1]=key
print(a)
# bubble sort
for i in range(n):
    for j in range(n-i-1):
        if a[j+1]<a[j]:
            a[j+1],a[j]=a[j],a[j+1]
print(a)