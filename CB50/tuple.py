t=(2,3,4,5,6)
print('tuple before adding new element')
print(t)
l=list(t)
l.append(int(input('enter the new element: ')))
t=tuple(l)
print('tuple after adding new element')
print(t)
#tuple is immutable