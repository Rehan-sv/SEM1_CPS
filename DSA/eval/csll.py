class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class circularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None


    # Insert at first
    def insertf(self,data):
        new=node(data)

        if self.head is None:
            self.head=self.tail=new
            new.next=self.head
        else:
            new.next=self.head
            self.head=new
            self.tail.next=self.head


    # Insert at last
    def insertl(self,data):
        new=node(data)

        if self.head is None:
            self.head=self.tail=new
            new.next=self.head
        else:
            new.next=self.head
            self.tail.next=new
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
            self.tail.next=self.head


    # Delete at last
    def dell(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head==self.tail:
            self.head=self.tail=None
            return

        temp=self.head

        while temp.next!=self.tail:
            temp=temp.next

        temp.next=self.head
        self.tail=temp


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

        if temp==self.tail:
            if index > 1:
                raise IndexError("Out of bound")

        new=node(data)

        new.next=temp.next
        temp.next=new

        if temp==self.tail:
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


    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp=self.head

        while True:
            print(temp.data,end=" -> ")
            temp=temp.next

            if temp==self.head:
                break

        print("(head)")


    # Reverse
    def reverse(self):
        if self.head is None or self.head==self.tail:
            return

        prev=self.tail
        temp=self.head

        while True:
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next

            if temp==self.head:
                break

        self.head,self.tail=self.tail,self.head
        
l=circularLinkedList()

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