def group_by_extension(files):
    grouped = {}
    for file in files:
        name, ext = file.split('.')
        grouped.setdefault(ext, []).append(file)
    return grouped

files = ["script.py", "notes.txt", "data.csv", "main.py", "image.png", "list.txt"]
print(group_by_extension(files))
# Expected: {'py': ['script.py', 'main.py'], 'txt': ['notes.txt', 'list.txt'], 'csv': ['data.csv'], 'png': ['image.png']}