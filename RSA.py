#Encrypt the message "Cryptographic Protocols" using the RSA public key (n, e) where n = 323 and e = 5. Decrypt the ciphertext with the
#private key (n, d) where d = 173 to confirm the original message

import random
from math import gcd

def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

def generate_rsa_keys():
    p = 61 
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    if gcd(e, phi) != 1:
        raise ValueError("e and phi are not coprime!")
    d = mod_inverse(e, phi)
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    encrypted_message = [mod_exp(ord(char), e, n) for char in plaintext]
    return encrypted_message

def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(mod_exp(char, d, n)) for char in ciphertext])
    return decrypted_message

if __name__ == "__main__":
    public_key, private_key = generate_rsa_keys()
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    plaintext = "HELLO RSA"
    print(f"Original message: {plaintext}")
    encrypted_message = rsa_encrypt(plaintext, public_key)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message = rsa_decrypt(encrypted_message, private_key)
    print(f"Decrypted message: {decrypted_message}")