from app.split_integer import split_integer


def test_split_into_equal_parts() -> None:
    assert split_integer(6, 3) == [2, 2, 2]


def test_split_with_remainder() -> None:
    assert split_integer(7, 3) == [3, 2, 2]


def test_split_zero_value() -> None:
    assert split_integer(0, 3) == [0, 0, 0]


def test_split_one_value() -> None:
    assert split_integer(1, 3) == [1, 0, 0]
