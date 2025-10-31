a = input("Enter the string: ")
reverse = ""
for i in a:              # loop through each character in the string
    reverse = i + reverse  # add each character to the front of 'reverse'
print("The reverse =", reverse)