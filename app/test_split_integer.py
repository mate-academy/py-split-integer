from app.split_integer import split_integer


def test_split_integer_even_parts() -> None:
    assert split_integer(value=8, number_of_parts=4) == [2, 2, 2, 2]


def test_split_integer_length() -> None:
    assert len(split_integer(value=9, number_of_parts=3)) == 3


def test_split_integer_sum_preserved() -> None:
    assert sum(split_integer(value=20, number_of_parts=6)) == 20


def test_split_integer_single_part() -> None:
    assert split_integer(value=7, number_of_parts=1) == [7]


def test_split_integer_more_parts_than_value() -> None:
    result = split_integer(value=3, number_of_parts=5)
    assert len(result) == 5
    assert sum(result) == 3
