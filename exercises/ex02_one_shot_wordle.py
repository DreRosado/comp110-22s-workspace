"""Emoji Wordle Assignment."""
__author__ = "730524237"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secretword: str = "python"
guess: str = input("What is your " + str(len(secretword)) + "-letter guess? ")
counter: int = 0
i: int = 0
emoji: str = ""
boolvariable: bool = False

while len(secretword) != len(guess):
    guess = input("That was not " + str(len(secretword)) + " letters! Try again:")

while counter < len(secretword):
    if guess[counter] == secretword[counter]:
        emoji += GREEN_BOX
    else:
        boolvariable = False
        while i < len(secretword):
            if guess[counter] == secretword[i]:  
                boolvariable = True
            i += 1
        if boolvariable is True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    counter += 1
    i = 0
    
print(emoji)  

if guess != secretword:
    print("Not quite. Play again soon!")
elif guess == secretword: 
    print("Woo! You got it!")
