class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class singleLinkedlist:
    def __init__(self):
        self.head=None

    def insertf(self,data):
        new=node(data)
        new.next=self.head
        self.head=new

    def insertl(self,data):
        new=node(data)

        if self.head is None:
            self.head=new
            return

        temp=self.head

        while temp.next:
            temp=temp.next

        temp.next=new

    def delf(self):
        if self.head is None:
            return

        self.head=self.head.next

    def dell(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head=None
            return

        temp=self.head

        while temp.next.next:
            temp=temp.next

        temp.next=None

    def insertpos(self,index,data):
        if index==0:
            self.insertf(data)
            return

        temp=self.head

        for _ in range(index-1):
            if temp is None:
                raise IndexError("out of bound")
            temp=temp.next

        if temp is None:
            raise IndexError("out of bound")

        new=node(data)
        new.next=temp.next
        temp.next=new

    def delpos(self,index):
        if index==0:
            self.delf()
            return

        temp=self.head

        for _ in range(index-1):
            if temp is None:
                raise IndexError("out of bound")
            temp=temp.next

        if temp is None or temp.next is None:
            raise IndexError("out of bound")

        temp.next=temp.next.next
    
    

    def display(self):
        temp=self.head

        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next

        print("None")


l=singleLinkedlist()

l.insertf(20)
l.insertf(30)
l.insertl(40)

l.display()

l.insertpos(1,25)
l.display()

l.delpos(1)
l.display()

l.delf()
l.display()

l.dell()
l.display()