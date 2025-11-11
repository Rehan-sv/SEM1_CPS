# Program 4: Periodic Table - Element State Finder

elements = {
    "H": {"name": "Hydrogen", "melting": 14, "boiling": 20},
    "He": {"name": "Helium", "melting": 1, "boiling": 4},
    "Li": {"name": "Lithium", "melting": 453, "boiling": 1603},
    "Be": {"name": "Beryllium", "melting": 1560, "boiling": 2742},
    "B": {"name": "Boron", "melting": 2349, "boiling": 4200},
    "C": {"name": "Carbon", "melting": 3915, "boiling": 3915},
    "N": {"name": "Nitrogen", "melting": 63, "boiling": 77},
    "O": {"name": "Oxygen", "melting": 54, "boiling": 90},
    "F": {"name": "Fluorine", "melting": 53, "boiling": 85},
    "Ne": {"name": "Neon", "melting": 25, "boiling": 27}
}

# Get user input
symbol = input("Enter element symbol (H, O, Li, etc): ")
temp = float(input("Enter temperature in Kelvin: "))

# Simple checking
if symbol in elements:
    # ✅ Correct way to access inner dictionary using the symbol
    print("\nElement name:", elements[symbol]["name"])
    print("Melting Point:", elements[symbol]["melting"], "K")
    print("Boiling Point:", elements[symbol]["boiling"], "K")

    # easy if conditions
    if temp < elements[symbol]["melting"]:
        print("It is solid at this temperature.")
    elif temp < elements[symbol]["boiling"]:
        print("It is liquid at this temperature.")
    else:
        print("It is gas at this temperature.")
else:
    print("Element not found.")
