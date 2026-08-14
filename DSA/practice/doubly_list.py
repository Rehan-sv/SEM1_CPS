class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # --- ADD OPERATIONS ---
    def add_first(self, data):
        new_node = DNode(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def add_at(self, index, data):
        if index == 0:
            self.add_first(data)
            return
        new_node = DNode(data)
        curr = self.head
        for _ in range(index - 1):
            if not curr:
                raise IndexError("Index out of bounds")
            curr = curr.next
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node

    # --- REMOVE OPERATIONS ---
    def remove_first(self):
        if not self.head:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def remove_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.prev.next = None

    def remove_at(self, index):
        if not self.head:
            return
        if index == 0:
            self.remove_first()
            return
        curr = self.head
        for _ in range(index):
            if not curr:
                raise IndexError("Index out of bounds")
            curr = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        if curr.prev:
            curr.prev.next = curr.next

    def display(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        print(" <-> ".join(nodes) + (" <-> None" if nodes else "None"))