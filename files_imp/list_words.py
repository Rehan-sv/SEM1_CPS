words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green'] 
f={}
for i in words:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)