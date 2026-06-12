from app.split_integer import split_integer


def test_split_integer_with_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_split_integer_with_equal_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_split_integer_with_difference_one() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_integer_with_multiple_parts() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_split_integer_when_parts_more_than_value() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
