class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None


    def add_first(self, data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head

    def add_at(self, index, data):
        if index == 0:
            self.add_first(data)
            return
        new_node = CNode(data)
        curr = self.head
        for _ in range(index - 1):
            if curr.next == self.head:
                raise IndexError("Index out of bounds")
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    # --- REMOVE OPERATIONS ---
    def remove_first(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = self.head.next
        self.head = self.head.next

    def remove_last(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        curr = self.head
        while curr.next.next != self.head:
            curr = curr.next
        curr.next = self.head

    def remove_at(self, index):
        if not self.head:
            return
        if index == 0:
            self.remove_first()
            return
        curr = self.head
        for _ in range(index - 1):
            if curr.next == self.head:
                raise IndexError("Index out of bounds")
            curr = curr.next
        if curr.next != self.head:
            curr.next = curr.next.next

    def display(self):
        if not self.head:
            print("None")
            return
        nodes = []
        curr = self.head
        while True:
            nodes.append(str(curr.data))
            curr = curr.next
            if curr == self.head:
                break
        print(" -> ".join(nodes) + " -> (Back to Head)")