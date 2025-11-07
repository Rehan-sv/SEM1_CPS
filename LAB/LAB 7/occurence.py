Word = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']
# Start with an empty set
set1 = set()
# Dictionary to store frequency
frequency = {}
for i in Word:
    # Add each i to the set of unique words
    set1.add(i)
    # Count frequency
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print("Unique is:", list(set1))
print("Frequency of occurrence:", frequency)