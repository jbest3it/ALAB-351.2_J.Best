# Prompts the user for a word.
word = input("Please enter a word: ")

# Prints the length of the word.
print(f"The length of the word is: {len(word)}")

# Prints the word in all uppercase.
print(f"The word in all uppercase is: {word.upper()}")

# Prints the word repeated 3 times (on the same line or separate lines).
print(f"The word repeated 3 times is: {(word + " ") * 3}")
