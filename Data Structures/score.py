# Problem 2 - Student Test Grading

# Read the correct answers
answer_key = input("Enter the correct answers: ")

# Read number of students
students = int(input("Enter the number of students: "))

# Create a list to store marks
marks = []

# For each student
for i in range(students):
    student_answers = input(f"Enter the answers of student {i + 1}: ")
    score = 0  # reset score for each student
    
    # Compare each answer one by one
    for j in range(len(answer_key)):
        if student_answers[j] == answer_key[j]:
            score += 1  # add 1 mark if correct
    
    # Store this student's score
    marks.append(score)

# Print all marks
print("Marks:", marks)
    