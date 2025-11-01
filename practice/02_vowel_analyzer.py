nip=input("enter a sentence:")
vowels="aeiou"
vowel_count_manual=0
for char in nip.lower():
    if char in vowels:
        vowel_count_manual+=1
        
print(f"The sentance entered:{nip} ")
print(f"the vowels count:{vowel_count_manual}")
         