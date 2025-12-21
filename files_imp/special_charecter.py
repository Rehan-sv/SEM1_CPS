s = input("Enter the string: ")
result = ""
for ch in s:
    if ch.isalnum():      # keeps only letters and numbers
        result = result + ch

print(result)
