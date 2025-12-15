def binary_search(array, target, low, high):
    while low <= high:
        mid = (low + high) // 2

        if target == array[mid]:
            return mid
        elif target < array[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1
# def binary_search(array, target, low,high):
#     while low <= high:
#         mid= (low +high)//2
#         if target==array[mid]:
#             return mid
#         elif target<array[mid]:
#             high=mid-1
#         else:
#             target>array[mid]
#             low=mid+1
#     return -1
# array=[1,2,3,4,5,6,7,8,9]
# target=4
# result=binary_search(array,target,0,9)
# print(result)
