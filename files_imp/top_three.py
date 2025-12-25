Sample_data= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
k=0
for i in Sample_data:
    if Sample_data[i]>k:
        k[i]=+1
    print(k)