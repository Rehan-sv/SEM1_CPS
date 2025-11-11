# Program 10: Attendance analysis

day1 = {"Rehan", "Sara", "Amit", "Neha"}
day2 = {"Neha", "Amit", "Zara"}

print("Day 1 students:", day1)
print("Day 2 students:", day2)
print()

# Students who attended both days
both_days = day1.intersection(day2)
print("Students who came on both days:", both_days)

# Students who missed one of the days
missed_students = (day1.union(day2)) - (day1.intersection(day2))
print("Students who missed one of the days:", missed_students)

# Check if everyone from day1 also attended day2
if day1.issubset(day2):
    print("All students from Day 1 also came on Day 2.")
else:
    print("Some students from Day 1 did not come on Day 2.")
