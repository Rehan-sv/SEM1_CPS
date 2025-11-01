''' 
text = input("Enter the text which you want to edit: ")
# Replace tabs with a single space
clean_text = text.replace("\t", " ")
print(clean_text)
'''
text=input("enter the text:")
clean_m=""
flage=False
for ch in text:
    if ch=="  "or ch=="\t":
            if len(clean_m)>0:
                clean_m+=" "
            flage=True
    else:
        clean_m +=ch
clean_builtin=" ".join(text.split())    
print("\t\t-----result------")
print(f"--The text without extra space is:---{clean_m}---") 
print(f"--The text without extra space is:---{clean_builtin}---")
    