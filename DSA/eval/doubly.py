class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


class doublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None


    def insertf(self,data):
        new=node(data)

        if self.head is None:
            self.head=self.tail=new
        else:
            new.next=self.head
            self.head.prev=new
            self.head=new


    def insertl(self,data):
        new=node(data)

        if self.head is None:
            self.head=self.tail=new
        else:
            self.tail.next=new
            new.prev=self.tail
            self.tail=new


    def delf(self):
        if self.head is None:
            print("List empty")
            return

        if self.head==self.tail:
            self.head=self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None


    def dell(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head==self.tail:
            self.head=self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None


    def insertp(self,data,index):
        if index==0:
            self.insertf(data)
            return

        temp=self.head

        for _ in range(index-1):
            if temp is None:
                raise IndexError("Out of bound")
            temp=temp.next

        if temp is None:
            raise IndexError("Out of bound")

        new=node(data)

        new.next=temp.next
        new.prev=temp

        if temp.next is not None:
            temp.next.prev=new

        temp.next=new

        if new.next is None:
            self.tail=new


    def delp(self,index):
        if index==0:
            self.delf()
            return

        temp=self.head

        for _ in range(index-1):
            if temp is None:
                raise IndexError("Out of bound")
            temp=temp.next

        if temp is None or temp.next is None:
            raise IndexError("Out of bound")

        if temp.next==self.tail:
            self.dell()
            return

        temp.next=temp.next.next
        temp.next.prev=temp
        
    def reverse(self):
        temp=self.head

        while temp:
            temp.next,temp.prev=temp.prev,temp.next
            temp=temp.prev

        self.head,self.tail=self.tail,self.head


    def display(self):
        temp=self.head

        while temp:
            print(temp.data,end=" <-> ")
            temp=temp.next

        print("None")


l=doublyLinkedList()

l.insertf(20)
l.insertf(30)
l.insertl(40)

l.display()

l.insertp(25,1)
l.display()

l.delp(1)
l.display()

l.delf()
l.display()

l.dell()
l.display()