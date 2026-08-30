# ==========================================
# NODE / PAGE CLASS
# ==========================================

class Node:

    def __init__(self, pageId, timeStamp, URL, pageTitle):

        self.pageId = pageId
        self.timeStamp = timeStamp
        self.URL = URL
        self.pageTitle = pageTitle

        self.prev = None
        self.next = None


# ==========================================
# BROWSER CLASS
# ==========================================

class Browser:

    def __init__(self, pageId, timeStamp, URL, pageTitle):

        self.pageId = pageId
        self.timeStamp = timeStamp
        self.URL = URL
        self.pageTitle = pageTitle


# ==========================================
# TRAVERSAL CLASS
# ==========================================

class Traversal:

    def __init__(self, startNode):

        self.current = startNode

    def forward(self):

        if self.current is None:

            print("No history to move forward.")
            return

        if self.current.prev is None:

            print(
                "Already at the most recent page:",
                self.current.pageTitle
            )

        else:

            self.current = self.current.prev

            print(
                "Forward ->",
                self.current.pageId,
                self.current.pageTitle
            )

    def backward(self):

        if self.current is None:

            print("No history to move backward.")
            return

        if self.current.next is None:

            print(
                "Already at the oldest page:",
                self.current.pageTitle
            )

        else:

            self.current = self.current.next

            print(
                "Backward ->",
                self.current.pageId,
                self.current.pageTitle
            )


# ==========================================
# WEB MANAGEMENT / DOUBLY LINKED LIST
# ==========================================

class WebManagement:

    def __init__(self):

        self.head = None
        self.tail = None
        self.size = 0


    # ======================================
    # GET HEAD
    # ======================================

    def getHead(self):

        return self.head


    # ======================================
    # INSERT AT FRONT
    # ======================================

    def insert_f(self, pageId, timeStamp, URL, pageTitle):

        newNode = Node(
            pageId,
            timeStamp,
            URL,
            pageTitle
        )

        if self.head is None:

            self.head = newNode
            self.tail = newNode

        else:

            newNode.next = self.head
            self.head.prev = newNode

            self.head = newNode

        self.size += 1

        print(
            "New Node has been added:",
            pageTitle
        )


    # ======================================
    # INSERT AT END
    # ======================================

    def insert_end(self, pageId, timeStamp, URL, pageTitle):

        newNode = Node(
            pageId,
            timeStamp,
            URL,
            pageTitle
        )

        if self.head is None:

            self.head = newNode
            self.tail = newNode

        else:

            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

        self.size += 1


    # ======================================
    # REMOVE BY PAGE ID
    # ======================================

    def remove_by_Id(self, Id):

        temp = self.head

        # Search for the node

        while temp is not None and temp.pageId != Id:

            temp = temp.next

        # Not found

        if temp is None:

            print("Not found")
            return

        # Remove from left side

        if temp.prev is not None:

            temp.prev.next = temp.next

        else:

            self.head = temp.next

        # Remove from right side

        if temp.next is not None:

            temp.next.prev = temp.prev

        else:

            self.tail = temp.prev

        self.size -= 1

        print(
            Id,
            "has been removed"
        )


    # ======================================
    # DELETE AT POSITION
    # ======================================

    def delete(self, k):

        if k < 1 or k > self.size:

            print("Invalid position")
            return

        temp = self.head

        # Move to kth node

        for i in range(1, k):

            temp = temp.next

        # Connect previous node

        if temp.prev is not None:

            temp.prev.next = temp.next

        else:

            self.head = temp.next

        # Connect next node

        if temp.next is not None:

            temp.next.prev = temp.prev

        else:

            self.tail = temp.prev

        self.size -= 1

        print(
            "Deleted node at position",
            k
        )


    # ======================================
    # SEARCH BY URL
    # ======================================

    def search(self, URL):

        temp = self.head

        k = 0

        found = False

        while temp is not None:

            if temp.URL == URL:

                print(
                    URL,
                    "found at position",
                    k
                )

                found = True
                break

            temp = temp.next

            k += 1

        if not found:

            print("Not found")


    # ======================================
    # DISPLAY
    # ======================================

    def display(self):

        temp = self.head

        while temp is not None:

            print(
                temp.pageId,
                "   ",
                temp.pageTitle,
                "   ",
                temp.URL,
                "   ",
                temp.timeStamp
            )

            temp = temp.next


    # ======================================
    # REVERSE DOUBLY LINKED LIST
    # ======================================

    def rev(self):

        temp = self.head

        swap = None

        while temp is not None:

            swap = temp.prev

            temp.prev = temp.next

            temp.next = swap

            temp = temp.prev

        swap = self.head

        self.head = self.tail

        self.tail = swap

        print("List reversed")


    # ======================================
    # DUPLICATE ENTIRE HISTORY
    # ======================================

    def duplicate(self):

        newList = WebManagement()

        temp = self.head

        while temp is not None:

            newList.insert_end(
                temp.pageId,
                temp.timeStamp,
                temp.URL,
                temp.pageTitle
            )

            temp = temp.next

        return newList


    # ======================================
    # DELETE FROM POSITION TO END
    # ======================================

    def del_from_k(self, pos):

        if pos < 1 or pos > self.size:

            print("Invalid position")
            return

        temp = self.head

        # Move to required position

        for i in range(1, pos):

            temp = temp.next

        # If there are nodes before temp

        if temp.prev is not None:

            temp.prev.next = None

            self.tail = temp.prev

        else:

            # Delete entire list

            self.head = None
            self.tail = None

        temp.prev = None

        self.size = pos - 1

        print(
            "Deleted all nodes from position",
            pos,
            "onward"
        )


