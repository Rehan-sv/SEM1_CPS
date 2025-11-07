def calculator():
    count = 0
    number_of_runs = int(input("Enter the number of runs you want: "))

    while count < number_of_runs:
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        choice = input("Enter your choice (+ or - or * or /): ")

        if choice == "+":
            print("You have chosen ADDITION")
            print("Result:", n1 + n2)
        elif choice == "-":
            print("You have chosen DIFFERENCE")
            print("Result:", n1 - n2)
        elif choice == "*":
            print("You have chosen MULTIPLICATION")
            print("Result:", n1 * n2)
        elif choice == "/":
            print("You have chosen DIVISION")
            if n2 != 0:
                print("Result:", n1 / n2)
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("You have not chosen a valid operator.")
        
        count += 1

    print("Program ends.")


# Call the function
calculator()
