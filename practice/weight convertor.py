weight=float(input("Enter the weight"))
unit=input("Enter the unit (kg or lbs)")
if unit=="kg":
    weight=weight*2.205
    print("kg to lbs =  ", weight)
elif unit=="lbs":
    weight=weight/2.205
    print("lbs to kg =  ",weight)
else:
    print("invalid unit")