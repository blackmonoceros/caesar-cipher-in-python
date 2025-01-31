# caesar-cipher-in-python

Python script that demonstrates a simple encryption method using the Caesar cipher. 
The Caesar cipher is a basic encryption technique where each letter in the text is 
shifted by a fixed number of positions in the alphabet.

How the Script Works
Input Parameters:
text: The string to be encrypted.
shift: The number of positions each letter is shifted in the alphabet.
Logic:
The script iterates through each character in the input text.
If the character is a letter (isalpha()), it calculates the new encrypted character by:
Determining the base ASCII value (ord('A') for uppercase or ord('a') for lowercase).
Shifting the character by the specified amount (shift) and wrapping around the alphabet 
using modulo (% 26).
Non-alphabetic characters (e.g., spaces, punctuation) are left unchanged.
Output:
The function returns the encrypted version of the input text.
Example Output
For the input text "Hello, Python World!" with a shift of 5, the output will be:

Encrypted text: Mjqqt, Udymts Btwqi!
