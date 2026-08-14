class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
            
    def addathead(self,data):
        new_node = Node(data)
        current = self.head
        new_node.next = self.head
        self.head = new_node
        return new_node
    
    def addatlast(self,data):
        new_node = Node(data)
        Current = self.head
        while Current.next is not None:
            Current = Current.next
        Current.next = new_node
        
    def addatposition(self,data,postion):
        new_node = Node(data)
        count = 0
        Current = self.head
        while Current is not None:
            if postion == 0:
                new_node.next = self.head
                self.head = new_node
                return new_node
            elif count == postion - 1:
                new_node.next = Current.next.next
                Current.next = new_node
                return
            else:
                Current = Current.next
                count+=1
                
                
    def deleteatposition(self,position):
        count = 0
        Current = self.head
        while Current is not None:
            if position == 0:
                self.head = self.head.next
                return
            elif count == position - 1:
                Current.next= Current.next.next
                return
            else:
                Current = Current.next
                count+=1
                
    def removeHead(self):
        self.head = self.head.next  

    def removeLast(self):
        current = self.head
        prev = None
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None

    def revere(self):
        current = self.head
        prev = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
    def search(self,value):
        current = self.head
        pos = 0
        while current.next is not None:
            if current.data == value:
                print("found at position",pos)
                break
            else:
                current = current.next
                pos+=1
        else:
            print("not found")
            
Linked_List = LinkedList()
Linked_List.insert(1)
Linked_List.insert(3)
Linked_List.insert(4)
Linked_List.insert(6)
Linked_List.addatlast(10)
head = Linked_List.addathead(9)
Linked_List.addatposition(19,1)
Linked_List.deleteatposition(1)
Linked_List.removeHead()
Linked_List.removeLast()
Linked_List.revere()
Linked_List.search(19)
Linked_List.display()