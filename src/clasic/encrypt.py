from clasic.utils import ALPHABET

def encrypt(plain_text: str, key: str) -> str:
    encrypted_text = ""
    key_length = len(key)

    for i, char in enumerate(plain_text):
        if char in ALPHABET:
            pi = ALPHABET.index(char)
            ki = ALPHABET.index(key[i % key_length])
            ci = (pi + ki) % 26
            encrypted_text += ALPHABET[ci]
        else:
            encrypted_text += char
    return encrypted_text