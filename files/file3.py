# 3. Read the entire content of the file "Questions" and write it to a new file "Qs_copy"
f = open("Questions","r")
q = open("Qs_copy","w")
q.write(f.read())
f.close()
q.close()