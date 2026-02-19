from clasic import encrypt, decrypt, get_key
import os
from dotenv import load_dotenv

load_dotenv()

def __main__():
    secret_key = os.getenv("SECRET_KEY")
    plain_text = "LOREMIPSUMDOLORSITAMETCONSECTETURADIPISICINGELIT"
    encrypted_text = encrypt(plain_text, secret_key)
    print(f"Encrypted Text: {encrypted_text}")
    decrypted_text = decrypt(encrypted_text, secret_key)
    print(f"Decrypted Text: {decrypted_text}")
    find_key = get_key(plain_text, encrypted_text)
    print(f"Found Key: {find_key}")

if __name__ == "__main__":
    __main__()