def encrypt(message, key):
    encrypted_message = ""
    message = message.lower()
    for i in range(len(message)):
        for x in range(len(alphabet)):
            if alphabet[x] == message[i]:
                new_value = (x + key) % len(alphabet)
                encrypted_message += alphabet[new_value]
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ""
    encrypted_message = encrypted_message.lower()
    for i in range(len(encrypted_message)):
        for x in range(len(alphabet)):
            if alphabet[x] == encrypted_message[i]:
                new_value = (x - key) % len(alphabet)
                decrypted_message += alphabet[new_value]
    return decrypted_message

message = "EMilfalkowski"
key = 2
alphabet = list(map(chr, range(97,123)))
encrypted_message = encrypt(message, key)
print(f'Wiadomość {message}, klucz: {key}')
print(f'Zaszyfrowana wiadomość: {encrypted_message}')
print(f'Odszyfrowana wiadomość: {decrypt(encrypted_message, key)}')
