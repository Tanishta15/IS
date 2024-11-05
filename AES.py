#Encrypt the message "Sensitive Information" using AES-128 with the following key: "0123456789ABCDEF0123456789ABCDEF". 

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

key = b'0123456789ABCDEF'
cipher = AES.new(key, AES.MODE_ECB)
plaintext = "Sensitive Information".encode()

ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
print("Cipher Text:", binascii.hexlify(ciphertext).decode())