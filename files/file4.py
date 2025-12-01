# 4. Demonstrate of 'w' mode overwriting contents of a file
# f = open("C:\\Users\\user\\OneDrive\\Documents\\VS CODE\\files\\Qs_copy.txt","r")
import os

print(os.getcwd())
f = open("Qs_copy.txt","r")
print("Before write open" , print(f.read()))
f.close()
f = open("Qs_copy.txt","w")
f.close()
f = open("Qs_copy.txt","r")
print("After write open", f.read())