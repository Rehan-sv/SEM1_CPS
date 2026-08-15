class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # ENQUEUE
    def enqueue(self, data):
        new = Node(data)

        if self.rear is None:
            self.front = self.rear = new
            return

        self.rear.next = new
        self.rear = new

    # DEQUEUE
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return temp.data

    # PEEK
    def peek(self):
        if self.front is None:
            print("Queue is Empty")
            return

        return self.front.data

    # DISPLAY
    def display(self):
        if self.front is None:
            print("Queue is Empty")
            return

        temp = self.front

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Example
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Dequeued:", q.dequeue())
print("Front:", q.peek())

q.display()