# caesar-cipher-in-python

Python script that demonstrates a simple encryption method using the Caesar cipher. 
The Caesar cipher is a basic encryption technique where each letter in the text is 
shifted by a fixed number of positions in the alphabet.

How does this script work?

The ord() and chr() functions:
ord(char) returns the ASCII code of the given character.
chr(code) converts the ASCII code back to char.
Handling letters:
The script checks if the character is a letter (isalpha()), and moves it accordingly in the alphabet.
It supports both uppercase and lowercase letters.
Other characters:
Characters that are not letters (e.g. spaces, numbers, punctuation marks) are left unchanged.
Output
For the text "Welcome to the world of Python!" and an offset of 3, the output will be:

Encrypted text: Zlwdm z vąflhflh Sbwkrqd!
