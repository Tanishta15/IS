##Encrypt the message "I am learning information security".Affine cipher with key = (15, 20)

def egcd(a, b): #Extended Euclidean Algorithm
    if a == 0: #a is 0, then the GCD is simply b, and the coefficients are (0, 1)
        return (b, 0, 1)
    else: #function calls itself recursively with b % a and a (using Euclidean division)
        g, y, x = egcd(b % a, a) 
        return (g, x - (b // a) * y, y) #function computes and returns the coefficients (x, y) such that g=a×x+b×y.

def modinv(a, m): #compute the modular inverse of a under modulo m
    g, x, y = egcd(a, m)
    if g != 1: #means a and m are not coprime, so a modular inverse does not exist
        raise Exception('Modular inverse does not exist')
    else: #If g is 1, the function returns x % m
        return x % m

#Convert text to uppercase -> apply Affine Cipher -> wraps result within 0–25 -> convert back to char -> join back
def encrypt(text, key):
    return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper()])

#key[1] subtracts the shift -> multiply modinv to reverse the multiplication done -> wraps result within 0–25 -> convert back to char -> join back
def decrypt(cipher, key):
    return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher])

message = "IAMLEARNINGINFORMATIONSECURITY"
key = (15, 20)

encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)