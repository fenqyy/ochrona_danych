def shift(alphabet):
    full_tab = [alphabet[i:] + alphabet[:i] for i in range(len(alphabet))]
    return full_tab

def vigenere_encrypt(message, key):
    encrypted_message = ""
    message = message.lower()
    full_key = (key * (len([c for c in message if c.isalpha()]) // len(key) + 1))[:len([c for c in message if c.isalpha()])]
    key_index = 0
    for x in message:
        if x.isalpha():
            row = alphabet.index(full_key[key_index])
            col = alphabet.index(x)
            encrypted_message += table[row][col]
            key_index += 1
        else:
            encrypted_message += x
    return encrypted_message

def vigenere_decrypt(encrypted_message, key):
    decrypted_message = ""
    encrypted_message = encrypted_message.lower()
    full_key = (key * (len([c for c in encrypted_message if c.isalpha()]) // len(key) + 1))[:len([c for c in encrypted_message if c.isalpha()])]
    key_index = 0
    for x in encrypted_message:
        if x.isalpha():
            row = alphabet.index(full_key[key_index])
            col = table[row].index(x)
            decrypted_message += alphabet[col]
            key_index += 1
        else:
            decrypted_message += x
    return decrypted_message


message = "The transformation can be represented by aligning two alphabets; the cipher alphabet is the plain alphabet rotated left or right by some number of positions. For instance, here is a Caesar cipher using a left rotation of three places, equivalent to a right shift of"
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