import string
import operator

# Expected frequency distribution of letters in English
ENGLISH_LETTER_FREQUENCY = {'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270,
                            'f': 0.0223, 'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015,
                            'k': 0.0077, 'l': 0.0403, 'm': 0.0241, 'n': 0.0675, 'o': 0.0751,
                            'p': 0.0193, 'q': 0.0010, 'r': 0.0599, 's': 0.0633, 't': 0.0906,
                            'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015, 'y': 0.0197, 'z': 0.0007}

def brute_force_decrypt_with_frequency_analysis(message):
    # Convert the message to lowercase
    message = message.lower()

    # Count the frequency of each letter in the message
    letter_counts = {letter: 0 for letter in string.ascii_lowercase}
    for letter in message:
        if letter in letter_counts:
            letter_counts[letter] += 1

    # Sort the letters in descending order of frequency
    sorted_letters = sorted(letter_counts.items(), key=operator.itemgetter(1), reverse=True)

    # Calculate the most likely shift based on the frequency distribution of the letters in the message
    most_frequent_letter = sorted_letters[0][0]
    shift = string.ascii_lowercase.index(most_frequent_letter) - string.ascii_lowercase.index('e')

    # Shift the alphabet by the calculated shift
    alphabet_shifted = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]

    # Create a dictionary mapping each letter to its shifted counterpart
    cipher = {letter: substitute for letter, substitute in zip(alphabet_shifted, string.ascii_lowercase)}

    # Apply the cipher to the message
    decrypted_message = "".join([cipher.get(letter, letter) for letter in message])

    # Print the decrypted message with the key used to decrypt it
    print("Key:", shift, "Decrypted message:", decrypted_message)
