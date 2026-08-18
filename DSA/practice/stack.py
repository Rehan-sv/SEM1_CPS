class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
        
    def push(self,data):
        new=node(data)
        if (self.head is None):
            self.head=new
    
    def pop(self):
        if self.head is None:
            print("The list is empty")
            return
        data=self.head.data
        self.head=self.head.next
        return data 
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    