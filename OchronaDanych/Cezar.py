def encrypt(message, key):
    encrypted_message = ""
    message_low = message.lower()
    for i in range(len(message_low)):
        for x in range(len(alphabet)):
            if alphabet[x] == message_low[i]:
                new_value = (x + key) % len(alphabet)
                encrypted_message += alphabet[new_value]
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ""
    message_low = encrypted_message.lower()
    for i in range(len(message_low)):
        for x in range(len(alphabet)):
            if alphabet[x] == message_low[i]:
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
