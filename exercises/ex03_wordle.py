"""Wordle Game."""
__author__ = 730524237

i: int = 0


def contains_char(secret_word: str, letter: str) -> bool: 
    """Function telling you whether or not the letter is in the word."""
    i: int = 0
    while i < len(secret_word):
        if letter == secret_word[i]:
            return True
        i += 1 
    return False


print(contains_char("python", "n"))
    