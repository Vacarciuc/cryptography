from collections import Counter
from .vigenere import VigenereCipher

class TextAnalysis:
    """Clase pentru analiza textului si atacul Vigenere."""
    def __init__(self, text: str):
        self.text = VigenereCipher.clean_text(text)

    def index_of_coincidence(self, text: str = None) -> float:
        """Calculeaza Index of Coincidence."""
        if text is None:
            text = self.text
        N = len(text)
        freq = Counter(text)
        ic = sum(f * (f - 1) for f in freq.values())
        return ic / (N * (N - 1)) if N > 1 else 0

    def guess_key_length(self, max_len: int = 15):
        """Sugereaza lungimea cheii bazata pe IC."""
        results = {}
        for key_len in range(1, max_len + 1):
            ic_values = []
            for i in range(key_len):
                column = self.text[i::key_len]
                ic_values.append(self.index_of_coincidence(column))
            avg_ic = sum(ic_values) / len(ic_values)
            results[key_len] = avg_ic
        return results

    @staticmethod
    def break_caesar(column: str) -> str:
        """Gaseste shift-ul ca un Caesar simplu, presupunand frecventa lui E."""
        freq = Counter(column)
        most_common = freq.most_common(1)[0][0]
        shift = (ord(most_common) - ord('E')) % 26
        return chr(shift + ord('A'))

    def break_vigenere(self, key_length: int) -> str:
        """Ataca textul Vigenere si returneaza cheia ghicita."""
        key = ""
        for i in range(key_length):
            column = self.text[i::key_length]
            key += self.break_caesar(column)
        return key
