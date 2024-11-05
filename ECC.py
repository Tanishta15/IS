#Using ECC encrypt the message "Secure Transactions" with the public key. 

#pip install ecdsa cryptography

from ecdsa import SigningKey, VerifyingKey, NIST384p
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import base64

private_key = SigningKey.generate(curve=NIST384p)  # Private key
public_key = private_key.get_verifying_key()  # Public key
message = "Secure Transactions"

def encrypt(public_key, message):
    public_key_bytes = public_key.to_string()
    encrypted_message = public_key_bytes + message.encode()
    return base64.b64encode(encrypted_message)

def decrypt(private_key, encrypted_message):
    encrypted_message_bytes = base64.b64decode(encrypted_message)
    public_key_bytes = encrypted_message_bytes[:private_key.get_verifying_key().to_string().__len__()]
    decrypted_message = encrypted_message_bytes[private_key.get_verifying_key().to_string().__len__():].decode()
    return decrypted_message

encrypted_message = encrypt(public_key, message)
print(f"Encrypted message: {encrypted_message}")
decrypted_message = decrypt(private_key, encrypted_message)
print(f"Decrypted message: {decrypted_message}")