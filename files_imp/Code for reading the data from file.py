# ============================
# LOAD PRODUCTS FROM FILE
# ============================

products = []

try:
    with open("products.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")

            if len(parts) == 5:
                product = {
                    "id": parts[0].strip(),
                    "name": parts[1].strip(),
                    "category": parts[2].strip(),
                    "price": float(parts[3].strip()),
                    "quantity": int(parts[4].strip())
                }
                products.append(product)

except FileNotFoundError:
    print("products.txt not found. Starting with empty list.")


# ============================
# MAIN MENU LOOP
# ============================

while True:
    print("\n====== SIMPLE GROCERY MENU ======")
    print("1. Display all products")
    print("2. Search by category")
    print("3. Update product quantity")
    print("4. Find costliest product")
    print("5. Category-wise summary")
    print("6. Save products to file")
    print("7. Exit")

    choice = input("Enter choice: ")

    # -------------------------
    # OPTION 1: Display Products
    # -------------------------
    if choice == "1":
        print("\n--- ALL PRODUCTS ---")
        for p in products:
            print(f"{p['id']} | {p['name']} | {p['category']} | ₹{p['price']} | Qty: {p['quantity']}")
        print()

    # -------------------------
    # OPTION 2: Search Category
    # -------------------------
    elif choice == "2":
        cat = input("Enter category to search: ")
        print(f"\n--- Products in {cat} ---")
        found = False

        for p in products:
            if p["category"].lower() == cat.lower():
                print(f"{p['id']} | {p['name']} | ₹{p['price']} | Qty: {p['quantity']}")
                found = True

        if not found:
            print("No products found.")
        print()

    # -------------------------
    # OPTION 3: Update Quantity
    # -------------------------
    elif choice == "3":
        pid = input("Enter product ID: ")
        new_qty = int(input("Enter new quantity: "))

        updated = False

        for p in products:
            if p["id"] == pid:
                p["quantity"] = new_qty
                updated = True
                print("Quantity updated successfully!")

        if not updated:
            print("Product ID not found.")
        print()

    # -------------------------
    # OPTION 4: Costliest Product
    # -------------------------
    elif choice == "4":
        if not products:
            print("No products available.\n")
        else:
            costliest = products[0]
            for p in products:
                if p["price"] > costliest["price"]:
                    costliest = p

            print("\n--- COSTLIEST PRODUCT ---")
            print(f"{costliest['id']} | {costliest['name']} | {costliest['category']} | Price: ₹{costliest['price']}\n")

    # -------------------------
    # OPTION 5: Category Summary
    # -------------------------
    elif choice == "5":
        summary = {}

        for p in products:
            cat = p["category"]
            qty = p["quantity"]

            if cat in summary:
                summary[cat] += qty
            else:
                summary[cat] = qty

        # Sort by quantity (descending)
        sorted_summary = sorted(summary.items(), key=lambda x: x[1], reverse=True)

        print("\n--- CATEGORY SUMMARY ---")
        for cat, qty in sorted_summary:
            print(f"{cat}: {qty}")
        print()

    # -------------------------
    # OPTION 6: SAVE TO FILE
    # -------------------------
    elif choice == "6":
        with open("products.txt", "w") as f:
            for p in products:
                f.write(f"{p['id']}, {p['name']}, {p['category']}, {p['price']}, {p['quantity']}\n")

        print("Data saved to file!\n")

    # -------------------------
    # OPTION 7: EXIT
    # -------------------------
    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.\n")
