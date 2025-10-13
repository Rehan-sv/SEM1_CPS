# String Functions Demonstration
# Sample string
text = "Hello Python 123"
print("Original String:", text)
print("-" * 40)
# 1. len() – returns length of string
print("1. Length of string:", len(text))
# 2. lower() – converts all characters to lowercase
print("2. Lowercase:", text.lower())
# 3. upper() – converts all characters to uppercase
print("3. Uppercase:", text.upper())
# 4. replace() – replaces a substring with another
print("4. Replace 'Python' with 'World':", text.replace("Python", "World"))
# 5. split() – splits the string into a list
print("5. Split by space:", text.split())
print(" Split by 'o':", text.split("o"))
# 6. find() – returns index of first occurrence (or -1 if not found)
print("6. Find 'Python':", text.find("Python"))
print(" Find 'Java':", text.find("Java"))
# 7. index() – similar to find(), but raises error if not found
print("7. Index of 'Python':", text.index("Python"))
# print(" Index of 'Java':", text.index("Java")) # Uncomment to see error
# 8. isalnum() – True if all characters are alphanumeric (no spaces/symbols)
print("8. Is 'Hello123' alphanumeric?:", "Hello123".isalnum())
print(" Is 'Hello 123' alphanumeric?:", "Hello 123".isalnum())
# 9. isdigit() – True if all characters are digits
print("9. Is '123' all digits?:", "123".isdigit())
print(" Is '123a' all digits?:", "123a".isdigit())
# 10. isnumeric() – True if all characters are numeric (includes unicode digits)
print("10. Is '½' numeric?:", "½".isnumeric())
print(" Is '123' numeric?:", "123".isnumeric())
# 11. islower() – True if all characters are lowercase
print("11. Is 'hello' lowercase?:", "hello".islower())
print(" Is 'Hello' lowercase?:", "Hello".islower())
# 12. isupper() – True if all characters are uppercase
print("12. Is 'HELLO' uppercase?:", "HELLO".isupper())
print(" Is 'Hello' uppercase?:", "Hello".isupper())
print("-" * 40)
print("End of String Function Demo ")