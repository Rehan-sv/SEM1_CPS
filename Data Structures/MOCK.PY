# ============================================================
#   Student Enrollment Tracker - 23CSE101 Lab Evaluation - II
# ============================================================

# a) Function to add a new student
def add_student(names_list, student_tuples, status_dict):
    name = input("Enter student name: ")
    year = int(input("Enter enrollment year: "))

    names_list.append(name)
    student_tuples.append((name, year))
    status_dict[name] = "Active"

    print(f"Student '{name}' added successfully.\n")


# b) Function to update activities
def update_activities(activity_set):
    new_activity = input("Enter activity name: ")

    if new_activity not in activity_set:
        activity_set.add(new_activity)

    print(f"Activity '{new_activity}' added (if unique).\n")
    return activity_set


# c) Function to check membership
def check_membership(status_dict):
    name = input("Enter student name to check: ")

    if name not in status_dict:
        print("Student not found.\n")
        return

    # get the student's status
    status = status_dict[name]

    # count total active members
    count_active = 0
    for val in status_dict.values():
        if val == "Active":
            count_active += 1

    print(f"Status: {status} | Total Active Members: {count_active}\n")


# ----------------------------- MAIN PROGRAM ------------------------------

names = []
students = []
activities = set()
statuses = {}

print("=== Student Enrollment Tracker ===\n")

while True:
    print("--- Menu ---")
    print("1. Add Student")
    print("2. Add Activity")
    print("3. Check Membership")
    print("4. Display All Data")
    print("5. Exit\n")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student(names, students, statuses)

    elif choice == "2":
        activities = update_activities(activities)

    elif choice == "3":
        check_membership(statuses)

    elif choice == "4":
        print("--- Current Data ---")
        print("Names List:", names)
        print("Students (Tuples):", students)
        print("Activities (Set):", activities)
        print("Statuses (Dict):", statuses)
        print()

    elif choice == "5":
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Please try again.\n")
