def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    ciphertext = ""
    for char in plaintext:
        encrypted = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
        ciphertext += encrypted
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        decrypted_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
        plaintext += decrypted_char
    return plaintext

message = "I am learning information security"
key = 20

encrypted= encrypt(message, key)
print(f"Encrypted message: {encrypted}")

decrypted = decrypt(encrypted, key)
print(f"Decrypted message: {decrypted}")
