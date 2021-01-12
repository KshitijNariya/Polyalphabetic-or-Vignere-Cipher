pt = input("Enter Plain Text: ")
key = input("Enter Key: ")
new_key = []
en = []
de = []

# new key
i = 0
j = 0
for kn in pt:
    if i < len(key):
        new_key.append(key[i])
        i += 1
    else:
        new_key.append(new_key[j])
        j += 1

print("New Key: ", ''.join(new_key))

# Encyption
i = 0
for kn in pt:
    en.append(chr((((ord(pt[i]) - 97) + (ord(new_key[i]) - 97)) % 26) + 97))
    i += 1
enc = ''.join(en)
print("Cipher Text: ", enc)

# Decryption
i = 0
for kn in enc:
    de.append(chr((((ord(enc[i]) - 97) - (ord(new_key[i]) - 97)) % 26) + 97))
    i += 1
dec = ''.join(de)
print("Plain Text: ", dec)
