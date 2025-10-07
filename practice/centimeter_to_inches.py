num=float(input("enter the numeber : "))
unit=input("Cm or inches : ")
if unit=="Cm":
    inches=num/2.54
    print("the number in inches is :",inches)
elif unit=="inches":
    cm=num*2.54
    print("the number in cm is :",cm)
    