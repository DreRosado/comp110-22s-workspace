"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730524237"

word: str = input("Enter a 5-character word:")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character:")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
correct_count: int = 0

print("Searching for " + letter + " in " + word)

if letter == word[0]:
    print(letter + " found at index 0")
    correct_count = correct_count + 1

if letter == word[1]:
    print(letter + " found at index 1")
    correct_count = correct_count + 1

if letter == word[2]:
    print(letter + " found at index 2")
    correct_count = correct_count + 1

if letter == word[3]:
    print(letter + " found at index 3")
    correct_count = correct_count + 1

if letter == word[4]:
    print(letter + " found at index 4")   
    correct_count = correct_count + 1

if correct_count == 1: 
    print("1 instance of " + letter + " found in " + word)

if correct_count > 1:
    print(str(correct_count) + " instances of " + letter + " found in " + word)

if correct_count == 0:
    print("No instances of " + letter + " found in " + word)