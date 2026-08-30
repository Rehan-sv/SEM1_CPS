

from collections import deque


class BinaryTree:

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None
        self._size = 0

    # ---------- Basic Accessors ----------

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def root(self):
        return self._root

    def parent(self, node):
        return node._parent

    def left(self, node):
        return node._left

    def right(self, node):
        return node._right

    def sibling(self, node):
        parent = self.parent(node)

        if parent is None:
            return None

        if node is self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, node):
        result = []

        if self.left(node) is not None:
            result.append(self.left(node))

        if self.right(node) is not None:
            result.append(self.right(node))

        return result

    def num_children(self, node):
        count = 0

        if node._left is not None:
            count += 1

        if node._right is not None:
            count += 1

        return count

    def is_root(self, node):
        return self.root() is node

    def is_leaf(self, node):
        return self.num_children(node) == 0

    # ---------- Depth and Height ----------

    def depth(self, node):
        """Number of levels separating node from the root."""

        if self.is_root(node):
            return 0

        return 1 + self.depth(self.parent(node))

    def _height(self, node):
        if self.is_leaf(node):
            return 0

        return 1 + max(self._height(c) for c in self.children(node))

    def height(self, node=None):
        """Height of the subtree rooted at node or whole tree."""

        if node is None:
            node = self.root()

        return self._height(node)

    # ---------- Traversals ----------

    def preorder(self, node=None, result=None):

        if result is None:
            result = []

        if node is None:
            if self.is_empty():
                return result

            node = self.root()

        result.append(node)

        for c in self.children(node):
            self.preorder(c, result)

        return result

    def postorder(self, node=None, result=None):

        if result is None:
            result = []

        if node is None:
            if self.is_empty():
                return result

            node = self.root()

        for c in self.children(node):
            self.postorder(c, result)

        result.append(node)

        return result

    def inorder(self, node=None, result=None):

        if result is None:
            result = []

        if node is None:
            if self.is_empty():
                return result

            node = self.root()

        if self.left(node) is not None:
            self.inorder(self.left(node), result)

        result.append(node)

        if self.right(node) is not None:
            self.inorder(self.right(node), result)

        return result

    # ---------- Breadth First Traversal ----------

    def breadthfirst(self):

        result = []

        if not self.is_empty():

            fringe = deque()
            fringe.append(self.root())

            while fringe:

                node = fringe.popleft()
                result.append(node)

                for c in self.children(node):
                    fringe.append(c)

        return result

    # ---------- Positions / Iterator ----------

    def positions(self):
        return self.inorder()

    def __iter__(self):

        result = []

        for node in self.positions():
            result.append(node._element)

        return iter(result)

    # ---------- Mutators ----------

    def add_root(self, e):

        if self._root is not None:
            raise ValueError("Root exists")

        self._size = 1
        self._root = self._Node(e)

        return self._root

    def add_left(self, node, e):

        if node._left is not None:
            raise ValueError("Left child exists")

        self._size += 1
        node._left = self._Node(e, parent=node)

        return node._left

    def add_right(self, node, e):

        if node._right is not None:
            raise ValueError("Right child exists")

        self._size += 1
        node._right = self._Node(e, parent=node)

        return node._right

    def replace(self, node, e):

        old = node._element
        node._element = e

        return old

    def delete(self, node):

        if self.num_children(node) == 2:
            raise ValueError("node has two children")

        child = node._left if node._left else node._right

        if child is not None:
            child._parent = node._parent

        if node is self._root:
            self._root = child

        else:
            parent = node._parent

            if node is parent._left:
                parent._left = child
            else:
                parent._right = child

        self._size -= 1

        node._parent = node

        return node._element

    def attach(self, node, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of node."""

        if not self.is_leaf(node):
            raise ValueError("node must be a leaf")

        if not type(self) is type(t1) is type(t2):
            raise TypeError("tree types must match")

        self._size += len(t1) + len(t2)

        if not t1.is_empty():

            t1._root._parent = node
            node._left = t1._root

            t1._root = None
            t1._size = 0

        if not t2.is_empty():

            t2._root._parent = node
            node._right = t2._root

            t2._root = None
            t2._size = 0


# ----------------------------------------------------------------------
# Demonstration / Quick Self-Test
# ----------------------------------------------------------------------

if __name__ == '__main__':

    T = BinaryTree()

    root = T.add_root(1)

    left = T.add_left(root, 2)
    right = T.add_right(root, 3)

    T.add_left(left, 4)
    T.add_right(left, 5)

    T.add_left(right, 6)

    print("Preorder :", [n._element for n in T.preorder()])
    print("Inorder  :", [n._element for n in T.inorder()])
    print("Postorder:", [n._element for n in T.postorder()])
    print("BFS      :", [n._element for n in T.breadthfirst()])
    print("Height   :", T.height())
    print("Size     :", len(T))