# Initialize counts
counts = {
    "Hyperthermophile": 0,
    "Thermophile": 0,
    "Mesophile": 0,
    "Psychrotrophs": 0,
    "Psychrophiles": 0
}

num = int(input("How many temperatures do you want to enter? "))

for i in range(num):
    temp = float(input(f"Enter temperature {i + 1}: "))

    if temp >= 60:
        counts["Hyperthermophile"] += 1
    if  45 <= temp < 60:
        counts["Thermophile"] += 1
    if 20 <= temp < 45:
        counts["Mesophile"] += 1
    if 0 <= temp < 20:
        counts["Psychrotrophs"] += 1
    if -15 <= temp < 0:
        counts["Psychrophiles"] += 1

# Print results
print("Hyperthermophile:", counts["Hyperthermophile"])
print("Thermophile:", counts["Thermophile"])
print("Mesophile:", counts["Mesophile"])
print("Psychrotrophs:", counts["Psychrotrophs"])
print("Psychrophiles:", counts["Psychrophiles"])
