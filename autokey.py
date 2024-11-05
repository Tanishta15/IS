##Encrypt the message "the house is being sold tonight". Vigenere cipher with key = 7

def autokey_encrypt(text, key):
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    encrypted = ""
    for i in range(len(text)):
        char = text[i]
        encrypted += chr((ord(char) - ord('a')) % 26 + ord('a'))
    return encrypted

def autokey_decrypt(text, key):
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    decrypted = ""
    for i in range(len(text)):
        char = text[i]
        shift = ord(key[i]) - ord('a')
        decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
    return decrypted

message = "the house is being sold tonight"
key = "7"
encrypted_message = autokey_encrypt(message.replace(" ", ""), key)
decrypted_message = autokey_decrypt(encrypted_message, key)

print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)