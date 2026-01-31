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