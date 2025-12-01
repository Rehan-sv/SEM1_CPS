#6. "with" statement to open a file - reserves context of file object
with open("Questions","r") as f:
    print(f.read())
    print("File closed? ", f.closed)
# # 'f' isn't available here and not required to close the file
print("File closed? ", f.closed)
f = open("Questions","r")
print(f.read())
print("File closed? ", f.closed)
f.close()
print("File closed? ", f.closed)    