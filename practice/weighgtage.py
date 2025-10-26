n = int(input("Enter the number of students:(end=0) "))

for i in range(n):
    print(f"student {i+1}: ")
    total_weighted = 0
    for j in range(6):
        mark = int(input(f"Enter grade for exam {j + 1}: "))
        if j < 4:           # first 4 exams = 15%
            weight = 0.15
        else:               # last 2 exams = 20%
            weight = 0.20
        total_weighted += mark * weight
    
    avg = total_weighted
    
    # Assign letter grade
    if avg > 90:
        grade = "A"
    elif avg > 50:
        grade = "B"
    else:
        grade = "C"
    
    print(f"Weighted Average: {avg} → Grade: {grade}")


       
        