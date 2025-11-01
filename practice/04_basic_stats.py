s=int(input("enter number of subjects:"))
a=[]
for i in range(s):
    c=int(input(f"enter the subject marks{i+1}:"))
    list=a.append(c)
    a.sort()
    higest=a[-1]
    lowest=a[0]
    length=len(a)
    total=sum(a)
    avg=total/length

print(f"THE LIST OF MARKS:{a}")
print(f"MAX MARKS:{higest}")
print(f"MIN MARKS:{lowest}")
print("average:",avg)
    