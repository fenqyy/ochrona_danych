def shift(alphabet):
    full_tab = [alphabet[i:] + alphabet[:i] for i in range(len(alphabet))]
    return full_tab

def vigenere_encrypt(message, key):
    encrypted_message = ""
    message = message.lower()
    full_key = (key * (len(message) // len(key) + 1))[:len(message)]
    for x_message, y_key in zip(message, full_key):
        row = alphabet.index(y_key)
        col = alphabet.index(x_message)
        encrypted_message += table[row][col]
    return encrypted_message

def vigenere_decrypt(encrypted_message, key):
    decrypted_message = ""
    encrypted_message = encrypted_message.lower()
    full_key = (key * (len(encrypted_message) // len(key) + 1))[:len(encrypted_message)]
    for x_message, y_key in zip(encrypted_message, full_key):
        row = alphabet.index(y_key)
        col = table[row].index(x_message)
        decrypted_message += alphabet[col]
    return decrypted_message


message = "EMilfalkowski"
key = "key"
alphabet = list(map(chr, range(97, 123)))
table = shift(alphabet)
encrypted_message = vigenere_encrypt(message, key)
print("Tabela dla szyfru Vigenere'a")
for i in table:
    print(i)
print(f'Wiadomość {message}, klucz: {key}')
print(f'Zaszyfrowana wiadomość: {encrypted_message}')
print(f'Odszyfrowana wiadomość: {vigenere_decrypt(encrypted_message, key)}')