a=int(input("enter the distance travelled:"))
if a<=5:
    c=10
elif a>5 and a<=15:
    c=10+(a-5)*2
elif a>15 and a<=25:
    c=30+(a-15)*3
else:
    c=60+(a-25)*5
b=100
d=b+c
print(d)