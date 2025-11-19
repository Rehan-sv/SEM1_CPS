def build_gradebook(grade_entries):
    gradebook = {}
    for entry in grade_entries:
        name, score = entry['name'], entry['score']
        gradebook.setdefault(name, []).append(score)
    return gradebook

entries = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 90},
    {'name': 'Alice', 'score': 92},
    {'name': 'Charlie', 'score': 78},
    {'name': 'Bob', 'score': 88},
    {'name': 'Alice', 'score': 81}
]
print(build_gradebook(entries))
# Expected: {'Alice': [85, 92, 81], 'Bob': [90, 88], 'Charlie': [78]}