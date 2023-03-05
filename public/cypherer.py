import random
import string

def generate_cipher(include_numbers=False):
    # Create a list of all characters to include in the cipher
    characters = list(string.ascii_lowercase)
    if include_numbers:
        characters += list(string.digits)

    # Shuffle the characters
    random.shuffle(characters)

    # Create a dictionary mapping each character to its shuffled counterpart
    cipher = {letter: substitute for letter, substitute in zip(string.ascii_lowercase, characters)}

    if include_numbers:
        # Add number-to-number mapping to the cipher
        random_numbers = list(string.digits)
        random.shuffle(random_numbers)
        cipher.update({number: substitute for number, substitute in zip(string.digits, random_numbers)})

    return cipher

# Get user input for whether to include numbers in the cipher
include_numbers = input("Include numbers in cipher? (y/n): ").lower() == "y"

# Generate a cipher and print the result
cipher = generate_cipher(include_numbers)
print("Cipher:", cipher)
