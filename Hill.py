import numpy as np

def text_to_numbers(text):
    text = text.replace(" ", "").upper()
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    return ''.join([chr(num + ord('A')) for num in numbers])

def hill_cipher_encrypt(plaintext, key):
    numbers = text_to_numbers(plaintext)
    if len(numbers) % 2 != 0: # Ensure the length is even by padding with 'X'
        numbers.append(ord('X') - ord('A'))

    encrypted_numbers = []  # Split into 2x1 column vectors
    for i in range(0, len(numbers), 2):
        vector = np.array([[numbers[i]], [numbers[i+1]]])
        encrypted_vector = np.dot(key, vector) % 26
        encrypted_numbers.extend(encrypted_vector.flatten())
    return numbers_to_text(encrypted_numbers)

def hill_cipher_decrypt(ciphertext, key):
    numbers = text_to_numbers(ciphertext)
    determinant = int(np.round(np.linalg.det(key))) % 26 # Compute the inverse of the key matrix modulo 26
    determinant_inv = pow(determinant, -1, 26)
    adjugate = np.array([[key[1, 1], -key[0, 1]], [-key[1, 0], key[0, 0]]])
    key_inv = (determinant_inv * adjugate) % 26

    decrypted_numbers = []
    for i in range(0, len(numbers), 2):
        vector = np.array([[numbers[i]], [numbers[i+1]]])
        decrypted_vector = np.dot(key_inv, vector) % 26
        decrypted_numbers.extend(decrypted_vector.flatten())
    return numbers_to_text(decrypted_numbers)

key_matrix = np.array([[3, 3], [2, 7]])
message = "We live in an insecure world"

encrypted_message = hill_cipher_encrypt(message, key_matrix)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = hill_cipher_decrypt(encrypted_message, key_matrix)
print(f"Decrypted message: {decrypted_message}")
