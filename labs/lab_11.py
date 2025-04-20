def vowels(sentence):
    words = sentence.split()
    cleaned_words = []

    for word in words:
        cleaned_word = word.strip(".,!?;:\"'()[]{}").lower()
        if cleaned_word:
            cleaned_words.append(cleaned_word)

    max_vowels = 0
    max_vowel_word = ""

    for word in cleaned_words:
        vowel_count = sum(1 for char in word if char.lower() in "aeiouy")

        if vowel_count > max_vowels:
            max_vowels = vowel_count
            for original_word in words:
                if word in original_word.lower().strip(".,!?;:\"'()[]{}"):
                    max_vowel_word = original_word
                    break

    return max_vowel_word


def shift_encipher(str, shift):
    result = ""

    if 1 <= shift <= 25:
        for char in str:
            if char == " ":
                result += " "
            else:
                ascii_val = ord(char)
                shifted_val = (ascii_val - 65 + shift) % 26 + 65
                result += chr(shifted_val)

    return result


def shift_decipher(str, shift):
    if not 1 <= shift <= 25:
        raise ValueError("Shift must be between 1 and 25 inclusive")

    left_shift = 26 - shift
    return shift_encipher(str, left_shift)


def rail_encipher(str):
    even_chars = str[0::2]
    odd_chars = str[1::2]

    return even_chars + odd_chars


def rail_decipher(str):
    length = len(str)
    first_half_len = (length + 1) // 2

    first_half = str[:first_half_len]
    second_half = str[first_half_len:]

    result = ""
    for i in range(length):
        if i % 2 == 0 and i // 2 < len(first_half):
            result += first_half[i // 2]
        elif i % 2 == 1 and i // 2 < len(second_half):
            result += second_half[i // 2]

    return result


if __name__ == "__main__":
    print("Testing vowels function:")
    print(vowels("This is a test sentence"))
    print(vowels("Application has many vowels"))
    print(vowels("Hello, world! How are you?"))
    print(vowels("Mary-Jane O'Connor"))

    print("\nTesting shift cipher functions:")
    encrypted = shift_encipher("HELLO WORLD", 3)
    print(f"Encrypted: {encrypted}")
    decrypted = shift_decipher(encrypted, 3)
    print(f"Decrypted: {decrypted}")

    print("\nTesting rail fence cipher functions:")
    encrypted = rail_encipher("ABCDE")
    print(f"Rail fence encrypted: {encrypted}")
    decrypted = rail_decipher(encrypted)
    print(f"Rail fence decrypted: {decrypted}")
