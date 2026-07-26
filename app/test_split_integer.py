
from app.split_integer import split_integer


def test_split_integer_examples_return_expected_parts() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
    assert split_integer(1, 5) == [0, 0, 0, 0, 1]


def test_split_integer_returns_sorted_parts() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)


def test_split_integer_max_minus_min_at_most_one() -> None:
    result = split_integer(32, 6)
    assert max(result) - min(result) <= 1


def test_split_integer_sum_equals_value() -> None:
    result = split_integer(3, 5)
    assert sum(result) == 3


def test_split_integer_elements_are_integers() -> None:
    result = split_integer(32, 6)
    assert all(isinstance(x, int) for x in result)
