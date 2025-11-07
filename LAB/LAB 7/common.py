set1={1, 2, 3, 4}
set2={4, 5, 6, 7}
set3={8}
a=set1.intersection(set2)
b=set2.intersection(set3)
c=set1.intersection(set3)
print("Compare set1 and set2:", len(a) == 0)
print("Compare set2 and set3:", len(b) == 0)
print("Compare set1 and set3:", len(c) == 0)