# ==========================================
# REGISTER FUNCTION
# ==========================================

def register(wm, pageId, timeStamp, URL, pageTitle):

    wm.insert_f(
        pageId,
        timeStamp,
        URL,
        pageTitle
    )


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    history = WebManagement()

    nav = Traversal(
        history.getHead()
    )

    choice = -1

    while choice != 0:

        print("\n================================")
        print("       BROWSER HISTORY")
        print("================================")

        print("1. Insert new page")
        print("2. Remove page by ID")
        print("3. Delete page at position")
        print("4. Search page by URL")
        print("5. Display history")
        print("6. Reverse history")
        print("7. Duplicate history")
        print("8. Delete from position to end")
        print("9. Move forward")
        print("10. Move backward")
        print("0. Exit")

        print("================================")

        choice = int(
            input("Enter choice: ")
        )


        # ======================================
        # INSERT
        # ======================================

        if choice == 1:

            pageId = int(
                input("Enter Page ID: ")
            )

            timeStamp = int(
                input("Enter Timestamp: ")
            )

            URL = input(
                "Enter URL: "
            )

            pageTitle = input(
                "Enter Page Title: "
            )

            register(
                history,
                pageId,
                timeStamp,
                URL,
                pageTitle
            )

            nav.current = history.getHead()


        # ======================================
        # REMOVE BY ID
        # ======================================

        elif choice == 2:

            Id = int(
                input("Enter Page ID to remove: ")
            )

            history.remove_by_Id(Id)


        # ======================================
        # DELETE AT POSITION
        # ======================================

        elif choice == 3:

            pos = int(
                input("Enter position to delete: ")
            )

            history.delete(pos)


        # ======================================
        # SEARCH
        # ======================================

        elif choice == 4:

            URL = input(
                "Enter URL to search: "
            )

            history.search(URL)


        # ======================================
        # DISPLAY
        # ======================================

        elif choice == 5:

            history.display()


        # ======================================
        # REVERSE
        # ======================================

        elif choice == 6:

            history.rev()


        # ======================================
        # DUPLICATE
        # ======================================

        elif choice == 7:

            copy = history.duplicate()

            print("\nDuplicated history:")

            copy.display()


        # ======================================
        # DELETE FROM POSITION
        # ======================================

        elif choice == 8:

            pos = int(
                input("Enter position to delete from: ")
            )

            history.del_from_k(pos)


        # ======================================
        # FORWARD
        # ======================================

        elif choice == 9:

            nav.forward()


        # ======================================
        # BACKWARD
        # ======================================

        elif choice == 10:

            nav.backward()


        # ======================================
        # EXIT
        # ======================================

        elif choice == 0:

            print(
                "Exiting Browser History Manager."
            )


        else:

            print(
                "Invalid choice, try again."
            )


# ==========================================
# RUN PROGRAM
# ==========================================

main()