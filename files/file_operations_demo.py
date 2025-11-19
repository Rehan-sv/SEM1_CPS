# 1. Read the entire content of the file "Questions" and print it
# f = open("Questions","r")
# print(f.read())
# f.close()

# 2. Read the first 10 characters of the file "Questions" and print them
# f = open("Questions","r")
# print(f.read(10))
# f.close()

# 3. Read the entire content of the file "Questions" and write it to a new file "Qs_copy"
# f = open("Questions","r")
# q = open("Qs_copy","w")
# q.write(f.read())
# f.close()
# q.close()

# 4. Demonstrate of 'w' mode overwriting contents of a file
# f = open("Qs_copy","r")
# print("Before write open" , f.read())
# f.close()
# f = open("Qs_copy","w")
# f.close()
# f = open("Qs_copy","r")
# print("After write open", f.read())

# 5. Demonstrate of 'a' mode appending contents to a file
# f = open("Qs_copy","r")
# print("Before append open" , f.read())
# f.close()
# f = open("Qs_copy","a")
# f.write("This is a new line")
# f.close()
# f = open("Qs_copy","r")
# print("After append open", f.read())

#6. "with" statement to open a file - reserves context of file object
# with open("Questions","r") as f:
#     print(f.read())
#     print("File closed? ", f.closed)
# # 'f' isn't available here and not required to close the file
# print("File closed? ", f.closed)
# f = open("Questions","r")
# print(f.read())
# print("File closed? ", f.closed)
# f.close()
# print("File closed? ", f.closed)

# 7. Count number of lines in a file
with open("Questions","r") as f:
    count = 0
    for line in f:
        count += 1
print("Number of lines in file: ", count)

# 8. Count the number of questions in the file
with open("Questions","r") as f:
    count = 0
    for line in f:
        if line.startswith("Q."):
            count += 1
print("Number of questions in file: ", count)

# Remove empty lines from the file
with open("Questions","r") as f:
    lines = f.readlines()
with open("Qs_clean","w") as f:
    for line in lines:
        if line.strip(): # if line is not empty
            f.write(line)