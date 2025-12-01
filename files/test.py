name=input("Enter your name")
f = open("Name.txt", "w")
f.write(name)
f.close()