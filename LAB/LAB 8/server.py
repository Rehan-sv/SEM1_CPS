server_loads = [10 , 5 , 2 , 8]
new_tasks = 5
new=[]
for i in server_loads:
    if i <= new_tasks:
        i=i+1
        new.append(i)
print(new)

