operator = input("Enter the operator (+, -, *, /): ")
n1 = float(input("Enter first number: "))
n2 = float(input("Enter the second number: "))

if operator == "+":
    print("Addition:", n1 + n2)
elif operator == "-":
    print("Subtraction:", n1 - n2)
elif operator == "*":
    print("Multiplication:", n1 * n2)
elif operator == "/":
    print("Division:", n1 / n2)
else:
    print("Invalid operator!")
