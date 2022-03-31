"""Utils."""
__author__ = 730524237


def only_evens(n: list[int]) -> list[int]:
    """Returns only even integers in list."""
    even_numbers = [] 
    for number in n:
        if number % 2 == 0: 
            even_numbers.append(number)
    return even_numbers


print(only_evens([1, 2, 3, 4, 10, 11, 12, 13]))