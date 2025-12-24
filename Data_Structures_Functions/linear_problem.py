n=int(input("Enter the number of books: "))
search=int(input("Enter which Id need to be searched? :"))
a=[]
for i in range(n):
    books_ID=int(input("Enter the books IDS: "))
    a.append(books_ID)
    
for i in range(n):
    if a[i]==search:
        print(i+1)