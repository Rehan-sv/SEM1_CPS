def build_gradebook(entries):
    gradebook = {}

    for entry in entries:
        name = entry["name"]
        score = entry["score"]

        if name in gradebook:
            gradebook[name].append(score)
        else:
            gradebook[name] = [score]

    return gradebook


def main():
    while True:
        print("\n====== GRADEBOOK MENU ======")
        print("1. Enter student grades")
        print("2. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            entries = []

            n = int(input("Enter number of grade entries: "))

            for i in range(n):
                print(f"\nEnter details for entry {i+1}")
                name = input("Enter student name: ")
                score = int(input("Enter score: "))

                entries.append({
                    "name": name,
                    "score": score
                })

            result = build_gradebook(entries)

            print("\n✅ Final Gradebook:")
            print(result)

        elif choice == 2:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")


main()
