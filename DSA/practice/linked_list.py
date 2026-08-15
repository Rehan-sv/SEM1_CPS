class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # --- ADD OPERATIONS ---
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def add_at(self, index, data):
        if index == 0:
            self.add_first(data)
            return
        new_node = Node(data)
        curr = self.head
        for _ in range(index - 1):
            if not curr:
                raise IndexError("Index out of bounds")
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    # --- REMOVE OPERATIONS ---
    def remove_first(self):
        if not self.head:
            return
        self.head = self.head.next

    def remove_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None

    def remove_at(self, index):
        if not self.head:
            return
        if index == 0:
            self.remove_first()
            return
        curr = self.head
        for _ in range(index - 1):
            if not curr.next:
                raise IndexError("Index out of bounds")
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
            
    def reverse(self):
        prev = None
        curr = self.head
        
        while curr:
            next_node = curr.next  # Store next node
            curr.next = prev       # Reverse the pointer
            prev = curr            # Move prev forward
            curr = next_node       # Move curr forward
            
        self.head = prev           # Update head to the last node

    def display(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(nodes) + " -> None")
        
        # ==========================================
# DRIVER CODE (Paste this at the bottom of your file)
# ==========================================

if __name__ == "__main__":
    # 1. Initialize the linked list
    my_list = SinglyLinkedList()

    print("--- TESTING ADD OPERATIONS ---")
    my_list.add_last(10)
    my_list.add_last(20)
    my_list.add_last(30)
    print("After adding 10, 20, 30 to the end:")
    my_list.display()

    my_list.add_first(5)
    print("After adding 5 to the first position:")
    my_list.display()

    my_list.add_at(2, 15) 
    print("After adding 15 at index 2:")
    my_list.display()

    print("\n--- TESTING REMOVE OPERATIONS ---")
    my_list.remove_first()
    print("After removing the first node:")
    my_list.display()

    my_list.remove_last()
    print("After removing the last node:")
    my_list.display()

    my_list.remove_at(1) 
    print("After removing the node at index 1:")
    my_list.display()

    print("\n--- TESTING REVERSE OPERATION ---")
    # Adding a couple more nodes to make the reversal obvious
    my_list.add_last(30)
    my_list.add_last(40)
    print("List before reversing:")
    my_list.display()

    my_list.reverse()
    print("List after reversing:")
    my_list.display()