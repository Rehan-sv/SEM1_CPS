class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


class circularDoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None


    # Insert at first
    def insertf(self,data):
        new=node(data)

        if self.head is None:
            self.head=self.tail=new
            new.next=new
            new.prev=new
        else:
            new.next=self.head
            new.prev=self.tail

            self.head.prev=new
            self.tail.next=new

            self.head=new


    # Insert at last
    def insertl(self,data):
        new=node(data)

        if self.head is None:
            self.head=self.tail=new
            new.next=new
            new.prev=new
        else:
            new.prev=self.tail
            new.next=self.head

            self.tail.next=new
            self.head.prev=new

            self.tail=new


    # Delete at first
    def delf(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head==self.tail:
            self.head=self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=self.tail
            self.tail.next=self.head


    # Delete at last
    def dell(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head==self.tail:
            self.head=self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=self.head
            self.head.prev=self.tail


    # Insert at position
    def insertp(self,data,index):
        if index==0:
            self.insertf(data)
            return

        temp=self.head

        for _ in range(index-1):
            if temp==self.tail:
                raise IndexError("Out of bound")
            temp=temp.next

        new=node(data)

        new.next=temp.next
        new.prev=temp

        temp.next.prev=new
        temp.next=new

        if new.next==self.head:
            self.tail=new


    # Delete at position
    def delp(self,index):
        if self.head is None:
            raise IndexError("Out of bound")

        if index==0:
            self.delf()
            return

        temp=self.head

        for _ in range(index-1):
            if temp==self.tail:
                raise IndexError("Out of bound")
            temp=temp.next

        if temp.next==self.head:
            raise IndexError("Out of bound")

        if temp.next==self.tail:
            self.dell()
            return

        temp.next=temp.next.next
        temp.next.prev=temp


    # Display forward
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp=self.head

        while True:
            print(temp.data,end=" <-> ")
            temp=temp.next

            if temp==self.head:
                break

        print("(head)")


    # Reverse
    def reverse(self):
        if self.head is None or self.head==self.tail:
            return

        temp=self.head

        while True:
            temp.next,temp.prev=temp.prev,temp.next
            temp=temp.prev

            if temp==self.head:
                break

        self.head,self.tail=self.tail,self.head