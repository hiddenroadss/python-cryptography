from random import randint

def generate_key():
    key = {}
    letters = 'ABCDEFGHIJKLMNOPQESTUVWXYZ'
    letters_for_cipher = list(letters)
    for char in letters:
        key[char] = letters_for_cipher.pop(randint(0, len(letters_for_cipher) - 1))
    return key


def encrypt(key, message):
    cipher = ''
    for char in message:
        if char in key:
            cipher += key[char]
        else:
            cipher += char
    return cipher

def get_decryption_key(key):
    decryption_key = {}
    for char in key:
        decryption_key[key[char]] = char
    return decryption_key

key = generate_key()
message = 'HASTA LA VISTA, BABY'
encrypted_message = encrypt(key, message)
decryption_key = get_decryption_key(key)
decrypted_message = encrypt(decryption_key, encrypted_message)
print(decrypted_message)