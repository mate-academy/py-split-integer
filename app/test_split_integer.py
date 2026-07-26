from .split_integer import split_integer


def test_split_integer_single_part() -> None:
    assert split_integer(8, 1) == [8]


def test_split_integer_two_parts_even() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_split_integer_two_parts_odd() -> None:
    assert split_integer(7, 2) == [3, 4]


def test_split_integer_four_parts() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_integer_six_parts() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_split_integer_large_number_of_parts() -> None:
    assert split_integer(100, 10) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


def test_split_integer_large_even_split() -> None:
    assert split_integer(100, 20) == [
        5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5
    ]


def test_split_integer_large_odd_split() -> None:
    assert split_integer(101, 20) == [
        5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6
    ]


def test_split_integer_minimum_values() -> None:
    assert split_integer(1, 1) == [1]
    assert split_integer(2, 1) == [2]
    assert split_integer(2, 2) == [1, 1]
