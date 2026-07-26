class Node:
    def __init__(self, pnr, name, timestamp):
        self.pnr = pnr
        self.name = name
        self.timestamp = timestamp
        self.next = None


class Waitlist:

    def __init__(self):
        self.head = None

    # Add Passenger
    def addPassenger(self, pnr, name, timestamp):
        new_node = Node(pnr, name, timestamp)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Cancel Passenger
    def cancelPassenger(self, pnr):

        if self.head is None:
            print("Waitlist Empty")
            return

        if self.head.pnr == pnr:
            self.head = self.head.next
            print("Passenger Cancelled")
            return

        prev = self.head
        curr = self.head.next

        while curr:

            if curr.pnr == pnr:
                prev.next = curr.next
                print("Passenger Cancelled")
                return

            prev = curr
            curr = curr.next

        print("Passenger Not Found")

    # Find Passenger
    def findPassenger(self, pnr):

        temp = self.head
        pos = 1

        while temp:

            if temp.pnr == pnr:
                print("Position :", pos)
                return

            temp = temp.next
            pos += 1

        print("Not Found")

    # Confirm Next Passenger
    def confirmNext(self):

        if self.head is None:
            print("Waitlist Empty")
            return

        print("Confirmed Passenger")
        print("PNR :", self.head.pnr)
        print("Name:", self.head.name)

        self.head = self.head.next

    def reorderByTimestamp(self):

        if self.head is None:
            return

        current = self.head

        while current:

            smallest = current
            temp = current.next

            while temp:

                if temp.timestamp < smallest.timestamp:
                    smallest = temp

                temp = temp.next

            current.pnr, smallest.pnr = smallest.pnr, current.pnr
            current.name, smallest.name = smallest.name, current.name
            current.timestamp, smallest.timestamp = smallest.timestamp, current.timestamp

            current = current.next

        print("Waitlist Reordered")

    # Display List
    def display(self):

        if self.head is None:
            print("Waitlist Empty")
            return

        temp = self.head

        print("\nWaitlist")

        while temp:

            print(temp.pnr, temp.name, temp.timestamp, end=" -> ")

            temp = temp.next

        print("None")


# ---------------- Driver Code ----------------

wl = Waitlist()

while True:

    print("\n----- MENU -----")
    print("1. Add Passenger")
    print("2. Cancel Passenger")
    print("3. Find Passenger")
    print("4. Confirm Next")
    print("5. Reorder By Timestamp")
    print("6. Display")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pnr = int(input("Enter PNR: "))
        name = input("Enter Name: ")
        timestamp = int(input("Enter Timestamp: "))
        wl.addPassenger(pnr, name, timestamp)

    elif choice == 2:
        pnr = int(input("Enter PNR to Cancel: "))
        wl.cancelPassenger(pnr)

    elif choice == 3:
        pnr = int(input("Enter PNR to Find: "))
        wl.findPassenger(pnr)

    elif choice == 4:
        wl.confirmNext()

    elif choice == 5:
        wl.reorderByTimestamp()

    elif choice == 6:
        wl.display()

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")