def generate_key(shift):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = {}
    cnt = 0
    for char in letters:
        key[char] = letters[(cnt + shift) % len(letters)]
        cnt += 1
    return key

def get_decryptiption_key(key):
    decryption_key = {}
    for char in key:
        decryption_key[key[char]] = char
    return decryption_key


def encrypt_message(key, message): 
    cipher = ''
    for char in message:
        if char in key:
            cipher += key[char]
        else:
            cipher += char
    return cipher

key = generate_key(3)
message = 'WHAT IS GOING ON'

encrypted_message = encrypt_message(key = key, message = message)
print(encrypted_message)

for i in range(26):
    decryption_key = generate_key(i)
    message = encrypt_message(decryption_key, encrypted_message)
    print(message)