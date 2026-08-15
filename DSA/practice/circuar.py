class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Display
    def display(self):
        if self.head is None:
            print("List is Empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Head)")

    # Add at Beginning
    def add_first(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            new.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new.next = self.head
        temp.next = new
        self.head = new

    # Add at End
    def add_last(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            new.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new
        new.next = self.head

    # Add at Kth Position (1-based)
    def add_k(self, pos, data):
        if pos == 1:
            self.add_first(data)
            return

        new = Node(data)
        temp = self.head

        for i in range(pos - 2):
            if temp.next == self.head:
                print("Invalid Position")
                return
            temp = temp.next

        new.next = temp.next
        temp.next = new

    # Remove First
    def remove_first(self):
        if self.head is None:
            print("List is Empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next

    # Remove Last
    def remove_last(self):
        if self.head is None:
            print("List is Empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        prev = None
        temp = self.head

        while temp.next != self.head:
            prev = temp
            temp = temp.next

        prev.next = self.head

    # Remove Kth Position (1-based)
    def remove_k(self, pos):
        if self.head is None:
            print("List is Empty")
            return

        if pos == 1:
            self.remove_first()
            return

        prev = None
        temp = self.head

        for i in range(pos - 1):
            prev = temp
            temp = temp.next

            if temp == self.head:
                print("Invalid Position")
                return

        prev.next = temp.next

    # Reverse Circular Linked List
    def reverse(self):
        if self.head is None or self.head.next == self.head:
            return

        prev = None
        curr = self.head
        nxt = None
        first = self.head

        while True:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

            if curr == first:
                break

        first.next = prev
        self.head = prev


# ---------------- Driver Program ----------------

cll = CircularLinkedList()

cll.add_last(10)
cll.add_last(20)
cll.add_last(30)
cll.display()

cll.add_first(5)
cll.display()

cll.add_k(3, 15)
cll.display()

cll.remove_first()
cll.display()

cll.remove_last()
cll.display()

cll.remove_k(2)
cll.display()

cll.reverse()
cll.display()