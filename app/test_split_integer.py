from app import split_integer


def test_split_integer_into_one_part() -> None:
    assert split_integer.split_integer(8, 1) == [8]


def test_split_integer_into_equal_parts() -> None:
    assert split_integer.split_integer(6, 2) == [3, 3]


def test_split_integer_with_remainder() -> None:
    assert split_integer.split_integer(17, 4) == [4, 4, 4, 5]


def test_split_integer_with_remainder_two() -> None:
    assert split_integer.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_split_integer_returns_correct_number_of_parts() -> None:
    result = split_integer.split_integer(17, 4)

    assert len(result) == 4


def test_split_integer_returns_original_value() -> None:
    result = split_integer.split_integer(17, 4)

    assert sum(result) == 17


def test_split_integer_parts_are_sorted() -> None:
    result = split_integer.split_integer(17, 4)

    assert result == sorted(result)


def test_split_integer_parts_difference_is_not_more_than_one() -> None:
    result = split_integer.split_integer(17, 4)

    assert max(result) - min(result) <= 1
