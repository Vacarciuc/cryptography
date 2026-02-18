import string

class VigenereCipher:
    """
    Acesta este un text simplu pentru testarea de criptografie
    """
    def __init__(self, key: str):
        self.key = self.clean_text(key)

    @staticmethod
    def clean_text(text: str) -> str:
        """Pastreaza doar litere mari A-Z."""
        text = text.upper()
        return ''.join([c for c in text if c in string.ascii_uppercase])

    def encrypt(self, plaintext: str) -> str:
        plaintext = self.clean_text(plaintext)
        ciphertext = ""
        for i, c in enumerate(plaintext):
            p = ord(c) - ord('A')
            k = ord(self.key[i % len(self.key)]) - ord('A')
            ciphertext += chr((p + k) % 26 + ord('A'))
        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        ciphertext = self.clean_text(ciphertext)
        plaintext = ""
        for i, c in enumerate(ciphertext):
            c_val = ord(c) - ord('A')
            k = ord(self.key[i % len(self.key)]) - ord('A')
            plaintext += chr((c_val - k) % 26 + ord('A'))
        return plaintext
