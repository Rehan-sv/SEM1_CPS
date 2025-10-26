# Define a function called convert that changes :) to 🙂 and :( to 🙁
def convert(text):
    # Replace all instances of :) with the smiling face emoji
    text = text.replace(":)", "🙂")
    # Replace all instances of :( with the sad face emoji
    text = text.replace(":(", "🙁")
    # Return the new text after replacements
    return text

# Ask the user to type some text
text = input("Enter text: ")

# Call the convert function with the user's text and print the result
print(convert(text))