# Program 9: Event management
dinner_guests = {"Aisha", "Rahul", "Neha", "Karan"}
afterparty_guests = {"Karan", "Vivek", "Neha", "Tina"}

print("Both events:", dinner_guests & afterparty_guests)
print("Only dinner:", dinner_guests - afterparty_guests)
print("Only afterparty:", afterparty_guests - dinner_guests)
print("Total unique guests:", dinner_guests | afterparty_guests)
