marks_list = []

def add_marks(marks_list):
    n=int(input("Enter the number of students"))
    for i in range(n):
        mark = int(input("Enter mark (0-100): "))
        marks_list.append(mark)

def display_marks(marks_list):
    if not marks_list:
        print("No marks entered")
    else:
        print("Marks:", marks_list)

def find_max(marks_list):
    print("Highest Mark =", max(marks_list))

def find_min(marks_list):
    print("Lowest Mark =", min(marks_list))

def search(marks_list, value):
    for i in range(len(marks_list)):
        if marks_list[i] == value:
            print("Mark found at index", i)
            return
    print("Mark not found")

def sort_marks(marks_list):
    marks_list.sort(reverse=True)
    print("Sorted marks:", marks_list)

while True:
    print("\n1. Add Student Mark")
    print("2. Display All Marks")
    print("3. Find Highest Mark")
    print("4. Find Lowest Mark")
    print("5. Search for a Mark")
    print("6. Sort Marks")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_marks(marks_list)
    elif choice == 2:
        display_marks(marks_list)
    elif choice == 3:
        find_max(marks_list)
    elif choice == 4:
        find_min(marks_list)
    elif choice == 5:
        value = int(input("Enter mark to search: "))
        search(marks_list, value)
    elif choice == 6:
        sort_marks(marks_list)
    elif choice == 7:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
