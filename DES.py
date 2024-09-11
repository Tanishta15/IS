from pyDes import des, CBC, PAD_PKCS5
import binascii

def des_encrypt(key, plaintext):
    key = key.encode('utf-8')
    plaintext = plaintext.encode('utf-8')
    
    cipher = des(key, CBC, key, pad=None, padmode=PAD_PKCS5)
    
    encrypted_text = cipher.encrypt(plaintext)
    
    return binascii.hexlify(encrypted_text).decode('utf-8')

def des_decrypt(key, encrypted_text):
    key = key.encode('utf-8')
    encrypted_text = binascii.unhexlify(encrypted_text)
    
    cipher = des(key, CBC, key, pad=None, padmode=PAD_PKCS5)
    
    decrypted_text = cipher.decrypt(encrypted_text)
    
    return decrypted_text.decode('utf-8')

# Example usage
if __name__ == '__main__':
    key = "12345678"  # 8-byte key
    plaintext = "Hello, DES!"
    
    # Encrypt the plaintext
    encrypted_text = des_encrypt(key, plaintext)
    print("Encrypted text:", encrypted_text)
    
    # Decrypt the encrypted text
    decrypted_text = des_decrypt(key, encrypted_text)
    print("Decrypted text:", decrypted_text)


S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
]

INITIAL_PERMUTATION = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

FINAL_PERMUTATION = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

def permute(block, table):
    return [block[x - 1] for x in table]

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def feistel(right, subkey):
    return xor(right, subkey)

def generate_subkeys(key):
    return [key] * 16 

def des_encrypt(plaintext, key):
    binary_plaintext = [int(x) for x in '{:064b}'.format(int.from_bytes(plaintext.encode(), 'big'))]
    binary_key = [int(x) for x in '{:064b}'.format(int.from_bytes(key.encode(), 'big'))]

    permuted_text = permute(binary_plaintext, INITIAL_PERMUTATION)

    left, right = permuted_text[:32], permuted_text[32:]
    subkeys = generate_subkeys(binary_key)

    for i in range(16):
        new_right = xor(left, feistel(right, subkeys[i]))
        left = right
        right = new_right

    combined = right + left

    encrypted_bits = permute(combined, FINAL_PERMUTATION)

    encrypted_text = int(''.join(map(str, encrypted_bits)), 2).to_bytes(8, 'big')
    return encrypted_text

if __name__ == '__main__':
    plaintext = "Hello123" 
    key = "abcdefgh"

    encrypted_text = des_encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text.hex())