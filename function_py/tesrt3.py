def r(l):
    t=input("enter the book to return:")
    if t in l:
        if l[t]['available']:
            available=True
            print("the book returned successfully")
        else:
            print("the book is already returned")
    else