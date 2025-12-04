def linear_search(list,target):
    for i in range(len(list)):
        if list[i]==target:
            return i
    return -1
list=[5,3,7,2,9,1]
target=7
result=linear_search(list,target)
print(result)
