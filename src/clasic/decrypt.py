from clasic.utils import ALPHABET

def decrypt(encrypted_message: str, key: str)-> str:
    decrypted_message = ""
    for i, char in enumerate(encrypted_message):
        if char in ALPHABET:
            ci = ALPHABET.index(char)
            ki = ALPHABET.index(key[i % len(key)])
            pi = (ci - ki) % len(ALPHABET)
            decrypted_message += ALPHABET[pi]
        else:
            decrypted_message += char
    return decrypted_message