a = input("Enter the sentence: ")
words = a.split()
k = words[0]
for i in words:
    if len(i) > len(k):
        k = i

print(k)
