letter=input("enter string:")

print(letter[::-1])

letter_rev=""
for i in letter:
    letter_rev=i +letter_rev
print(letter_rev)    
