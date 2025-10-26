n=int(input("Enter the number of student "))
hall_ticket=0
for i in range (n):
    attended_class=int(input(f"Enter the  total number calsses attended by a student{i}"))
    attendance_percentage=(attended_class/40)*100
    print(attendance_percentage)
    if attendance_percentage>75:  
        hall_ticket=hall_ticket+1
    if attendance_percentage<75:
        print("attendence is below 75")
print("hall ticket given",hall_ticket)
    
