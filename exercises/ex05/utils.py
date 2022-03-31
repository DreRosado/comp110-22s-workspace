"""Utils."""
__author__ = 730524237


def only_evens(n: list[int]) -> list[int]:
    """Returns only even integers in list."""
    even_numbers = [] 
    for number in n:
        if number % 2 == 0: 
            even_numbers.append(number)
    return even_numbers


def sub(a: list[int], b: int, c: int) -> list[int]:
    """Generate a subset of a list using 2 integers."""
    subset = []
    start_index = b
    end_index = c
    if c > len(a): 
        end_index = len(a)
    if b < 0:
        start_index = 0
    
    while start_index < end_index: 
        subset.append(a[start_index])
        start_index += 1 
    return subset


list_of_numbers = [10, 20, 30, 40, 50]

sub(list_of_numbers, 3, 5)


def concat(a: list[int], b: list[int]) -> list[int]:
    """Returns a list of the combined two lists."""
    mergedlist = []
    for number in a:
        mergedlist.append(number)
    for number in b:
        mergedlist.append(number)
    return mergedlist

    
