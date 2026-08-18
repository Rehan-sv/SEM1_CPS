class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty")
            return

        return self.stack.pop()

    def peek(self):
        if len(self.stack)==0:
            print("Stack is empty")
            return

        return self.stack[-1]

    def display(self):
        print(self.stack)


s=Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Peek:",s.peek())

print("Pop:",s.pop())

s.display()