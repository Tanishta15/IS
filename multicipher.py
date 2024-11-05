#Encrypt the message "I am learning information security". Multiplicative cipher with key = 15

def mod_inverse(key, mod=26):
    for x in range(1, mod):
        if (key * x) % mod == 1:
            return x

def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper() 
    ciphertext = ""
    for char in plaintext:
        encrypted = chr(((ord(char) - ord('A')) * key % 26) + ord('A'))
        ciphertext += encrypted
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    key_inverse = mod_inverse(key)
    for char in ciphertext:
        decrypted_char = chr(((ord(char) - ord('A')) * key_inverse % 26) + ord('A'))
        plaintext += decrypted_char
    return plaintext

plaintext = "I am learning information security"
key = 15
ciphertext = encrypt(plaintext, key)
print("Encrypted:", ciphertext)
decrypted = decrypt(ciphertext, key)
print("Decrypted:", decrypted)