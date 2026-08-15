class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # PUSH
    def push(self, data):
        new = Node(data)

        new.next = self.top
        self.top = new

    # POP
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return

        temp = self.top
        self.top = self.top.next

        return temp.data

    # PEEK
    def peek(self):
        if self.top is None:
            print("Stack is Empty")
            return

        return self.top.data

    # DISPLAY
    def display(self):
        if self.top is None:
            print("Stack is Empty")
            return

        temp = self.top

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Example
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Popped:", s.pop())
print("Top:", s.peek())

s.display()