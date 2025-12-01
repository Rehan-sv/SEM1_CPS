# 5. Demonstrate of 'a' mode appending contents to a file
f = open("Qs_copy.txt","r")
print("Before append open" , f.read())
f.close()
f = open("Qs_copy.txt","a")
f.write("This is a new line")
f.close()
f = open("Qs_copy.txt","r")
print("After append open", f.read())
