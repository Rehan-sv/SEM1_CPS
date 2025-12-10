def find_error(data):
    for timestamp, level, msg in data:
        if level == "ERROR":
            return timestamp
    return None


def main():
    while True:
        print("\n----- ENTER THE LOG -----")
        print("1. Enter log entries")
        print("2. Exit")

        choice = int(input("Enter your choice: "))   # ✅ input fixed

        if choice == 1:
            data = []
            n = int(input("Enter the number of log entries: "))  # ✅ input fixed

            for i in range(n):
                print(f"\nEnter log {i+1}")
                timestamp = input("Enter the time: ")
                level = input("Enter the level (INFO/WARN/ERROR): ")
                msg = input("Enter the message: ")

                data.append((timestamp, level, msg))  # ✅ tuple fixed

            result = find_error(data)

            if result is not None:
                print("\n✅ First ERROR at:", result)
            else:
                print("\n✅ No ERROR found")

        elif choice == 2:
            print("EXITING PROGRAM >>>>")
            break

        else:
            print("Invalid choice")


main()
