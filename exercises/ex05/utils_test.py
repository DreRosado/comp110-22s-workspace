"""Test of utils file."""
__author__ = 730524237

from utils import only_evens, sub, concat


def test_only_evens_only_odd() -> None:
    """Tests only odd numbers."""
    xs: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(xs) == []


def test_only_evens_only_even() -> None:
    """Tests only even numbers."""
    xs: list[int] = [2, 4, 6, 8]
    assert only_evens(xs) == [2, 4, 6, 8]


def test_only_evens_many_ints() -> None: 
    """Tests both even and odd numbers."""
    xs: list[int] = [1, 2, 3, 4, 10, 11, 12, 13]
    assert only_evens(xs) == [2, 4, 10, 12]


def test_sub_empty() -> None:
    """Tests an empty list."""
    xs: list[int] = []
    assert sub(xs, 0, 4) == []


def test_sub_negative_index() -> None:
    """Tests a negative index."""
    xs: list[int] = ([1, 2, 3, 4, 5])
    assert sub(xs, -2, 2) == [1, 2]


def test_sub_index_more_than_length() -> None: 
    """Tests an index higher than the length of list."""
    xs: list[int] = [1, 2, 3, 4, 10, 11, 12, 13]
    assert sub(xs, 4, 9) == [10, 11, 12, 13]


def test_concat_empty_list() -> None:
    """Tests two empty lists."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_two_lists() -> None:
    """Tests two lists."""
    xs: list[int] = [1, 2, 3, 4]
    ys: list[int] = [5, 6, 7, 8]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_big_to_small_list() -> None:
    """Tests a bigger list before a smaller list."""
    xs: list[int] = [5, 6, 7, 8]
    ys: list[int] = [1, 2, 3, 4]
    assert concat(xs, ys) == [5, 6, 7, 8, 1, 2, 3, 4]
