days=5
seat=10
ticket=120
total=0
for i in range(days):
    daily_revenue=0
    for i in range(seat):
        trip=seat*ticket
        print(f"for each trip: {i+1} ")
        total=total+trip
print("THe total:  ",total)
    
    