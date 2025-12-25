l={}
n=int(input("enter the no of books:"))
for i in range(n):
    book=input("enter the book:")
    author=input("enter the author name:")
    s=input("enter the book status(yes/no):")
    if s.lower()=="yes":
        available=True
    elif s.lower()=="no":
        available=False
    else:
        print("invalid status")
    l[book]={"author":author,"available":available}
print(l)
def add(l):
    book=input("enter the book:")
    author=input("enter the author name:")
    available=True
    l[book]={"author":author,"available":available}
def borrow(l):
    t=input("enter the book to borrow:")
    if t in l:
        if l[t]['available']:
            available=False
            print("the book borrowed successfully")
        else:
            print("the book is already borrowed")
    else:
        print("the book is not in the library")
def r(l):
    t=input("enter the book to return:")
    if t in l:
        if l[t]['available']:
            available=True
            print("the book returned successfully")
        else:
            print("the book is already returned")
    else:
        print("the book is not in the library")
def available(l):
    for i in l:
        if l[i]["available"]:
            print(i,"-",l[i]["author"])
add(l)
borrow(l)
r(l)
available(l)