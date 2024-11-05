#With the ElGamal public key (p = 7919, g = 2, h = 6465) and the private key x = 2999, encrypt the message "Asymmetric Algorithms".
#python3 -m pip install pycryptodome --break-system-packages

from Crypto.Util.number import bytes_to_long, long_to_bytes
from random import randint

p = 7919  # Large prime number
g = 2     # Generator
h = 6465  # Public key component (h = g^x mod p)
x = 2999  # Private key

message = "Asymmetric Algorithms"
message_int = bytes_to_long(message.encode('utf-8'))  # Convert message to an integer

k = randint(1, p-2)  # Random number k (1 <= k <= p-2)
c1 = pow(g, k, p)  # c1 = g^k mod p
c2 = (message_int * pow(h, k, p) % p)  # c2 = m * h^k mod p

ciphertext = (c1, c2)
print(f"Ciphertext: {ciphertext}")

decrypted_int = (c2 * pow(c1, p - 1 - x, p)) % p  # m = c2 * (c1^(p-1-x) mod p)
decrypted_message = long_to_bytes(decrypted_int).decode('utf-8')
print(f"Decrypted message: {decrypted_message}")