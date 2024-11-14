def count(message: str):
    message = message.lower()
    max_freq = {}
    for i in message:
        if i in max_freq:
            max_freq[i] += 1
        else:
            max_freq[i] = 1
    max_char = max(max_freq, key= max_freq.get)
    return max_char, max_freq[max_char]

def find_key(message):
    message = message.lower()
    key = 0
    for x in alphabet:
        
    return key


message = "goknhcnmqyumk"
alphabet = list(map(chr, range(97,123)))
most_frequent = ['a', 'e', 'i', 'o']
print(count(message))