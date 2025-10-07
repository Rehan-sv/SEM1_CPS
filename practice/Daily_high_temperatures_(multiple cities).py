temps = [55,62,68,74,59,45,41,58,60,67,65,78,82,88,91,
         92,90,93,87,80,78,79,72,68,61,59]
hot=0
pleasant=0
cold=0
total=0
count=0
for t in temps:
    total=total+t
    count=count+1
    if t>=85:
        print("It's been a hot day!",t)
        hot=hot+1
    elif t>=60:
        print("It's been a pleasant day!",t)
        pleasant=pleasant+1
    else:
        print("It's been a cold day!",t)
        cold=cold+1
print("Number of hot days:",hot)
print("Number of pleasant days:",pleasant)
print("Number of cold days:",cold)
average =total / count
print("Average temperature:",average) 
        
        
        
