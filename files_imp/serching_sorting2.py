books = [
    {"title": "The Hobbit", "author": "Tolkien", "year": 1937},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "Animal Farm", "author": "George Orwell", "year": 1945},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"title": "The Alchemist", "author": "Paulo Coelho", "year": 1988},
]

def swap(lst,i,j):
    temp=lst[i]
    lst[i]=lst[j]
    temp=lst[j]

def sort_titles(books):
    n=len(books)
    for i in range(n):
        for j in range(n-i-1):
            if books[j]["title"].lower()> books[j+1].lower():
                swap(books,j,j+1)
    return books

def sort_author(books):
    n=len(books)
    for i in range (n):
        for j in range(n-i-1):
            if books[j]["author"]>books[j+1]["author"]:
                swap(books,j,j+1)
    return books

def sort_by_year(books):
    n = len(books)
    for i in range(n):
        for j in range(n - i - 1):
            if books[j]["year"] > books[j+1]["year"]:
                swap(books, j, j + 1)
    return books

author_name=input("Enter the name of the author: ")
def search_by_author(books, author_name):
    results = []
    for b in books:
        if b["author"].lower() == author_name.lower():
            results.append(b["title"])
    return results
print(search_by_author(books,author_name))

query=input("Enter the title u want to find: ")
def search_book(books,query):
    titles=[]
    for i in range(len(books)):
        if query.lower() in books[i]["title"].lower():
            titles.append(books[i]["title"])  
        return titles
print(search_book(books,query))

def earliest_book(books):
    min_book = books[0]   
    for i in range(len(books)):
        if books[i]["year"] < min_book["year"]:
            min_book = books[i]    
    return min_book




            