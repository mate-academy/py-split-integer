
from app import split_integer


def test_split_into_one_part() -> None:
    assert split_integer.split_integer(8, 1) == [8]


def test_split_into_equal_parts() -> None:
    assert split_integer.split_integer(6, 2) == [3, 3]


def test_split_into_several_parts() -> None:
    assert split_integer.split_integer(17, 4) == [4, 4, 4, 5]


def test_split_into_parts_with_remainder() -> None:
    assert split_integer.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_parts_are_sorted() -> None:
    result = split_integer.split_integer(17, 4)
    assert result == sorted(result)


def test_parts_difference_is_at_most_one() -> None:
    result = split_integer.split_integer(32, 6)
    assert max(result) - min(result) <= 1


def test_number_of_parts() -> None:
    result = split_integer.split_integer(17, 4)
    assert len(result) == 4


def test_split_into_parts_equal_to_value() -> None:
    assert split_integer.split_integer(5, 5) == [1, 1, 1, 1, 1]


def test_split_into_more_parts_than_value() -> None:
    assert split_integer.split_integer(3, 5) == [0, 0, 1, 1, 1]
