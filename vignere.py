def vigenere_encrypt(text, key):
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    encrypted = ""
    for i in range(len(text)):
        if text[i] == " ":
            encrypted += " "
        else:
            shift = ord(key[i]) - ord('a')
            encrypted += chr((ord(text[i]) - ord('a') + shift) % 26 + ord('a'))
    return encrypted

def vigenere_decrypt(text, key):
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    decrypted = ""
    for i in range(len(text)):
        if text[i] == " ":
            decrypted += " "
        else:
            shift = ord(key[i]) - ord('a')
            decrypted += chr((ord(text[i]) - ord('a') - shift) % 26 + ord('a'))
    return decrypted

message = "the house is being sold tonight"
key = "dollars"

encrypted_message = vigenere_encrypt(message.replace(" ", ""), key)
decrypted_message = vigenere_decrypt(encrypted_message, key)

print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)