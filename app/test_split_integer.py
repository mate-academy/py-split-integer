from app.split_integer import split_integer


def test_split_into_single_part() -> None:
    assert split_integer(8, 1) == [8]


def test_split_into_equal_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_split_with_remainder() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_larger_number_into_multiple_parts() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_number_of_parts_equals_value() -> None:
    assert split_integer(5, 5) == [1, 1, 1, 1, 1]


def test_value_less_than_number_of_parts() -> None:
    assert split_integer(2, 5) == [0, 0, 0, 1, 1]
