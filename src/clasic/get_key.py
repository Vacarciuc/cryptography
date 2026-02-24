from .utils import ALPHABET

def get_key(plain_text: str, encrypted_message: str) -> str:
    key_length = 0
    key = ""
    group_length = len(encrypted_message) // 2
    if group_length % 2 != 0:
        group_length = int(group_length) - 1
    for i in range(group_length, 1, -1):
        key_length = find_simetri(encrypted_message, i)
    print(f"Found key length: {key_length}")
    key = find_key(plain_text, encrypted_message, key_length)
    second_key_length = second_find_key_length(plain_text, encrypted_message)
    print(f"Second key length: {second_key_length}")
    return key



def find_simetri(text:str, num_chars: int) -> int:
    comparable_text = text[:num_chars]
    print(f"Checking: {comparable_text}")
    first_index = text.find(comparable_text)
    return text.find(comparable_text, first_index + 1)


def find_key(plain_text: str, encrypted_message: str, key_length: int) -> str:
    key = ""
    for p_char, e_char in zip(plain_text, encrypted_message):
        if p_char in ALPHABET and e_char in ALPHABET:
            pi = ALPHABET.index(p_char)
            ci = ALPHABET.index(e_char)
            ki = (ci - pi) % len(ALPHABET)
            key += ALPHABET[ki]
    if key_length > 0:
        return key[:key_length]
    else:
        return key


def second_find_key_length(plain_text: str, encrypted_message: str) -> int:
    group_found = []
    for i in range(len(plain_text)):
        for j in range(len(encrypted_message)):
            if plain_text[i] == encrypted_message[j]:
                group_found.append(j - i)
    if not group_found:
        return -1
    print(group_found)
    return min(group_found)