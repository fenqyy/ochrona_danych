def encrypt(message, key):
    encrypted_message = ""
    message = message.lower()
    for i in range(len(message)):
        if message[i].isalpha():
            for x in range(len(alphabet)):
                if alphabet[x] == message[i]:
                    new_value = (x + key) % len(alphabet)
                    encrypted_message += alphabet[new_value]
        else:
            encrypted_message += message[i]
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ""
    encrypted_message = encrypted_message.lower()
    for i in range(len(encrypted_message)):
        if encrypted_message[i].isalpha():
            for x in range(len(alphabet)):
                if alphabet[x] == encrypted_message[i]:
                    new_value = (x - key) % len(alphabet)
                    decrypted_message += alphabet[new_value]
        else:
            decrypted_message += encrypted_message[i]
    return decrypted_message

message = "The transformation can be represented by aligning two alphabets; the cipher alphabet is the plain alphabet rotated left or right by some number of positions. For instance, here is a Caesar cipher using a left rotation of three places, equivalent to a right shift of"
key = 7
alphabet = list(map(chr, range(97,123)))
encrypted_message = encrypt(message, key)
print(f'Wiadomość {message}, klucz: {key}')
print(f'Zaszyfrowana wiadomość: {encrypted_message}')
print(f'Odszyfrowana wiadomość: {decrypt(encrypted_message, key)}')