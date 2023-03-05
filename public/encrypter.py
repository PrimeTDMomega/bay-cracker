import random

# Generate a random alphabet substitution cipher
alphabet = list("abcdefghijklmnopqrstuvwxyz")
random.shuffle(alphabet)
cipher = {letter: substitute for letter, substitute in zip("abcdefghijklmnopqrstuvwxyz", alphabet)}

def encrypt(message):
    # Convert the message to lowercase and substitute each letter
    encrypted_message = "".join(cipher.get(letter.lower(), letter) for letter in message)
    return encrypted_message

# Get input from the user and encrypt it
message = input("Enter your message: ")
encrypted_message = encrypt(message)

# Print the encrypted message
print("Your encrypted message is :", encrypted_message)