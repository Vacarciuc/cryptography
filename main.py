from cipher.vigenere import VigenereCipher
from cipher.analysis import TextAnalysis

def main():
    plaintext = "THIS IS A SECRET MESSAGE THAT WE WANT TO HIDE"
    key = "KEY"

    # Criptare
    cipher = VigenereCipher(key)
    ciphertext = cipher.encrypt(plaintext)
    print("Ciphertext:", ciphertext)

    # Analiza
    analysis = TextAnalysis(ciphertext)
    key_lengths = analysis.guess_key_length(10)
    print("\nPosibile lungimi cheie (IC mediu):")
    for k, ic in key_lengths.items():
        print(f"{k}: {ic:.4f}")

    # Presupunem ca lungimea cheii e 3 (cea mai apropiata de IC ~0.065)
    guessed_key = analysis.break_vigenere(3)
    print("\nCheia ghicita:", guessed_key)

    # Decriptare
    recovered = VigenereCipher(guessed_key).decrypt(ciphertext)
    print("\nMesaj decriptat:", recovered)

if __name__ == "__main__":
    main()
