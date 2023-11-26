def calculate_letter_frequency(text):
    return {char: (text.count(char) / len(text)) * 100 for char in set(text)}

def decrypt_with_key(ciphertext, key):
    return ''.join(key.get(char, char) for char in ciphertext)

ciphertext = 'UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSXEPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ'
frequency = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09,
                         'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23,
                         'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15,
                         'q': 0.10, 'z': 0.07}

# Calculate and Sort letters by frequency in the ciphertext
sorted_frequency = sorted(
    calculate_letter_frequency(ciphertext).items(), key=lambda x: x[1], reverse=True)

# Try to match the most frequent letters with the most frequent letters in English
possible_key = {}
for i in range(len(sorted_frequency)):
    ciphertext_letter = sorted_frequency[i][0]

    # Exclude lowercase letters
    if ciphertext_letter.isupper():
        letter = max(frequency, key=frequency.get)
        possible_key[ciphertext_letter] = letter
        del frequency[letter]


# Print the percentage of frequencies in the possible key letters
print("\nPercentage of Frequencies in Possible Key Letters:")
uppercase_letters = [k for k in possible_key if k.isupper()]
for letter in uppercase_letters:
    print(f"{letter}: {calculate_letter_frequency(ciphertext)[letter]:.2f}%")

# Decrypt the ciphertext using the possible key
decrypted_text = decrypt_with_key(ciphertext, possible_key)

print("\nDecrypted Text:")
print(decrypted_text)