# Brute force decryption with frequency analysis

The `brute_force_decrypt_with_frequency_analysis` function is a Python implementation of a brute force decryption algorithm that uses frequency analysis to improve the decryption process when the encrypted message is in English. The function takes a single argument, which is the encrypted message to be decrypted.

The function first converts the encrypted message to lowercase and counts the frequency of each letter in the message using a dictionary. The letters in the dictionary are sorted in descending order of frequency to identify the most frequent letter in the encrypted message.

The most likely shift for the Caesar cipher is then calculated as the difference between the index of the most frequent letter in the encrypted message and the index of the letter 'e' in the English alphabet. The shift is used to shift the English alphabet and create a dictionary that maps each letter in the alphabet to its corresponding shifted letter.

The cipher is then applied to the encrypted message using the dictionary to obtain the decrypted message. The decrypted message and the key used to decrypt it are printed as output.

This algorithm can be useful when the encrypted message is in English and the number of possible shifts is relatively small. By analyzing the frequency of letters in the message, we can identify the most likely shift and decrypt the message with greater efficiency than a pure brute force algorithm.

Here is an example of the `brute_force_decrypt_with_frequency_analysis` function:

```
encrypted_message = "wkhuh lv dq hadpsoh"
brute_force_decrypt_with_frequency_analysis(encrypted_message)

```

Output:

```
Key: 3 Decrypted message: there is a message
```
