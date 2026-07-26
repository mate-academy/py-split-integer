from app.split_integer import split_integer


def test_split_single_part() -> None:
    assert split_integer(1, 1) == [1]


def test_split_equal_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_return_value_when_one_part() -> None:
    assert split_integer(17, 1) == [17]


def test_split_sorted_when_not_divisible() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_split_when_value_less_than_parts() -> None:
    assert split_integer(2, 3) == [0, 1, 1]
