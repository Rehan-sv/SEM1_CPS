class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Stack:
    def __init__(self):
        self.head=None

    def push(self,data):
        new=node(data)

        new.next=self.head
        self.head=new

    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return

        data=self.head.data
        self.head=self.head.next
        return data

    def peek(self):
        if self.head is None:
            print("Stack is empty")
            return

        return self.head.data

    def display(self):
        temp=self.head

        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next

        print("None")


s=Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Peek:",s.peek())

print("Pop:",s.pop())

s.display()