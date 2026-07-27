class Coach:
    def __init__(self, number, ctype, capacity, vacant):
        self.number = number
        self.ctype = ctype
        self.capacity = capacity
        self.vacant = vacant
        self.next = None


class Train:
    def __init__(self):
        self.head = None

    # Check duplicate coach number
    def duplicate(self, number):
        temp = self.head
        while temp:
            if temp.number == number:
                return True
            temp = temp.next
        return False    

    # Attach coach at rear
    def attach_rear(self):
        number = input("Coach Number: ")

        if self.duplicate(number):
            print("Duplicate Coach Number!")
            return

        ctype = input("Coach Type: ")
        capacity = int(input("Seating Capacity: "))
        vacant = int(input("Vacant Berths: "))

        new = Coach(number, ctype, capacity, vacant)

        if self.head is None:
            self.head = new
            print("Coach Attached.")
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new
        print("Coach Attached.")

    # Detach front coach
    def detach_front(self):
        if self.head is None:
            print("Train is Empty.")
            return

        print("Detached Coach:", self.head.number)
        self.head = self.head.next

    # Insert coach at position
    def insert_position(self):
        pos = int(input("Position: "))

        number = input("Coach Number: ")

        if self.duplicate(number):
            print("Duplicate Coach Number!")
            return

        ctype = input("Coach Type: ")
        capacity = int(input("Capacity: "))
        vacant = int(input("Vacant Berths: "))

        new = Coach(number, ctype, capacity, vacant)

        if pos == 1:
            new.next = self.head
            self.head = new
            print("Inserted.")
            return

        temp = self.head
        count = 1

        while temp and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid Position.")
            return

        new.next = temp.next
        temp.next = new

        print("Inserted.")

    # Delete coach by number
    def delete_coach(self):
        if self.head is None:
            print("Train Empty.")
            return

        num = input("Coach Number to delete: ")

        if self.head.number == num:
            self.head = self.head.next
            print("Deleted.")
            return

        prev = self.head
        curr = self.head.next

        while curr:
            if curr.number == num:
                prev.next = curr.next
                print("Deleted.")
                return

            prev = curr
            curr = curr.next

        print("Coach Not Found.")

    # Display train
    def display(self):
        if self.head is None:
            print("Train Empty.")
            return

        temp = self.head
        pos = 1

        while temp:
            print("--------------------------------")
            print("Position :", pos)
            print("Coach No :", temp.number)
            print("Type     :", temp.ctype)
            print("Capacity :", temp.capacity)
            print("Vacant   :", temp.vacant)

            temp = temp.next
            pos += 1

    # Count coaches
    def count(self):
        cnt = 0
        temp = self.head

        while temp:
            cnt += 1
            temp = temp.next

        print("Total Coaches =", cnt)

    # Reverse train
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev

        print("Train Reversed.")

    # Search coach
    def search(self):
        num = input("Enter Coach Number: ")

        temp = self.head
        pos = 1

        while temp:
            if temp.number == num:
                print("Coach Found")
                print("Position :", pos)
                print("Type :", temp.ctype)
                print("Capacity :", temp.capacity)
                print("Vacant :", temp.vacant)
                return

            temp = temp.next
            pos += 1

        print("Coach Not Found.")


train = Train()

while True:

    print("\n===== TRAIN COACH MANAGEMENT =====")
    print("1. Attach Coach at Rear")
    print("2. Detach Coach from Front")
    print("3. Insert Coach at Position")
    print("4. Delete Coach by Number")
    print("5. Display Train")
    print("6. Count Coaches")
    print("7. Reverse Train")
    print("8. Search Coach")
    print("9. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        train.attach_rear()

    elif ch == 2:
        train.detach_front()

    elif ch == 3:
        train.insert_position()

    elif ch == 4:
        train.delete_coach()

    elif ch == 5:
        train.display()

    elif ch == 6:
        train.count()

    elif ch == 7:
        train.reverse()

    elif ch == 8:
        train.search()

    elif ch == 9:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")