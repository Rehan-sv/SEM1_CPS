text=input("enter the text:")
clean_m=""
flage=False
for ch in text:
    if ch=="  "or ch=="\t":
            if len(clean_m)>0:
                clean_m+=" "
            is_whitespace=True
    else:
        clean_m +=ch
clean_builtin=" ".join(text.split())    
print("\t\t-----result------")
print(f"--The text without extra space is:---{clean_m}---") 
print(f"--The text without extra space is:---{clean_builtin}---")    
        
                 