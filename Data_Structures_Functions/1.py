def find_duplicate (packets):
    feq={}
    for i in packets:
        if i in feq:
            feq[i]+=1
        else:
            feq[i]=1

    dup={}
    for i,count in feq.items():
        if count>1:
            dup[i]= count
    
    return dup
packets = [1001, 1002, 1003, 1002, 1004, 1005, 1001, 1003, 1002]
print(find_duplicate(packets))