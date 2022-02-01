"""Emoji Wordle Assignment."""
__author__ = "730524237"

secretword: str = "python"

guess: str = input("What is your " + str(len(secretword)) + "-letter guess? ")
counter: int = 0
emoji: str = ""
while len(secretword) != len(guess):
    guess: str = input("That was not " + str(len(secretword)) + " letters! Try again:")

while counter < len(secretword):
    if guess[counter] == secretword[counter]:
        print()
        counter = counter + 1
    elif guess[counter] != secretword[counter]:
        print("\U00002B1C")
        counter = counter + 1

if guess != secretword:
    print("Not quite. Play again soon!")
    exit()
elif guess == secretword: 
    print("Woo! You got it!")