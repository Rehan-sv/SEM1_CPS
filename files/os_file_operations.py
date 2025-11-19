import os

# Remove Qs_copy if it exists
if os.path.exists("Qs_copy"):
    os.remove("Qs_copy")
    print("File Qs_copy removed")
else:
    print("File Qs_copy doesn't exist")

# List all files in the current directory
print("Files in current directory:")
for file in os.listdir():
    print(file)

# List all files recursively in the current directory
print("Files in current directory recursively:")
for folder, subfolders, files in os.walk("."):
    for file in files:
        print(os.path.join(folder, file))