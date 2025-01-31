def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Leave non-alphabetic characters unchanged
    return encrypted_text

# Example usage
text = "Hello, Python World!"
shift = 5
encrypted = caesar_cipher(text, shift)
print("Encrypted text:", encrypted)