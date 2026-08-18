class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Queue:
    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self,data):
        new=node(data)

        if self.head is None:
            self.head=self.tail=new
            return

        self.tail.next=new
        self.tail=new

    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
            return

        data=self.head.data
        self.head=self.head.next

        if self.head is None:
            self.tail=None

        return data

    def display(self):
        temp=self.head

        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next

        print("None")


q=Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Dequeue:",q.dequeue())

q.display()