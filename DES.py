from pyDes import des, ECB, PAD_PKCS5

key = "A1B2C3D4"  
des_cipher = des(key, ECB, padmode=PAD_PKCS5)
message = "Confidential Data"

encrypted_message = des_cipher.encrypt(message)
print(f"Encrypted message: {encrypted_message.hex()}")

decrypted_message = des_cipher.decrypt(encrypted_message)
print(f"Decrypted message: {decrypted_message.decode('utf-8')}")
