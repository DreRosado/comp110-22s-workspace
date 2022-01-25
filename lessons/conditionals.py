"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1 and 5, can you guess what it is?")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You've guessed correctly! Thanks for playing!")
    print("I hope you have a wonderful day!")
else:
    print("Sorry, that's not my number! Thanks for playing!")
    print("Try running your program again.")
    if guess > SECRET: 
        print("Your guess is too high!")
    if guess < SECRET: 
        print("Your guess is too low!")


print("Game over.")