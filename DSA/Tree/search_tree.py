class Node:
    def __init__(self, parent, data, leftchild=None, rightchild=None):
        self.parent = parent
        self.data = data
        self.leftchild = leftchild
        self.rightchild = rightchild

    def setleft(self, leftchild):
        self.leftchild = leftchild

    def setright(self, rightchild):
        self.rightchild = rightchild

    def setdata(self, data):
        self.data = data

    def getleft(self):
        return self.leftchild

    def getright(self):
        return self.rightchild

    def getdata(self):
        return self.data

    def getparent(self):
        return self.parent


class BinTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def setroot(self, n):
        self.root = n

    def getroot(self):
        return self.root

    def insert(self, data):

        # Empty tree
        if self.root is None:
            self.root = Node(None, data, None, None)
            self.size += 1
            return

        prev = None
        temp = self.root

        # Find position
        while temp is not None:

            prev = temp

            if temp.getdata() > data:
                temp = temp.getleft()
            else:
                temp = temp.getright()

        # Insert node
        if prev.getdata() > data:
            prev.setleft(Node(prev, data, None, None))
        else:
            prev.setright(Node(prev, data, None, None))

        self.size += 1

    def deletion(self, key):

        # Empty tree
        if self.root is None:
            print("key not found")
            return

        # Search for key
        prev = None
        temp = self.root

        while temp is not None and temp.getdata() != key:

            prev = temp

            if temp.getdata() > key:
                temp = temp.getleft()
            else:
                temp = temp.getright()

        # Key not found
        if temp is None:
            print("key not found")
            return

        # Two children
        if temp.getleft() is not None and temp.getright() is not None:

            succ = temp.getright()
            sprev = temp

            # Find inorder successor
            while succ.getleft() is not None:
                sprev = succ
                succ = succ.getleft()

            # Copy successor's data
            temp.setdata(succ.getdata())

            # Now delete successor
            temp = succ
            prev = sprev

        # 0 or 1 child
        if temp.getleft() is not None:
            child = temp.getleft()
        else:
            child = temp.getright()

        # Deleting root
        if prev is None:
            self.root = child

            if child is not None:
                child.parent = None

        # temp is left child
        elif prev.getleft() == temp:
            prev.setleft(child)

            if child is not None:
                child.parent = prev

        # temp is right child
        else:
            prev.setright(child)

            if child is not None:
                child.parent = prev

        self.size -= 1

    def inorder(self, temp):

        if temp is None:
            return

        self.inorder(temp.getleft())

        print(temp.getdata(), end=" ")

        self.inorder(temp.getright())


# Main
t = BinTree()

t.insert(90)
t.insert(80)
t.insert(70)
t.insert(60)

t.inorder(t.getroot())