def largest(x, y):
    if x > y:
        return x
    else:
        return y

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Largest number is:", largest(x, y))
