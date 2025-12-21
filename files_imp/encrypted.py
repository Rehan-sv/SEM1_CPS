u=input("enter the user name:")
p=input("enter the password:")
l=list(map(int,input("enter the key numbers:").split()))
print(l)
key=0
for i in l:
    if i>0:
        key=5
    elif i<0:
        key=-1
        break
    elif i==0:
        key=0
        break
print(key)
def encrypt(p, key):
    encrypted = ""
    for ch in p:
        pos = ord(ch) - 97        # step 1: letter → number (0–25)
        new_pos = (pos + key) % 26  # step 2: move forward
        encrypted += chr(new_pos + 97)  # step 3: number → letter
    return encrypted

def decrypt(encrypted, key):
    decrypted = ""
    for ch in encrypted:
        pos = ord(ch) - 97        # letter → number
        new_pos = (pos - key) % 26  # move backward
        decrypted += chr(new_pos + 97)
    return decrypted

enc = encrypt(p, key)
dec = decrypt(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)    