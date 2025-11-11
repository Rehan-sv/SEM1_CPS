# Program 15: Forbidden Character Check (using if loop)

forbidden_chars = {' ', '!', '@', '#', '$'}
password = "hello@123"

invalid = set()  # to store any invalid characters found

# check each letter in the password
for ch in password:
    if ch in forbidden_chars:
        invalid.add(ch)  # add that character to invalid set

# print result
if invalid:
    print("Invalid characters found in password:", invalid)
else:
    print("Password is clean. No forbidden characters.")
