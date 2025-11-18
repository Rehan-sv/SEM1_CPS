flowers = {
    "Hibiscus": {"price":100, "col":["Red","White","Pink","Violet","Orange","Yellow"]},
    "Rose": {"price":200, "col":["Red","White","Maroon","Yellow"]},
    "Marigold": {"price":50, "col":["Orange","Yellow"]},
    "Dahlia": {"price":150, "col":["Red","White","Pink"]},
    "Lotus": {"price":300, "col":["Blue","Pink","Yellow"]}
}

# ------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------

def max_colours(flowers):
    """Return flower with maximum colour varieties."""
    max_flower = ""
    max_count = 0
    for f in flowers:
        if len(flowers[f]["col"]) > max_count:
            max_count = len(flowers[f]["col"])
            max_flower = f
    return max_flower


def flowers_with_colour(flowers, colour):
    """Return which flowers contain the given colour."""
    result = []
    for f in flowers:
        if colour in flowers[f]["col"]:
            result.append(f)
    return result


def buy_with_budget(flowers, amount):
    """Which flowers can be fully purchased with given amount?"""
    res = []
    for f in flowers:
        cost = flowers[f]["price"] * len(flowers[f]["col"])
        if cost <= amount:
            res.append(f)
    return res


def unique_colours(flowers):
    """List colours that appear in only one flower."""
    allc = []
    for f in flowers:
        allc += flowers[f]["col"]

    uniq = []
    for c in allc:
        if allc.count(c) == 1:
            uniq.append(c)

    return uniq


# ------------------------------------------------------
# USER INPUT SECTION (Super Easy)
# ------------------------------------------------------

print("1. Flower with maximum colours")
print("2. Flowers available in a given colour")
print("3. Flowers you can buy fully with your budget")
print("4. Unique colours")
print("---------------------------------------------")

choice = int(input("Enter choice (1-4): "))

# OPTION 1
if choice == 1:
    print("Flower with maximum colour varieties:", max_colours(flowers))

# OPTION 2
elif choice == 2:
    colour = input("Enter colour: ")
    res = flowers_with_colour(flowers, colour)
    print("Flowers with colour", colour, ":", " ".join(res) if res else "None")

# OPTION 3
elif choice == 3:
    amount = int(input("Enter budget amount: "))
    res = buy_with_budget(flowers, amount)
    print("Flowers you can buy fully:", " ".join(res) if res else "None")

# OPTION 4
elif choice == 4:
    print("Unique colours:")
    for c in unique_colours(flowers):
        print(c)

else:
    print("Error")
