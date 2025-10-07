# Step 1: Create a dictionary to store the counts, starting each at 0.
counts = {
    "Hyperthermophile": 0,
    "Thermophile": 0,
    "Mesophile": 0,
    "Psychrotrophs": 0,
    "Psychrophiles": 0
}

# Step 2: Ask the user how many temperatures to check.
num_temps = int(input("How many temperatures do you want to enter? "))

# Step 3: Loop to get each temperature and update the counts.
for i in range(num_temps):
    temp = float(input(f"Enter temperature {i + 1}: "))

    # Check each condition and add 1 to the count if it's a match.
    if temp >= 60:
        counts["Hyperthermophile"] += 1
    if 45 <= temp <= 122:
        counts["Thermophile"] += 1
    if 20 <= temp <= 45:
        counts["Mesophile"] += 1
    if 0 <= temp <= 45:
        counts["Psychrotrophs"] += 1
    if -15 <= temp <= 10:
        counts["Psychrophiles"] += 1
        print()
        print("hyperthermophile", counts["Hyperthermophile"])
        print("thermophile", counts["Thermophile"]) 
        print("mesophile", counts["Mesophile"])
        print("psychrotrophs", counts["Psychrotrophs"])
        print("psychrophiles", counts["Psychrophiles"])
           
        