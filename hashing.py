#Your function should start with an initial hash value of 5381 and for each character in the input string, multiply the 
# current hash value by 33, add the ASCII value of the character, and use bitwise operationsto ensure thorough mixing of 
# the bits. Finally, ensure the hash value is kept within a 32-bit range by applying an appropriate mask.

def custom_hash(input_string: str) -> int:
    hash_value = 5381 # Initialize the hash value to 5381
    for char in input_string:
        hash_value = (hash_value * 33) + ord(char)
        hash_value = hash_value & 0xFFFFFFFF
    return hash_value

test_strings = [
    "hello"
]
for string in test_strings:
    hash_value = custom_hash(string)
    print(f"Hash for '{string}': {hash_value}")